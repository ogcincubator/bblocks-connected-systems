
# CommandStatus (Schema)

`ogc.api.connected-systems.part2.command-status` *v0.1*

A CommandStatus report: the state of execution of a Command at a given report time, with status code, percent completion, message and any results.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

2 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `command-status-inline-result-complex.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.
- `command-status-inline-result-simple.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.

## Examples

3 example(s) taken from the specification are included and validated against this schema.


## Examples

### Command status accepted
#### json
```json
{
  "id": "rlg2905142qs5uvish4vktotffds2iss8aa0a00",
  "command@id": "1125alnna75hafppknk9aefpvs",
  "reportTime": "2021-03-15T04:53:34.348Z",
  "statusCode": "ACCEPTED"
}
```


### Command status completed
#### json
```json
{
  "id": "155rufq7aplr8id10839fc8d6u0ulqfu1bjfumo",
  "command@id": "1125alnna75hafppknk9aefpvs",
  "reportTime": "2021-03-15T04:53:36.021Z",
  "statusCode": "COMPLETED",
  "message": "Camera moved to new position"
}
```


### Command status result obs link
#### json
```json
{
  "id": "155rufq7aplr8id10839fc8d6u0ulqfu1bjfumo",
  "command@id": "1125alnna75hafppknk9aefpvs",
  "reportTime": "2021-03-15T04:53:36.021Z",
  "statusCode": "EXECUTING",
  "message": "New image acquired",
  "result": [
    {
      "observation@link": {
        "href": "https://data.example.org/api/observations/11g2s5ddggg7dogt5gs8949s",
        "type": "application/json"
      }
    }
  ]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  id:
    description: Local identifier of the status report
    type: string
    minLength: 1
    readOnly: true
  command@id:
    description: Local identifier of the command that this report applies to
    type: string
    minLength: 1
    readOnly: true
  reportTime:
    description: Time at which this report was generated. If omitted on creation,
      the server sets it to the time the request was received.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-instant/schema.yaml
    readOnly: true
  statusCode:
    description: Current status code
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-status-code/schema.yaml
  percentCompletion:
    description: Current progress expressed as a percentage of total task execution
    type: number
    minimum: 0
    maximum: 100
  executionTime:
    description: Time period during which the command was executed or is scheduled
      to be executed (depending on status code)
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
  message:
    description: Human readable message providing more details on the current status
      (can be both an error or information message depending on the status code)
    type: string
    minLength: 1
  results:
    description: New result(s) of the command available at the time of the progress
      report (can be a partial result)
    type: array
    items:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-result/schema.yaml
required:
- id
- command@id
- reportTime
- statusCode

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-status/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-status/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/commandStatus.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandStatus.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/command-status`

