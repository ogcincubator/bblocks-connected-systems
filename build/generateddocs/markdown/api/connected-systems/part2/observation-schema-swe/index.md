
# ObservationSchemaSwe (Schema)

`ogc.api.connected-systems.part2.observation-schema-swe` *v0.1*

Observation schema for SWE Common encodings (text, binary, etc.), giving the record schema and the encoding rules of the observation stream.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ObservationSchemaSwe

Converted from [`api/part2/openapi/schemas/json/observationSchemaSwe.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observationSchemaSwe.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `obsFormat` | `string` | yes |  |
| `recordSchema` | `../common/sweCommonDefs.json#/$defs/AnyComponent` | yes |  |
| `encoding` |  | yes |  |

## Examples

3 example(s) taken from the specification are included and validated against this schema.


## Examples

### ObservationSchema geopose swejson
#### json
```json
{
  "obsFormat": "application/swe+json",
  "recordSchema": {
    "type": "DataRecord",
    "label": "Basic YPR Pose",
    "description": "Pose of platform (position + euler angles) in WGS84/ENU",
    "definition": "http://www.opengis.net/spec/geopose/1.0/req/basic-ypr",
    "fields": [
      {
        "name": "time",
        "type": "Time",
        "definition": "http://www.opengis.net/def/property/OGC/0/SamplingTime",
        "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
        "label": "Sampling Time",
        "uom": {
          "href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
        }
      },
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
  },
  "encoding": {
    "type": "JSONEncoding"
  }
}
```


### ObservationSchema scalar swecsv
#### json
```json
{
  "obsFormat": "application/swe+csv",
  "recordSchema": {
    "type": "DataRecord",
    "fields": [
      {
        "name": "time",
        "type": "Time",
        "definition": "http://www.opengis.net/def/property/OGC/0/SamplingTime",
        "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
        "label": "Sampling Time",
        "uom": {
          "href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
        }
      },
      {
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
    ]
  },
  "encoding": {
    "type": "TextEncoding",
    "collapseWhiteSpaces": true,
    "decimalSeparator": ".",
    "tokenSeparator": ",",
    "blockSeparator": "\n"
  }
}
```


### ObservationSchema scalar swejson
#### json
```json
{
  "obsFormat": "application/swe+json",
  "recordSchema": {
    "type": "DataRecord",
    "fields": [
      {
        "name": "time",
        "type": "Time",
        "definition": "http://www.opengis.net/def/property/OGC/0/SamplingTime",
        "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
        "label": "Sampling Time",
        "uom": {
          "href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
        }
      },
      {
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
    ]
  },
  "encoding": {
    "type": "JSONEncoding"
  }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  obsFormat:
    type: string
  recordSchema:
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
  encoding: {}
required:
- obsFormat
- recordSchema
- encoding
oneOf:
- title: SWE JSON
  properties:
    obsFormat:
      const: application/swe+json
    encoding:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#JSONEncoding
- title: SWE Text
  properties:
    obsFormat:
      const: application/swe+text
    encoding:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#TextEncoding
- title: SWE CSV
  properties:
    obsFormat:
      const: application/swe+csv
    encoding:
      allOf:
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#TextEncoding
      - properties:
          tokenSeparator:
            const: ','
          blockSeparator:
            const: '

              '
- title: SWE Binary
  properties:
    obsFormat:
      const: application/swe+binary
    encoding:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#BinaryEncoding

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-swe/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-swe/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/observationSchemaSwe.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observationSchemaSwe.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/observation-schema-swe`

