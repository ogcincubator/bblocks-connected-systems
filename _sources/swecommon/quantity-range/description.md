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

