
# Procedure (SensorML) (Schema)

`ogc.api.connected-systems.part1.procedure-sensorml` *v0.1*

A Procedure (SensorML 3.0 JSON encoding): a specification of how observations are made or commands are executed, such as a sensor datasheet, method or protocol that systems implement.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

2 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `ins-sensor-sml.json`: `ProcedureTypeUris` does not allow `http://www.w3.org/ns/ssn-system/SensorKind` (used as `featureType`/`definition`).
- `sensor-datasheet-sml.json`: `ProcedureTypeUris` does not allow `http://www.w3.org/ns/ssn-system/SensorKind` (used as `featureType`/`definition`).


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- oneOf:
  - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/simple-process/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/aggregate-process/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/physical-component/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/physical-system/schema.yaml
- properties:
    definition:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/uris/schema.yaml#ProcedureTypeUris
    position:
      not: {}
    links:
      description: Links to related resources
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml
  required:
  - definition
  - uniqueId

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/procedure-sensorml/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/procedure-sensorml/schema.yaml)

## Sources

* [api/part1/openapi/schemas/sensorml/procedure.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/procedure.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/procedure-sensorml`

