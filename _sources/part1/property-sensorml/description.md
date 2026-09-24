<!-- generated -->
# Property (SensorML)

Converted from [`api/part1/openapi/schemas/sensorml/property.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/property.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `links` | `../common/links.json` |  | Links to related resources |

## Known failing examples

9 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `air-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `avg-cpu-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `combustion-chamber-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `daily-avg-air-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `engine-power.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `engine-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `received-rf-power-xband.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `received-rf-power.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `water-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.

