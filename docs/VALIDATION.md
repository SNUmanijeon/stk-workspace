# Validation evidence

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
validation. The shared additions do not call STK. Native STK objects, example
scenarios, custom propagators, engines and populated artifact templates have
not been promoted by this release.

STK availability, scenario selection, relocation checks and cleanup completion
are specific to each workspace. Read that workspace's ignored map/audit;
successful runtime/load checks from an earlier checkout do not establish them
for a new one. Fresh clones require their own licensed STK installation and
local API configuration for STK-specific work.

## Distribution

The starter manifest enumerates reviewed shared files only. Its ZIP includes
SHA256SUMS.txt for source payloads. Local scenarios, mission outputs, settings,
audit records, dependency distributions and Git metadata are excluded.
