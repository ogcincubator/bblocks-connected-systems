
# ControlStream_create (Schema)

`ogc.api.connected-systems.part2.control-stream-create` *v0.1*

Create payload for a ControlStream: the ControlStream properties plus the required `schema` (command schema) describing the content of its commands.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ControlStream_create

Converted from [`api/part2/openapi/schemas/json/controlStream_create.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/controlStream_create.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `schema` | `commandSchema.json` | yes | Schema describing the content of commands in this control stream. The exact syntax of the schema depends on the encoding format. |

## Known failing examples

1 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `controlstream-ptz-create.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/control-stream/schema.yaml
- properties:
    schema:
      description: Schema describing the content of commands in this control stream.
        The exact syntax of the schema depends on the encoding format.
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-schema/schema.yaml
      writeOnly: true
  required:
  - schema

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/control-stream-create/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/control-stream-create/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/controlStream_create.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/controlStream_create.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/control-stream-create`

