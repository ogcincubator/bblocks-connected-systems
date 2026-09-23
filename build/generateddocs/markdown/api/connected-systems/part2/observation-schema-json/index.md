
# ObservationSchemaJson (Schema)

`ogc.api.connected-systems.part2.observation-schema-json` *v0.1*

Observation schema for the JSON format (`application/json`), describing the observation result, parameters and related fields with SWE Common components.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ObservationSchemaJson

Converted from [`api/part2/openapi/schemas/json/observationSchemaJson.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observationSchemaJson.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `obsFormat` | `"application/json"` | yes |  |
| `parametersSchema` | `../common/sweCommonDefs.json#/$defs/DataRecord` |  | Record schema for the observation `parameters` property. If omitted, parameters are not included in the datastream. |
| `resultSchema` | `../common/sweCommonDefs.json#/$defs/AnyComponent` |  | Schema for the observation `result` property. This describes the observed properties included in the result and how they are structured if the result is a record, a vector quantity or a coverage. |
| `resultLink` | `object` |  | Encoding information in case the result is provided out-of-band via the `result@link` property. |

## Examples

4 example(s) taken from the specification are included and validated against this schema.


## Examples

### ObservationSchema geopose json
#### json
```json
{
  "obsFormat": "application/json",
  "resultSchema": {
    "type": "DataRecord",
    "label": "Basic YPR Pose",
    "description": "Pose of platform (position + euler angles) in WGS84/ENU",
    "definition": "http://www.opengis.net/spec/geopose/1.0/req/basic-ypr",
    "fields": [
      {
        "name": "position",
        "type": "Vector",
        "label": "Tangent Point Position",
        "definition": "http://sensorml.com/ont/swe/property/Location",
        "referenceFrame": "http://www.opengis.net/def/crs/EPSG/0/4979",
        "coordinates": [
          {
            "name": "lat",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/GeodeticLatitude",
            "axisID": "Lat",
            "label": "Geodetic Latitude",
            "uom": {
              "code": "deg"
            }
          },
          {
            "name": "lon",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/Longitude",
            "axisID": "Lon",
            "label": "Longitude",
            "uom": {
              "code": "deg"
            }
          },
          {
            "name": "h",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/HeightAboveEllipsoid",
            "axisID": "h",
            "label": "Ellipsoidal Height",
            "uom": {
              "code": "m"
            }
          }
        ]
      },
      {
        "name": "angles",
        "type": "Vector",
        "label": "Yaw Pitch Roll Angles",
        "description": "Euler angles with order of rotation yaw/pitch/roll in rotating frame",
        "definition": "http://sensorml.com/ont/swe/property/EulerAngles",
        "referenceFrame": "http://www.opengis.net/def/cs/OGC/0/ENU",
        "coordinates": [
          {
            "name": "yaw",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/YawAngle",
            "axisID": "Z",
            "label": "Yaw Angle",
            "description": "Heading angle from true north, measured clockwise",
            "uom": {
              "code": "deg"
            }
          },
          {
            "name": "pitch",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/PitchAngle",
            "axisID": "Y",
            "label": "Pitch Angle",
            "description": "Rotation around the lateral axis, up/down from the local horizontal plane (positive when pointing up)",
            "uom": {
              "code": "deg"
            }
          },
          {
            "name": "roll",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/RollAngle",
            "axisID": "X",
            "label": "Roll Angle",
            "description": "Rotation around the longitudinal axis",
            "uom": {
              "code": "deg"
            }
          }
        ]
      }
    ]
  }
}
```


### ObservationSchema imagelink json
#### json
```json
{
  "obsFormat": "application/json",
  "resultLink": {
    "mediaType": "image/png"
  }
}
```


### ObservationSchema scalar json
#### json
```json
{
  "obsFormat": "application/json",
  "resultSchema": {
    "name": "temp",
    "type": "Quantity",
    "definition": "http://mmisw.org/ont/cf/parameter/air_temperature",
    "label": "Room Temperature",
    "description": "Ambient air temperature measured inside the room",
    "uom": {
      "code": "Cel"
    },
    "nilValues": [
      { "reason": "http://www.opengis.net/def/nil/OGC/0/missing", "value": "NaN" },
      { "reason": "http://www.opengis.net/def/nil/OGC/0/BelowDetectionRange", "value": "-Infinity" },
      { "reason": "http://www.opengis.net/def/nil/OGC/0/AboveDetectionRange", "value": "+Infinity" }
    ]
  }
}
```


### ObservationSchema vector json
#### json
```json
{
  "obsFormat": "application/json",
  "resultSchema": {
    "name": "location",
    "type": "Vector",
    "label": "Platform Location",
    "definition": "http://sensorml.com/ont/swe/property/Location",
    "referenceFrame": "http://www.opengis.net/def/crs/EPSG/0/4979",
    "coordinates": [
      {
        "name": "lat",
        "type": "Quantity",
        "definition": "http://sensorml.com/ont/swe/property/GeodeticLatitude",
        "axisID": "Lat",
        "label": "Geodetic Latitude",
        "uom": {
          "code": "deg"
        }
      },
      {
        "name": "lon",
        "type": "Quantity",
        "definition": "http://sensorml.com/ont/swe/property/Longitude",
        "axisID": "Lon",
        "label": "Longitude",
        "uom": {
          "code": "deg"
        }
      },
      {
        "name": "h",
        "type": "Quantity",
        "definition": "http://sensorml.com/ont/swe/property/HeightAboveEllipsoid",
        "axisID": "h",
        "label": "Ellipsoidal Height",
        "uom": {
          "code": "m"
        }
      }
    ]
  }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  obsFormat:
    const: application/json
  parametersSchema:
    description: Record schema for the observation `parameters` property. If omitted,
      parameters are not included in the datastream.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-record/schema.yaml
  resultSchema:
    description: Schema for the observation `result` property. This describes the
      observed properties included in the result and how they are structured if the
      result is a record, a vector quantity or a coverage.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
  resultLink:
    description: Encoding information in case the result is provided out-of-band via
      the `result@link` property.
    type: object
    properties:
      mediaType:
        description: Media type of out-of-band resources obtained by dereferencing
          the result links
        type: string
    required:
    - mediaType
required:
- obsFormat
oneOf:
- title: Inline Result
  required:
  - resultSchema
- title: Result Link
  required:
  - resultLink

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-json/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-json/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/observationSchemaJson.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observationSchemaJson.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/observation-schema-json`

