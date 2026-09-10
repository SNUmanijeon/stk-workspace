"""Preview or add starter files into an existing directory without overwrites."""
import argparse
import json
from pathlib import Path
import shutil
import sys

SOURCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE / "src"))
from stk_toolkit.workspace import inside


def install(target: Path, apply: bool = False) -> dict:
    target = target.resolve()
    if target.exists() and not target.is_dir():
        raise ValueError("Target is not a directory")
    manifest = json.loads((SOURCE / "starter_manifest.json").read_text(encoding="utf-8"))
    files = manifest["files"]
    if len(files) != len(set(files)):
        raise ValueError("Duplicate manifest entries")
    pending, identical, conflicts = [], [], []
    for relative in files:
        if Path(relative).is_absolute() or ".." in Path(relative).parts or ".git" in Path(relative).parts:
            raise ValueError(f"Invalid manifest entry: {relative}")
        src = inside(SOURCE, relative)
        dst = inside(target, relative)
        if not src.is_file():
            raise ValueError(f"Missing source file: {relative}")
        parent = dst.parent
        while parent != target:
            if parent.exists() and not parent.is_dir():
                conflicts.append(relative)
                break
            parent = parent.parent
        else:
            if dst.exists():
                (identical if dst.is_file() and src.read_bytes() == dst.read_bytes() else conflicts).append(relative)
            else:
                pending.append(relative)
    report = {"target": str(target), "mode": "apply" if apply else "preview", "add": pending, "identical": identical, "conflicts": conflicts, "applied": False}
    if apply and conflicts:
        raise ValueError("No files copied. Reconcile differing files first: " + ", ".join(conflicts))
    if apply:
        for relative in pending:
            destination = inside(target, relative)
            destination.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation also guards against a newly appearing file.
            with destination.open("xb") as output, inside(SOURCE, relative).open("rb") as source:
                shutil.copyfileobj(source, output)
        report["applied"] = True
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        result = install(args.target, args.apply)
        print(json.dumps(result, indent=2))
        return int(bool(result["conflicts"]))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Installation stopped: {error}\n")


if __name__ == "__main__":
    sys.exit(main())
