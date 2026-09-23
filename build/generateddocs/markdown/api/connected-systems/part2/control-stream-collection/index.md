
# ControlStreamCollection (Schema)

`ogc.api.connected-systems.part2.control-stream-collection` *v0.1*

Paged collection of ControlStream resources as returned by list queries, with the items plus navigation `links`.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ControlStreamCollection

Converted from [`api/part2/openapi/schemas/json/controlStreamCollection.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/controlStreamCollection.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `items` | `array` | yes |  |
| `links` | `../common/commonDefs.json#/$defs/Links` |  | Links to related resources (including paging) |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  items:
    type: array
    items:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/control-stream/schema.yaml
  links:
    description: Links to related resources (including paging)
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml
required:
- items

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/control-stream-collection/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/control-stream-collection/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/controlStreamCollection.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/controlStreamCollection.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/control-stream-collection`

