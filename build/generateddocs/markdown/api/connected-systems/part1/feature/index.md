
# Feature (GeoJSON) (Schema)

`ogc.api.connected-systems.part1.feature` *v0.1*

Generic GeoJSON feature used as the base of the Connected Systems feature resources, with local `id`, `geometry`, `bbox`, free-form `properties` and `links`.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Feature (GeoJSON)

Converted from [`api/part1/openapi/schemas/geojson/feature.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/feature.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` |  |  | Local ID of the feature (ignored on create or update) |
| `geometry` |  |  | Geometry of the feature |
| `bbox` |  |  | Optional bounding box for the feature |
| `properties` | `object` |  | Feature properties |
| `links` | `../common/links.json` |  | Links to related resources |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml
- type: object
  properties:
    id:
      description: Local ID of the feature (ignored on create or update)
      minLength: 1
    geometry:
      description: Geometry of the feature
    bbox:
      description: Optional bounding box for the feature
    properties:
      description: Feature properties
      type: object
      required:
      - featureType
      - uid
      - name
      properties:
        featureType:
          description: Identifier of the type of feature, either a URI, a CURIE, or
            a simple token
          type: string
        uid:
          description: Globally unique identifier of the feature
          type: string
          format: uri
          example: urn:x-org:namespace:id
        name:
          description: Human readable name of the feature
          type: string
          minLength: 1
        description:
          description: Human readable description of the feature
          type: string
          minLength: 1
    links:
      description: Links to related resources
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/feature/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/feature/schema.yaml)


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
[context.jsonld](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/feature/context.jsonld)

## Sources

* [api/part1/openapi/schemas/geojson/feature.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/feature.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/feature`

