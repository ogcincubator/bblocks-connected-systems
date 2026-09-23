<!-- generated -->
# AbstractPhysicalProcess

Converted from [`sensorml/schemas/json/AbstractPhysicalProcess.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/AbstractPhysicalProcess.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.sensorml.abstract-physical-process#SpatialFrame`:

- `SpatialFrame`: A general spatial Cartesian Reference Frame where the axes and origin will be defined textually relative to a physical component.
- `TemporalFrame`: A general temporal frame such as a mission start time or timer start time. The origin should just describe context of the start of time (e.g., start of local timer).
- `Position`

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `attachedTo` | `commonDefs.json#/$defs/XLink` |  | References the physical component or system (e.g., platform) to which to which this component or system is attached. |
| `localReferenceFrames` | `array` |  | A list of spatial reference frames, attached to the physical component itself. |
| `localTimeFrames` | `array` |  | Supports local time reference frames such as "time past mission start". Note that units are handled in timePosition so they are not specified in the TemporalFrame. |
| `position` | `#/$defs/Position` |  | Provides positional information relating the component's spatial reference frame to an external spatial reference frame. |

