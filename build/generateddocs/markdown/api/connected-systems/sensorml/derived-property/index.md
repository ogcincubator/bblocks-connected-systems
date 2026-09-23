
# DerivedProperty (Schema)

`ogc.api.connected-systems.sensorml.derived-property` *v0.1*

DerivedProperty schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# DerivedProperty

Converted from [`sensorml/schemas/json/DerivedProperty.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/DerivedProperty.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `uniqueId` | `string` |  | Unique identifier of the property |
| `label` |  | yes |  |
| `description` |  |  |  |
| `baseProperty` | `string` | yes | URI pointing to the definition of the base property this property is derived from |
| `objectType` | `string` |  | URI pointing to the type of entity that the base property applies to |
| `statistic` | `string` |  | URI pointing to the definition of the statistic applied to the base property values |
| `qualifiers` | `array` |  | Additional qualifiers for the property (e.g., frequency range, measurement height, medium, etc.) |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-swe-identifiable/schema.yaml
- properties:
    uniqueId:
      description: Unique identifier of the property
      type: string
      format: uri
      example: urn:example:property:avg-cpu-temp
    label:
      example: Average CPU Temp
    description:
      example: Hourly average of the CPU temperature
    baseProperty:
      description: URI pointing to the definition of the base property this property
        is derived from
      type: string
      format: uri
      example: https://qudt.org/vocab/quantitykind/Temperature
    objectType:
      description: URI pointing to the type of entity that the base property applies
        to
      type: string
      format: uri
      example: http://dbpedia.org/resource/Central_processing_unit
    statistic:
      description: URI pointing to the definition of the statistic applied to the
        base property values
      type: string
      format: uri
      example: http://sensorml.com/ont/x-stats/HourlyMean
    qualifiers:
      description: Additional qualifiers for the property (e.g., frequency range,
        measurement height, medium, etc.)
      type: array
      minItems: 1
      items:
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnySimpleComponent
  required:
  - label
  - baseProperty

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/derived-property/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/derived-property/schema.yaml)

## Sources

* [sensorml/schemas/json/DerivedProperty.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/DerivedProperty.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/derived-property`

