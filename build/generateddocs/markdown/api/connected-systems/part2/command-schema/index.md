
# CommandSchema (Schema)

`ogc.api.connected-systems.part2.command-schema` *v0.1*

Schema describing the content of commands in a ControlStream; the syntax depends on the command format (JSON, SWE, Protobuf or other).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# CommandSchema

Converted from [`api/part2/openapi/schemas/json/commandSchema.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandSchema.json) in the OGC API - Connected Systems repository.


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
oneOf:
- title: JSON
  $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-json/schema.yaml
- title: SWE Common
  $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-swe/schema.yaml
- title: Protobuf
  $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-protobuf/schema.yaml
- title: Other format
  $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-any-other/schema.yaml
required:
- commandFormat

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/commandSchema.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandSchema.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/command-schema`

