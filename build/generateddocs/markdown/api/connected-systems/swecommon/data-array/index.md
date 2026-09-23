
# DataArray (Schema)

`ogc.api.connected-systems.swecommon.data-array` *v0.1*

Implementation of ISO-11404 Array datatype. This defines an array of identical data components with a elementCount. Values are given as a block and can be encoded in different ways

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# DataArray

Implementation of ISO-11404 Array datatype. This defines an array of identical data components with a elementCount. Values are given as a block and can be encoded in different ways

Converted from [`swecommon/schemas/json/DataArray.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/DataArray.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.swecommon.data-array#AbstractArray`:

- `AbstractArray`

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"DataArray"` | yes |  |

## Examples

4 example(s) taken from the specification are included and validated against this schema.


## Examples

### Array1
#### json
```json
{
  "type": "DataArray",
  "label": "Calibration Table",
  "elementType": {
    "name": "point",
    "type": "DataRecord",
    "label": "Data Point",
    "fields": [
      {
        "name": "t",
        "type": "Quantity",
        "definition": "https://qudt.org/vocab/quantitykind/Temperature",
        "label": "Temperature",
        "uom": { "code": "Cel" }
      },
      {
        "name": "r",
        "type": "Quantity",
        "definition": "https://qudt.org/vocab/quantitykind/Resistance",
        "label": "Resistance",
        "uom": { "code": "KOhm" }
      }
    ]
  },
  "values": [
    {"t": 12, "r": 3.03},
    {"t": 30.1, "r": 1.68},
    {"t": 40.0, "r": 1.16},
    {"t": 50.1, "r": 0.85},
    {"t": 59.8, "r": 0.62}
  ]
}
```


### Array2
#### json
```json
{
  "type": "DataArray",
  "definition": "http://sensorml.com/ont/swe/property/Trajectory",
  "label": "Mobile Trajectory",
  "elementCount": {
    "definition": "http://www.opengis.net/def/property/OGC/0/NumberOfPoints",
    "label": "Implicit Size"
  },
  "elementType": {
    "name": "point",
    "type": "Vector",
    "definition": "http://www.opengis.net/def/property/OGC/0/PlatformLocation",
    "referenceFrame": "http://www.opengis.net/def/crs/EPSG/0/4326",
    "label": "Location Point",
    "coordinates": [
      {
        "name": "lat",
        "type": "Quantity",
        "definition": "http://sensorml.com/ont/swe/property/GeodeticLatitude",
        "label": "Latitude",
        "axisID": "Lat",
        "uom": { "code": "deg" }
      },
      {
        "name": "lon",
        "type": "Quantity",
        "definition": "http://sensorml.com/ont/swe/property/Longitude",
        "label": "Longitude",
        "axisID": "Lon",
        "uom": { "code": "deg" }
      }
    ]
  }
}
```


### Array3 encoded values
#### json
```json
{
  "$schema": "file:///home/autermann/Source/ogcapi-connected-systems/swecommon/schemas/json/DataArray.json",
  "type": "DataArray",
  "definition": "http://sensorml.com/ont/swe/property/RasterImage",
  "label": "Satellite Image",
  "elementCount": {
    "definition": "http://www.opengis.net/def/property/OGC/0/NumberOfRows",
    "value": 4
  },
  "elementType": {
    "name": "row",
    "type": "DataArray",
    "definition": "http://sensorml.com/ont/swe/property/RasterImage",
    "elementCount": {
      "definition": "http://www.opengis.net/def/property/OGC/0/NumberOfSamples",
      "value": 4
    },
    "elementType": {
      "name": "pixel",
      "type": "DataRecord",
      "definition": "http://sensorml.com/ont/swe/property/GridCell",
      "fields": [
        {
          "name": "band1",
          "type": "Quantity",
          "definition": "http://qudt.org/vocab/quantitykind/Radiance",
          "label": "Radiance",
          "description": "Radiance measured on band1",
          "uom": { "code": "W.m-2.Sr-1" }
        },
        {
          "name": "band2",
          "type": "Quantity",
          "definition": "http://qudt.org/vocab/quantitykind/Radiance",
          "label": "Radiance",
          "description": "Radiance measured on band2",
          "uom": { "code": "W.m-2.Sr-1" }
        },
        {
          "name": "band3",
          "type": "Quantity",
          "definition": "http://qudt.org/vocab/quantitykind/Radiance",
          "label": "Radiance",
          "description": "Radiance measured on band3",
          "uom": { "code": "W.m-2.Sr-1" }
        }
      ]
    }
  },
  "encoding": {
    "type": "BinaryEncoding",
    "byteEncoding": "raw",
    "byteOrder": "bigEndian",
    "members": [
      {
        "type": "Component",
        "ref": "row/pixel/band1",
        "dataType": "http://www.opengis.net/def/dataType/OGC/0/unsignedByte"
      },
      {
        "type": "Component",
        "ref": "row/pixel/band2",
        "dataType": "http://www.opengis.net/def/dataType/OGC/0/unsignedByte"
      },
      {
        "type": "Component",
        "ref": "row/pixel/band3",
        "dataType": "http://www.opengis.net/def/dataType/OGC/0/unsignedByte"
      }
    ]
  },
  "values":{"href": "data:application/octet-stream;base64,MptSyfqPYAB5A9aV3j1uYw9EywICwMDZVcmnRlpS1NI1crn8K7NUe/X0I8r4IVq9"}
}

```


### Array3
#### json
```json
{
  "type": "DataArray",
  "definition": "http://sensorml.com/ont/swe/property/RasterImage",
  "label": "Satellite Image",
  "elementCount": {
    "definition": "http://www.opengis.net/def/property/OGC/0/NumberOfRows",
    "value": 3000
  },
  "elementType": {
    "name": "row",
    "type": "DataArray",
    "definition": "http://sensorml.com/ont/swe/property/RasterImage",
    "elementCount": {
      "definition": "http://www.opengis.net/def/property/OGC/0/NumberOfSamples",
      "value": 3000
    },
    "elementType": {
      "name": "pixel",
      "type": "DataRecord",
      "definition": "http://sensorml.com/ont/swe/property/GridCell",
      "fields": [
        {
          "name": "band1",
          "type": "Quantity",
          "definition": "http://qudt.org/vocab/quantitykind/Radiance",
          "label": "Radiance",
          "description": "Radiance measured on band1",
          "uom": { "code": "W.m-2.Sr-1" }
        },
        {
          "name": "band2",
          "type": "Quantity",
          "definition": "http://qudt.org/vocab/quantitykind/Radiance",
          "label": "Radiance",
          "description": "Radiance measured on band2",
          "uom": { "code": "W.m-2.Sr-1" }
        },
        {
          "name": "band3",
          "type": "Quantity",
          "definition": "http://qudt.org/vocab/quantitykind/Radiance",
          "label": "Radiance",
          "description": "Radiance measured on band3",
          "uom": { "code": "W.m-2.Sr-1" }
        }
      ]
    }
  }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Implementation of ISO-11404 Array datatype. This defines an array of
  identical data components with a elementCount. Values are given as a block and can
  be encoded in different ways
allOf:
- $ref: '#/$defs/AbstractArray'
- properties:
    type:
      const: DataArray
  required:
  - type
  - elementType
$defs:
  AbstractArray:
    type: object
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-data-component/schema.yaml
    - properties:
        elementCount:
          description: Specifies the size of the array (i.e., the number of elements
            of the defined type it contains)
          oneOf:
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AssociationAttributeGroup
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#ElementCount
        elementType:
          description: Defines the structure of the element that will be repeated
            in the array
          allOf:
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#SoftNamedProperty
          - oneOf:
            - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AssociationAttributeGroup
            - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
        encoding:
          description: Specifies the type of method used to encode the array values
          oneOf:
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#BinaryEncoding
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#TextEncoding
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#XMLEncoding
          - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#JSONEncoding
        values:
          description: If present, contains an encoded block of the values contained
            in the array. Values are optional so that the array definition can be
            used a as a schema for values provided separately
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#EncodedValues
    $anchor: AbstractArray

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-array/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-array/schema.yaml)

## Sources

* [swecommon/schemas/json/DataArray.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/DataArray.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/data-array`

