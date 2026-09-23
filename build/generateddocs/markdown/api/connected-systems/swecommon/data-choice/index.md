
# DataChoice (Schema)

`ogc.api.connected-systems.swecommon.data-choice` *v0.1*

Implementation of a choice of two or more Data Components (also called disjoint union)

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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


## Examples

### Choice1
#### json
```json
{
  "type": "DataChoice",
  "label": "Weather Data Message",
  "items": [
    {
      "name": "TEMP",
      "type": "DataRecord",
      "label": "Temperature Measurement",
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
          "name": "temp",
          "type": "Quantity",
          "definition": "http://mmisw.org/ont/cf/parameter/air_temperature",
          "label": "Air Temperature",
          "uom": { "code": "Cel" }
        }
      ]
    },
    {
      "name": "PRESS",
      "type": "DataRecord",
      "label": "Pressure Measurement",
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
          "name": "press",
          "type": "Quantity",
          "definition": "http://mmisw.org/ont/cf/parameter/air_pressure_at_mean_sea_level",
          "label": "Air Pressure",
          "uom": { "code": "HPa" }
        }
      ]
    }
  ]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Implementation of a choice of two or more Data Components (also called
  disjoint union)
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-data-component/schema.yaml
- properties:
    type:
      const: DataChoice
    choiceValue:
      description: This category component marks the data stream element that will
        indicate the actual choice made. Possible choices are listed in the Category
        constraint section as an enumeration and should map to item names.
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/category/schema.yaml
    items:
      description: Definition of the choice items. Items can be of any component types
      type: array
      items:
        allOf:
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#SoftNamedProperty
        - oneOf:
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AssociationAttributeGroup
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
  required:
  - type
  - items

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-choice/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-choice/schema.yaml)

## Sources

* [swecommon/schemas/json/DataChoice.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/DataChoice.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/data-choice`

