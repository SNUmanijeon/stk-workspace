# STK workspace setup materials

The option-2 starter is now prepared at the workspace root: one repository for shared material, with all local studies in ignored `scenarios/`.

## Start here

- [Quick start and full folder map](README.md)
- [GitHub publication and future clones](docs/GITHUB_SETUP.md)
- [Migration planning prompt](STK_WORKSPACE_MIGRATION_PROMPT.md)
- [Current migration status](docs/MIGRATION_PLAN.md)
- [Template source folders and conventions](templates/README.md)
- [Validation record](docs/VALIDATION.md)

## Local setup

Use a Python 3.10+ interpreter to run `tools/bootstrap.py`. Alternatively, pass its executable path to `tools/bootstrap.ps1 -Python`. Then run `tools/preflight.py` and create a study with `tools/new_scenario.py NAME`.

The setup utilities use only the Python standard library. No STK session is opened, and no mission dynamics, reference scenario, or finished artifact template is created by bootstrap. Fill local STK API settings as needed and perform a separately documented numerical validation after importing actual models.

## Drop into another workspace

Extract the starter ZIP to a temporary source directory. Run its `tools/install_starter.py --target YOUR_WORKSPACE` to preview; add `--apply` to copy missing files. The installer refuses differing files before copying. Reconcile existing instructions/ignore rules deliberately. Run bootstrap from the target after installation.

Use the installed target root as the project and Git root. The archive contains shared source files only, not existing local scenarios, reports, credentials, installed STK libraries, or `.git` metadata.

## Templates

`templates/plots`, `presentations`, `reports`, `tables`, and `diagrams` are reserved for future artifact sources. `templates/scenarios/basic` supplies the working local-study scaffold. Register actual templates in `templates/registry.json`. Generated artifacts stay under `scenarios/<name>/output/<run_id>`.

## Versioning

The root ignore file shares only listed toolkit locations and excludes legacy root contents and all of `scenarios`. Back up local mission definitions/results separately. Clone the same repository to share toolkit updates across workspaces; use GitHub templates for independent repositories.

GitHub status and the steps needed to finish publication are recorded in `docs/GITHUB_SETUP.md`.
