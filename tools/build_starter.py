"""Build a ZIP containing only the reviewed starter manifest files."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from stk_toolkit.workspace import inside


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "output/stk-workspace-starter.zip")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "starter_manifest.json").read_text(encoding="utf-8"))
    payloads = {}
    for relative in manifest["files"]:
        if Path(relative).is_absolute() or ".." in Path(relative).parts or ".git" in Path(relative).parts:
            raise ValueError(f"Unsafe manifest path: {relative}")
        path = inside(ROOT, relative)
        payloads[relative] = path.read_bytes()
    output = args.output.resolve()
    if output in [inside(ROOT, name) for name in payloads]:
        raise ValueError("Output would overwrite a source file")
    output.parent.mkdir(parents=True, exist_ok=True)
    sums = "\n".join(f"{hashlib.sha256(data).hexdigest()}  {name}" for name, data in sorted(payloads.items())) + "\n"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(payloads.items()):
            archive.writestr(name, data)
        archive.writestr("SHA256SUMS.txt", sums)
    print(json.dumps({"archive": str(output), "source_files": len(payloads), "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
