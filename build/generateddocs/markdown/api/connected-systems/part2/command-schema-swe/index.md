
# CommandSchemaSwe (Schema)

`ogc.api.connected-systems.part2.command-schema-swe` *v0.1*

Command schema for SWE Common encodings (text, binary, etc.), giving the record schema and encoding rules of the command stream.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# CommandSchemaSwe

Converted from [`api/part2/openapi/schemas/json/commandSchemaSwe.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandSchemaSwe.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `commandFormat` | `string` | yes |  |
| `recordSchema` | `../common/sweCommonDefs.json#/$defs/AnyComponent` | yes |  |
| `encoding` |  | yes |  |

## Examples

2 example(s) taken from the specification are included and validated against this schema.


## Examples

### CommandSchema ptz swecsv
#### json
```json
{
  "commandFormat": "application/swe+csv",
  "recordSchema": {
    "type": "DataRecord",
    "fields": [
      {
        "name": "time",
        "type": "Time",
        "definition": "http://www.opengis.net/def/property/OGC/0/IssueTime",
        "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
        "label": "Issue Time",
        "uom": {
          "href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
        }
      },
      {
        "name": "pan",
        "type": "Quantity",
        "definition": "http://sensorml.com/ont/swe/property/PanAngle",
        "label": "Pan Angle",
        "description": "Rotation of the camera around its vertical axis (i.e., causing the image to translate along its horizontal axis)",
        "uom": {
          "code": "deg"
        }
      },
      {
        "name": "tilt",
        "type": "Quantity",
        "definition": "http://sensorml.com/ont/swe/property/TiltAngle",
        "label": "Pan Angle",
        "description": "Rotation of the camera around its horizontal axis (i.e., causing the image to translate along its vertical axis)",
        "uom": {
          "code": "deg"
        }
      },
      {
        "name": "zoom",
        "type": "Quantity",
        "definition": "http://sensorml.com/ont/swe/property/ZoomFactor",
        "label": "Zoom Factor",
        "description": "Amount of zoom, 0 being the highest FOV and 100 being the lowest",
        "uom": {
          "code": "%"
        }
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


### CommandSchema ptz swejson
#### json
```json
{
  "commandFormat": "application/swe+json",
  "recordSchema": {
    "type": "DataRecord",
    "fields": [
      {
        "name": "time",
        "type": "Time",
        "definition": "http://www.opengis.net/def/property/OGC/0/IssueTime",
        "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
        "label": "Issue Time",
        "uom": {
          "href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
        }
      },
      {
        "name": "pan",
        "type": "Quantity",
        "definition": "http://sensorml.com/ont/swe/property/PanAngle",
        "label": "Pan Angle",
        "description": "Rotation of the camera around its vertical axis (i.e., causing the image to translate along its horizontal axis)",
        "uom": {
          "code": "deg"
        }
      },
      {
        "name": "tilt",
        "type": "Quantity",
        "definition": "http://sensorml.com/ont/swe/property/PanAngle",
        "label": "Tilt Angle",
        "description": "Rotation of the camera around its horizontal axis (i.e., causing the image to translate along its vertical axis)",
        "uom": {
          "code": "deg"
        }
      },
      {
        "name": "zoom",
        "type": "Quantity",
        "definition": "http://sensorml.com/ont/swe/property/ZoomFactor",
        "label": "Zoom Factor",
        "description": "Amount of zoom, 0 being the highest FOV and 100 being the lowest",
        "uom": {
          "code": "%"
        }
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
  commandFormat:
    type: string
  recordSchema:
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
  encoding: {}
required:
- commandFormat
- recordSchema
- encoding
oneOf:
- title: SWE JSON
  properties:
    commandFormat:
      const: application/swe+json
    encoding:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#JSONEncoding
- title: SWE Text
  properties:
    commandFormat:
      const: application/swe+text
    encoding:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#TextEncoding
- title: SWE CSV
  properties:
    commandFormat:
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
    commandFormat:
      const: application/swe+binary
    encoding:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#BinaryEncoding

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-swe/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-swe/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/commandSchemaSwe.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandSchemaSwe.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/command-schema-swe`

