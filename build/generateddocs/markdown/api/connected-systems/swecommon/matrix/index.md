
# Matrix (Schema)

`ogc.api.connected-systems.swecommon.matrix` *v0.1*

Implementation of ISO-11404 Array datatype. This defines an array of identical data components with a elementCount. Values are given as a block and can be encoded in different ways

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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


## Examples

### Matrix1
#### json
```json
{
  "type": "Matrix",
  "definition": "http://sensorml.com/ont/swe/property/RotationMatrix",
  "referenceFrame": "http://www.opengis.net/def/crs/OGC/0/ECI_J2000",
  "label": "3D Orientation Matrix",
  "elementType": {
    "name": "row",
    "type": "Matrix",
    "elementType": {
      "name": "coef",
      "type": "Quantity",
      "definition": "http://sensorml.com/ont/swe/property/Coordinate",
      "label": "Matrix Coef",
      "uom": { "code": "1" }
    }
  },
  "values": [
    [0.36,0.48,-0.8],
    [-0.8,0.6,0],
    [0.48,0.64,0.6]
  ]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Implementation of ISO-11404 Array datatype. This defines an array of
  identical data components with a elementCount. Values are given as a block and can
  be encoded in different ways
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-array/schema.yaml#AbstractArray
- properties:
    type:
      const: Matrix
    referenceFrame:
      description: Frame of reference (usually spatial) with respect to which the
        coordinates of this matrix are expressed
      type: string
      format: uri-reference
    localFrame:
      description: Frame of reference whose position and orientation are provided
        by the transformation defined by this matrix
      type: string
      format: uri-reference
  required:
  - type
  - elementType

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/matrix/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/matrix/schema.yaml)

## Sources

* [swecommon/schemas/json/Matrix.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Matrix.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/matrix`

