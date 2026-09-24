
# DataStream (Schema)

`ogc.api.connected-systems.swecommon.data-stream` *v0.1*

Defines the structure of the element that will be repeated in the stream

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# DataStream

Defines the structure of the element that will be repeated in the stream

Converted from [`swecommon/schemas/json/DataStream.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/DataStream.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"DataStream"` | yes |  |
| `elementType` |  | yes | Definition and structure of one stream element |
| `encoding` |  | yes | Method used to encode the stream values |
| `values` | `basicTypes.json#/$defs/AssociationAttributeGroup` |  | Encoded values for the stream (can be out of band) |

## Known issues in the source

This block is a faithful copy of the upstream file, which has the following mismatches with the examples of the specification (see `SCHEMA-FIXES.md`):

- The DataStream example does not validate: the first field of `elementType` has no `name`, which is required. Possible resolution: add `"name": "time"` to the example.
- The DataStream example does not validate: the first field of `elementType` has no `name`, which is required. Possible resolution: add `"name": "time"` to the example.

## Known failing examples

1 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `datastream1.json`: The first field of `elementType` has no `name`, which is required (this is an example bug, not a schema bug).

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### Datastream1
#### json
```json
{
  "type": "DataStream",
  "label": "Aircraft Navigation",
  "elementType": {
    "name": "navData",
    "type": "DataRecord",
    "fields": [
      {
        "type": "Time",
        "definition": "http://www.opengis.net/def/property/OGC/0/SamplingTime",
        "referenceFrame": "http://www.opengis.net/def/trs/USNO/0/GPS",
        "referenceTime": "1970-01-01T00:00:00Z",
        "label": "Sampling Time",
        "uom": { "code": "s" }
      },
      {
        "name": "location",
        "type": "Vector",
        "definition": "http://www.opengis.net/def/property/OGC/0/PlatformLocation",
        "referenceFrame": "http://www.opengis.net/def/crs/EPSG/0/4979",
        "label": "Platform Location",
        "coordinates": [
          {
            "name": "lat",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/GeodeticLatitude",
            "label": "Latitude",
            "axisID": "Lat",
            "uom": { "code": "deg" }
          },
          {
            "name": "lon",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/Longitude",
            "label": "Longitude",
            "axisID": "Lon",
            "uom": { "code": "deg" }
          },
          {
            "name": "alt",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/HeightAboveEllipsoid",
            "label": "Altitude",
            "axisID": "h",
            "uom": { "code": "m" }
          }
        ]
      },
      {
        "name": "attitude",
        "type": "Vector",
        "definition": "http://www.opengis.net/def/property/OGC/0/PlatformOrientation",
        "referenceFrame": "http://www.opengis.net/def/cs/OGC/0/ENU",
        "label": "Platform Attitude",
        "coordinates": [
          {
            "name": "heading",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/TrueHeading",
            "label": "Heading",
            "axisID": "Z",
            "uom": { "code": "deg" }
          },
          {
            "name": "pitch",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/PitchAngle",
            "label": "Pitch",
            "axisID": "X",
            "uom": { "code": "deg" }
          },
          {
            "name": "roll",
            "type": "Quantity",
            "definition": "http://sensorml.com/ont/swe/property/RollAngle",
            "label": "Roll",
            "axisID": "Y",
            "uom": { "code": "deg" }
          }
        ]
      }
    ]
  },
  "encoding": {
    "type": "TextEncoding",
    "tokenSeparator": ",",
    "blockSeparator": "\n",
    "decimalSeparator": "."
  }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Defines the structure of the element that will be repeated in the stream
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-swe-identifiable/schema.yaml
- properties:
    type:
      const: DataStream
    elementType:
      description: Definition and structure of one stream element
      allOf:
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#SoftNamedProperty
      - oneOf:
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AssociationAttributeGroup
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
    encoding:
      description: Method used to encode the stream values
      oneOf:
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#BinaryEncoding
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#TextEncoding
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#XMLEncoding
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#JSONEncoding
    values:
      description: Encoded values for the stream (can be out of band)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AssociationAttributeGroup
  required:
  - type
  - elementType
  - encoding

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-stream/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-stream/schema.yaml)

## Sources

* [swecommon/schemas/json/DataStream.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/DataStream.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/data-stream`

