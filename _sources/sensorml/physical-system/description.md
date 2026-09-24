<!-- generated -->
# PhysicalSystem

Converted from [`sensorml/schemas/json/PhysicalSystem.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/PhysicalSystem.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"PhysicalSystem"` |  |  |
| `components` | `AggregateProcess.json#/$defs/ComponentList` |  | The list of sub-components |
| `connections` | `AggregateProcess.json#/$defs/ConnectionList` |  |  |

## Known failing examples

4 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `sensor_datasheet_with_modes.json`: `DescribedObject` requires `uniqueId`, which embedded components/modes/processes in the example do not have.
- `sensor_instance_with_parent_and_frame.json`: `timeInstantOrNow` is a `oneOf`: the string `now` matches both the `const` and the `date-time` branch.
- `system_with_components_and_connections.json`: `timeInstantOrNow` is a `oneOf`: the string `now` matches both the `const` and the `date-time` branch.
- `weather_station_system.json`: `DescribedObject` requires `uniqueId`, which embedded components/modes/processes in the example do not have.

## Examples

8 example(s) taken from the specification are included and validated against this schema.

