<!-- generated -->
# Matrix

Implementation of ISO-11404 Array datatype. This defines an array of identical data components with a elementCount. Values are given as a block and can be encoded in different ways

Converted from [`swecommon/schemas/json/Matrix.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Matrix.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"Matrix"` | yes |  |
| `referenceFrame` | `string` |  | Frame of reference (usually spatial) with respect to which the coordinates of this matrix are expressed |
| `localFrame` | `string` |  | Frame of reference whose position and orientation are provided by the transformation defined by this matrix |

## Examples

1 example(s) taken from the specification are included and validated against this schema.

