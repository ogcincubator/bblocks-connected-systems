
# CommandSchemaAnyOther (Schema)

`ogc.api.connected-systems.part2.command-schema-any-other` *v0.1*

Command schema for any other command format, identified by `commandFormat` and carrying free-form schema properties.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# CommandSchemaAnyOther

Converted from [`api/part2/openapi/schemas/json/commandSchemaAnyOther.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandSchemaAnyOther.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `commandFormat` | `string` | yes |  |
| `any` |  |  | Any other properties to describe schema |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  commandFormat:
    type: string
    not:
      enum:
      - application/json
      - application/swe+json
      - application/swe+text
      - application/swe+binary
      - application/x-protobuf
  any:
    description: Any other properties to describe schema
required:
- commandFormat

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-any-other/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-any-other/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/commandSchemaAnyOther.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandSchemaAnyOther.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/command-schema-any-other`

