
# AbstractDataComponent (Schema)

`ogc.api.connected-systems.swecommon.abstract-data-component` *v0.1*

Abstract base class for all data components

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# AbstractDataComponent

Abstract base class for all data components

Converted from [`swecommon/schemas/json/AbstractDataComponent.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/AbstractDataComponent.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `string` |  |  |
| `updatable` | `boolean` |  | Specifies if the value of a data component can be updated externally (i.e., is variable) |
| `optional` | `boolean` |  | Specifies if the data for this component can be omitted in the datastream |
| `definition` | `string` |  | The definition of the property whose value is provided by this component (semantic link) |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Abstract base class for all data components
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-swe-identifiable/schema.yaml
- properties:
    type:
      type: string
    updatable:
      description: Specifies if the value of a data component can be updated externally
        (i.e., is variable)
      type: boolean
      default: false
    optional:
      description: Specifies if the data for this component can be omitted in the
        datastream
      type: boolean
      default: false
    definition:
      description: The definition of the property whose value is provided by this
        component (semantic link)
      type: string
      format: uri

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-data-component/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-data-component/schema.yaml)

## Sources

* [swecommon/schemas/json/AbstractDataComponent.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/AbstractDataComponent.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/abstract-data-component`

