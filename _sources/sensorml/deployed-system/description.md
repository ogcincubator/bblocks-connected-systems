<!-- generated -->
# DeployedSystem

Converted from [`sensorml/schemas/json/DeployedSystem.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/DeployedSystem.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `description` | `string` |  | A textual description of the deployed system |
| `system` | `commonDefs.json#/$defs/XLink` | yes | Link to the system being deployed |
| `configuration` | `Settings.json` |  | The configuration of the system used during this deployment (e.g., sampling rate setting, etc.) |

