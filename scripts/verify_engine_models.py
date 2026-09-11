
"""Load shared engine assets in a fresh owned STK Engine; never save or propagate."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import shutil
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--api-dir', type=Path, help='Installed/extracted STK 13 Python API directory')
    parser.add_argument('--reverse', action='store_true', help='Check the opposite import order')
    args = parser.parse_args()
    api = args.api_dir
    local = ROOT / 'settings/local.json'
    if api is None and local.exists():
        configured = json.loads(local.read_text(encoding='utf-8')).get('stk_api_dir')
        if configured:
            api = Path(configured)
    if api is not None:
        sys.path.insert(0, str(api if api.is_absolute() else ROOT / api))
    from agi.stk13.stkengine import STKEngine
    from agi.stk13.stkobjects import AgEComponent
    from agi.stk13.stkobjects.astrogator import AgVAEngineConstant

    base = ROOT / 'assets/engine_models'
    registry = json.loads((base/'registry.json').read_text(encoding='utf-8'))
    models = list(registry['models'])
    if args.reverse:
        models.reverse()
    result = {'models': [], 'scenario_saved': False, 'propagated': False,
              'attached_to_interactive': False}
    with tempfile.TemporaryDirectory(prefix='stk-engine-model-check-') as temporary:
        copied = []
        for item in models:
            source = (base/item['path']).resolve()
            if base.resolve() not in source.parents:
                raise ValueError('Engine asset path escapes its directory')
            if hashlib.sha256(source.read_bytes()).hexdigest() != item['sha256']:
                raise ValueError('Engine asset checksum mismatch: ' + item['id'])
            destination = Path(temporary)/source.name
            shutil.copyfile(source, destination)
            copied.append((item, destination))
        engine = STKEngine.StartApplication(noGraphics=True)
        try:
            root = engine.NewObjectRoot()
            root.NewScenario('EngineModelAssetCheck')
            for dimension, unit in [('DistanceUnit', 'm'), ('Time', 'sec'),
                                    ('ForceUnit', 'N'), ('SpecificImpulseUnit', 's')]:
                root.UnitPreferences.SetCurrentUnit(dimension, unit)
            folder = root.CurrentScenario.ComponentDirectory.GetComponents(
                AgEComponent.eComponentAstrogator).GetFolder('Engine Models')
            for item, path in copied:
                component = folder.LoadComponent(str(path))
                if component.Name != item['display_name']:
                    raise ValueError('Unexpected native component name: ' + component.Name)
            # Re-read after all imports: detect one component overwriting another.
            for item, _ in copied:
                component = folder.Item(item['display_name'])
                native = AgVAEngineConstant(component)
                for key, actual in [('thrust_n', native.Thrust), ('isp_s', native.Isp),
                                    ('standard_gravity_m_s2', native.g)]:
                    if not math.isclose(actual, item[key], rel_tol=0, abs_tol=1e-12):
                        raise ValueError('Native readback differs: ' + item['id'] + '/' + key)
                result['models'].append({'name': component.Name, 'thrust_n': native.Thrust,
                                         'isp_s': native.Isp, 'standard_gravity_m_s2': native.g})
            result['stk_version'] = engine.Version
            result['status'] = 'passed'
        finally:
            engine.ShutDown()
    result['owned_engine_shutdown'] = True
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
