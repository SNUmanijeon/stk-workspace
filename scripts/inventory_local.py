"""Create or verify a local preservation snapshot. No STK connection or file moves."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from stk_toolkit.inventory import compare_snapshots, snapshot_tree


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--compare', type=Path, help='Previous snapshot; writes comparison and current snapshot')
    args = parser.parse_args()
    directory = args.directory.resolve()
    output = args.output.resolve()
    if output == directory or directory in output.parents:
        parser.error('Keep the output outside the inventoried directory')
    if args.output.exists():
        parser.error('Output exists; choose a new audit file')
    current = snapshot_tree(args.directory)
    if args.compare:
        previous = json.loads(args.compare.read_text(encoding='utf-8'))
        comparison = compare_snapshots(previous, current)
        payload = {'snapshot': current, 'comparison': comparison}
    else:
        comparison = {'identical': True}
        payload = current
    with args.output.open('x', encoding='utf-8') as stream:
        json.dump(payload, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'files': len(current['files']), 'links': len(current['links']),
                      'comparison': comparison if args.compare else 'not_requested'}))
    return 0 if comparison['identical'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
