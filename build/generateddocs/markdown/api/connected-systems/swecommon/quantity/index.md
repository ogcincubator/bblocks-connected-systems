
# Quantity (Schema)

`ogc.api.connected-systems.swecommon.quantity` *v0.1*

Scalar component with decimal representation and a unit of measure used to store value of a continuous quantity

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Quantity

Scalar component with decimal representation and a unit of measure used to store value of a continuous quantity

Converted from [`swecommon/schemas/json/Quantity.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Quantity.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"Quantity"` | yes |  |
| `uom` | `basicTypes.json#/$defs/UnitReference` | yes | Unit of measure used to express the value of this data component |
| `constraint` | `basicTypes.json#/$defs/AllowedValues` |  |  |
| `nilValues` | `basicTypes.json#/$defs/NilValuesNumber` |  |  |
| `value` | `basicTypes.json#/$defs/NumberOrSpecial` |  |  |

## Examples

8 example(s) taken from the specification are included and validated against this schema.


## Examples

### AllowedValues1
#### json
```json
{
  "type": "Quantity",
  "definition": "http://qudt.org/vocab/quantitykind/Angle",
  "label": "Planar Angle",
  "uom": { "code": "deg" },
  "constraint": {
    "intervals": [[-180, 180]]
  }
}
```


### AllowedValues3
#### json
```json
{
  "type": "Quantity",
  "definition": "http://sensorml.com/ont/swe/property/GeodeticLatitude",
  "label": "Latitude",
  "uom": { "code": "deg" },
  "constraint": {
    "intervals": [[-90, 90]],
    "significantFigures": 6
  }
}
```


### AllowedValues4
#### json
```json
{
  "type": "Quantity",
  "definition": "http://qudt.org/vocab/quantitykind/RadialDistance",
  "label": "Radial Distance",
  "description": "Radial distance is always positive",
  "uom": { "code": "m" },
  "constraint": {
    "intervals": [[0, "+Infinity"]]
  }
}
```


### Nil values1
#### json
```json
{
  "type": "Quantity",
  "definition": "http://sweet.jpl.nasa.gov/2.0/physRadiation.owl#IonizingRadiation",
  "label": "Radiation Dose",
  "description": "Radiation dose measured by Gamma detector",
  "uom": { "code": "uR" },
  "nilValues": [
    { "reason": "http://www.opengis.net/def/nil/OGC/0/BelowDetectionRange", "value": "-Infinity" },
    { "reason": "http://www.opengis.net/def/nil/OGC/0/AboveDetectionRange", "value": "Infinity" }
  ]
}
```


### Quantity1
#### json
```json
{
  "type": "Quantity",
  "definition": "http://qudt.org/vocab/quantitykind/Temperature",
  "label": "Outside Temperature",
  "description": "Outside temperature taken at the top of the antenna",
  "uom": { "code": "Cel" },
  "value": 21.5
}
```


### Quantity2
#### json
```json
{
  "type": "Quantity",
  "definition": "http://sensorml.com/ont/swe/property/SpectralRadiance",
  "label": "Radiance",
  "description": "Radiance measured on band1",
  "uom": { "code": "W.m-2.Sr-1.um-1" },
  "value": 2.83e-2
}
```


### Quantity3
#### json
```json
{
  "type": "Quantity",
  "definition": "http://sensorml.com/ont/swe/property/HeightAboveMSL",
  "referenceFrame": "http://www.opengis.net/def/crs/EPSG/0/5714",
  "axisID": "H",
  "label": "MSL Height",
  "description": "Height above mean sea level",
  "uom": { "code": "m" }
}
```


### Quantity4
#### json
```json
{
  "type": "Quantity",
  "definition": "https://qudt.org/vocab/quantitykind/CostPerUnitEnergy",
  "label": "Electricity Cost",
  "description": "Average cost of electricity in Europe",
  "uom": {
    "href": "https://qudt.org/vocab/unit/EUR-PER-KiloW-HR"
  }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Scalar component with decimal representation and a unit of measure used
  to store value of a continuous quantity
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml
- properties:
    type:
      const: Quantity
    uom:
      description: Unit of measure used to express the value of this data component
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#UnitReference
    constraint:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AllowedValues
    nilValues:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#NilValuesNumber
    value:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#NumberOrSpecial
  required:
  - type
  - definition
  - label
  - uom

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/quantity/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/quantity/schema.yaml)

## Sources

* [swecommon/schemas/json/Quantity.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Quantity.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/quantity`

