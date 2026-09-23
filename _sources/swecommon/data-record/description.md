<!-- generated -->
# DataRecord

Implementation of ISO-11404 Record datatype. This allows grouping (sequence) of data components which can themselves be simple types, records, arrays or choices

Converted from [`swecommon/schemas/json/DataRecord.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/DataRecord.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"DataRecord"` | yes |  |
| `fields` | `array` | yes | Definition of the record fields. Fields can be scalars or can themself be aggregates such as records, vectors, arrays, or choices. |

## Examples

2 example(s) taken from the specification are included and validated against this schema.

