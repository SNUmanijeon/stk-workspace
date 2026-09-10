# STK workspace migration planning prompt

Copy the text below into a task opened at the root of the STK workspace you want to reorganize, or ask the task to read this file and follow it. This is a reusable planning prompt, not an instruction to migrate the current workspace immediately.

---

Prepare an evidence-based migration plan for this existing STK/Python workspace. The target is one Git repository at the selected workspace root, containing reusable code, STK assets, examples, artifact templates, and instructions. Local mission projects belong in a root-level `scenarios/` directory excluded from Git.

This task is planning only. Read existing files and create a migration-plan document, but do not move, delete, overwrite, or rename existing scenarios; change a running STK session; initialize Git; install software; create a remote repository; commit; or push. Record implementation steps for a later execution task.

## Intended structure

```text
STK/                             # Selected workspace and future Git root
  AGENTS.md                      # Brief instructions and documentation routing
  README.md                      # Setup, quick start, supported environment
  .gitignore
  .gitattributes                 # Explicit treatment of actual file formats
  pyproject.toml                 # Installable Python package and dependencies
  docs/
    STK_WORKFLOW.md               # Shared run procedure and modeling conventions
    CATALOG.md                    # Assets, examples, scripts, validation evidence
    MIGRATION_PLAN.md             # Source-to-destination map and verification
  src/
    stk_toolkit/
      __init__.py
      runtime.py                 # STK connection and explicit session selection
      scenario.py                # Scenario load/copy/save and working-path checks
      objects/                   # Builders/loaders, not a duplicate values database
      analysis/                  # Stable targeting, propagation, sensitivity logic
      reporting/                 # Extraction, figures, tables, report helpers
  assets/
    locations/
      koonibba/
      naro_space_center/
      contec_jeju/
      contec_sweden/
    area_targets/
      w3_tra/
    propagators/
      reentry_space_prop/
    engine_models/
      reentry_constant_thrust_and_isp/
    sequences/                   # Other reusable STK components as needed
  settings/                      # Avoid collision with STK-owned Config/ on Windows
    defaults/                    # Shared, documented defaults
    studies/                     # Only deliberately reusable study definitions
    local.example.json           # Machine-specific settings template
  scripts/
    monte_carlo.py               # Representative runnable method entry points
    launch_from_naro.py
  examples/
    see_raw/                     # Original scenario plus required dependencies
    landing_dispersion_test/     # Small reproducible demonstration
  templates/                     # Tracked reusable artifact sources
    registry.json
    plots/
    presentations/
    reports/
    tables/
    diagrams/
    scenarios/basic/
  tools/
    bootstrap.ps1                # Idempotent local setup; no STK/license installer
    new_scenario.py              # Creates a named study without overwriting
    preflight.py                 # Environment, assets, paths, and session checks
  tests/
  scenarios/                     # Entire directory ignored by Git
    WORKSPACE_MAP.md              # Local projects and current work; not shared
    sandbox/
      README.md
      config/
      stk/                       # Complete working STK scenario file set
      scripts/
      output/
    mission_name/
      README.md
      config/
      stk/
      scripts/
      output/
        run_id/
          manifest.json
          validation.json
          data/
          figures/
          reports/
          slides/
          logs/
```

The tree is a design target. Names are illustrative; do not invent asset contents, coordinates, object types, engine parameters, scenario provenance, or validation results to fill it. Expand the structure when existing material justifies it. Keep folders small and combine trivial modules where that improves clarity.

## Inspect before designing the migration

1. Read applicable instructions and existing READMEs. Check whether this directory is already in a Git repository, whether an ancestor is a repository, and whether child repositories exist. Do not assume a new `.git` directory is needed.
2. Inventory scenario folders, object/component exports, reusable scripts, report generators, reference evidence, generated outputs, environment files, and any known local changes. Exclude dependency caches from routine searching. Identify files that cannot be inspected.
3. Record authoritative sources and dependencies. Classify material as shared library, shared asset, validated example, exploratory reference, local project, generated result, or unresolved.
4. Identify hard-coded paths, scenario/object names, units, time scales, coordinate frames, STK/Python/API versions, local preferences, and external data dependencies. Distinguish documented expectations from live verification.
5. If this workspace contains an existing mission library or heritage registry, preserve and build on it. Do not create a competing implementation merely to match the proposed tree.

## Design decisions the plan must resolve

- Keep reusable plot, presentation, report, table, and diagram sources under tracked `templates/`. Register usable templates with stable IDs, versions, input requirements, render commands, and validation status. Leave future categories explicitly unpopulated until real templates are added. Render outputs under local scenario output and record template versions.
- If a starter release is already present, reuse its bootstrap, installer, documentation, and template registry. Check actual implementation status before proposing replacements. Use root `settings/` to avoid conflicting with STK-owned `Config/` on Windows.

