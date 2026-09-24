<!-- generated -->
# Time

Scalar component used to represent a time quantity either as ISO 8601 (e.g., 2004-04-18T12:03:04.6Z) or as a duration relative to a time of reference

Converted from [`swecommon/schemas/json/Time.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Time.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"Time"` | yes |  |
| `referenceTime` | `string` |  | Specifies the origin of the temporal reference frame as an ISO8601 date (used to specify time after an epoch that is to say in a custom frame) |
| `localFrame` | `string` |  | Temporal frame of reference whose origin is located by the value of this component |
| `uom` | `basicTypes.json#/$defs/UnitReference` | yes | Temporal unit of measure used to express the value of this data component |
| `constraint` | `basicTypes.json#/$defs/AllowedTimes` |  |  |
| `nilValues` | `basicTypes.json#/$defs/NilValuesTime` |  |  |
| `value` | `basicTypes.json#/$defs/DateTimeNumberOrSpecial` |  |  |

## Known failing examples

1 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `allowedTimes1.json`: `DateTimeNumberOrSpecial` is a `oneOf`: `+Infinity` matches both the special-number and the date-time branch.

## Examples

6 example(s) taken from the specification are included and validated against this schema.

