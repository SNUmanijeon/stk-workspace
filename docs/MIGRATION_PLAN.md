# Workspace migration status

The reusable repository structure and template categories are established.
Preservation targets and cleanup status are specific to each checkout; consult
its ignored scenarios/WORKSPACE_MAP.md and local audit. This shared document
does not assert that local content has been removed. Detailed file hashes and
relocation evidence belong in the local audit, not this public repository.

Retained scenarios should keep their original internal layout when needed to
preserve references and report dependencies. New projects use the standard
config/, stk/, scripts/ and output/ layout. Consult the local map for exact paths.

## Remaining model migration

Shared assets and example categories still contain documentation placeholders.
Version 0.2.0 adds standard-library analytical transfer/rocket helpers and
preservation inventories; see [reusable methods](REUSABLE_METHODS.md).
Specialized mission solvers and native components remain local. Before
populating assets/examples, inspect retained sources, establish provenance and
dependencies, import reviewed components or complete scenarios without altering
serialized names, validate a local working copy, and update the catalog,
template registry and distribution manifest.

Root toolkit configuration uses settings/ to avoid colliding with STK's Config/.
Runtime caches stay outside the tracked file set. The additive installer remains
available for other workspaces and refuses to overwrite differing files.
