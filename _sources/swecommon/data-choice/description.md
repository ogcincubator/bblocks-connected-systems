<!-- generated -->
# DataChoice

Implementation of a choice of two or more Data Components (also called disjoint union)

Converted from [`swecommon/schemas/json/DataChoice.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/DataChoice.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"DataChoice"` | yes |  |
| `choiceValue` | `Category.json` |  | This category component marks the data stream element that will indicate the actual choice made. Possible choices are listed in the Category constraint section as an enumeration and should map to item names. |
| `items` | `array` | yes | Definition of the choice items. Items can be of any component types |

## Examples

1 example(s) taken from the specification are included and validated against this schema.

