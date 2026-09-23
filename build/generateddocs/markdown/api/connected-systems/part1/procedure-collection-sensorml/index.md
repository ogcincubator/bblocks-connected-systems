
# ProcedureCollection (SensorML) (Schema)

`ogc.api.connected-systems.part1.procedure-collection-sensorml` *v0.1*

Paged collection of Procedure resources (SensorML encoding) as returned by list queries, with the items plus navigation `links`.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ProcedureCollection (SensorML)

Converted from [`api/part1/openapi/schemas/sensorml/procedureCollection.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/procedureCollection.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `items` | `procedureArray.json` | yes |  |
| `links` | `../common/links.json` |  | Links to related resources (including paging) |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  items:
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/procedure-array-sensorml/schema.yaml
  links:
    description: Links to related resources (including paging)
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml
required:
- items

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/procedure-collection-sensorml/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/procedure-collection-sensorml/schema.yaml)

## Sources

* [api/part1/openapi/schemas/sensorml/procedureCollection.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/procedureCollection.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/procedure-collection-sensorml`

