# STK workspace operating manual

## Source and output locations

The repository root is the selected local project root. Shared code goes in `src/stk_toolkit`, reusable runners in `scripts`, exported STK objects in `assets`, complete references in `examples`, toolkit settings in `settings`, and artifact sources in `templates`.

Local work belongs in ignored `scenarios/<name>`, with complete STK files in `stk`, local scripts in `scripts`, configuration in `config`, and run deliverables in `output/<run_id>`. Record active work in ignored `scenarios/WORKSPACE_MAP.md`.

The root Git ignore file deliberately excludes unlisted root items so existing legacy scenarios and installed dependencies are not accidentally shared. Root `Config` is STK-owned; toolkit `settings` is separate. Git exclusions are neither access restrictions nor backups.

## Before an analysis

Read the relevant catalog and source READMEs. Confirm the baseline, units, coordinate frames, time scales, mass bookkeeping, required component versions, and actual environment. Mark unresolved parameters explicitly. Select the intended STK session and avoid changing unsaved interactive work. Each mutable STK session and run has one owner.

Create a local scenario scaffold. Copy or use supported STK save operations to create a complete working scenario, including object/component dependencies. Do not copy only the `.sc` file and assume it is sufficient. Do not mutate tracked examples or change serialized internal names merely to match filesystem names.

## Run and validate

Use shared methods where their documented assumptions apply. Keep mission-specific orchestration local until it has a stable reuse case. A setup check is not a dynamics validation.

For each run, retain configuration, baseline identity/checksum, STK/API/Python version, code commit plus dirty/source state, logs, target residuals/convergence, and relevant conservation/bookkeeping checks. State tolerances before evaluating results. Monte Carlo runs also record seed, distributions, sample count, and failure handling.

## Generate deliverables

Select a documented source in `templates/registry.json` when available. Record the template ID/version, the run/input identity, units, and transformations. Write generated files under the local run's output directory. Inspect figures and rendered reports for layout, labels, units, and consistency with source data.

An empty template or asset category is not a validated implementation. Never fabricate coordinates, engine values, propagated results, or a validation status to complete a directory tree.

## Shared changes

Add reusable functionality with its assumptions, example invocation, dependencies, and focused validation. Update `docs/CATALOG.md` and the distribution manifest when shipping new files. Keep reviewed originals until migrated replacements have been verified. Record accepted decisions in the manual/catalog/configuration rather than relying on chat history.
