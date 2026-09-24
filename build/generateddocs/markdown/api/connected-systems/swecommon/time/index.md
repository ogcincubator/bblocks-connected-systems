
# Time (Schema)

`ogc.api.connected-systems.swecommon.time` *v0.1*

Scalar component used to represent a time quantity either as ISO 8601 (e.g., 2004-04-18T12:03:04.6Z) or as a duration relative to a time of reference

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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


## Examples

### AllowedTimes1
#### json
```json
{
  "type": "Time",
  "definition": "http://www.opengis.net/def/property/OGC/0/SamplingTime",
  "referenceFrame": "http://www.opengis.net/def/trs/USNO/0/GPS",
  "label": "Acquisition Time",
  "uom": {
    "href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
  },
  "constraint": {
    "intervals": [["2009-01-01T00:00:00Z", "+Infinity"]]
  }
}
```


### AllowedTimes2
#### json
```json
{
  "type": "Time",
  "definition": "http://www.opengis.net/def/property/OGC/0/SamplingTime",
  "referenceFrame": "urn:org:systems:001#SCAN-START-TIME",
  "label": "Lidar Pulse Time",
  "description": "Time stamp of LiDAR pulse relative to start of scan",
  "uom": { "code": "ms" },
  "constraint": {
    "intervals": [[0, 1e6]]
  }
}
```


### Time1
#### json
```json
{
  "type": "Time",
  "definition": "http://www.opengis.net/def/property/OGC/0/SamplingTime",
  "referenceFrame": "http://www.opengis.net/def/trs/USNO/0/GPS",
  "label": "Sampling Time",
  "description": "Time at which the measurement was made",
  "uom": {
    "href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
  },
  "value": "2009-11-05T16:29:26Z"
}
```


### Time2
#### json
```json
{
  "type": "Time",
  "definition": "http://www.opengis.net/def/property/OGC/0/RunTime",
  "referenceTime": "1970-01-01T00:00:00Z",
  "label": "Model Run Time",
  "description": "Run time of the model expressed as a Unix time",
  "uom": {"code": "s" },
  "value": 1257415633
}
```


### Time3
#### json
```json
{
  "type": "Time",
  "definition": "http://www.opengis.net/def/property/OGC-EO/0/MissionStartTime",
  "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
  "localFrame": "urn:org:systems:001#MISSION-START-TIME",
  "label": "Flight Time",
  "description": "Time at take-off in UTC",
  "uom": {
    "href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
  },
  "value": "2009-01-26T10:21:45+01:00"
}
```


### Time4
#### json
```json
{
  "type": "Time",
  "definition": "http://www.opengis.net/def/property/OGC-EO/0/ScanStartTime",
  "referenceFrame": "urn:org:systems:001#MISSION-START-TIME",
  "localFrame": "urn:org:systems:001#SCAN-START-TIME",
  "label": "Scanline Time",
  "description": "Acquisition time of the scan line",
  "uom": { "code": "s" }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Scalar component used to represent a time quantity either as ISO 8601
  (e.g., 2004-04-18T12:03:04.6Z) or as a duration relative to a time of reference
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml
- properties:
    type:
      const: Time
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
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#DateTimeNumberOrSpecial
  required:
  - type
  - definition
  - label
  - uom

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/time/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/time/schema.yaml)

## Sources

* [swecommon/schemas/json/Time.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Time.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/time`

