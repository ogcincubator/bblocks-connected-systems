
# QuantityRange (Schema)

`ogc.api.connected-systems.swecommon.quantity-range` *v0.1*

Decimal pair for specifying a quantity range with a unit of measure

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# QuantityRange

Decimal pair for specifying a quantity range with a unit of measure

Converted from [`swecommon/schemas/json/QuantityRange.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/QuantityRange.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"QuantityRange"` | yes |  |
| `uom` | `basicTypes.json#/$defs/UnitReference` | yes | Unit of measure used to express the value of this data component |
| `constraint` | `basicTypes.json#/$defs/AllowedValues` |  |  |
| `nilValues` | `basicTypes.json#/$defs/NilValuesNumber` |  |  |
| `value` | `array` |  |  |

## Examples

2 example(s) taken from the specification are included and validated against this schema.


## Examples

### Quantity range1
#### json
```json
{
  "type": "QuantityRange",
  "definition": "http://mmisw.org/ont/mmi/device/OperationalRange",
  "label": "Operational Range",
  "description": "Operational temperature range of the cryogenic thermometer",
  "uom": { "code": "K" },
  "value": [10, 300]
}
```


### Quantity range2
#### json
```json
{
  "type": "QuantityRange",
  "definition": "http://mmisw.org/ont/mmi/device/OperationalRange",
  "label": "Operational Range",
  "description": "Operational temperature range of the cryogenic thermometer",
  "uom": { "code": "K" },
  "value": [10, 300]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Decimal pair for specifying a quantity range with a unit of measure
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml
- properties:
    type:
      const: QuantityRange
    uom:
      description: Unit of measure used to express the value of this data component
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#UnitReference
    constraint:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AllowedValues
    nilValues:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#NilValuesNumber
    value:
      type: array
      minItems: 2
      maxItems: 2
      items:
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#NumberOrSpecial
  required:
  - type
  - definition
  - label
  - uom

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/quantity-range/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/quantity-range/schema.yaml)

## Sources

* [swecommon/schemas/json/QuantityRange.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/QuantityRange.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/quantity-range`

