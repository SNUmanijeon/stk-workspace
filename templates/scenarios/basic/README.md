# {{SCENARIO_NAME}}

Local study scaffold. No STK scenario or numerical assumptions have been created.

- `config/project.json`: baseline and study parameters to define.
- `stk/`: complete working scenario and its dependencies.
- `scripts/`: study-specific orchestration using the shared toolkit.
- `output/<run_id>/`: run manifests, data, figures, reports, slides, logs, and validation.

Record units, frames, time system, baseline identity, code revision/source snapshot, and template versions for each run. For Monte Carlo work, include random seed, distributions, sample count, and failed cases. This project is excluded from Git; back up its definition and results separately.
