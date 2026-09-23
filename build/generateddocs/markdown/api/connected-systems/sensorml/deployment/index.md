
# Deployment (Schema)

`ogc.api.connected-systems.sensorml.deployment` *v0.1*

Deployment schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Deployment

Converted from [`sensorml/schemas/json/Deployment.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Deployment.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"Deployment"` |  |  |
| `definition` | `string` |  | Type of deployment (semantic link) |
| `location` | `https://geojson.org/schema/Geometry.json` |  | The deployment location or area |
| `platform` | `DeployedSystem.json` |  | The platform that the systems are deployed on |
| `deployedSystems` | `array` |  | The list of deployed systems |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/described-object/schema.yaml
- properties:
    type:
      const: Deployment
    definition:
      description: Type of deployment (semantic link)
      type: string
      format: uri
    location:
      description: The deployment location or area
      $ref: https://geojson.org/schema/Geometry.json
    platform:
      description: The platform that the systems are deployed on
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/deployed-system/schema.yaml
    deployedSystems:
      description: The list of deployed systems
      type: array
      items:
        allOf:
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#SoftNamedProperty
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/deployed-system/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/deployment/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/deployment/schema.yaml)

## Sources

* [sensorml/schemas/json/Deployment.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Deployment.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/deployment`

