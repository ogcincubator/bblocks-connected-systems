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

