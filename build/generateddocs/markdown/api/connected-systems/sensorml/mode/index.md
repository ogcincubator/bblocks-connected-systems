
# Mode (Schema)

`ogc.api.connected-systems.sensorml.mode` *v0.1*

Mode schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Mode

Converted from [`sensorml/schemas/json/Mode.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Mode.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `configuration` | `Settings.json` |  | Value settings that further constrain the properties of the base process in this mode. |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/described-object/schema.yaml
- properties:
    configuration:
      description: Value settings that further constrain the properties of the base
        process in this mode.
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/settings/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/mode/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/mode/schema.yaml)

## Sources

* [sensorml/schemas/json/Mode.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Mode.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/mode`

