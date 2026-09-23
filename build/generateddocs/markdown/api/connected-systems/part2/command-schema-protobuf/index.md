
# CommandSchemaProtobuf (Schema)

`ogc.api.connected-systems.part2.command-schema-protobuf` *v0.1*

Command schema for the Protobuf format, describing command parameters using a Protobuf message definition.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# CommandSchemaProtobuf

Converted from [`api/part2/openapi/schemas/json/commandSchemaProtobuf.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandSchemaProtobuf.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `commandFormat` | `"application/x-protobuf"` | yes |  |
| `messageSchema` |  | yes | Protobuf schema provided as a string or as a link to an external proto file |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  commandFormat:
    const: application/x-protobuf
  messageSchema:
    description: Protobuf schema provided as a string or as a link to an external
      proto file
    oneOf:
    - title: Inline schema
      type: string
      minLength: 1
    - title: Link to external file
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
required:
- commandFormat
- messageSchema

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-protobuf/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema-protobuf/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/commandSchemaProtobuf.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandSchemaProtobuf.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/command-schema-protobuf`

