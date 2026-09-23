
# Vector (Schema)

`ogc.api.connected-systems.swecommon.vector` *v0.1*

Implementation of a mathematical vector composed of a list of scalar coordinates expressed in the mandatory reference frame.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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


## Examples

### Vector1
#### json
```json
{
  "type": "Vector",
  "definition": "http://www.opengis.net/def/property/OGC/0/PlatformLocation",
  "referenceFrame": "http://www.opengis.net/def/crs/EPSG/0/4326",
  "label": "Platform Location",
  "coordinates": [
    {
      "name": "lat",
      "type": "Quantity",
      "definition": "http://sensorml.com/ont/swe/property/GeodeticLatitude",
      "label": "Latitude",
      "axisID": "Lat",
      "uom": { "code": "deg" },
      "value": 45.36
    },
    {
      "name": "lon",
      "type": "Quantity",
      "definition": "http://sensorml.com/ont/swe/property/Longitude",
      "label": "Longitude",
      "axisID": "Lon",
      "uom": { "code": "deg" },
      "value": 5.2
    }
  ]
}
```


### Vector2
#### json
```json
{
  "type": "Vector",
  "definition": "http://qudt.org/vocab/quantitykind/LinearVelocity",
  "referenceFrame": "http://www.opengis.net/def/crs/OGC/0/ECI_J2000",
  "label": "Platform Velocity",
  "coordinates": [
    {
      "name": "vx",
      "type": "Quantity",
      "definition": "http://qudt.org/vocab/quantitykind/Speed",
      "label": "Velocity X",
      "uom": { "code": "m/s" }
    },
    {
      "name": "vy",
      "type": "Quantity",
      "definition": "http://qudt.org/vocab/quantitykind/Speed",
      "label": "Velocity Y",
      "uom": { "code": "m/s" }
    },
    {
      "name": "vz",
      "type": "Quantity",
      "definition": "http://qudt.org/vocab/quantitykind/Speed",
      "label": "Velocity Z",
      "uom": { "code": "m/s" }
    }
  ]
}
```


### Vector3
#### json
```json
{
  "type": "Vector",
  "definition": "http://sensorml.com/ont/swe/property/RotationQuaternion",
  "referenceFrame": "http://www.opengis.net/def/crs/OGC/0/ECI_J2000",
  "localFrame": "urn:org:systems:001#PLATFORM_FRAME",
  "label": "Platform Orientation",
  "coordinates": [
    {
      "name": "qx",
      "type": "Quantity",
      "definition": "http://sensorml.com/ont/swe/property/Coordinate",
      "label": "QX",
      "uom": { "code": "1" }
    },
    {
      "name": "qy",
      "type": "Quantity",
      "definition": "http://sensorml.com/ont/swe/property/Coordinate",
      "label": "QY",
      "uom": { "code": "1" }
    },
    {
      "name": "qz",
      "type": "Quantity",
      "definition": "http://sensorml.com/ont/swe/property/Coordinate",
      "label": "QZ",
      "uom": { "code": "1" }
    },
    {
      "name": "qw",
      "type": "Quantity",
      "definition": "http://sensorml.com/ont/swe/property/Coordinate",
      "label": "QW",
      "uom": { "code": "1" }
    }
  ]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Implementation of a mathematical vector composed of a list of scalar
  coordinates expressed in the mandatory reference frame.
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-data-component/schema.yaml
- properties:
    type:
      const: Vector
    referenceFrame:
      description: Frame of reference (usually spatial) with respect to which the
        coordinates of this vector are expressed. A reference frame anchors a vector
        value to a real world datum.
      type: string
      format: uri-reference
    localFrame:
      description: Frame of reference whose origin is located by the coordinates of
        this vector
      type: string
      format: uri-reference
    coordinates:
      description: Definition of the coordinate provided as a data component with
        a numerical representation
      type: array
      items:
        allOf:
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#SoftNamedProperty
        - oneOf:
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/count/schema.yaml
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/quantity/schema.yaml
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/time/schema.yaml
  required:
  - type
  - definition
  - referenceFrame
  - label
  - coordinates

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/vector/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/vector/schema.yaml)

## Sources

* [swecommon/schemas/json/Vector.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Vector.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/vector`

