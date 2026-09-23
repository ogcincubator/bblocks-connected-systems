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

