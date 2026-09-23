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

