<!-- generated -->
# ObservationSchemaJson

Converted from [`api/part2/openapi/schemas/json/observationSchemaJson.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observationSchemaJson.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `obsFormat` | `"application/json"` | yes |  |
| `parametersSchema` | `../common/sweCommonDefs.json#/$defs/DataRecord` |  | Record schema for the observation `parameters` property. If omitted, parameters are not included in the datastream. |
| `resultSchema` | `../common/sweCommonDefs.json#/$defs/AnyComponent` |  | Schema for the observation `result` property. This describes the observed properties included in the result and how they are structured if the result is a record, a vector quantity or a coverage. |
| `resultLink` | `object` |  | Encoding information in case the result is provided out-of-band via the `result@link` property. |

## Examples

4 example(s) taken from the specification are included and validated against this schema.

