
# Deployment (SensorML) (Schema)

`ogc.api.connected-systems.part1.deployment-sensorml` *v0.1*

A Deployment (SensorML 3.0 JSON encoding): the installation of one or more systems at a location and time, describing where and when they operate.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Deployment (SensorML)

Converted from [`api/part1/openapi/schemas/sensorml/deployment.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/deployment.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `definition` | `../common/uris.json#/$defs/DeploymentTypeUris` | yes |  |
| `links` | `../common/links.json` |  | Links to related resources |

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### Deployment sml
#### json
```json
{
  "type": "Deployment",
  "id": "iv3f2kcq27gfi",
  "definition": "http://www.w3.org/ns/sosa/Deployment",
  "uniqueId": "urn:x-saildrone:mission:2025",
  "label": "Saildrone - 2017 Arctic Mission",
  "description": "In July 2017, three saildrones were launched from Dutch Harbor, Alaska, in partnership with NOAA Research...",
  "classifiers": [
    {
      "definition": "https://schema.org/DefinedRegion",
      "label": "Region",
      "value": "Arctic"
    }
  ],
  "contacts": [
    {
      "role": "http://sensorml.com/ont/swe/property/Operator",
      "organisationName": "Saildrone, Inc.",
      "contactInfo": {
        "website": "https://www.saildrone.com/",
        "address": {
          "deliveryPoint": "1050 W. Tower Ave.",
          "city": "Alameda",
          "postalCode": "94501",
          "administrativeArea": "CA",
          "country": "USA"
        }
      }
    },
    {
      "role": "http://sensorml.com/ont/swe/property/DataProvider",
      "organisationName": "NOAA Pacific Marine Environmental Laboratory (PMEL)",
      "contactInfo": {
        "website": "https://www.pmel.noaa.gov"
      }
    }
  ],
  "validTime": [
    "2017-07-17T00:00:00Z",
    "2017-09-29T00:00:00Z"
  ],
  "location": {
    "type": "Polygon",
    "coordinates": [[
      [-173.70, 53.76],
      [-173.70, 75.03],
      [-155.07, 75.03],
      [-155.07, 53.76],
      [-173.70, 53.76]
    ]]
  },
  "platform": {
    "system": {
      "href": "https://data.example.org/api/systems/27559?f=sml",
      "uid": "urn:x-saildrone:platforms:SD-1003",
      "title": "Saildrone SD-1003"
    }
  },
  "deployedSystems": [
    {
      "name": "air_temp_sensor",
      "description": "Air temperature sensor installed in the boom",
      "system": {
        "href": "https://data.example.org/api/systems/41548?f=sml",
        "uid": "urn:x-saildrone:sensors:temp01",
        "title": "Air Temperature Sensor"
      },
      "configuration": {
        "setValues": [{
          "ref": "parameters/sampling_rate",
          "value": 0.1
        }]
      }
    },
    {
      "name": "water_temp_sensor",
      "description": "Water temperature sensor installed on the keel",
      "system": {
        "href": "https://data.example.org/api/systems/36584?f=sml",
        "uid": "urn:x-saildrone:sensors:temp02",
        "title": "Water Temperature Sensor"
      }
    },
    {
      "name": "wind_sensor",
      "description": "Wind sensor installed at the top of the mast",
      "system": {
        "href": "https://data.example.org/api/systems/47752?f=sml",
        "uid": "urn:x-saildrone:sensors:wind01",
        "title": "Wind Speed and Direction Sensor"
      }
    }
  ],
  "links": [
    {
      "rel" : "self",
      "href" : "https://data.example.org/api/deployments/iv3f2kcq27gfi?f=sml",
      "type" : "application/sml+json",
      "title" : "this document"
    }, {
      "rel" : "alternate",
      "href" : "https://data.example.org/api/deployments/iv3f2kcq27gfi?f=json",
      "type" : "application/geo+json",
      "title" : "this resource as GeoJSON"
    }
  ]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/deployment/schema.yaml
- properties:
    definition:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/uris/schema.yaml#DeploymentTypeUris
    links:
      description: Links to related resources
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml
  required:
  - definition
  - uniqueId

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployment-sensorml/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployment-sensorml/schema.yaml)

## Sources

* [api/part1/openapi/schemas/sensorml/deployment.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/deployment.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/deployment-sensorml`

