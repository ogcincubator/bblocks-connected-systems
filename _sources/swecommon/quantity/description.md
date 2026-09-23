<!-- generated -->
# Quantity

Scalar component with decimal representation and a unit of measure used to store value of a continuous quantity

Converted from [`swecommon/schemas/json/Quantity.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Quantity.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"Quantity"` | yes |  |
| `uom` | `basicTypes.json#/$defs/UnitReference` | yes | Unit of measure used to express the value of this data component |
| `constraint` | `basicTypes.json#/$defs/AllowedValues` |  |  |
| `nilValues` | `basicTypes.json#/$defs/NilValuesNumber` |  |  |
| `value` | `basicTypes.json#/$defs/NumberOrSpecial` |  |  |

## Examples

8 example(s) taken from the specification are included and validated against this schema.

