
# Procedure (GeoJSON) (Schema)

`ogc.api.connected-systems.part1.procedure` *v0.1*

A Procedure (GeoJSON encoding, a profile of the OGC API - Features feature): a specification of how observations are made or commands are executed, such as a sensor datasheet, method or protocol that systems implement.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Procedure (GeoJSON)

Converted from [`api/part1/openapi/schemas/geojson/procedure.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/procedure.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `geometry` | `null` |  |  |
| `properties` |  |  |  |

## Known failing examples

1 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `sensor-datasheet-geojson.json`: `ProcedureTypeUris` does not allow `http://www.w3.org/ns/ssn-system/SensorKind` (used as `featureType`/`definition`).


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/feature/schema.yaml
- properties:
    geometry:
      type: 'null'
    properties:
      properties:
        featureType:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/uris/schema.yaml#ProcedureTypeUris

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/procedure/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/procedure/schema.yaml)


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
[context.jsonld](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/procedure/context.jsonld)

## Sources

* [api/part1/openapi/schemas/geojson/procedure.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/geojson/procedure.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/procedure`

