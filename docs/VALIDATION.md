# Starter validation

Checked on 2026-09-10 using Python 3.12.14 on Windows.

## Completed

- Automated tests: 9 passed; 1 skipped because the environment did not allow test symlink creation. The skipped check is explicitly not claimed as verified.
- Installer preview left a nonexistent target unchanged.
- Installation into a fresh directory with spaces succeeded.
- Setup succeeded from a different current working directory.
- Repeated bootstrap preserved existing settings, notes, and local workspace-map content.
- A new named local project was created; collisions, invalid names, reserved Windows names, and a file blocking the sandbox were rejected.
- Differing destination files and parent-path conflicts stopped installation before any copying.
- Current-root bootstrap and structural preflight passed; no missing required paths.
- Git ignore checks confirmed that local scenarios, existing STK Config files, legacy OTV scenarios, and loose legacy scripts are excluded from the shared set.

## Runtime limits

The local workspace now uses the official STK 13.1 Python API from the installed distribution in an ignored runtime cache. API import preflight passed. A separate hidden STK Desktop instance loaded the retained relocated scenario successfully and was shut down without saving or propagating. The original regular files were checksum-verified after relocation; detailed results remain in the ignored local audit. Fresh clones still require their own STK installation, license, and API configuration.

The relocation check establishes file preservation and scenario loading, not a new numerical validation. No propagator, engine, location, complete example, or dynamics algorithm has been promoted into shared assets or scientifically revalidated by this cleanup.

## Distribution

The starter manifest enumerates shared files only. The ZIP includes SHA256SUMS.txt for its source payloads. Legacy scenarios, local projects, installed dependencies, and Git metadata are not part of that payload.
