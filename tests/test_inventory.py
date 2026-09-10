import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
from stk_toolkit.inventory import compare_snapshots, inspect_python_source, snapshot_tree


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.source = self.base/'scenario with spaces'
        (self.source/'empty').mkdir(parents=True)
        (self.source/'object.sa').write_bytes(b'original object\x00\xff')

    def test_relocation_and_tampering(self):
        original = snapshot_tree(self.source)
        target = self.base/'relocated'
        shutil.copytree(self.source, target)
        self.assertTrue(compare_snapshots(original, snapshot_tree(target))['identical'])
        (target/'object.sa').write_bytes(b'changed')
        (target/'new.txt').write_text('added')
        (target/'empty').rmdir()
        diff = compare_snapshots(original, snapshot_tree(target))
        self.assertFalse(diff['identical'])
        self.assertEqual(diff['files']['changed'], ['object.sa'])
        self.assertEqual(diff['files']['added'], ['new.txt'])
        self.assertEqual(diff['directories']['missing'], ['empty'])

    def test_source_is_never_executed(self):
        script = self.source/'source.py'
        script.write_text('"""Reusable description."""\nraise RuntimeError("must not run")\nimport math\ndef example(): pass\n')
        result = inspect_python_source(script)
        self.assertEqual(result['definitions'], ['example'])
        self.assertEqual(result['imports'], ['math'])
        script.write_text('def incomplete(')
        self.assertEqual(inspect_python_source(script)['status'], 'unparsed')

    def test_external_and_broken_links_are_not_followed(self):
        outside = self.base/'outside'
        outside.mkdir()
        (outside/'private.txt').write_text('outside inventory')
        try:
            (self.source/'external').symlink_to(outside, target_is_directory=True)
            (self.source/'broken').symlink_to(self.base/'missing')
        except OSError:
            self.skipTest('Symlink creation unavailable')
        result = snapshot_tree(self.source)
        self.assertEqual(len(result['files']), 1)
        self.assertEqual(len(result['links']), 2)
        self.assertEqual((outside/'private.txt').read_text(), 'outside inventory')
        with self.assertRaises(ValueError):
            snapshot_tree(self.source/'external')

    def test_exclusions_and_empty_directory(self):
        (self.source/'.git').mkdir()
        (self.source/'.git'/'config').write_text('local git settings')
        result = snapshot_tree(self.source)
        self.assertEqual(result['directories'], ['empty'])
        with self.assertRaises(ValueError):
            compare_snapshots(result, snapshot_tree(self.source, exclude_names=()))


    @unittest.skipUnless(os.name == 'nt', 'Windows junction behavior')
    def test_windows_junction_is_not_traversed(self):
        outside = self.base/'external dependency cache'
        outside.mkdir()
        (outside/'library.py').write_text('not in snapshot')
        link = self.source/'node_modules'
        environment = dict(os.environ, STK_TEST_LINK=str(link), STK_TEST_TARGET=str(outside))
        subprocess.run(['powershell', '-NoProfile', '-Command',
            '$null = New-Item -ItemType Junction -Path $env:STK_TEST_LINK -Target $env:STK_TEST_TARGET -ErrorAction Stop'],
            env=environment, check=True, capture_output=True)
        self.addCleanup(lambda: os.rmdir(link) if link.exists() else None)
        result = snapshot_tree(self.source)
        self.assertEqual(len(result['files']), 1)
        self.assertEqual(result['links'][0]['path'], 'node_modules')
        self.assertEqual((outside/'library.py').read_text(), 'not in snapshot')

    def test_cli_outside_original_directory(self):
        output = self.base/'before.json'
        command = [sys.executable, str(ROOT/'scripts/inventory_local.py'), str(self.source)]
        subprocess.run(command+['--output', str(output)], cwd=self.base, check=True, capture_output=True)
        self.assertEqual(len(json.loads(output.read_text())['files']), 1)
        destination = self.base/'relocated'
        shutil.copytree(self.source, destination)
        subprocess.run([sys.executable, str(ROOT/'scripts/inventory_local.py'), str(destination),
                        '--compare', str(output), '--output', str(self.base/'after.json')],
                       cwd=self.base, check=True, capture_output=True)
        refused = subprocess.run(command+['--output', str(self.source/'audit.json')], capture_output=True)
        self.assertNotEqual(refused.returncode, 0)
        self.assertFalse((self.source/'audit.json').exists())


if __name__ == '__main__':
    unittest.main()
