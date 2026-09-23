
# Count (Schema)

`ogc.api.connected-systems.swecommon.count` *v0.1*

Scalar component with integer representation used for a discrete counting value

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Count

Scalar component with integer representation used for a discrete counting value

Converted from [`swecommon/schemas/json/Count.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Count.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"Count"` | yes |  |
| `constraint` | `basicTypes.json#/$defs/AllowedValues` |  |  |
| `nilValues` | `basicTypes.json#/$defs/NilValuesInteger` |  |  |
| `value` | `integer` |  |  |

## Examples

3 example(s) taken from the specification are included and validated against this schema.


## Examples

### AllowedValues2
#### json
```json
{
  "type": "Count",
  "definition": "http://www.opengis.net/def/property/OGC/0/NumberOfPixels",
  "label": "Image Width",
  "constraint": {
    "values": [256, 512, 1024]
  }
}
```


### Count1
#### json
```json
{
  "type": "Count",
  "definition": "http://www.opengis.net/def/property/OGC/0/NumberOfPixels",
  "label": "Row Size",
  "description": "Number of pixels in each row of the image",
  "value": 1024
}
```


### Nil values2
#### json
```json
{
  "type": "Count",
  "definition": "http://sweet.jpl.nasa.gov/2.0/physRadiation.owl#Radiance",
  "label": "Band 1",
  "nilValues": [
    { "reason": "http://www.opengis.net/def/nil/OGC/0/BelowDetectionRange", "value": 0 },
    { "reason": "http://www.opengis.net/def/nil/OGC/0/AboveDetectionRange", "value": 255 }
  ]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Scalar component with integer representation used for a discrete counting
  value
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml
- properties:
    type:
      const: Count
    constraint:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AllowedValues
    nilValues:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#NilValuesInteger
    value:
      type: integer
  required:
  - type
  - definition
  - label

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/count/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/count/schema.yaml)

## Sources

* [swecommon/schemas/json/Count.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Count.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/count`

