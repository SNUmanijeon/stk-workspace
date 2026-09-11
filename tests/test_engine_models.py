
"""Static native-component identity/units checks; live checks use the STK runner."""
import hashlib
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET


BASE = Path(__file__).resolve().parents[1] / 'assets/engine_models'


class EngineModelTests(unittest.TestCase):
    def test_native_values_identity_and_distribution(self):
        registry = json.loads((BASE/'registry.json').read_text(encoding='utf-8'))
        manifest = json.loads((BASE.parents[1]/'starter_manifest.json').read_text(encoding='utf-8'))
        expected = {'IGT Engine': 80.0, 'Reentry Constant Thrust and Isp': 160.0}
        identifiers = set()
        self.assertEqual(len(registry['models']), 2)
        for item in registry['models']:
            with self.subTest(name=item['display_name']):
                path = BASE/item['path']
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), item['sha256'])
                tree = ET.parse(path)
                self.assertEqual(tree.findtext('Type'), 'EngineModel')
                self.assertEqual(tree.findtext('SpecificType'), 'EngineConstant')
                component = tree.find('./Data/VAR')
                self.assertEqual(component.get('name'), item['serialized_name'])
                scope = component.find('SCOPE')
                for name, unit, value in [('Thrust', 'N', expected[item['display_name']]),
                                          ('Isp', 's', 295.0), ('g', 'm*sec^-2', 9.80665)]:
                    quantity = scope.find("./VAR[@name='" + name + "']/QUANTITY")
                    self.assertEqual(quantity.get('Unit'), unit)
                    self.assertAlmostEqual(float(quantity.findtext('REAL')), value, places=12)
                identifier = scope.find("./VAR[@name='IdentifierInformation']/SCOPE/VAR[@name='Identifier']/STRING").text
                self.assertNotIn(identifier, identifiers)
                identifiers.add(identifier)
                self.assertIn('assets/engine_models/' + item['path'], manifest['files'])
                self.assertNotIn(':\\', path.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
