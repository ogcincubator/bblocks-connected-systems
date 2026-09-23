<!-- generated -->
# AbstractSimpleComponent

Converted from [`swecommon/schemas/json/AbstractSimpleComponent.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/AbstractSimpleComponent.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `referenceFrame` | `string` |  | Frame of reference (usually temporal or spatial) with respect to which the value of the component is expressed. A reference frame anchors a value to a real world datum. |
| `axisID` | `string` |  | Specifies the reference axis (refer to CRS axisID). The reference frame URI should also be specified unless it is inherited from parent Vector |
| `nilValues` |  |  | Defines reserved values with special meaning (e.g., missing, out-of-range, etc.) |
| `constraint` |  |  |  |
| `value` |  |  | Inline value(s) for the component. This property is optional to enable structure to act as a schema for values provided separately (e.g., in a datastream) |

