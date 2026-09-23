
# SamplingFeature (GeoJSON) (Schema)

`ogc.api.connected-systems.part1.sampling-feature` *v0.1*

A Sampling Feature (GeoJSON encoding): a feature such as a station, specimen or transect that is sampled or observed by systems, and serves as the feature of interest of observations; profile of the OGC API - Features feature.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# SamplingFeature (GeoJSON)

SamplingFeature

Converted from [`api/part1/openapi/schemas/geojson/samplingFeature.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/samplingFeature.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `properties` | `object` |  |  |

## Examples

9 example(s) taken from the specification are included and validated against this schema.


## Examples

### Sampling part geojson
#### json
```json
{
  "type": "Feature",
  "id": "1a0f80f9",
  "geometry": null,
  "properties": {
    "uid": "urn:x-ogc:sf:456",
    "name": "CPU 2",
    "description": "CPU 2 located in the robot chassis",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/FeaturePart",
    "sampledFeature@link": {
      "href": "https://data.example.org/api/systems/8624d054?f=json",
      "type" : "application/geo+json",
      "title": "Tactical Ground Robot 457"
    }
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/447845?f=json",
      "type" : "application/geo+json",
      "title": "Water Level Sensor"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/context.jsonld",
  "type": "Feature",
  "id": "1a0f80f9",
  "geometry": null,
  "properties": {
    "uid": "urn:x-ogc:sf:456",
    "name": "CPU 2",
    "description": "CPU 2 located in the robot chassis",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/FeaturePart",
    "sampledFeature@link": {
      "href": "https://data.example.org/api/systems/8624d054?f=json",
      "type": "application/geo+json",
      "title": "Tactical Ground Robot 457"
    }
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/447845?f=json",
      "type": "application/geo+json",
      "title": "Water Level Sensor"
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
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<file:///github/workspace/1a0f80f9> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Water Level Sensor" ;
            dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parentSystem> ;
            oa:hasTarget <https://data.example.org/api/systems/447845?f=json> ] .


```


### Sampling point geojson
#### json
```json
{
  "type": "Feature",
  "id": "SP001",
  "geometry": {
    "type": "Point",
    "coordinates": [ 12.31, -86.98, -21]
  },
  "properties": {
    "uid": "urn:x-usgs:sites:301244087575701:sf:bottom",
    "name": "Bottom of Well - USGS Site #301244087575701",
    "description": "Sampling point is 2-4 inches above the bottom of the well",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint",
    "sampledFeature@link": {
      "href": "https://api.usgs.gov/collections/hydrological_features/items/112TRRC?f=json",
      "type" : "application/geo+json",
      "title": "Aquifer 112TRRC"
    }
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/context.jsonld",
  "type": "Feature",
  "id": "SP001",
  "geometry": {
    "type": "Point",
    "coordinates": [
      12.31,
      -86.98,
      -21
    ]
  },
  "properties": {
    "uid": "urn:x-usgs:sites:301244087575701:sf:bottom",
    "name": "Bottom of Well - USGS Site #301244087575701",
    "description": "Sampling point is 2-4 inches above the bottom of the well",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint",
    "sampledFeature@link": {
      "href": "https://api.usgs.gov/collections/hydrological_features/items/112TRRC?f=json",
      "type": "application/geo+json",
      "title": "Aquifer 112TRRC"
    }
  }
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/SP001> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.231e+01 -8.698e+01 -21 ) ] .


```


### Sampling point xyz geojson
#### json
```json
{
  "type": "Feature",
  "id": "tkckcs6che9i8",
  "geometry": null,
  "properties": {
    "uid": "urn:x-osh:saildrone:1001:water-sf",
    "name": "Water Sampling Point",
    "description": "Sampling point for the CTD measurements",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/SamplingPointXYZ",
    "sampledFeature@link": {
      "href": "http://dbpedia.org/resource/Seawater",
      "type" : "text/html",
      "title": "Seawater"
    },
    "pose": {
      "type": "RelativePose",
      "referenceFrame": "urn:x-osh:saildrone:1001#PLATFORM_FRAME",
      "position": {
        "x": 0.0,
        "y": 0.0,
        "z": -0.5
      },
      "angles": {
        "yaw": 0,
        "pitch": 0,
        "roll": 0
      }
    }
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/fs4g5sd6?f=json",
      "type" : "application/geo+json",
      "title": "CTD Sensor"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/context.jsonld",
  "type": "Feature",
  "id": "tkckcs6che9i8",
  "geometry": null,
  "properties": {
    "uid": "urn:x-osh:saildrone:1001:water-sf",
    "name": "Water Sampling Point",
    "description": "Sampling point for the CTD measurements",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/SamplingPointXYZ",
    "sampledFeature@link": {
      "href": "http://dbpedia.org/resource/Seawater",
      "type": "text/html",
      "title": "Seawater"
    },
    "pose": {
      "type": "RelativePose",
      "referenceFrame": "urn:x-osh:saildrone:1001#PLATFORM_FRAME",
      "position": {
        "x": 0.0,
        "y": 0.0,
        "z": -0.5
      },
      "angles": {
        "yaw": 0,
        "pitch": 0,
        "roll": 0
      }
    }
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/fs4g5sd6?f=json",
      "type": "application/geo+json",
      "title": "CTD Sensor"
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
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<file:///github/workspace/tkckcs6che9i8> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "CTD Sensor" ;
            dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parentSystem> ;
            oa:hasTarget <https://data.example.org/api/systems/fs4g5sd6?f=json> ] .


```


### Sampling proxy geojson
#### json
```json
{
  "type": "Feature",
  "id": "1a0f80f9",
  "geometry": null,
  "properties": {
    "uid": "x-safecity:sg:traffic:sf:PIE12-34",
    "name": "PIE Junction 34",
    "description": "Junction 34 on Pan-Island Expressway",
    "featureType": "Junction",
    "sampledFeature@link": {
      "href": "https://ext.features.org/api/collections/roads/PIE12?f=json",
      "type" : "application/geo+json"
    }
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/751588?f=json",
      "type" : "application/geo+json",
      "title": "Traffic Camera 456"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/context.jsonld",
  "type": "Feature",
  "id": "1a0f80f9",
  "geometry": null,
  "properties": {
    "uid": "x-safecity:sg:traffic:sf:PIE12-34",
    "name": "PIE Junction 34",
    "description": "Junction 34 on Pan-Island Expressway",
    "featureType": "Junction",
    "sampledFeature@link": {
      "href": "https://ext.features.org/api/collections/roads/PIE12?f=json",
      "type": "application/geo+json"
    }
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/751588?f=json",
      "type": "application/geo+json",
      "title": "Traffic Camera 456"
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
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<file:///github/workspace/1a0f80f9> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Traffic Camera 456" ;
            dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parentSystem> ;
            oa:hasTarget <https://data.example.org/api/systems/751588?f=json> ] .


```


### Sampling specimen geojson
#### json
```json
{
  "type": "Feature",
  "id": "f6b464cf",
  "geometry": {
    "type": "Point",
    "coordinates": [ 30.706, -134.196, 272 ]
  },
  "properties": {
    "uid": "urn:x-csiro:samples:1114457888",
    "name": "Rock Sample CSIRO:1114457888",
    "description": "Rock sample collected on traverse",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_Specimen",
    "samplingTime": "2007-01-24T12:14:50Z",
    "materialClass": "http://dbpedia.org/resource/Rock_(geology)",
    "sampledFeature@link": {
      "href": "https://api.usgs.gov/collections/geological_features/items/1458955?f=json",
      "type" : "application/geo+json",
      "title": "Geological Unit 235"
    }
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/2ad45f69?f=json",
      "type" : "application/geo+json",
      "title": "Field Technician #123 (Rock Sampler)"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/context.jsonld",
  "type": "Feature",
  "id": "f6b464cf",
  "geometry": {
    "type": "Point",
    "coordinates": [
      30.706,
      -134.196,
      272
    ]
  },
  "properties": {
    "uid": "urn:x-csiro:samples:1114457888",
    "name": "Rock Sample CSIRO:1114457888",
    "description": "Rock sample collected on traverse",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_Specimen",
    "samplingTime": "2007-01-24T12:14:50Z",
    "materialClass": "http://dbpedia.org/resource/Rock_(geology)",
    "sampledFeature@link": {
      "href": "https://api.usgs.gov/collections/geological_features/items/1458955?f=json",
      "type": "application/geo+json",
      "title": "Geological Unit 235"
    }
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/2ad45f69?f=json",
      "type": "application/geo+json",
      "title": "Field Technician #123 (Rock Sampler)"
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

<file:///github/workspace/f6b464cf> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Field Technician #123 (Rock Sampler)" ;
            dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parentSystem> ;
            oa:hasTarget <https://data.example.org/api/systems/2ad45f69?f=json> ] ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.0706e+01 -1.34196e+02 272 ) ] .


```


### SamplingProfile at location geojson
#### json
```json
{
  "type": "Feature",
  "id": "SPF001",
  "geometry": {
    "type": "Point",
    "coordinates": [-151.458848, 59.649740, 7.6]
  },
  "properties": {
    "uid": "urn:x-noaa:npn:HWPA2:spf",
    "name": "Homer Wind Profiler Beam 1",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/SamplingProfile",
    "sampledFeature@link": {
      "href": "http://dbpedia.org/resource/Atmosphere_of_Earth",
      "type" : "text/html",
      "title": "Atmosphere"
    },
    "pose": {
      "type": "RelativePose",
      "referenceFrame": "http://www.opengis.net/def/cs/OGC/0/NED",
      "position": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "angles": {
        "yaw": 0.0,
        "pitch": 0.0,
        "roll": 0.0
      }
    },
    "profileAxis": "-Z",
    "numBins": 10,
    "startDistance": 1.2,
    "stepDistance": 0.4
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/72562?f=json",
      "type" : "application/geo+json",
      "title": "Homer Wind Profiler"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/context.jsonld",
  "type": "Feature",
  "id": "SPF001",
  "geometry": {
    "type": "Point",
    "coordinates": [
      -151.458848,
      59.64974,
      7.6
    ]
  },
  "properties": {
    "uid": "urn:x-noaa:npn:HWPA2:spf",
    "name": "Homer Wind Profiler Beam 1",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/SamplingProfile",
    "sampledFeature@link": {
      "href": "http://dbpedia.org/resource/Atmosphere_of_Earth",
      "type": "text/html",
      "title": "Atmosphere"
    },
    "pose": {
      "type": "RelativePose",
      "referenceFrame": "http://www.opengis.net/def/cs/OGC/0/NED",
      "position": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "angles": {
        "yaw": 0.0,
        "pitch": 0.0,
        "roll": 0.0
      }
    },
    "profileAxis": "-Z",
    "numBins": 10,
    "startDistance": 1.2,
    "stepDistance": 0.4
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/72562?f=json",
      "type": "application/geo+json",
      "title": "Homer Wind Profiler"
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

<file:///github/workspace/SPF001> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Homer Wind Profiler" ;
            dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parentSystem> ;
            oa:hasTarget <https://data.example.org/api/systems/72562?f=json> ] ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( -1.514588e+02 5.964974e+01 7.6e+00 ) ] .


```


### Viewing frustum at location geojson
#### json
```json
{
  "type": "Feature",
  "id": "VF002",
  "geometry": {
    "type": "Point",
    "coordinates": [103.868811, 1.327909]
  },
  "properties": {
    "uid": "urn:x-safecity:sg:dahua:SG00010:vf",
    "name": "Camera Viewing Frustum",
    "description": "Viewing frustum of fixed camera",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/ViewingFrustum",
    "sampledFeature@link": {
      "href": "https://data.example.org/api/collections/roads/PIE12",
      "type" : "application/geo+json",
      "title": "Pan-Island Expressway"
    },
    "pose": {
      "type": "RelativePose",
      "referenceFrame": "http://www.opengis.net/def/cs/OGC/0/NED",
      "position": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "angles": {
        "yaw": 123.0,
        "pitch": -2.0,
        "roll": 0.0
      }
    },
    "frustumAxis": "X",
    "upAxis": "-Z",
    "fov": 46.0,
    "aspectRatio": 1.33,
    "length": 50.0
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/751588?f=json",
      "type" : "application/geo+json",
      "title": "Traffic Camera 456"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/context.jsonld",
  "type": "Feature",
  "id": "VF002",
  "geometry": {
    "type": "Point",
    "coordinates": [
      103.868811,
      1.327909
    ]
  },
  "properties": {
    "uid": "urn:x-safecity:sg:dahua:SG00010:vf",
    "name": "Camera Viewing Frustum",
    "description": "Viewing frustum of fixed camera",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/ViewingFrustum",
    "sampledFeature@link": {
      "href": "https://data.example.org/api/collections/roads/PIE12",
      "type": "application/geo+json",
      "title": "Pan-Island Expressway"
    },
    "pose": {
      "type": "RelativePose",
      "referenceFrame": "http://www.opengis.net/def/cs/OGC/0/NED",
      "position": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "angles": {
        "yaw": 123.0,
        "pitch": -2.0,
        "roll": 0.0
      }
    },
    "frustumAxis": "X",
    "upAxis": "-Z",
    "fov": 46.0,
    "aspectRatio": 1.33,
    "length": 50.0
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/751588?f=json",
      "type": "application/geo+json",
      "title": "Traffic Camera 456"
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

<file:///github/workspace/VF002> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Traffic Camera 456" ;
            dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parentSystem> ;
            oa:hasTarget <https://data.example.org/api/systems/751588?f=json> ] ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.038688e+02 1.327909e+00 ) ] .


```


### Viewing frustum on platform geojson
#### json
```json
{
  "type": "Feature",
  "id": "VF001",
  "geometry": null,
  "properties": {
    "uid": "urn:x-usgs:sites:301244087575701",
    "name": "Camera Viewing Frustum",
    "description": "Viewing frustum of camera attached to the boom",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/ViewingFrustum",
    "sampledFeature@link": {
      "href": "http://dbpedia.org/resource/Atmosphere_of_Earth",
      "type" : "text/html",
      "title": "Atmosphere"
    },
    "pose": {
      "type": "RelativePose",
      "referenceFrame": "urn:x-osh:saildrone:1001#PLATFORM_FRAME",
      "position": {
        "x": 0.0,
        "y": 1.0,
        "z": 2.5
      },
      "angles": {
        "yaw": 0.0,
        "pitch": -6.0,
        "roll": 0.0
      }
    },
    "frustumAxis": "Y",
    "upAxis": "Z",
    "fov": 58,
    "aspectRatio": 1.33
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/422381?f=json",
      "type" : "application/geo+json",
      "title": "Saildrone 1001"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/context.jsonld",
  "type": "Feature",
  "id": "VF001",
  "geometry": null,
  "properties": {
    "uid": "urn:x-usgs:sites:301244087575701",
    "name": "Camera Viewing Frustum",
    "description": "Viewing frustum of camera attached to the boom",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/ViewingFrustum",
    "sampledFeature@link": {
      "href": "http://dbpedia.org/resource/Atmosphere_of_Earth",
      "type": "text/html",
      "title": "Atmosphere"
    },
    "pose": {
      "type": "RelativePose",
      "referenceFrame": "urn:x-osh:saildrone:1001#PLATFORM_FRAME",
      "position": {
        "x": 0.0,
        "y": 1.0,
        "z": 2.5
      },
      "angles": {
        "yaw": 0.0,
        "pitch": -6.0,
        "roll": 0.0
      }
    },
    "frustumAxis": "Y",
    "upAxis": "Z",
    "fov": 58,
    "aspectRatio": 1.33
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/422381?f=json",
      "type": "application/geo+json",
      "title": "Saildrone 1001"
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
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<file:///github/workspace/VF001> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Saildrone 1001" ;
            dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parentSystem> ;
            oa:hasTarget <https://data.example.org/api/systems/422381?f=json> ] .


```


### Viewing sector at location geojson
#### json
```json
{
  "type": "Feature",
  "id": "VS001",
  "geometry": {
    "type": "Point",
    "coordinates": [103.868811, 1.327909]
  },
  "properties": {
    "uid": "urn:x-safecity:sg:dahua:SG00010:vf",
    "name": "Camera Viewable Area",
    "description": "Area visible to the PTZ camera",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/SphericalSector",
    "sampledFeature@link": {
      "href": "https://ext.features.org/api/collections/roads/PIE12?f=json",
      "type" : "application/geo+json",
      "title": "Pan-Island Expressway"
    },
    "pose": {
      "type": "RelativePose",
      "referenceFrame": "http://www.opengis.net/def/cs/OGC/0/NED",
      "position": {
        "x": 0.0,
        "y": 1.0,
        "z": 2.5
      },
      "angles": {
        "yaw": 0.0,
        "pitch": 0.0,
        "roll": 0.0
      }
    },
    "radius": 50.0,
    "minElev": -90.0,
    "maxElev": 25.0,
    "minAzim": 23.0,
    "maxAzim": 223.0
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/751588?f=json",
      "type" : "application/geo+json",
      "title": "Traffic Camera 456"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/context.jsonld",
  "type": "Feature",
  "id": "VS001",
  "geometry": {
    "type": "Point",
    "coordinates": [
      103.868811,
      1.327909
    ]
  },
  "properties": {
    "uid": "urn:x-safecity:sg:dahua:SG00010:vf",
    "name": "Camera Viewable Area",
    "description": "Area visible to the PTZ camera",
    "featureType": "http://www.opengis.net/def/samplingFeatureType/OGC-SML/2.0/SphericalSector",
    "sampledFeature@link": {
      "href": "https://ext.features.org/api/collections/roads/PIE12?f=json",
      "type": "application/geo+json",
      "title": "Pan-Island Expressway"
    },
    "pose": {
      "type": "RelativePose",
      "referenceFrame": "http://www.opengis.net/def/cs/OGC/0/NED",
      "position": {
        "x": 0.0,
        "y": 1.0,
        "z": 2.5
      },
      "angles": {
        "yaw": 0.0,
        "pitch": 0.0,
        "roll": 0.0
      }
    },
    "radius": 50.0,
    "minElev": -90.0,
    "maxElev": 25.0,
    "minAzim": 23.0,
    "maxAzim": 223.0
  },
  "links": [
    {
      "rel": "parentSystem",
      "href": "https://data.example.org/api/systems/751588?f=json",
      "type": "application/geo+json",
      "title": "Traffic Camera 456"
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

<file:///github/workspace/VS001> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Traffic Camera 456" ;
            dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parentSystem> ;
            oa:hasTarget <https://data.example.org/api/systems/751588?f=json> ] ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.038688e+02 1.327909e+00 ) ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SamplingFeature
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/feature/schema.yaml
- type: object
  properties:
    properties:
      type: object
      required:
      - featureType
      - sampledFeature@link
      properties:
        validTime:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
        sampledFeature@link:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/schema.yaml)


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
[context.jsonld](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/sampling-feature/context.jsonld)

## Sources

* [api/part1/openapi/schemas/geojson/samplingFeature.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/samplingFeature.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/sampling-feature`

