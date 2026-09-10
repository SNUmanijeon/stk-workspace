"""Check workspace structure and optionally STK API import, without opening STK."""
import argparse
import importlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from stk_toolkit.workspace import workspace_root


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-stk", action="store_true")
    args = parser.parse_args()
    workspace_root(ROOT)
    required = ("AGENTS.md", "docs/STK_WORKFLOW.md", "templates/registry.json", "settings/local.json", "scenarios/sandbox")
    missing = [path for path in required if not (ROOT / path).exists()]
    report = {"python": sys.executable, "python_version": sys.version.split()[0], "workspace": str(ROOT), "missing": missing, "stk_import": "not_checked", "stk_session": "not_opened", "numerical_validation": "not_performed"}
    failed = bool(missing)
    if args.require_stk:
        try:
            config = json.loads((ROOT / "settings/local.json").read_text(encoding="utf-8"))
            api = config.get("stk_api_dir")
            if api:
                path = Path(api).expanduser()
                sys.path.insert(0, str(path if path.is_absolute() else ROOT / path))
            version = str(config.get("stk_version", "13"))
            if not version.isdigit():
                raise ValueError("stk_version must contain only digits")
            importlib.import_module(f"agi.stk{version}.stkdesktop")
            report["stk_import"] = "available"
        except Exception as error:
            report["stk_import"] = f"unavailable: {type(error).__name__}: {error}"
            failed = True
    print(json.dumps(report, indent=2))
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
