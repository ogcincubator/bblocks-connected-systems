
# DeployedSystem (SensorML) (Schema)

`ogc.api.connected-systems.part1.deployed-system-sensorml` *v0.1*

A deployed System (SensorML 3.0 JSON encoding): a system as listed within a Deployment, tying it to its installation in that deployment.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# DeployedSystem (SensorML)

Converted from [`api/part1/openapi/schemas/sensorml/deployedSystem.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/deployedSystem.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | `string` |  | Local ID of the deployed system resource (e.g., locally unique on a server) |
| `links` | `../common/links.json` |  | Links to related resources |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/deployed-system/schema.yaml
- properties:
    id:
      description: Local ID of the deployed system resource (e.g., locally unique
        on a server)
      type: string
      minLength: 1
      readOnly: true
    links:
      description: Links to related resources
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployed-system-sensorml/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/deployed-system-sensorml/schema.yaml)

## Sources

* [api/part1/openapi/schemas/sensorml/deployedSystem.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/deployedSystem.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/deployed-system-sensorml`

