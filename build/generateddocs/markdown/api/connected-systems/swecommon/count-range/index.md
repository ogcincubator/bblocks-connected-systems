
# CountRange (Schema)

`ogc.api.connected-systems.swecommon.count-range` *v0.1*

Integer pair used for specifying a count range

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# CountRange

Integer pair used for specifying a count range

Converted from [`swecommon/schemas/json/CountRange.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/CountRange.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"CountRange"` | yes |  |
| `constraint` | `basicTypes.json#/$defs/AllowedValues` |  |  |
| `nilValues` | `basicTypes.json#/$defs/NilValuesText` |  |  |
| `value` | `array` |  |  |

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### Count range1
#### json
```json
{
  "type": "CountRange",
  "definition": "http://www.opengis.net/def/property/OGC/0/ArrayIndex",
  "label": "Index Range",
  "value": [0, 3000]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Integer pair used for specifying a count range
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml
- properties:
    type:
      const: CountRange
    constraint:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AllowedValues
    nilValues:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#NilValuesText
    value:
      type: array
      minItems: 2
      maxItems: 2
      items:
        type: integer
  required:
  - type
  - definition
  - label

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/count-range/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/count-range/schema.yaml)

## Sources

* [swecommon/schemas/json/CountRange.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/CountRange.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/count-range`

