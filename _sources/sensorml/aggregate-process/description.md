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

## Known failing examples

1 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `process_chain.json`: `DescribedObject` requires `uniqueId`, which embedded components/modes/processes in the example do not have.

