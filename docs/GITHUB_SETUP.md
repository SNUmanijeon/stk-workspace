# GitHub repository

The shared starter is [SNUmanijeon/stk-workspace](https://github.com/SNUmanijeon/stk-workspace). It is public. Only reviewed toolkit code, instructions, template scaffolds, and placeholder asset/example documentation belong in it. Local scenario data, reports, dependencies, and machine settings are excluded.

## New workspace

Clone the repository, open its root as the local project folder, and run `python tools/bootstrap.py` followed by `python tools/preflight.py` with Python 3.10+. Configure the STK API path in ignored `settings/local.json`. A clone does not install STK or provide a license. The `--require-stk` check verifies API import only.

## Shared updates

Review the staged file list before committing. The root allowlist excludes unlisted legacy items and all `scenarios/`. Add new shared paths deliberately; keep `starter_manifest.json` current for ZIP distribution. Clones receive shared toolkit updates while local scenarios remain independent and need separate backup. GitHub template repositories evolve independently and do not automatically receive upstream updates.

## Authentication

GitHub connector access and local Git authentication are separate. Local pushes require a supported GitHub sign-in method, such as Git Credential Manager or GitHub CLI. Do not put a token in a remote URL or share one in chat.

[GitHub publication documentation](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
