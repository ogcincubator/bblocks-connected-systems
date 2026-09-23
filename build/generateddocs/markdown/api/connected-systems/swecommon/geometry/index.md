
# Geometry (Schema)

`ogc.api.connected-systems.swecommon.geometry` *v0.1*

Implementation of ISO-19107 geometry datatype. This allows embedding a geometry in a larger schema

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Geometry

Implementation of ISO-19107 geometry datatype. This allows embedding a geometry in a larger schema

Converted from [`swecommon/schemas/json/Geometry.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Geometry.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"Geometry"` | yes |  |
| `constraint` | `object` |  |  |
| `nilValues` | `basicTypes.json#/$defs/NilValuesText` |  |  |
| `srs` | `string` | yes | Coordinate reference system with respect to which the coordinates of this geometry are expressed |
| `value` | `https://geojson.org/schema/Geometry.json` |  |  |

## Examples

3 example(s) taken from the specification are included and validated against this schema.


## Examples

### Geometry1
#### json
```json
{
  "type": "Geometry",
  "definition": "http://sensorml.com/ont/swe/property/TargetLocation",
  "srs": "http://www.opengis.net/def/crs/EPSG/0/4326",
  "label": "Target Location",
  "description": "A point geometry",
  "value": {
    "type": "Point",
    "coordinates": [12.34, 56.36]
  }
}
```


### Geometry2
#### json
```json
{
  "type": "Geometry",
  "definition": "http://sensorml.com/ont/swe/property/Trajectory",
  "srs": "http://www.opengis.net/def/crs/EPSG/0/4326",
  "label": "Desired Trajectory",
  "description": "Desired UxS trajectory defined as a line string",
  "value": {
    "type": "LineString",
    "coordinates": [[12.34, 56.36], [12.45, 56.37], [12.45, 56.39], [12.34, 56.36]]
  }
}
```


### Geometry3
#### json
```json
{
  "type": "Geometry",
  "definition": "http://sensorml.com/ont/x-swe/property/SurveillanceArea",
  "srs": "http://www.opengis.net/def/crs/EPSG/0/4326",
  "label": "Surveillance Area",
  "description": "Desired UxS surveillance area defined as a polygon",
  "value": {
    "type": "Polygon",
    "coordinates": [
      [[12.34, 56.36], [12.45, 56.37], [12.45, 56.39], [12.34, 56.36]]
    ]
  }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Geometry
description: Implementation of ISO-19107 geometry datatype. This allows embedding
  a geometry in a larger schema
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-data-component/schema.yaml
- properties:
    type:
      const: Geometry
    constraint:
      type: object
      properties:
        geomTypes:
          type: array
          minLength: 1
          items:
            type: string
            enum:
            - Point
            - MultiPoint
            - LineString
            - MultiLineString
            - Polygon
            - MultiPolygon
      additionalProperties: false
    nilValues:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#NilValuesText
    srs:
      description: Coordinate reference system with respect to which the coordinates
        of this geometry are expressed
      type: string
      format: uri
    value:
      $ref: https://geojson.org/schema/Geometry.json
  required:
  - type
  - srs
  - definition
  - label

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/geometry/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/geometry/schema.yaml)

## Sources

* [swecommon/schemas/json/Geometry.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Geometry.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/geometry`

