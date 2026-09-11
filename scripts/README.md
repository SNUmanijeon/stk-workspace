# Representative scripts

- hohmann_budget.py: explicit SI inputs; signed two-body transfer burns, coast time and optional ideal mass/time budget.
- inventory_local.py: local SHA-256/layout/link snapshots and relocation comparison; never launches STK or moves files.

- verify_engine_models.py: imports both engine assets into a new owned STK Engine and reads back their values; requires licensed STK 13 and its separately supplied API.

The analytical and inventory runners use Python 3.10+ standard library. See [method specifications](../docs/REUSABLE_METHODS.md).

Mission-specific Monte Carlo and launch simulation drivers remain local until separately validated for sharing.
