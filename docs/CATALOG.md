# Shared material catalog

## Implemented

| Item | Location | Status |
|---|---|---|
| Workspace bootstrap | tools/bootstrap.py | Local folder/configuration setup |
| New local study | tools/new_scenario.py | Scaffold only; no STK .sc creation |
| Preflight | tools/preflight.py | Structure check; optional API import only |
| Additive installer | tools/install_starter.py | Preview, conflict detection, add-only copy |
| Basic study template | templates/scenarios/basic | Version 1.0.0 |
| Two-body transfer / ideal rocket budget | src/stk_toolkit/two_body.py; scripts/hohmann_budget.py | two-body-budget 1.0.0; analytical/reference tests, no STK propagation claim |
| File preservation and source inspection | src/stk_toolkit/inventory.py; scripts/inventory_local.py | preservation-inventory 1.0.0; SHA-256/layout/link comparison, no dependency-resolution claim |

See [reusable method specifications](REUSABLE_METHODS.md) for provenance, input units, dependencies, examples and validation. These additions generalize repeated legacy helpers and do not replace specialized mission drivers.

## Native engine assets

| Asset ID/version | STK display name | Thrust / Isp | Status |
|---|---|---|---|
| igt-engine / 1.0.0 | IGT Engine | 80 N / 295 s | Native export; distinct identifier; STK 13.1 import/readback |
| reentry-constant-thrust-and-isp / 1.0.0 | Reentry Constant Thrust and Isp | 160 N / 295 s | Native export of legacy 160 N component; STK 13.1 import/readback |

See [engine guidance](../assets/engine_models/README.md) and [registry](../assets/engine_models/registry.json) for exact names, provenance, dependencies and validation limits. Legacy 80 N definitions sharing the old name are superseded by IGT Engine **for shared use**; historical scenarios are not rewritten.

## Candidate imports, not yet migrated

Koonibba; Naro Space Center; CONTEC Jeju and Sweden ground stations; W3 TRA; Reentry Space Prop; Monte Carlo methods; Naro launch simulation; raw SEE and landing-dispersion examples.

These names identify requested categories. The starter provides no authoritative numerical definitions or validation evidence for them. Inventory source files and dependencies before importing them.

Consult the ignored local workspace map for each checkout's preserved scenarios and unresolved migration decisions. Re-establish provenance and validation evidence from retained material before importing shared methods.

For each future import record a stable ID, source/provenance, complete dependencies, intended use, assumptions, validation status/evidence, and replacement/supersession information.
