<!-- generated -->
# Procedure (GeoJSON)

Converted from [`api/part1/openapi/schemas/geojson/procedure.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/procedure.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `geometry` | `null` |  |  |
| `properties` |  |  |  |

## Known failing examples

1 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `sensor-datasheet-geojson.json`: `ProcedureTypeUris` does not allow `http://www.w3.org/ns/ssn-system/SensorKind` (used as `featureType`/`definition`).

