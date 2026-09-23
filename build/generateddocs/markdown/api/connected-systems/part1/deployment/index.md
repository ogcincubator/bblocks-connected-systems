
# Deployment (GeoJSON) (Schema)

`ogc.api.connected-systems.part1.deployment` *v0.1*

A Deployment (GeoJSON encoding, a profile of the OGC API - Features feature): the installation of one or more systems at a location and time, describing where and when they operate.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Deployment (GeoJSON)

Converted from [`api/part1/openapi/schemas/geojson/deployment.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/deployment.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `properties` |  |  |  |

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### Deployment geojson
#### json
```json
{
  "type": "Feature",
  "id": "iv3f2kcq27gfi",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [53.76,-173.7],
      [53.76,-155.07],
      [75.03,-155.07],
      [75.03,-173.7],
      [53.76,-173.7]
    ]]
  },
  "properties": {
    "uid": "urn:x-ogc:deployments:D001",
    "name": "Saildrone - 2017 Arctic Mission",
    "featureType": "http://www.w3.org/ns/sosa/Deployment",
    "description": "In July 2017, three saildrones were launched from Dutch Harbor, Alaska, in partnership with NOAA Research...",
    "validTime": ["2017-07-17T00:00:00Z", "2017-09-29T00:00:00Z"],
    "platform@link": {
      "href": "https://data.example.org/api/systems/27559?f=sml",
      "uid": "urn:x-saildrone:platforms:SD-1003",
      "title": "Saildrone SD-1003"
    },
    "deployedSystems@link": [
      {
        "href": "https://data.example.org/api/systems/41548?f=sml",
        "uid": "urn:x-saildrone:sensors:temp01",
        "title": "Air Temperature Sensor"
      },
      {
        "href": "https://data.example.org/api/systems/36584?f=sml",
        "uid": "urn:x-saildrone:sensors:temp02",
        "title": "Water Temperature Sensor"
      },
      {
        "href": "https://data.example.org/api/systems/47752?f=sml",
        "uid": "urn:x-saildrone:sensors:wind01",
        "title": "Wind Speed and Direction Sensor"
      }
    ]
  },
  "links": [
    {
      "rel" : "self",
      "href" : "https://data.example.org/api/deployments/iv3f2kcq27gfi?f=json",
      "type" : "application/geo+json",
      "title" : "this document"
    }, {
      "rel" : "alternate",
      "href" : "https://data.example.org/api/deployments/iv3f2kcq27gfi?f=sml",
      "type" : "application/sml+json",
      "title" : "this resource as SensorML"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployment/context.jsonld",
  "type": "Feature",
  "id": "iv3f2kcq27gfi",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          53.76,
          -173.7
        ],
        [
          53.76,
          -155.07
        ],
        [
          75.03,
          -155.07
        ],
        [
          75.03,
          -173.7
        ],
        [
          53.76,
          -173.7
        ]
      ]
    ]
  },
  "properties": {
    "uid": "urn:x-ogc:deployments:D001",
    "name": "Saildrone - 2017 Arctic Mission",
    "featureType": "http://www.w3.org/ns/sosa/Deployment",
    "description": "In July 2017, three saildrones were launched from Dutch Harbor, Alaska, in partnership with NOAA Research...",
    "validTime": [
      "2017-07-17T00:00:00Z",
      "2017-09-29T00:00:00Z"
    ],
    "platform@link": {
      "href": "https://data.example.org/api/systems/27559?f=sml",
      "uid": "urn:x-saildrone:platforms:SD-1003",
      "title": "Saildrone SD-1003"
    },
    "deployedSystems@link": [
      {
        "href": "https://data.example.org/api/systems/41548?f=sml",
        "uid": "urn:x-saildrone:sensors:temp01",
        "title": "Air Temperature Sensor"
      },
      {
        "href": "https://data.example.org/api/systems/36584?f=sml",
        "uid": "urn:x-saildrone:sensors:temp02",
        "title": "Water Temperature Sensor"
      },
      {
        "href": "https://data.example.org/api/systems/47752?f=sml",
        "uid": "urn:x-saildrone:sensors:wind01",
        "title": "Wind Speed and Direction Sensor"
      }
    ]
  },
  "links": [
    {
      "rel": "self",
      "href": "https://data.example.org/api/deployments/iv3f2kcq27gfi?f=json",
      "type": "application/geo+json",
      "title": "this document"
    },
    {
      "rel": "alternate",
      "href": "https://data.example.org/api/deployments/iv3f2kcq27gfi?f=sml",
      "type": "application/sml+json",
      "title": "this resource as SensorML"
    }
  ]
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/iv3f2kcq27gfi> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "this resource as SensorML" ;
            dct:type "application/sml+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/alternate> ;
            oa:hasTarget <https://data.example.org/api/deployments/iv3f2kcq27gfi?f=sml> ],
        [ rdfs:label "this document" ;
            dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://data.example.org/api/deployments/iv3f2kcq27gfi?f=json> ] ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 5.376e+01 -1.737e+02 ) ( 5.376e+01 -1.5507e+02 ) ( 7.503e+01 -1.5507e+02 ) ( 7.503e+01 -1.737e+02 ) ( 5.376e+01 -1.737e+02 ) ) ) ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/feature/schema.yaml
- properties:
    properties:
      required:
      - validTime
      properties:
        featureType:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/uris/schema.yaml#DeploymentTypeUris
        validTime:
          description: Time period during which the systems are deployed.
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
        platform@link:
          description: Link to the platform on which the systems are deployed.
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
        deployedSystems@link:
          type: array
          items:
            description: Link to the system being deployed. Either a URN if the system
              is stored locally, or a URL if the system is hosted externally
            $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployment/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployment/schema.yaml)


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
[context.jsonld](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployment/context.jsonld)

## Sources

* [api/part1/openapi/schemas/geojson/deployment.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/deployment.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/deployment`

