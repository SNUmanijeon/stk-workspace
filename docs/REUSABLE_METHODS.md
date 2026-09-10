# Reusable analytical and preservation helpers

## Two-body transfer budget (two-body-budget, version 1.0.0)

src/stk_toolkit/two_body.py extracts the repeated hohmann_delta_v, period
and finite_duration operations from legacy orbit-transfer comparison scripts.
It adds explicit SI input names, finite/positive checks, available-propellant
checks, and stable small-delta-v arithmetic. Installing it does not rewrite
legacy mission scripts or their saved results.

Inputs are gravitational parameter in m^3/s^2, radii from the body center in m,
mass in kg, thrust in N, and effective exhaust velocity in m/s. Select all
physical parameters explicitly. Exhaust velocity is the chosen Isp in seconds
times the chosen standard gravity in m/s^2. No central-body or mission constants
are implicit. Times are elapsed seconds; no epoch, time scale or Earth-fixed
coordinate transformation is involved.

hohmann_transfer assumes coplanar circular initial/final orbits and two
instantaneous tangential burns. Positive signed delta-v raises the orbit;
negative lowers it. Total delta-v sums magnitudes. Coast duration is one-half
the transfer ellipse period. Equal radii give zero burns and zero coast time.
The equal-radius convention is explicit; it differs from evaluating the
half-period expression for a transfer that is not needed.

ideal_burn gives rocket-equation mass loss and constant-thrust duration for
the magnitude of a characteristic delta-v. It does not target a finite-burn
trajectory or account for gravity/steering losses, staging, drag or J2. For
sequential burns pass the returned final mass into the next burn. A combined
budget is equivalent only when exhaust velocity and thrust stay constant and
there are no intervening mass changes. An insufficient dry-mass reserve raises
ValueError; no clipping conceals the deficit.

Example using deliberately synthetic parameters (not mission output):

    python scripts/hohmann_budget.py --mu-m3-s2 1 --departure-radius-m 1 --arrival-radius-m 4

Expected signed burns are about 0.2649110641 and 0.1837722340 m/s; coast is
about 12.41823533 s. Use the Python functions for per-burn mass bookkeeping.

Validation: analytic vis-viva reference at radii 1 and 4, reversed transfers,
Kepler scaling, zero maneuver, a 60-digit decimal small-raise reference,
half-mass rocket identity, sequential mass/time accounting, invalid inputs,
and fuel exhaustion. Local extraction validation compares the old pure
functions across raising/lowering cases without importing their STK drivers.
These are analytical checks, not STK propagation or mission validation.

## Preservation inventory (preservation-inventory, version 1.0.0)

src/stk_toolkit/inventory.py generalizes legacy collection catalog and cleanup
verification patterns. It records regular-file SHA-256/size, directory layout
including empty directories, and link targets. Paths are relative to the scan
root. Windows junctions and symbolic links are recorded without traversal;
external dependencies are not silently copied or treated as preserved content.
The default exclusion is the exact name .git at every depth, recorded in
the snapshot. Use the same exclusions for before/after comparisons.

    python scripts/inventory_local.py scenarios/my_mission --output scenarios/before.json
    # After an independently authorized relocation to scenarios/renamed_mission:
    python scripts/inventory_local.py scenarios/renamed_mission --compare scenarios/before.json --output scenarios/after.json

The output must be a new file outside the scanned directory. A comparison
reports missing, added and changed entries separately and exits nonzero on
differences. Preserve the original snapshot for later comparisons; comparison
outputs contain both snapshot and comparison fields. The API also offers
inspect_python_source to read docstrings, top-level definitions and imports
without running source code, including code with top-level side effects.

Run against quiescent files. A detected change while hashing stops the scan;
this is not an atomic filesystem snapshot or a defense against hostile
concurrent filesystem mutation. Integrity equivalence does not prove dependency
resolution, scientific validity or successful STK loading. The tools never move
or delete files, launch STK, save scenarios, or propagate trajectories. Inventory
output can expose private filenames and link targets: keep it local/ignored.

Validation covers relocation with spaces in paths, changed/added files, removed
empty directories, source inspection without execution, matching exclusions,
CLI execution outside the checkout and Windows junction non-traversal. Symbolic
link tests can skip where the account cannot create links; report that limitation.

## Dependencies and deferred material

Both features require only Python 3.10+ standard library; dependencies = []
remains intentional. No NumPy, SciPy, STK API wheel, virtual environment or
installed distribution is needed or included. STK APIs remain supplied by a
separate licensed installation for STK-specific work.

Mission target solvers, atmospheric entry packages, native engine/propagator
components, station definitions, and populated report/deck sources need their
own provenance and validation before promotion. They are not dependencies of
these helpers. No artifact template is introduced here, so the existing
scenario-basic template registry entry is unchanged.
