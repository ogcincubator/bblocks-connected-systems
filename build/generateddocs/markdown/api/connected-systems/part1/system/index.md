
# System (GeoJSON) (Schema)

`ogc.api.connected-systems.part1.system` *v0.1*

A System (GeoJSON encoding, a profile of the OGC API - Features feature): a sensor, actuator, platform, sampler or other asset that produces observations or receives commands, with its identity, type and relationships to other resources.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# System (GeoJSON)

Converted from [`api/part1/openapi/schemas/geojson/system.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/system.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `properties` |  |  |  |

## Examples

2 example(s) taken from the specification are included and validated against this schema.


## Examples

### Thermometer sensor geojson
#### json
```json
{
  "type": "Feature",
  "id": "123",
  "geometry": {
    "type": "Point",
    "coordinates": [41.8781, -87.6298]
  },
  "properties": {
    "uid": "urn:x-ogc:systems:001",
    "name": "Outdoor Thermometer 001",
    "description": "Digital thermometer located on first floor window 1",
    "featureType": "http://www.w3.org/ns/sosa/Sensor",
    "assetType": "Equipment",
    "systemKind@link": {
      "href": "https://data.example.org/api/procedures/TP60S?f=json",
      "uid": "urn:x-myorg:datasheets:ThermoPro:TP60S:v001",
      "title": "Thermo Pro TP60S",
      "type" : "application/geo+json"
    }
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/system/context.jsonld",
  "type": "Feature",
  "id": "123",
  "geometry": {
    "type": "Point",
    "coordinates": [
      41.8781,
      -87.6298
    ]
  },
  "properties": {
    "uid": "urn:x-ogc:systems:001",
    "name": "Outdoor Thermometer 001",
    "description": "Digital thermometer located on first floor window 1",
    "featureType": "http://www.w3.org/ns/sosa/Sensor",
    "assetType": "Equipment",
    "systemKind@link": {
      "href": "https://data.example.org/api/procedures/TP60S?f=json",
      "uid": "urn:x-myorg:datasheets:ThermoPro:TP60S:v001",
      "title": "Thermo Pro TP60S",
      "type": "application/geo+json"
    }
  }
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/123> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 4.18781e+01 -8.76298e+01 ) ] .


```


### Uav platform geojson
#### json
```json
{
  "type": "Feature",
  "id": "PLT412",
  "geometry": null,
  "properties": {
    "uid": "urn:x-ogc:systems:uav:solo154",
    "name": "UAV System 412",
    "description": "3DR Solo UAV",
    "featureType": "http://www.w3.org/ns/sosa/Platform",
    "systemKind@link": {
      "href": "https://data.example.org/api/procedures/nrof8qi7wc9a?f=json",
      "uid": "urn:x-ogc:datasheets:uav:3dr-solo:v1",
      "type" : "application/geo+json"
    }
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/system/context.jsonld",
  "type": "Feature",
  "id": "PLT412",
  "geometry": null,
  "properties": {
    "uid": "urn:x-ogc:systems:uav:solo154",
    "name": "UAV System 412",
    "description": "3DR Solo UAV",
    "featureType": "http://www.w3.org/ns/sosa/Platform",
    "systemKind@link": {
      "href": "https://data.example.org/api/procedures/nrof8qi7wc9a?f=json",
      "uid": "urn:x-ogc:datasheets:uav:3dr-solo:v1",
      "type": "application/geo+json"
    }
  }
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .

<file:///github/workspace/PLT412> a geojson:Feature .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/feature/schema.yaml
- properties:
    properties:
      properties:
        featureType:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/uris/schema.yaml#SystemTypeUris
        assetType:
          description: Type of asset represented by this system.
          type: string
          enum:
          - Equipment
          - Human
          - LivingThing
          - Simulation
          - Process
          - Group
          - Other
        validTime:
          description: Time period during which the system description is valid.
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
        systemKind@link:
          description: Link to the system kind description (i.e., its nature or specifications).
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/system/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/system/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "type": "@type",
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        }
      },
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/system/context.jsonld)

## Sources

* [api/part1/openapi/schemas/geojson/system.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/system.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/system`

