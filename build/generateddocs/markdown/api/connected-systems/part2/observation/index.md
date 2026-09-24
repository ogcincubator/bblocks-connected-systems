
# Observation (Schema)

`ogc.api.connected-systems.part2.observation` *v0.1*

An Observation: the result of observing a property of a feature of interest at a given time, produced by a System and stored in a DataStream.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Observation

Converted from [`api/part2/openapi/schemas/json/observation.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observation.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | yes | Local ID of the observation |
| `datastream@id` | `string` | yes | Local ID of the datastream that the observation is part of |
| `samplingFeature@id` | `string` |  | Local ID of the sampling feature that is the target of the observation |
| `procedure@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the procedure/method used to make the observation |
| `phenomenonTime` | `../common/commonDefs.json#/$defs/TimeInstant` |  | Time at which the observation result is a valid estimate of the sampling feature property(ies). Defaults to the same value as `resultTime`. |
| `resultTime` | `../common/commonDefs.json#/$defs/TimeInstant` | yes | Time at which the observation result was generated. |
| `parameters` | `object` |  | Parameters of the observation. Must be valid according to the parameters schema provided in the datastream metadata. |
| `result` |  |  | Result of the observation. Must be valid according to the result schema provided in the datastream metadata. |
| `result@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to external result data (e.g., large raster dataset served by a tiling service) |

## Known failing examples

5 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `obs-link-create.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.
- `obs-location-create.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.
- `obs-profile-create.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.
- `obs-simple-create.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.
- `observationSchema-image-link.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.

## Examples

6 example(s) taken from the specification are included and validated against this schema.


## Examples

### Obs geopose
#### json
```json
{
  "id": "maqdpujcj8dkstqhibju0ncmvqqh0k8",
  "datastream@id": "tm3kijpkaoei6",
  "phenomenonTime": "2023-03-15T10:03:34Z",
  "resultTime": "2023-03-15T10:03:34Z",
  "result": {
    "position": {
      "lat": -86.5861,
      "lon": 34.7304,
      "h": 183
    },
    "angles": {
      "yaw": -124.3,
      "pitch": 3.4,
      "roll": -5.8
    }
  }
}
```


### Obs link inline image
#### json
```json
{
  "id": "fefaig45w46v5186d6w",
  "datastream@id": "f44f85rrt",
  "foi@id": "55f48g48th",
  "phenomenonTime": "2023-04-03T18:45:23Z",
  "resultTime": "2023-04-03T18:45:23Z",
  "result@link": {
    "href": "data:image/png;base64,dGhlIGltYWdlIGFzIGJhc2U2NAo=",
    "title": "Inline PNG image",
    "type": "image/png"
  }
}

```


### Obs link
#### json
```json
{
  "id": "fefaig45w46v5186d6w",
  "datastream@id": "f44f85rrt",
  "foi@id": "55f48g48th",
  "phenomenonTime": "2023-04-03T18:45:23Z",
  "resultTime": "2023-04-03T18:45:23Z",
  "result@link": {
    "href": "https://data.x-ecmwf.int/wms?service=WMS&version=1.1.0&request=GetMap&format=image/tiff&layers=HRES-2T-20230215-0600-T1&bbox=-180,90,180,-90&width=3600&height=1800&srs=EPSG:4326",
    "title": "Imagery on external WMS server",
    "type": "image/tiff; application=geotiff",
    "if": "http://www.opengis.net/def/serviceType/ogc/wms/1.1"
  }
}
```


### Obs location
#### json
```json
{
  "id": "1125alnna75hafppknk9aefpvs",
  "datastream@id": "1vf8i5ois38u8",
  "phenomenonTime": "2021-03-15T04:53:34Z",
  "resultTime": "2021-03-15T04:53:34Z",
  "result": {
    "lat": -86.5861,
    "lon": 34.7304,
    "alt": 183
  }
}
```


### Obs profile
#### json
```json
{
  "id": "1125alnna75hafppk4845g4s6",
  "datastream@id": "1vf8i5ois447g",
  "phenomenonTime": "2022-03-15T04:53:34Z",
  "resultTime": "2022-03-15T04:53:34Z",
  "result": [12.5, 11.3, 10.6, 9.1, 7.4, 5.6, 5.5, 5.5, 5.4]
}
```


### Obs simple
#### json
```json
{
  "id": "1h6pmb3ntfmogfppknk9aefpvs",
  "datastream@id": "958tf25kjm2f6",
  "phenomenonTime": "2021-03-15T04:53:34Z",
  "resultTime": "2021-03-15T04:53:34Z",
  "result": 23.5
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  id:
    description: Local ID of the observation
    type: string
    minLength: 1
    readOnly: true
  datastream@id:
    description: Local ID of the datastream that the observation is part of
    type: string
    minLength: 1
    readOnly: true
  samplingFeature@id:
    description: Local ID of the sampling feature that is the target of the observation
    type: string
    minLength: 1
  procedure@link:
    description: Link to the procedure/method used to make the observation
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
  phenomenonTime:
    description: Time at which the observation result is a valid estimate of the sampling
      feature property(ies). Defaults to the same value as `resultTime`.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-instant/schema.yaml
  resultTime:
    description: Time at which the observation result was generated.
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-instant/schema.yaml
  parameters:
    description: Parameters of the observation. Must be valid according to the parameters
      schema provided in the datastream metadata.
    type: object
  result:
    description: Result of the observation. Must be valid according to the result
      schema provided in the datastream metadata.
  result@link:
    description: Link to external result data (e.g., large raster dataset served by
      a tiling service)
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
required:
- id
- datastream@id
- resultTime
oneOf:
- title: Inline result
  required:
  - result
- title: Link to external result
  required:
  - result@link

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/observation.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observation.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/observation`

