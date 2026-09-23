<!-- generated -->
# AggregateProcess

Converted from [`sensorml/schemas/json/AggregateProcess.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/AggregateProcess.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.sensorml.aggregate-process#ComponentList`:

- `ComponentList`
- `ConnectionList`

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"AggregateProcess"` |  |  |
| `components` | `#/$defs/ComponentList` |  | The list of sub-processes |
| `connections` | `#/$defs/ConnectionList` |  | The explicit definition of data links between outputs, inputs, and parameters of the components within an aggregate process. |

## Examples

1 example(s) taken from the specification are included and validated against this schema.

