# Validation evidence

## Release 0.2.1 engine assets

The native engine exports are IGT Engine (80 N, 295 s) and Reentry Constant
Thrust and Isp (160 N, 295 s). Both use 9.80665 m/s^2 for the Isp conversion.
STK 13.1 exported the reviewed definitions; native duplication gave IGT Engine
a distinct identifier. Native verification loads copied assets into an empty
owned Engine scenario, in both import orders, then re-reads both names and
physical values. No mission scenario is loaded, saved or propagated.

The suite has 23 tests: 21 pass and the same two symbolic-link creation tests
skip. Engine tests check XML types, exact serialized names, SI units, distinct
component identifiers, file hashes and manifest inclusion. Clean-checkout
validation confirms portable asset lookup, native loading and distribution
checksums. The 127 original local engine component files remain byte-identical;
that private inventory is excluded from Git.

These checks establish configuration and load compatibility, not flight
performance or trajectory accuracy. No artifact template or third-party
Python dependency is added. The optional native verifier requires a separately
supplied licensed STK 13 installation/API.

## Release 0.2.0

Checked on Windows with Python 3.12.14. The shared suite has 22 tests:
20 pass and two symbolic-link creation tests skip because the account lacks
that capability. The separate Windows junction non-traversal test passes.

Analytical checks cover signed raising/lowering transfers, an independent
vis-viva reference, Kepler scaling, an explicit zero-transfer convention,
a 60-digit decimal reference for a small radius change, rocket-equation mass
accounting, sequential burns, invalid inputs and insufficient propellant.

A local comparison extracted only three pure functions from the legacy source
AST, without importing its mission driver. Across six transfer cases and ten
burn budgets, delta-v agreed within 1e-12 relative / 1e-12 m/s absolute,
coast time within 1e-14 relative, and duration within 1e-12 relative /
1e-10 s absolute; final mass matched. Raw source identities, hashes and private
comparison records remain in the local audit.

Preservation tests cover exact relocation, changed/added content, empty
directory removal, exclusion mismatch, AST inspection without execution,
CLI execution outside the checkout and output-placement safeguards. A native
Windows junction to an external dependency directory was recorded without
traversing or modifying its target.

Setup, scaffold, installer conflict detection and repeated-bootstrap
preservation tests also pass. Release validation includes a clean local clone,
bootstrap and preflight, package installation/import from outside the checkout,
representative analytical/inventory workflows, template lookup, and a
manifest-only distribution ZIP with checksums.

## Scope and runtime limits

These are file-structure and analytical reference checks, not mission-dynamics
validation. The analytical and inventory helpers do not call STK. Release
0.2.1 adds an optional native engine verifier. Other native objects, example
scenarios, custom propagators and populated artifact templates remain unmigrated.

STK availability, scenario selection, relocation checks and cleanup completion
are specific to each workspace. Read that workspace's ignored map/audit;
successful runtime/load checks from an earlier checkout do not establish them
for a new one. Fresh clones require their own licensed STK installation and
local API configuration for STK-specific work.

## Distribution

The starter manifest enumerates reviewed shared files only. Its ZIP includes
SHA256SUMS.txt for source payloads. Local scenarios, mission outputs, settings,
audit records, dependency distributions and Git metadata are excluded.
