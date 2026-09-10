# Representative scripts

- hohmann_budget.py: explicit SI inputs; signed two-body transfer burns, coast time and optional ideal mass/time budget.
- inventory_local.py: local SHA-256/layout/link snapshots and relocation comparison; never launches STK or moves files.

Both use Python 3.10+ standard library. See [method specifications](../docs/REUSABLE_METHODS.md).

Mission-specific Monte Carlo and launch simulation drivers remain local until separately validated for sharing.
