
# DataRecord (Schema)

`ogc.api.connected-systems.swecommon.data-record` *v0.1*

Implementation of ISO-11404 Record datatype. This allows grouping (sequence) of data components which can themselves be simple types, records, arrays or choices

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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


## Examples

### Record1
#### json
```json
{
  "type": "DataRecord",
  "label": "Weather Data Record",
  "fields": [
    {
      "name": "time",
      "type": "Time",
      "definition": "http://www.opengis.net/def/property/OGC/0/SamplingTime",
      "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
      "label": "Sampling Time",
      "uom": {
        "href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
      }
    },
    {
      "name": "temperature",
      "type": "Quantity",
      "definition": "http://mmisw.org/ont/cf/parameter/air_temperature",
      "label": "Air Temperature",
      "uom": { "code": "Cel" }
    },
    {
      "name": "pressure",
      "type": "Quantity",
      "definition": "http://mmisw.org/ont/cf/parameter/air_pressure_at_mean_sea_level",
      "label": "Air Pressure",
      "uom": { "code": "mbar" }
    },
    {
      "name": "windSpeed",
      "type": "Quantity",
      "definition": "http://mmisw.org/ont/cf/parameter/wind_speed",
      "label": "Wind Speed",
      "uom": { "code": "km/h" }
    },
    {
      "name": "windDirection",
      "type": "Quantity",
      "definition": "http://mmisw.org/ont/cf/parameter/wind_to_direction",
      "label": "Wind Direction",
      "uom": { "code": "deg" }
    }
  ]
}
```


### Record2
#### json
```json
{
  "type": "DataRecord",
  "definition": "urn:x-ogc:def:property:CSM::RadialDistortionCoefficients",
  "label": "Radial Distortion Coefficients",
  "fields": [
    {
      "name": "k1",
      "type": "Quantity",
      "definition": "urn:x-ogc:def:property:CSM::DISTOR_RAD1",
      "label": "Coef k1",
      "uom": { "code": "mm-2" },
      "value": 1.92709e-5
    },
    {
      "name": "k2",
      "type": "Quantity",
      "definition": "urn:x-ogc:def:property:CSM::DISTOR_RAD2",
      "label": "Coef k2",
      "uom": { "code": "mm-2" },
      "value": -5.14206e-10
    },
    {
      "name": "k3",
      "type": "Quantity",
      "definition": "urn:x-ogc:def:property:CSM::DISTOR_RAD3",
      "label": "Coef k3",
      "uom": { "code": "mm-2" },
      "value": -3.33356e-12
    }
  ]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Implementation of ISO-11404 Record datatype. This allows grouping (sequence)
  of data components which can themselves be simple types, records, arrays or choices
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-data-component/schema.yaml
- properties:
    type:
      const: DataRecord
    fields:
      description: Definition of the record fields. Fields can be scalars or can themself
        be aggregates such as records, vectors, arrays, or choices.
      type: array
      minItems: 1
      items:
        allOf:
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#SoftNamedProperty
        - oneOf:
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AssociationAttributeGroup
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
  required:
  - type
  - fields

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-record/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-record/schema.yaml)

## Sources

* [swecommon/schemas/json/DataRecord.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/DataRecord.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/data-record`

