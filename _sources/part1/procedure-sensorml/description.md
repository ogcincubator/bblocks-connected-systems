<!-- generated -->
# Procedure (SensorML)

Converted from [`api/part1/openapi/schemas/sensorml/procedure.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/procedure.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `definition` | `../common/uris.json#/$defs/ProcedureTypeUris` | yes |  |
| `position` |  |  |  |
| `links` | `../common/links.json` |  | Links to related resources |

## Known failing examples

2 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `ins-sensor-sml.json`: `ProcedureTypeUris` does not allow `http://www.w3.org/ns/ssn-system/SensorKind` (used as `featureType`/`definition`).
- `sensor-datasheet-sml.json`: `ProcedureTypeUris` does not allow `http://www.w3.org/ns/ssn-system/SensorKind` (used as `featureType`/`definition`).

## Examples

2 example(s) taken from the specification are included and validated against this schema.

