
# DataStreamSchemaDef (Schema)

`ogc.api.connected-systems.part2.data-stream-schema-def` *v0.1*

Schema definition of the observation record of a DataStream, describing phenomenon time, result time, feature of interest, result and parameters with SWE Common components.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# DataStreamSchemaDef

Converted from [`api/part2/openapi/schemas/json/dataStreamSchemaDef.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/dataStreamSchemaDef.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `phenomenonTime` | `../common/sweCommonDefs.json#/$defs/Time` |  | Descriptor for the observation `phenomenonTime` property. If omitted, values for phenomenon time are not included in the datastream and are assumed to be equal to the observation result time. |
| `resultTime` | `../common/sweCommonDefs.json#/$defs/Time` |  | Descriptor for the observation `resultTime` property. If omitted, the result time is a fixed value provided in the datastream metadata and is not included in observations. |
| `featureOfInterest` | `../common/sweCommonDefs.json#/$defs/Category` |  | Descriptor for the `featureOfInterest` property. If omitted, the single fixed FOI is provided in the datastream metadata and is not included in observations. |
| `result` | `../common/sweCommonDefs.json#/$defs/AnyComponent` | yes | Descriptor for the observation `result` property. This describes the observed properties included in the result and how they are structured if the result is a record, a vector quantity or a coverage. |
| `parameters` | `../common/sweCommonDefs.json#/$defs/DataRecord` |  | Descriptor for the observation `parameters` property. If omitted, parameters are not included in the datastream. |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  phenomenonTime:
    description: Descriptor for the observation `phenomenonTime` property. If omitted,
      values for phenomenon time are not included in the datastream and are assumed
      to be equal to the observation result time.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/time/schema.yaml
  resultTime:
    description: Descriptor for the observation `resultTime` property. If omitted,
      the result time is a fixed value provided in the datastream metadata and is
      not included in observations.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/time/schema.yaml
  featureOfInterest:
    description: Descriptor for the `featureOfInterest` property. If omitted, the
      single fixed FOI is provided in the datastream metadata and is not included
      in observations.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/category/schema.yaml
  result:
    description: Descriptor for the observation `result` property. This describes
      the observed properties included in the result and how they are structured if
      the result is a record, a vector quantity or a coverage.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
  parameters:
    description: Descriptor for the observation `parameters` property. If omitted,
      parameters are not included in the datastream.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-record/schema.yaml
required:
- result
oneOf:
- title: resultTime schema required
  required:
  - resultTime
- title: phenomenonTime schema required
  required:
  - phenomenonTime

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/data-stream-schema-def/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/data-stream-schema-def/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/dataStreamSchemaDef.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/dataStreamSchemaDef.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/data-stream-schema-def`

