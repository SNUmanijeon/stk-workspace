# STK workspace

A reusable STK/Python workspace with shared code, reference assets, and artifact templates in Git, and local mission projects under ignored `scenarios/`.

**Current release: 0.1.0, workspace starter.** Setup and project-creation utilities are implemented. Mission algorithms, STK objects, raw/reference scenarios, and finished plot/presentation templates have not been migrated into this starter. The retained local scenario is stored under ignored scenarios/. Other legacy root content is removed from this workspace and is not part of the shared starter.

## Quick start

Use Python 3.10 or newer. Run from this folder, with `python` replaced by your Python executable if needed:

```powershell
python tools/bootstrap.py
python tools/preflight.py
python tools/new_scenario.py my_mission
python -m unittest discover -s tests -v
```

PowerShell wrapper with an explicit interpreter:

```powershell
.\tools\bootstrap.ps1 -Python 'C:\path\to\python.exe'
```

Bootstrap creates the local sandbox, local workspace map, and `settings/local.json` without replacing existing content. It does not install Python, STK, an STK license, or third-party libraries. The Python setup tools use only the standard library. An editable package installation is optional: `python -m pip install -e .`.

For STK import diagnostics, set `stk_api_dir` in `settings/local.json` if the API is not installed in the chosen interpreter, then run `python tools/preflight.py --require-stk`. This does not connect to a running STK session or prove license/numerical readiness.

## Folder map

```text
STK/                              # Project root and Git root
  AGENTS.md
  README.md
  pyproject.toml
  starter_manifest.json           # Explicit distributable file inventory
  docs/                           # Workflow, catalog, migration and GitHub guides
  src/stk_toolkit/                 # Reusable Python package
  assets/                         # Exported STK objects/components
    locations/                    # Koonibba, Naro, CONTEC Jeju/Sweden
    area_targets/                 # W3 TRA and future areas
    propagators/                  # Reentry Space Prop and future models
    engine_models/                # Reentry Constant Thrust and Isp
    sequences/
  settings/                       # Toolkit settings, separate from STK Config/
  scripts/                        # Representative analysis runners
  examples/                       # Complete, validated reference scenarios
  templates/                      # Tracked reusable artifact sources
    registry.json
    plots/
    presentations/
    reports/
    tables/
    diagrams/
    scenarios/basic/              # Implemented local-project scaffold
  tools/                          # Bootstrap, install, preflight, new scenario
  tests/
  scenarios/                      # Ignored: created by bootstrap
    WORKSPACE_MAP.md
    sandbox/
      README.md
      config/
      stk/
      scripts/
      output/
    my_mission/
      README.md
      config/
      stk/
      scripts/
      output/<run_id>/
        data/
        figures/
        reports/
        slides/
        logs/
```

## Install into an existing workspace

Keep this starter in a separate directory while previewing installation:

```powershell
python tools/install_starter.py --target 'C:\path\to\existing\STK'
python tools/install_starter.py --target 'C:\path\to\existing\STK' --apply
```

The first command previews. Apply adds missing files, accepts identical files, and refuses differing files or unsafe paths before copying. Existing instructions/ignore rules need deliberate reconciliation, not replacement. It does not move legacy scenarios or initialize Git. After installation, run the target's bootstrap.

`Config` and `config` are the same name on typical Windows filesystems, so this starter uses `settings` at the root. Scenario-specific configuration still uses `scenarios/<name>/config`.

## Git, migration, and templates

- [Adopt another existing workspace](docs/ADOPT_EXISTING_WORKSPACE.md)
- [Contribute reusable material](docs/CONTRIBUTING.md)
- [GitHub setup](docs/GITHUB_SETUP.md)
- [Migration status and next steps](docs/MIGRATION_PLAN.md)
- [Reusable planning prompt](STK_WORKSPACE_MIGRATION_PROMPT.md)
- [Operating manual](docs/STK_WORKFLOW.md)
- [Template conventions](templates/README.md)

The root ignore policy shares only listed toolkit paths, keeping local data, runtime caches, and unreviewed root files out of Git. Add a new shared root folder deliberately to `.gitignore`. Git does not back up `scenarios`; preserve local mission definitions and evidence separately. Keep `starter_manifest.json` current when adding files intended for the installer or ZIP distribution.

Clone the same repository for workspaces that should share toolkit updates. Use a GitHub template only for independent repositories. The starter's `.gitignore` exclusions and template changes do not synchronize local mission data.
