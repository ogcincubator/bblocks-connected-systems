
# Command (Schema)

`ogc.api.connected-systems.part2.command` *v0.1*

A Command: a request sent through a ControlStream to a System to perform an action, carrying its parameters, issue time and execution constraints.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Command

Converted from [`api/part2/openapi/schemas/json/command.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/command.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | yes | Local ID of the command |
| `controlstream@id` | `string` | yes | Local ID of the control stream that the command is part of. This can be omitted when posting the command to a specific control stream URL. |
| `samplingFeature@id` | `string` |  | Local ID of the sampling feature that is the target of the command |
| `procedure@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the procedure/method used to process the command |
| `issueTime` | `../common/commonDefs.json#/$defs/TimeInstant` | yes | Time at which the command was issued. If omitted on creation, the server sets it to the time the request was received. |
| `executionTime` | `../common/commonDefs.json#/$defs/TimePeriod` |  | Time period during which the command was executed |
| `sender` | `string` |  | Identifier of the person or entity who submitted the command |
| `currentStatus` | `commandStatusCode.json` |  | Current status of the command |
| `parameters` |  | yes | Command parameters. Must be valid according to the schema provided in the control stream metadata |

## Known failing examples

2 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `command-ptz-create.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.
- `uav-mission.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### Command ptz
#### json
```json
{
  "id": "1125alnna75hafppknk9aefpvs",
  "controlstream@id": "hf62t0dotfd5k",
  "sender": "user01",
  "issueTime": "2021-03-15T04:53:34.248Z",
  "executionTime": [
    "2021-03-15T04:53:34.543Z",
    "2021-03-15T04:53:36.021Z"
  ],
  "currentStatus": "COMPLETED",
  "parameters": {
    "pan": -10.0,
    "tilt": 23.0,
    "zoom": 0.4
  }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  id:
    description: Local ID of the command
    type: string
    minLength: 1
    readOnly: true
  controlstream@id:
    description: Local ID of the control stream that the command is part of. This
      can be omitted when posting the command to a specific control stream URL.
    type: string
    minLength: 1
    readOnly: true
  samplingFeature@id:
    description: Local ID of the sampling feature that is the target of the command
    type: string
    minLength: 1
  procedure@link:
    description: Link to the procedure/method used to process the command
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
  issueTime:
    description: Time at which the command was issued. If omitted on creation, the
      server sets it to the time the request was received.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-instant/schema.yaml
    readOnly: true
  executionTime:
    description: Time period during which the command was executed
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
    readOnly: true
  sender:
    description: Identifier of the person or entity who submitted the command
    type: string
    minLength: 1
    readOnly: true
  currentStatus:
    description: Current status of the command
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-status-code/schema.yaml
    readOnly: true
  parameters:
    description: Command parameters. Must be valid according to the schema provided
      in the control stream metadata
required:
- id
- controlstream@id
- issueTime
- parameters

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/command.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/command.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/command`

