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

