
# ObservationSchemaProtobuf (Schema)

`ogc.api.connected-systems.part2.observation-schema-protobuf` *v0.1*

Observation schema for the Protobuf format, describing the observation record using a Protobuf message definition.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ObservationSchemaProtobuf

Converted from [`api/part2/openapi/schemas/json/observationSchemaProtobuf.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observationSchemaProtobuf.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `obsFormat` | `"application/x-protobuf"` | yes |  |
| `messageSchema` |  | yes | Protobuf schema provided as a string or as a link to an external proto file |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  obsFormat:
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
- obsFormat
- messageSchema

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-protobuf/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-protobuf/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/observationSchemaProtobuf.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observationSchemaProtobuf.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/observation-schema-protobuf`

