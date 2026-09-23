
# CategoryRange (Schema)

`ogc.api.connected-systems.swecommon.category-range` *v0.1*

Pair of categorical values used to specify a range in an ordinal reference system (specified by the code space)

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# CategoryRange

Pair of categorical values used to specify a range in an ordinal reference system (specified by the code space)

Converted from [`swecommon/schemas/json/CategoryRange.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/CategoryRange.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"CategoryRange"` | yes |  |
| `codeSpace` | `string` |  | Name of the dictionary defining an ordered set of values with respect to which the range is expressed (ordinal reference system) |
| `constraint` | `basicTypes.json#/$defs/AllowedTokens` |  |  |
| `nilValues` | `basicTypes.json#/$defs/NilValuesText` |  |  |
| `value` | `array` |  |  |

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### Category range1
#### json
```json
{
  "type": "CategoryRange",
  "definition": "http://sweet.jpl.nasa.gov/2.0/timeGeologic.owl#GeologicTime",
  "label": "Approximate Dating",
  "description": "Approximate geological dating expressed as a range of geological eras",
  "codeSpace": "http://sweet.jpl.nasa.gov/2.0/timeGeologic.owl#Era",
  "value": ["Paleozoic", "Mesozoic"]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Pair of categorical values used to specify a range in an ordinal reference
  system (specified by the code space)
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml
- properties:
    type:
      const: CategoryRange
    codeSpace:
      description: Name of the dictionary defining an ordered set of values with respect
        to which the range is expressed (ordinal reference system)
      type: string
      format: uri
    constraint:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AllowedTokens
    nilValues:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#NilValuesText
    value:
      type: array
      minItems: 2
      maxItems: 2
      items:
        type: string
  required:
  - type
  - definition
  - label

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/category-range/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/category-range/schema.yaml)

## Sources

* [swecommon/schemas/json/CategoryRange.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/CategoryRange.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/category-range`

