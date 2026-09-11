# IGT Engine

- Asset ID/version: igt-engine / 1.0.0
- STK display name: **IGT Engine**
- Serialized component name/file: IGT_Engine / IGT_Engine.EngineModel
- Component type: Astrogator EngineConstant (constant thrust and Isp)
- Constant/100-percent thrust: **80 N**
- Specific impulse: **295 s**
- Standard gravity for the Isp conversion: 9.80665 m/s^2

This is the existing 80 N definition, renamed through STK's native component
duplication/export API at the user's request. Its new component identifier
lets it coexist with the legacy 160 N model. Thrust, Isp and standard gravity
are preserved. STK serializes the display-name space as an underscore.

The source was a saved 80 N Reentry Constant Thrust and Isp component.
Its checksum and the exported checksum are recorded in ../registry.json;
private source locations and inventories remain in the local audit.
Source scenario references were not rewritten.

Import this .EngineModel file into the Astrogator Component Browser's
Engine Models folder in a local working scenario. Select **IGT Engine**
for the maneuver engine. At thrust efficiency 1, the engine supplies 80 N.
A maneuver's efficiency/scaling settings remain separate; the component's
Thrust field is not an independent hard limiter.

No external files/components are required. STK 13 with the relevant
Astrogator license is needed to use it. There is no epoch, coordinate frame
or central-body gravity model in this constant engine component; g is the
Isp conversion constant, not local gravitational acceleration.

See [engine asset guidance](../README.md) for loading and validation.
