# Shared material catalog

## Implemented

| Item | Location | Status |
|---|---|---|
| Workspace bootstrap | tools/bootstrap.py | Local folder/configuration setup |
| New local study | tools/new_scenario.py | Scaffold only; no STK .sc creation |
| Preflight | tools/preflight.py | Structure check; optional API import only |
| Additive installer | tools/install_starter.py | Preview, conflict detection, add-only copy |
| Basic study template | templates/scenarios/basic | Version 1.0.0 |

## Candidate imports, not yet migrated

Koonibba; Naro Space Center; CONTEC Jeju and Sweden ground stations; W3 TRA; Reentry Space Prop; Reentry Constant Thrust and Isp; Monte Carlo methods; Naro launch simulation; raw SEE and landing-dispersion examples.

These names identify requested categories. The starter provides no authoritative numerical definitions or validation evidence for them. Inventory source files and dependencies before importing them.

Consult the ignored local workspace map for the retained scenario. The previous root-level mission library and legacy studies are no longer part of this cleaned workspace. Re-establish provenance and validation evidence from retained material before importing shared methods.

For each future import record a stable ID, source/provenance, complete dependencies, intended use, assumptions, validation status/evidence, and replacement/supersession information.
