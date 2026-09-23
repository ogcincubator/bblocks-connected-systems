<!-- generated -->
# Vector

Implementation of a mathematical vector composed of a list of scalar coordinates expressed in the mandatory reference frame.

Converted from [`swecommon/schemas/json/Vector.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Vector.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"Vector"` | yes |  |
| `referenceFrame` | `string` | yes | Frame of reference (usually spatial) with respect to which the coordinates of this vector are expressed. A reference frame anchors a vector value to a real world datum. |
| `localFrame` | `string` |  | Frame of reference whose origin is located by the coordinates of this vector |
| `coordinates` | `array` | yes | Definition of the coordinate provided as a data component with a numerical representation |

## Examples

3 example(s) taken from the specification are included and validated against this schema.

