"""Read-only preservation snapshots; never execute study scripts or follow links."""
from __future__ import annotations

import ast
import hashlib
import os
from pathlib import Path
import stat


def _linked(path: Path) -> bool:
    info = path.lstat()
    return path.is_symlink() or bool(getattr(info, "st_file_attributes", 0) & 0x400)


def snapshot_tree(root: str | Path, *, exclude_names: tuple[str, ...] = (".git",)) -> dict:
    """Hash every regular file, record empty directories and link targets.

    Paths in the result are relative, enabling relocation comparison. Exclusions
    match exact entry names at every depth and are recorded. Symlinks and Windows
    reparse points are recorded but never traversed; no third-party dependencies.
    A snapshot is integrity evidence, not a dependency or STK load validation.
    """
    root = Path(root).absolute()
    if _linked(root) or not root.is_dir():
        raise ValueError("Inventory root must be an ordinary directory")
    if any(not n or '/' in n or '\\' in n or n in ('.', '..') for n in exclude_names):
        raise ValueError("Exclusions must be nonempty entry names")
    files, links, directories = [], [], []

    def visit(folder: Path) -> None:
        for path in sorted(folder.iterdir(), key=lambda p: p.name):
            if path.name in exclude_names:
                continue
            rel = path.relative_to(root).as_posix()
            before = path.lstat()
            if _linked(path):
                links.append({"path": rel, "target": os.readlink(path)})
            elif stat.S_ISDIR(before.st_mode):
                directories.append(rel)
                visit(path)
            elif stat.S_ISREG(before.st_mode):
                digest = hashlib.sha256()
                with path.open('rb') as stream:
                    for chunk in iter(lambda: stream.read(1024*1024), b''):
                        digest.update(chunk)
                after = path.lstat()
                if (before.st_size, before.st_mtime_ns, before.st_ino) != (after.st_size, after.st_mtime_ns, after.st_ino):
                    raise RuntimeError(f"File changed while inventorying: {rel}")
                files.append({"path": rel, "size": before.st_size, "sha256": digest.hexdigest()})
            else:
                raise ValueError(f"Unsupported special file: {rel}")
    visit(root)
    return {"schema_version": 1, "exclude_names": list(exclude_names),
            "files": files, "directories": directories, "links": links}


def compare_snapshots(before: dict, after: dict) -> dict:
    """Compare exact file content, directory layout and link targets, ignoring roots."""
    if before['schema_version'] != 1 or after['schema_version'] != 1:
        raise ValueError("Unsupported inventory schema")
    if set(before['exclude_names']) != set(after['exclude_names']):
        raise ValueError("Snapshot exclusions differ")
    result = {}
    for kind in ('files', 'links', 'directories'):
        def indexed(snapshot):
            rows = snapshot[kind]
            return {r if isinstance(r, str) else r['path']: r for r in rows}
        old, new = indexed(before), indexed(after)
        result[kind] = {
            'missing': sorted(old.keys() - new.keys()),
            'added': sorted(new.keys() - old.keys()),
            'changed': sorted(p for p in old.keys() & new.keys() if old[p] != new[p]),
        }
    result['identical'] = not any(items for changes in result.values() for items in changes.values())
    return result


def inspect_python_source(path: str | Path) -> dict:
    """Extract documentation, definitions and imports using AST, without importing.

    Call only for a regular file selected from the snapshot; syntax errors are
    returned as data so an inventory can retain and flag incomplete sources.
    """
    path = Path(path)
    if _linked(path) or not path.is_file():
        raise ValueError("Source must be an ordinary file")
    try:
        tree = ast.parse(path.read_text(encoding='utf-8-sig'), filename=path.name)
    except (SyntaxError, UnicodeError) as error:
        return {'status': 'unparsed', 'error': str(error)}
    return {'status': 'parsed', 'docstring': ast.get_docstring(tree),
            'definitions': [n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))],
            'imports': sorted({n.module or '' for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)} |
                              {a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names})}
