# Adopt an existing STK workspace

Use this guide for a local ChatGPT Work or Codex task that will convert an existing workspace to this repository's structure. It is an implementation workflow. The older STK_WORKSPACE_MIGRATION_PROMPT.md is planning-only and does not override an explicit request to execute this workflow.

Repository: https://github.com/SNUmanijeon/stk-workspace

## What the user supplies

- The existing workspace's absolute local path, attached to the task with read/write access.
- The exact scenario folders to preserve, including their paths if names are ambiguous.
- Any additional reports, data, scripts, or reference documents to preserve.
- Cleanup scope: items explicitly authorized for removal, or "inventory first; do not delete unclassified material."
- Optional known Python/STK versions, interpreter location, external data paths, validated reference outputs, and conventions that must be retained.

Do not infer a preservation list from scenario names, recency, or the decisions in a different workspace. If the list is absent or ambiguous, inventory candidates and ask the user to identify them. Continue independent repository inspection and source review while waiting; do not perform dependent moves or deletion. An unspecified preservation list never means "preserve nothing."

Local scenario folders must be accessible on disk. Uploading only .sc files into a cloud chat does not provide the full scenario file sets, installed STK runtime, or local filesystem access.

## Task instructions

Reform the supplied workspace using the existing repository above, preserving the user's specified local scenarios. Inventory useful reusable material and contribute validated, compatible improvements to this same repository. Proceed through implementation and verification within the supplied scope; do not stop after producing a plan unless blocked by missing access or a necessary user decision.

### 1. Establish current state and authority

Read the workspace's applicable instructions. Fetch the current repository and read AGENTS.md, docs/STK_WORKFLOW.md, docs/CATALOG.md, docs/CONTRIBUTING.md, templates/README.md, and starter_manifest.json.

Inspect local Git state, parent and child repositories, existing remotes, uncommitted work, running STK sessions, dependencies, and scenario locations. Existing workspace evidence takes precedence over assumptions copied from the original workspace. Do not delete or replace an existing .git directory or discard unrelated history.

Write a local inventory and source-to-destination plan under an ignored local audit directory. Record preservation targets, dependencies, reusable candidates, and separately authorized deletion targets before changing them.

### 2. Join the same repository

Use a clone/checkout of SNUmanijeon/stk-workspace with origin pointing to that exact repository. Do not create a new GitHub repository, fork, or template-derived repository. Preserve its commit ancestry so future fetch/pull/push operations work normally.

For a nonempty workspace, use a temporary clean clone and a reviewed, additive installation/migration. Reconcile differing instructions and configuration instead of overwriting them. The existing installer previews conflicts but does not establish shared Git history by itself.

The final selected workspace root must also be the repository root; scenarios belongs directly beneath it. Do not leave the actual shared repository nested in a subfolder. If existing unrelated Git history prevents a straightforward adoption, preserve that history and resolve the structure deliberately rather than forcing an unrelated main branch onto origin.

Keep the checked-out shared main synchronized with origin/main. Preserve local modifications when incorporating incoming changes.

### 3. Preserve local scenarios and supporting material

Relocate each explicitly selected complete scenario folder into scenarios/<unique-name>, including its object files, Flight_Dynamics components, local scripts, reports, data, and supporting material. Preserve the original internal layout when restructuring it would break references. New projects can use the standard scaffold.

Before moving, record a file inventory with SHA-256 hashes and a separate symlink/junction inventory. Verify resolved source and destination paths stay in the authorized workspace. Do not traverse external link targets during cleanup; preserve or explicitly re-establish required links.

Identify references to other local folders before those folders are removed. Preserve required dependencies or replace them with a tested, documented shared implementation. Do not leave a preserved scenario dependent on a deleted source directory.

Verify hashes after relocation. If a path fix is necessary, record it as a deliberate change with before/after evidence rather than falsely claiming byte-for-byte identity. Historical report provenance can retain old paths if it is clearly historical and not an executable dependency.

