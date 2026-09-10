# Contributing reusable STK material

The shared repository is https://github.com/SNUmanijeon/stk-workspace. Contributions from every local workspace should improve this repository while keeping local scenarios independent.

## Choose the right destination

| Material | Destination | Requirements |
|---|---|---|
| Stable Python functions/classes | src/stk_toolkit | Documented inputs/outputs, assumptions, compatible interface |
| Representative runnable analysis | scripts | Arguments, starting conditions, dependencies, example invocation |
| Mission-specific orchestration | scenarios/<name>/scripts | Keep local until useful beyond one study |
| Exported STK objects/components | assets | Authoritative source, complete dependencies, exact internal names, validation |
| Complete reference scenario | examples | Deliberately shareable bundle, provenance, expected behavior; never a live run destination |
| Shared configuration | settings | Units, origin, meaningful defaults; no personal installation paths |
| Plot/slide/report/table/diagram source | templates | Stable ID/version, inputs, rendering instructions, registry entry when usable |
| Third-party Python dependency | pyproject.toml or feature dependency specification | Justification, supported versions, installation instructions |
| Results and populated deliverables | scenarios/<name>/output | Local; do not publish by default |

## Evaluate before extracting

Compare the candidate with existing shared behavior. Prefer an extension or bug fix over another near-duplicate implementation. Share repeated, stable operations; keep a specialized algorithm as a documented example if generalizing it would obscure its assumptions.

Maintain backward compatibility where feasible. Parameterize mission values without replacing them with invented universal defaults. Avoid mixing a filesystem relocation with an unverified numerical redesign.

For reusable STK exports, preserve the exact serialized names, central-body assumptions, component dependencies, and applicable units. Verify loading in a clean local working copy. Do not include an installed vendor library or API distribution as though it were user-authored model content.

## Validation and evidence

Tests must exercise meaningful behavior: bounds, unit handling, path independence, mass accounting, convergence, reference comparisons, and applicable numerical tolerances. Use a real validated reference for scientific results; passing a syntax/import check is not a scientific validation.

Keep large or nonpublic test evidence local, and record a shareable validation summary. Small public fixtures can be committed when they are appropriate and reproducible. When adding a template, inspect representative rendered output; an empty category remains a placeholder.

Update docs/CATALOG.md, README invocation/setup instructions, package metadata/dependencies, and starter_manifest.json for distributed source additions. Update templates/registry.json only for real usable templates. Do not copy environment-specific validation claims from another workspace.

## Publication and multiple workspaces

The repository is public. Only contribute clearly reusable, non-confidential source, examples, assets, and templates that can be shared. Exclude credentials, local mission results, personal absolute paths, confidential mission definitions, installed dependencies, caches, and local audit data. If a candidate's redistribution rights or content classification is unclear, keep that candidate local and resolve the specific question.

Fetch current origin/main before changes and again before publishing. Preserve local work and incoming contributions. Push compatible, validated changes using normal Git history without force. Reserve a branch and pull request for breaking or experimental work; report that it is not yet available on main.

Record the shared commit and any local modifications with each analysis. Another workspace should adopt updated shared code deliberately and rerun relevant checks; local scenarios do not synchronize through Git.

For an existing-workspace conversion, follow docs/ADOPT_EXISTING_WORKSPACE.md and its preservation rules. Extract and verify useful material before deleting obsolete sources.
