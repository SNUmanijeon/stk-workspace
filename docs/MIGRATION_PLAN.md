# Workspace migration status

The reusable repository structure and template categories are established. The requested cleanup retains the selected legacy scenario under ignored `scenarios/`. Obsolete root-level scenarios, scripts, outputs, preferences, and dependency caches are removed after preservation checks. Detailed file hashes and relocation evidence belong in the local cleanup audit, not this shared repository.

The retained scenario intentionally keeps its original internal layout to preserve references and report dependencies. New projects use the standard `config/`, `stk/`, `scripts/`, and `output/` layout. Consult the ignored local workspace map for the retained scenario path.

## Remaining model migration

Shared assets and example categories still contain documentation placeholders. No numerical mission algorithm is claimed to have been generalized. Before populating them, inspect retained sources, establish provenance and dependencies, import reviewed components or complete scenarios without altering serialized names, validate a local working copy, and update the catalog, template registry, and distribution manifest.

Root toolkit configuration uses `settings/` to avoid colliding with STK's `Config/`. Runtime caches stay outside the tracked file set. The additive installer remains available for other workspaces and refuses to overwrite differing files.
