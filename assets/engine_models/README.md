# Shared Astrogator engine models

| STK display name | Constant thrust at 100 percent | Isp | Asset |
|---|---:|---:|---|
| IGT Engine | 80 N | 295 s | [IGT_Engine.EngineModel](igt_engine/IGT_Engine.EngineModel) |
| Reentry Constant Thrust and Isp | 160 N | 295 s | [Reentry_Constant_Thrust_and_Isp.EngineModel](reentry_constant_thrust_and_isp/Reentry_Constant_Thrust_and_Isp.EngineModel) |

Both are self-contained EngineConstant components, using standard gravity
9.80665 m/s^2 for Isp conversion. Thrust efficiency/multiplier settings in
a maneuver can scale the commanded thrust; they are not part of these files.
The registry records exact serialized names, distinct identifiers, units,
source/export SHA-256 and dependencies.

The local inventory found both thrust variants under one legacy display name
and identifier. STK's native DuplicateComponent created the distinct IGT Engine
identity from the 80 N source; the 160 N definition retains the legacy name.
No mission scenario, saved result, installed library or machine setting is
included here.

## Use and verify

Use the STK Component Browser import/load action in a local working scenario,
under Astrogator / Engine Models. Choose IGT Engine for 80 N or
Reentry Constant Thrust and Isp for 160 N. Check legacy name collisions first;
some old scenarios embed an 80 N component under the 160 N asset's name.

Optional native verification (requires licensed STK 13 and its Python API):

    python scripts/verify_engine_models.py --api-dir PATH_TO_STK_API
    python scripts/verify_engine_models.py --api-dir PATH_TO_STK_API --reverse

The API path can instead come from ignored settings/local.json.
The runner copies assets to a temporary directory, creates a new owned
headless Engine and empty scenario, imports both components, then reads both
names and physical values after all imports. It shuts down its own Engine
without saving or propagating. It never attaches to interactive work.
The opposite order checks that neither component overwrites the other.

STK 13.1 native import/coexistence and parameter readback are the validation
scope. Static tests check serialized units, names, identifiers, checksums and
distribution inclusion. These checks do not propagate a trajectory or validate
real engine performance. Earlier STK versions have not been tested.
