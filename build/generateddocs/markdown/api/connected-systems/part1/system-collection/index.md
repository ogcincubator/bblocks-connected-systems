
# SystemCollection (GeoJSON) (Schema)

`ogc.api.connected-systems.part1.system-collection` *v0.1*

Paged collection of System resources (GeoJSON encoding) as returned by list queries, with the items plus navigation `links`.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# SystemCollection (GeoJSON)

Converted from [`api/part1/openapi/schemas/geojson/systemCollection.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/systemCollection.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `features` | `systemArray.json` |  |  |
| `links` | `../common/links.json` |  | Links to related resources (including paging) |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.yaml
- type: object
  properties:
    features:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/system-array/schema.yaml
    links:
      description: Links to related resources (including paging)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/system-collection/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/system-collection/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "dct:type",
    "features": {
      "@context": {
        "type": "@type"
      },
      "@id": "geojson:features",
      "@container": "@set"
    },
    "bbox": {
      "@id": "geojson:bbox",
      "@container": "@list"
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
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "properties": "@nest",
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "id": "@id",
    "geometry": {
      "@context": {
        "type": "@type",
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        }
      },
      "@id": "geojson:geometry"
    },
    "href": "oa:hasTarget",
    "rel": "http://www.iana.org/assignments/relation",
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/system-collection/context.jsonld)

## Sources

* [api/part1/openapi/schemas/geojson/systemCollection.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/systemCollection.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/system-collection`

