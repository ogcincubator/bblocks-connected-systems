
# ObservationSchemaAnyOther (Schema)

`ogc.api.connected-systems.part2.observation-schema-any-other` *v0.1*

Observation schema for any other observation format, identified by `obsFormat` and carrying free-form schema properties.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ObservationSchemaAnyOther

Converted from [`api/part2/openapi/schemas/json/observationSchemaAnyOther.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observationSchemaAnyOther.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `obsFormat` | `string` | yes |  |
| `any` |  |  | Any other properties to describe schema |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  obsFormat:
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
- obsFormat

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-any-other/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema-any-other/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/observationSchemaAnyOther.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observationSchemaAnyOther.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/observation-schema-any-other`

