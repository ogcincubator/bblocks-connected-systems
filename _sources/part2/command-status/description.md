<!-- generated -->
# CommandStatus

Converted from [`api/part2/openapi/schemas/json/commandStatus.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandStatus.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | yes | Local identifier of the status report |
| `command@id` | `string` | yes | Local identifier of the command that this report applies to |
| `reportTime` | `../common/commonDefs.json#/$defs/TimeInstant` | yes | Time at which this report was generated. If omitted on creation, the server sets it to the time the request was received. |
| `statusCode` | `commandStatusCode.json` | yes | Current status code |
| `percentCompletion` | `number` |  | Current progress expressed as a percentage of total task execution |
| `executionTime` | `../common/commonDefs.json#/$defs/TimePeriod` |  | Time period during which the command was executed or is scheduled to be executed (depending on status code) |
| `message` | `string` |  | Human readable message providing more details on the current status (can be both an error or information message depending on the status code) |
| `results` | `array` |  | New result(s) of the command available at the time of the progress report (can be a partial result) |

## Known failing examples

2 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `command-status-inline-result-complex.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.
- `command-status-inline-result-simple.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.

## Examples

5 example(s) taken from the specification are included and validated against this schema.

