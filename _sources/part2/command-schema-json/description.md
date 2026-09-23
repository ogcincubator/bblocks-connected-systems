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

