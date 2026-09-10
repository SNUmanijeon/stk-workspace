"""Create local workspace folders without overwriting user data."""

from __future__ import annotations

import json
from pathlib import Path
import re
import shutil


RESERVED = {"CON", "PRN", "AUX", "NUL"} | {
    f"{prefix}{index}" for prefix in ("COM", "LPT") for index in range(1, 10)
}


def workspace_root(root: str | Path) -> Path:
    root = Path(root).resolve()
    marker = root / "pyproject.toml"
    if not marker.is_file() or 'name = "stk-workspace-toolkit"' not in marker.read_text(encoding="utf-8"):
        raise ValueError(f"Not an STK toolkit workspace: {root}")
    return root


def inside(root: Path, relative: str) -> Path:
    candidate = (root / relative).resolve()
    if candidate == root or root not in candidate.parents:
        raise ValueError(f"Path escapes workspace: {relative}")
    # Do not follow existing junctions/symlinks, even those pointing within root.
    current = root
    for part in Path(relative).parts:
        current = current / part
        if current.is_symlink() or (hasattr(current, "is_junction") and current.is_junction()):
            raise ValueError(f"Linked path requires manual review: {current}")
    return candidate


def validate_name(name: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", name) or name.upper() in RESERVED:
        raise ValueError("Use 1-64 letters/digits/hyphens/underscores, starting with a letter or digit; Windows reserved names are not allowed.")
    return name


def create_scenario(root: str | Path, name: str) -> Path:
    root = workspace_root(root)
    name = validate_name(name)
    destination = inside(root, f"scenarios/{name}")
    if destination.exists():
        raise FileExistsError(f"Local project already exists: {destination}")
    template = inside(root, "templates/scenarios/basic")
    readme = (template / "README.md").read_text(encoding="utf-8").replace("{{SCENARIO_NAME}}", name)
    config = json.loads((template / "project.json").read_text(encoding="utf-8"))
    config["name"] = name
    destination.mkdir(parents=True, exist_ok=False)
    for directory in ("config", "stk", "scripts", "output"):
        (destination / directory).mkdir()
    (destination / "README.md").write_text(readme, encoding="utf-8")
    (destination / "config" / "project.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    return destination


def bootstrap(root: str | Path) -> dict:
    root = workspace_root(root)
    scenarios = inside(root, "scenarios")
    local = inside(root, "settings/local.json")
    sandbox = inside(root, "scenarios/sandbox")
    workspace_map = inside(root, "scenarios/WORKSPACE_MAP.md")
    for folder in (scenarios, sandbox):
        if folder.exists() and not folder.is_dir():
            raise ValueError(f"Expected directory: {folder}")
    for file in (local, workspace_map):
        if file.exists() and not file.is_file():
            raise ValueError(f"Expected file: {file}")
    scenarios.mkdir(exist_ok=True)
    if not local.exists():
        shutil.copyfile(root / "settings/local.example.json", local)
    if not sandbox.exists():
        create_scenario(root, "sandbox")
    if not workspace_map.exists():
        workspace_map.write_text("# Local STK projects\n\nThis file and all scenarios are local and ignored by Git.\n\n| Project | Status | Notes |\n|---|---|---|\n| sandbox | Scaffold | No STK scenario created yet |\n", encoding="utf-8")
    return {"workspace": str(root), "sandbox": str(sandbox), "status": "ready", "stk_connected": False}
