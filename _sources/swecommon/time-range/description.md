<!-- generated -->
# TimeRange

Time value pair for specifying a time range (can be a decimal or ISO 8601)

Converted from [`swecommon/schemas/json/TimeRange.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/TimeRange.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"TimeRange"` | yes |  |
| `referenceTime` | `string` |  | Specifies the origin of the temporal reference frame as an ISO8601 date (used to specify time after an epoch that is to say in a custom frame) |
| `localFrame` | `string` |  | Temporal frame of reference whose origin is located by the value of this component |
| `uom` | `basicTypes.json#/$defs/UnitReference` | yes | Temporal unit of measure used to express the value of this data component |
| `constraint` | `basicTypes.json#/$defs/AllowedTimes` |  |  |
| `nilValues` | `basicTypes.json#/$defs/NilValuesTime` |  |  |
| `value` | `array` |  |  |

## Examples

1 example(s) taken from the specification are included and validated against this schema.

