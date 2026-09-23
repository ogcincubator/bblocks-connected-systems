
# ControlStream (Schema)

`ogc.api.connected-systems.part2.control-stream` *v0.1*

A ControlStream: a channel through which commands are sent to a controllable System, describing the supported command parameters, result schema and formats.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ControlStream

Converted from [`api/part2/openapi/schemas/json/controlStream.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/controlStream.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `system@link` | `../common/commonDefs.json#/$defs/Link` | yes | Link to the system receiving the commands |
| `inputName` | `string` |  | Name of the system control input receiving data from this control stream |
| `procedure@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the procedure used to execute commands (only provided if all commands in the control stream share the same procedure) |
| `deployment@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the deployment during which the commands are/were received (only provided if all commands in the control stream share the same deployment) |
| `featureOfInterest@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the ultimate feature of interest (only provided if all commands in the control stream share the same feature of interest) |
| `samplingFeature@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the sampling feature (only provided if all commands in the control stream share the same sampling feature) |
| `controlledProperties` |  | yes |  |
| `issueTime` |  | yes |  |
| `executionTime` |  | yes |  |
| `live` |  | yes |  |
| `async` | `boolean` | yes | Flag indicating if the command channel processes commands asynchronously |
| `schema` | `commandSchema.json` |  | Schema describing the content of commands in this control stream. The exact syntax of the schema depends on the encoding format. |
| `links` | `../common/commonDefs.json#/$defs/Links` |  | Links to related resources |

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### Controlstream ptz
#### json
```json
{
  "id": "hf62t0dotfd5k",
  "name": "Garage Video Camera 001 - PTZ Control",
  "inputName": "ptz",
  "system@link": {
    "href": "https://data.example.org/api/systems/4722256",
    "uid": "urn:x-ogc:systems:CAM001",
    "title": "Garage Video Camera 001"
  },
  "issueTime": [
    "2012-06-29T14:32:34Z",
    "2012-06-29T14:37:34Z"
  ],
  "executionTime": [
    "2012-06-29T14:32:34Z",
    "2012-06-29T14:37:34Z"
  ],
  "controlledProperties": [
    {
      "definition": "http://sensorml.com/ont/swe/property/PanAngle",
      "label": "Pan Angle"
    },
    {
      "definition": "http://sensorml.com/ont/swe/property/TiltAngle",
      "label": "Tilt Angle"
    },
    {
      "definition": "http://sensorml.com/ont/swe/property/ZoomFactor",
      "label": "Zoom Factor"
    }
  ],
  "formats": [
    "application/json"
  ],
  "live": true,
  "async": false,
  "links": [
    {
      "rel": "commands",
      "href": "https://data.example.org/api/controls/hf62t0dotfd5k/commands"
    }
  ]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/base-stream/schema.yaml
- properties:
    system@link:
      description: Link to the system receiving the commands
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
      readOnly: true
    inputName:
      description: Name of the system control input receiving data from this control
        stream
      type: string
    procedure@link:
      description: Link to the procedure used to execute commands (only provided if
        all commands in the control stream share the same procedure)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    deployment@link:
      description: Link to the deployment during which the commands are/were received
        (only provided if all commands in the control stream share the same deployment)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    featureOfInterest@link:
      description: Link to the ultimate feature of interest (only provided if all
        commands in the control stream share the same feature of interest)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    samplingFeature@link:
      description: Link to the sampling feature (only provided if all commands in
        the control stream share the same sampling feature)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    controlledProperties:
      oneOf:
      - type: 'null'
      - description: List of properties that are controllable through this control
          stream
        type: array
        minItems: 1
        items:
          type: object
          properties:
            definition:
              type: string
              format: uri
            label:
              type: string
            description:
              type: string
      readOnly: true
    issueTime:
      oneOf:
      - type: 'null'
      - description: Time extent spanning all issue times of commands in this control
          stream
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
        readOnly: true
    executionTime:
      oneOf:
      - type: 'null'
      - description: Time extent spanning all execution times of commands in this
          control stream
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
        readOnly: true
    live:
      oneOf:
      - type: 'null'
      - description: Flag indicating if the command channel can currently accept commands
        type: boolean
        readOnly: true
    async:
      description: Flag indicating if the command channel processes commands asynchronously
      type: boolean
    schema:
      description: Schema describing the content of commands in this control stream.
        The exact syntax of the schema depends on the encoding format.
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema/schema.yaml
      writeOnly: true
    links:
      description: Links to related resources
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml
required:
- name
- system@link
- controlledProperties
- issueTime
- executionTime
- live
- async

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/control-stream/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/control-stream/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/controlStream.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/controlStream.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/control-stream`

