<!-- generated -->
# DerivedProperty

Converted from [`sensorml/schemas/json/DerivedProperty.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/DerivedProperty.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `uniqueId` | `string` |  | Unique identifier of the property |
| `label` |  | yes |  |
| `description` |  |  |  |
| `baseProperty` | `string` | yes | URI pointing to the definition of the base property this property is derived from |
| `objectType` | `string` |  | URI pointing to the type of entity that the base property applies to |
| `statistic` | `string` |  | URI pointing to the definition of the statistic applied to the base property values |
| `qualifiers` | `array` |  | Additional qualifiers for the property (e.g., frequency range, measurement height, medium, etc.) |

