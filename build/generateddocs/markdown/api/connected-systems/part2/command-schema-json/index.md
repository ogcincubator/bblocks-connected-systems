
# CommandSchemaJson (Schema)

`ogc.api.connected-systems.part2.command-schema-json` *v0.1*

Command schema for the JSON format (`application/json`), defining the `parametersSchema` and optional result and feasibility result schemas with SWE Common components.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# CommandSchemaJson

Converted from [`api/part2/openapi/schemas/json/commandSchemaJson.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandSchemaJson.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `commandFormat` | `"application/json"` | yes |  |
| `parametersSchema` | `../common/sweCommonDefs.json#/$defs/AnyComponent` | yes | Schema for the command `parameters`. |
| `resultSchema` | `../common/sweCommonDefs.json#/$defs/AnyComponent` |  | Schema for the inline command results (if any). |
| `feasibilityResultSchema` | `../common/sweCommonDefs.json#/$defs/AnyComponent` |  | Schema for the feasibility results (if any). |

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### CommandSchema ptz json
#### json
```json
{
  "commandFormat": "application/json",
  "parametersSchema": {
    "type": "DataRecord",
    "fields": [
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
    const: application/json
  parametersSchema:
    description: Schema for the command `parameters`.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
  resultSchema:
    description: Schema for the inline command results (if any).
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
  feasibilityResultSchema:
    description: Schema for the feasibility results (if any).
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
required:
- commandFormat
- parametersSchema

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-json/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-json/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/commandSchemaJson.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandSchemaJson.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/command-schema-json`