- Keep Python code under `src/stk_toolkit`; place exported STK components and object data under `assets`. Builders/loaders should refer to one authoritative definition. A location may be a Place or Facility or have multiple intentional representations; inspect and document this rather than guessing.
- Use lowercase snake_case for new Python modules and catalog identifiers. Preserve STK display names and serialized internal references unless an explicitly tested migration requires changing them.
- Put reusable algorithms in the package and runnable examples of their use in `scripts`. Keep unusual mission orchestration inside the local scenario project until reuse is justified. Do not rewrite complex numerical algorithms during initial relocation.
- Copy validated examples into local scenarios for execution. Never use a tracked example or shared baseline as the default mutable run destination.
- Define how complete scenario bundles and custom components are saved using supported STK operations. Include ancillary files and dependencies, and verify loading from the destination. Never move only the `.sc` file and assume the scenario is complete.
- Preserve raw reference scenarios and provenance. A reduced demonstration must be identified as a derivative, not silently substituted for the raw source. Catalog validation status and evidence for every example.
- Use workspace-relative paths and configuration for local installation/data paths. Resolve assets from a documented workspace or package location, not the terminal's incidental working directory. Define asset lookup for installed packages, including wheel packaging if it is supported.
- Give every mutable run a unique ID, configuration snapshot, log, validation result, and code/baseline identity. Record dirty-code state or an equivalent source snapshot so a commit alone is not mistaken for the exact executed code. For stochastic runs, record seed, distributions, sample count, and failed-case handling.
- Use explicit STK session selection. One task owns a mutable session/run at a time. Protect unsaved interactive work; do not attach to and replace an arbitrary open scenario.
- Ignore all of `scenarios/`. Explain that local mission scripts and configuration there need independent backup or deliberate promotion into tracked shared examples/study definitions. Git is not backing them up.
- Include only verified shareable source assets in the publication set. Inventory large or binary assets before choosing normal Git, external versioned downloads, or a separate asset store. Do not add installed STK/Python distributions, credentials, license files, caches, or generated bulk results.
- Prefer conservative `.gitattributes` rules based on inspected file formats. Do not normalize proprietary serialized files blindly. Test save/load round trips for any serialization-related change.

## Required setup behavior

Specify an idempotent bootstrap that creates the ignored local directories and sandbox, configures the chosen Python environment, installs the local toolkit, and reports missing STK prerequisites clearly. It must preserve existing local configuration and scenario contents. Installing STK or obtaining a license is outside its scope.

Git does not recreate ignored or empty directories in a fresh clone. Bootstrap must therefore create `scenarios/` and its local workspace map; do not rely on an ignored `.gitkeep`.

Define a `new_scenario` command that accepts a name and optional example, checks paths, refuses collisions, creates the local folder layout, and copies or saves the complete starting scenario with dependencies. Specify command syntax only after deciding how it will actually be implemented; do not present proposed commands as working commands.

## Root instructions to include in the implementation plan

Keep `AGENTS.md` brief. It should instruct local Codex tasks to read `docs/STK_WORKFLOW.md` and relevant catalog entries before STK changes; consult `scenarios/WORKSPACE_MAP.md` when selecting local work; reuse shared methods; protect tracked examples/assets during runs; write generated material inside the selected local scenario; and report actual validation evidence.

Put stable operating rules in the shared manual, numerical defaults in configuration/assets, and local task status in the ignored workspace map. Record accepted modeling decisions in files rather than relying only on conversation history. Honor explicit user instructions and applicable higher-priority instructions when resolving conflicts.

For ChatGPT Work, provide a short Project Instructions text directing tasks to the same accessible manual. Do not assume that merely placing a file on disk configures a cloud ChatGPT Project.

## Migration and acceptance

Produce a phased plan: inventory and source map; scaffold; copy-based pilot migration; focused numerical/structural verification; migrate remaining reusable material; verify a clean checkout; prepare publication. Keep originals in place until replacements and dependencies have been verified. List proposed later cleanup separately from the migration itself.

The acceptance checks must include:

- Clean checkout in a different absolute directory with no references to the old workspace.
- Repeatable bootstrap that preserves existing local work.
- Package import, representative command invocation, and ignored-directory creation.
- Verified Git exclusions, plus a check that no local scenarios are already tracked.
- Representative STK example load, required components, and relevant propagation/targeting checks using stated tolerances and verified reference results.
- Shared examples/assets unchanged after a local test run.
- Representative figure/report creation from real run outputs.
- Clear distinction between checks completed, checks proposed, and checks blocked by unavailable STK/API/license access. Pure Python checks do not prove STK numerical equivalence.

Produce `docs/MIGRATION_PLAN.md` with the proposed tree, actual source-to-destination table, reusable/publication candidate inventory, unresolved questions, staged implementation steps, validation strategy, rollback approach, and exact proposed Git setup procedure. Ask only questions that cannot be resolved from available evidence and materially affect the plan. Do not publish or perform the migration in this planning task.

---

After reviewing the plan, a separate implementation request can say: "Implement the approved migration plan through local validation and publication preparation. Preserve original sources until their replacements are verified. Do not create or push a GitHub repository yet."
