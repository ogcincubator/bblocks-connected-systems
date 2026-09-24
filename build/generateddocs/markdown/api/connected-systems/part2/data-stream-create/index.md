
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

## Known failing examples

1 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `datastream-simple-create.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### Datastream simple create
#### json
```json
{
  "name": "Indoor Thermometer 001 - Living Room Temperature",
  "description": "Indoor temperature measured on the south wall of the living room at 1.5m above the floor",
  "featureOfInterest@link": {
    "href": "https://data.example.org/api/collections/buildings/items/754",
    "title": "My House"
  },
  "samplingFeature@link": {
    "href": "https://data.example.org/api/samplingFeatures/4478",
    "title": "Thermometer Sampling Point"
  },
  "schema": {
    "obsFormat": "application/json",
    "resultSchema": {
      "name": "temp",
      "type": "Quantity",
      "definition": "http://mmisw.org/ont/cf/parameter/air_temperature",
      "label": "Room Temperature",
      "description": "Ambient air temperature measured inside the room",
      "uom": {
        "code": "Cel"
      },
      "nilValues": [
        { "reason": "http://www.opengis.net/def/nil/OGC/0/missing", "value": "NaN" },
        { "reason": "http://www.opengis.net/def/nil/OGC/0/BelowDetectionRange", "value": "-Infinity" },
        { "reason": "http://www.opengis.net/def/nil/OGC/0/AboveDetectionRange", "value": "+Infinity" }
      ]
    }
  }
}
```

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

