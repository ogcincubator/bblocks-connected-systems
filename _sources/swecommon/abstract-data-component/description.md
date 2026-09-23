<!-- generated -->
# AbstractDataComponent

Abstract base class for all data components

Converted from [`swecommon/schemas/json/AbstractDataComponent.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/AbstractDataComponent.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `string` |  |  |
| `updatable` | `boolean` |  | Specifies if the value of a data component can be updated externally (i.e., is variable) |
| `optional` | `boolean` |  | Specifies if the data for this component can be omitted in the datastream |
| `definition` | `string` |  | The definition of the property whose value is provided by this component (semantic link) |

