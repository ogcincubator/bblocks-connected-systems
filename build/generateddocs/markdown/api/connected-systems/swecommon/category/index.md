
# Category (Schema)

`ogc.api.connected-systems.swecommon.category` *v0.1*

Scalar component used to represent a categorical value as a simple token identifying a term in a code space

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Category

Scalar component used to represent a categorical value as a simple token identifying a term in a code space

Converted from [`swecommon/schemas/json/Category.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Category.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"Category"` | yes |  |
| `codeSpace` | `string` |  | Name of the dictionary where the possible values for this component are listed and defined |
| `constraint` | `basicTypes.json#/$defs/AllowedTokens` |  |  |
| `nilValues` | `basicTypes.json#/$defs/NilValuesText` |  |  |
| `value` | `string` |  |  |

## Examples

3 example(s) taken from the specification are included and validated against this schema.


## Examples

### AllowedTokens2
#### json
```json
{
  "type": "Category",
  "definition": "http://www.opengis.net/def/property/OGC/0/SensorStatus",
  "label": "Sensor Status",
  "description": "Current connection status of the sensor",
  "constraint": {
    "values": [ "Off", "Stand-by", "Ready", "Busy" ]
  }
}
```


### Category1
#### json
```json
{
  "type": "Category",
  "definition": "http://sweet.jpl.nasa.gov/2.0/timeGeologic.owl#GeologicTime",
  "label": "Geological Period",
  "description": "Name of the geological period according to the nomenclature of the International Commission on Stratigraphy",
  "codeSpace": "http://sweet.jpl.nasa.gov/2.0/timeGeologic.owl#Period",
  "value": "Jurassic"
}
```


### Category2
#### json
```json
{
  "type": "Category",
  "definition": "http://sweet.jpl.nasa.gov/2.0/biol.owl#Species",
  "label": "Bird Species",
  "description": "Bird species according to the classification of the World Bird Database",
  "codeSpace": "http://www.birdlife.org/datazone/species/index.html"
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Scalar component used to represent a categorical value as a simple token
  identifying a term in a code space
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml
- properties:
    type:
      const: Category
    codeSpace:
      description: Name of the dictionary where the possible values for this component
        are listed and defined
      type: string
      format: uri
    constraint:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AllowedTokens
    nilValues:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#NilValuesText
    value:
      type: string
  required:
  - type
  - definition
  - label

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/category/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/category/schema.yaml)

## Sources

* [swecommon/schemas/json/Category.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Category.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/category`

