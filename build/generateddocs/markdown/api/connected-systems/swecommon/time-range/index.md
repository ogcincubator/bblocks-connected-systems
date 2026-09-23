
# TimeRange (Schema)

`ogc.api.connected-systems.swecommon.time-range` *v0.1*

Time value pair for specifying a time range (can be a decimal or ISO 8601)

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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


## Examples

### Time range1
#### json
```json
{
  "type": "TimeRange",
  "definition": "http://www.opengis.net/def/property/EO/0/SurveyPeriod",
  "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
  "label": "Survey Period",
  "uom": {
    "href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
  },
  "value": ["2008-01-05T11:02:54Z", "2009-11-05T16:29:26Z"]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Time value pair for specifying a time range (can be a decimal or ISO
  8601)
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml
- properties:
    type:
      const: TimeRange
    referenceTime:
      description: Specifies the origin of the temporal reference frame as an ISO8601
        date (used to specify time after an epoch that is to say in a custom frame)
      type: string
      format: date-time
    localFrame:
      description: Temporal frame of reference whose origin is located by the value
        of this component
      type: string
      format: uri
    uom:
      description: Temporal unit of measure used to express the value of this data
        component
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#UnitReference
    constraint:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AllowedTimes
    nilValues:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#NilValuesTime
    value:
      type: array
      minItems: 2
      maxItems: 2
      items:
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#DateTimeNumberOrSpecial
  required:
  - type
  - definition
  - label
  - uom

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/time-range/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/time-range/schema.yaml)

## Sources

* [swecommon/schemas/json/TimeRange.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/TimeRange.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/time-range`

