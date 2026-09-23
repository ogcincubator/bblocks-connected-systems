
# DataStream_create (Schema)

`ogc.api.connected-systems.part2.data-stream-create` *v0.1*

Create payload for a DataStream: the DataStream properties plus the required `schema` (observation schema) describing the content of its observations.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# DataStream_create

Converted from [`api/part2/openapi/schemas/json/dataStream_create.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/dataStream_create.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `schema` | `observationSchema.json` | yes | Schema describing the content of observations in this datastream. The exact syntax of the schema depends on the encoding format. |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/data-stream/schema.yaml
- properties:
    schema:
      description: Schema describing the content of observations in this datastream.
        The exact syntax of the schema depends on the encoding format.
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema/schema.yaml
      writeOnly: true
  required:
  - schema

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/data-stream-create/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/data-stream-create/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/dataStream_create.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/dataStream_create.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/data-stream-create`

