
# DeployedSystemArray (GeoJSON) (Schema)

`ogc.api.connected-systems.part1.deployed-system-array` *v0.1*

Bare JSON array of deployed System resources (GeoJSON encoding), used as the request payload for batch creation or update of several resources at once.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# DeployedSystemArray (GeoJSON)

Converted from [`api/part1/openapi/schemas/geojson/deployedSystemArray.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/deployedSystemArray.json) in the OGC API - Connected Systems repository.


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: array
items:
  title: Deployed System Feature
  $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployed-system/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployed-system-array/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployed-system-array/schema.yaml)


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
[context.jsonld](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployed-system-array/context.jsonld)

## Sources

* [api/part1/openapi/schemas/geojson/deployedSystemArray.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/deployedSystemArray.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/deployed-system-array`

