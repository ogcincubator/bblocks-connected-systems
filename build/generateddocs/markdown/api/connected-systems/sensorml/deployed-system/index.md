
# DeployedSystem (Schema)

`ogc.api.connected-systems.sensorml.deployed-system` *v0.1*

DeployedSystem schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# DeployedSystem

Converted from [`sensorml/schemas/json/DeployedSystem.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/DeployedSystem.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `description` | `string` |  | A textual description of the deployed system |
| `system` | `commonDefs.json#/$defs/XLink` | yes | Link to the system being deployed |
| `configuration` | `Settings.json` |  | The configuration of the system used during this deployment (e.g., sampling rate setting, etc.) |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  description:
    description: A textual description of the deployed system
    type: string
    minLength: 1
  system:
    description: Link to the system being deployed
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
  configuration:
    description: The configuration of the system used during this deployment (e.g.,
      sampling rate setting, etc.)
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/settings/schema.yaml
required:
- system

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/deployed-system/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/deployed-system/schema.yaml)

## Sources

* [sensorml/schemas/json/DeployedSystem.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/DeployedSystem.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/deployed-system`

