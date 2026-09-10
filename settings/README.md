# Toolkit settings

`local.example.json` is tracked. Bootstrap copies it to ignored `local.json` only when missing. The chosen interpreter is the one used to run the tools; `python_executable` is informational until an explicit launcher uses it.

Future shared defaults and study definitions belong here with provenance, units, and validation status. Do not invent nominal physics values during setup. Keep this directory distinct from STK's existing `Config` directory.
