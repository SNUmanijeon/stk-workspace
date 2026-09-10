# STK workspace instructions

Read `docs/STK_WORKFLOW.md` and the relevant entries in `docs/CATALOG.md` before STK implementation or analysis. Consult `scenarios/WORKSPACE_MAP.md` for local work when it exists.

- Shared Python belongs in `src/stk_toolkit`; representative runners in `scripts`; exported STK objects in `assets`; complete reference scenarios in `examples`; reusable artifact templates in `templates`.
- Toolkit settings belong in `settings`. Do not confuse them with STK's own `Config` folder on Windows.
- Put local mission projects, their scripts, and generated deliverables in `scenarios/<name>`. This entire directory is ignored by Git and needs independent backup.
- Never run a mutating analysis against tracked examples, assets, or templates. Create a local working copy and select the intended STK session explicitly.
- Reuse validated code before creating another implementation. The starter does not yet implement mission dynamics or contain migrated STK models. Inspect existing legacy sources where available; do not treat placeholder folders as validated assets.
- Record units, reference frames, time scales, assumptions, code/input versions, convergence, and validation evidence with each run. Keep scientific checks separate from file-structure checks.
- Read `templates/README.md` before adding or using an artifact template. Record its ID/version in the run manifest. Write its rendered output under the local scenario, not back into the template folder.
- Preserve existing work during setup and migration. Read `docs/MIGRATION_PLAN.md` before relocating legacy material. Update the catalog when a shared method or asset is added or superseded.
- Follow the user's explicit instructions when they change these defaults. Do not infer permission to publish local mission data from a request to publish the reusable toolkit.
