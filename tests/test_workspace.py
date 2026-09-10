from pathlib import Path
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from stk_toolkit.workspace import bootstrap, create_scenario, validate_name

spec = importlib.util.spec_from_file_location("installer", ROOT / "tools/install_starter.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "workspace with spaces"
        self.root.mkdir()
        shutil.copyfile(ROOT / "pyproject.toml", self.root / "pyproject.toml")
        (self.root / "settings").mkdir()
        shutil.copyfile(ROOT / "settings/local.example.json", self.root / "settings/local.example.json")
        shutil.copytree(ROOT / "templates/scenarios/basic", self.root / "templates/scenarios/basic")

    def test_bootstrap_preserves_user_content(self):
        bootstrap(self.root)
        config = self.root / "settings/local.json"
        readme = self.root / "scenarios/sandbox/README.md"
        workspace_map = self.root / "scenarios/WORKSPACE_MAP.md"
        config.write_text('{"custom": true}', encoding="utf-8")
        readme.write_text("my notes", encoding="utf-8")
        workspace_map.write_text("my projects", encoding="utf-8")
        bootstrap(self.root)
        self.assertEqual(config.read_text(), '{"custom": true}')
        self.assertEqual(readme.read_text(), "my notes")
        self.assertEqual(workspace_map.read_text(), "my projects")

    def test_named_project_and_collision(self):
        destination = create_scenario(self.root, "mission-600")
        self.assertEqual(json.loads((destination / "config/project.json").read_text())["name"], "mission-600")
        self.assertTrue((destination / "stk").is_dir())
        self.assertEqual(list(destination.glob("**/*.sc")), [])
        with self.assertRaises(FileExistsError):
            create_scenario(self.root, "mission-600")

    def test_bad_names(self):
        for name in ("../escape", "a/b", "a\\b", "CON", "nul", "COM1", ".hidden", "trailing.", "", "x" * 65):
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate_name(name)

    def test_wrong_workspace(self):
        with self.assertRaises(ValueError):
            bootstrap(self.root.parent)

    def test_sandbox_file_does_not_get_replaced(self):
        (self.root / "scenarios").mkdir()
        blocker = self.root / "scenarios/sandbox"
        blocker.write_text("keep")
        with self.assertRaises(ValueError):
            bootstrap(self.root)
        self.assertEqual(blocker.read_text(), "keep")

    def test_link_escape_is_rejected(self):
        elsewhere = self.root.parent / "elsewhere"
        elsewhere.mkdir()
        try:
            (self.root / "scenarios").symlink_to(elsewhere, target_is_directory=True)
        except OSError:
            self.skipTest("Symlink creation unavailable in this environment")
        with self.assertRaises(ValueError):
            create_scenario(self.root, "unsafe")
        self.assertEqual(list(elsewhere.iterdir()), [])


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.target = Path(self.temporary.name) / "target"

    def test_preview_does_not_create_target(self):
        result = installer.install(self.target)
        self.assertTrue(result["add"])
        self.assertFalse(self.target.exists())

    def test_install_and_repeat(self):
        first = installer.install(self.target, True)
        second = installer.install(self.target, True)
        self.assertTrue(first["applied"])
        self.assertFalse(second["add"])
        self.assertTrue(second["identical"])
        self.assertFalse((self.target / "scenarios").exists())

    def test_conflict_prevents_all_copying(self):
        self.target.mkdir()
        blocker = self.target / "README.md"
        blocker.write_text("existing user content")
        with self.assertRaises(ValueError):
            installer.install(self.target, True)
        self.assertEqual(blocker.read_text(), "existing user content")
        self.assertEqual(list(self.target.iterdir()), [blocker])

    def test_parent_file_conflict(self):
        self.target.mkdir()
        (self.target / "docs").write_text("existing")
        with self.assertRaises(ValueError):
            installer.install(self.target, True)
        self.assertFalse((self.target / "README.md").exists())


if __name__ == "__main__":
    unittest.main()
