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

