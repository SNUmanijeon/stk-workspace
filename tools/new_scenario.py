"""Create a local study scaffold; no STK .sc file is generated."""
import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from stk_toolkit.workspace import create_scenario


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        print(create_scenario(args.root, args.name))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Project creation failed: {error}\n")


if __name__ == "__main__":
    main()
