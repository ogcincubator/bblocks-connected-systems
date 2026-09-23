
# Property (SensorML) (Schema)

`ogc.api.connected-systems.part1.property-sensorml` *v0.1*

A Property (SensorML 3.0 JSON encoding): a definition of an observable or controllable property (e.g. temperature, wind speed) that systems and procedures can reference.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Property (SensorML)

Converted from [`api/part1/openapi/schemas/sensorml/property.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/property.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `links` | `../common/links.json` |  | Links to related resources |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/derived-property/schema.yaml
- properties:
    links:
      description: Links to related resources
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml
  required:
  - uniqueId

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/property-sensorml/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/property-sensorml/schema.yaml)

## Sources

* [api/part1/openapi/schemas/sensorml/property.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/property.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/property-sensorml`

