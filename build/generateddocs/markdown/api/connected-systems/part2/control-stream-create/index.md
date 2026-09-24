
# ControlStream_create (Schema)

`ogc.api.connected-systems.part2.control-stream-create` *v0.1*

Create payload for a ControlStream: the ControlStream properties plus the required `schema` (command schema) describing the content of its commands.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ControlStream_create

Converted from [`api/part2/openapi/schemas/json/controlStream_create.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/controlStream_create.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `schema` | `commandSchema.json` | yes | Schema describing the content of commands in this control stream. The exact syntax of the schema depends on the encoding format. |

## Known failing examples

1 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `controlstream-ptz-create.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### Controlstream ptz create
#### json
```json
{
  "name": "Garage Video Camera 001 - PTZ Control",
  "inputName": "ptz",
  "async": false,
  "schema": {
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
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/control-stream/schema.yaml
- properties:
    schema:
      description: Schema describing the content of commands in this control stream.
        The exact syntax of the schema depends on the encoding format.
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema/schema.yaml
      writeOnly: true
  required:
  - schema

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/control-stream-create/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/control-stream-create/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/controlStream_create.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/controlStream_create.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/control-stream-create`

