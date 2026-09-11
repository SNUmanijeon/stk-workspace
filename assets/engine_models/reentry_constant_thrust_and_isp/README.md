# Reentry Constant Thrust and Isp

- Asset ID/version: reentry-constant-thrust-and-isp / 1.0.0
- STK display name: **Reentry Constant Thrust and Isp**
- Serialized name/file: Reentry_Constant_Thrust_and_Isp / Reentry_Constant_Thrust_and_Isp.EngineModel
- Component type: Astrogator EngineConstant (constant thrust and Isp)
- Constant/100-percent thrust: **160 N**
- Specific impulse: **295 s**
- Standard gravity for the Isp conversion: 9.80665 m/s^2

This exports the saved 160 N legacy component through STK 13.1, retaining
its display name and component identifier. Physical parameters are unchanged
apart from round-off in the serialized standard-gravity value. Source and
export checksums are in ../registry.json; private locations remain local.

Some historical scenarios use this same legacy name and identifier for an
80 N definition. Check an existing scenario before importing the 160 N file:
replacing its legacy 80 N component would change its maneuver model.
Use a deliberate local working-copy migration and select **IGT Engine**
for the 80 N case. Historical scenario files were not altered by this export.

No external files/components are required. See [engine asset guidance](../README.md)
for STK requirements, nominal thrust semantics and verification.