Where STK is available, load each relocated scenario in a separate explicitly owned instance and inspect the expected object/component inventory. Do not save, propagate, or replace unsaved interactive work merely to test relocation. Record any unavailable runtime/license checks honestly. Keep originals/deletion targets pending if required dependencies or load checks remain unresolved.

Update scenarios/WORKSPACE_MAP.md and local audit records. Keep local scenario contents excluded from Git. This is local preservation, not a backup service.

### 4. Extract reusable contributions before cleanup

Follow docs/CONTRIBUTING.md. Review local Python modules, analysis scripts, library extensions, numerical methods, report/figure generators, dependency requirements, STK objects/components, and existing artifact templates.

Compare each candidate with current shared functionality. Reuse or extend existing code when appropriate; avoid duplicate implementations and gratuitous renaming. Keep unusual mission orchestration local until it has a clear shared use case.

Separate actual reusable source and documented configuration from local mission data. The repository is public: publish clearly reusable non-confidential material within the user's request, but keep mission results, credentials, personal paths, confidential designs, and material with unclear redistribution rights local. Resolve a specific ambiguity before publishing the affected item; continue unaffected contributions.

For external Python libraries, record justified dependencies and compatible versions instead of committing site-packages, virtual environments, caches, proprietary installers, or STK API distributions. Use optional dependency groups where a library supports only one feature.

Document and test each contribution. Update the catalog, relevant settings/examples, template registry if applicable, package dependencies, and starter manifest. Record sources, assumptions, units, expected outputs, and validation evidence. Do not invent missing models or label exploratory code as validated.

### 5. Validate, publish, then clean up

Run focused setup and contribution tests. Verify at least one representative workflow for each promoted method. Distinguish pure Python, API import, scenario-load, and numerical checks. For changed numerical logic, compare against an established reference with explicit tolerances.

Use an isolated clean checkout to verify setup, imports, asset lookup, and applicable example/report generation outside the original absolute directory. Confirm scenarios, runtime caches, local settings, and any audit containing private information are untracked.

Fetch the latest remote state immediately before publishing. Commit and push validated compatible changes to the same repository without force-pushing or replacing other work. Resolve concurrent changes with normal Git history. If a contribution is breaking or insufficiently validated, publish it on a clearly named branch with a pull request and explain that it is not yet part of shared main.

The user's request to update this repository authorizes routine compatible contributions; do not repeatedly ask permission to publish that already-authorized shared material. It does not authorize publishing local scenario data.

Delete only the explicitly authorized obsolete sources after their required content has been preserved or extracted and verified. Keep unclassified files and any material with unresolved dependencies. Use native filesystem operations with checked absolute paths; never let recursive deletion follow a junction outside the workspace.

### 6. Finish with a concrete result

Report the final repository URL and branch/commit, preserved scenario paths, migrated shared features, template/dependency additions, deletion count/scope, completed validation and its limits, remaining issues, and how to start a new local scenario.

Do not claim completion merely because folders exist, imports pass, a commit was created locally, or a pull request was opened. Verify the remote contains the intended contribution and explain what is still awaiting validation or merge.

## Persistent project instructions

Use this exact repository as the shared source of STK workspace conventions and reusable code. Read its operating manual and contribution guide for relevant work. Preserve selected local scenarios under ignored scenarios; contribute validated reusable improvements to the same repository; keep scenario-specific data and outputs local. Consult scenarios/WORKSPACE_MAP.md rather than assuming another task's context is available. Explicit user instructions determine preservation and cleanup scope.

## Required distinctions

- A clone of the same repository shares history and can receive updates; a template-generated repository does not automatically stay synchronized.
- Copying a ZIP installs files but does not connect Git history or authentication.
- AGENTS.md supplies local Codex guidance; separately configure ChatGPT Work project instructions to consult the same accessible manual.
- Connector authentication and local Git authentication are distinct; missing access is not permission to expose tokens or bypass repository controls.
