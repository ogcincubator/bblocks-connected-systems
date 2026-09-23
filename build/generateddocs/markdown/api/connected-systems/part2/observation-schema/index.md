
# ObservationSchema (Schema)

`ogc.api.connected-systems.part2.observation-schema` *v0.1*

Schema describing the content of observations in a DataStream; the syntax depends on the observation format (JSON, SWE, Protobuf or other).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ObservationSchema

Converted from [`api/part2/openapi/schemas/json/observationSchema.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observationSchema.json) in the OGC API - Connected Systems repository.


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
oneOf:
- title: JSON
  $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-json/schema.yaml
- title: SWE Common
  $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-swe/schema.yaml
- title: Protobuf
  $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-protobuf/schema.yaml
- title: Other format
  $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-any-other/schema.yaml
required:
- obsFormat

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/observationSchema.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observationSchema.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/observation-schema`

