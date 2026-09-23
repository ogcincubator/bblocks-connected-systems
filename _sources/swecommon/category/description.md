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

