<!-- generated -->
# DataStreamSchemaDef

Converted from [`api/part2/openapi/schemas/json/dataStreamSchemaDef.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/dataStreamSchemaDef.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `phenomenonTime` | `../common/sweCommonDefs.json#/$defs/Time` |  | Descriptor for the observation `phenomenonTime` property. If omitted, values for phenomenon time are not included in the datastream and are assumed to be equal to the observation result time. |
| `resultTime` | `../common/sweCommonDefs.json#/$defs/Time` |  | Descriptor for the observation `resultTime` property. If omitted, the result time is a fixed value provided in the datastream metadata and is not included in observations. |
| `featureOfInterest` | `../common/sweCommonDefs.json#/$defs/Category` |  | Descriptor for the `featureOfInterest` property. If omitted, the single fixed FOI is provided in the datastream metadata and is not included in observations. |
| `result` | `../common/sweCommonDefs.json#/$defs/AnyComponent` | yes | Descriptor for the observation `result` property. This describes the observed properties included in the result and how they are structured if the result is a record, a vector quantity or a coverage. |
| `parameters` | `../common/sweCommonDefs.json#/$defs/DataRecord` |  | Descriptor for the observation `parameters` property. If omitted, parameters are not included in the datastream. |

