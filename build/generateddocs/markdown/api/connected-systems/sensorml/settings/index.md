
# Settings (Schema)

`ogc.api.connected-systems.sensorml.settings` *v0.1*

Settings schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Settings

Converted from [`sensorml/schemas/json/Settings.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Settings.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `setValues` | `array` |  |  |
| `setArrayValues` | `array` |  |  |
| `setModes` | `array` |  |  |
| `setConstraints` | `array` |  |  |
| `setStatus` | `array` |  |  |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  setValues:
    type: array
    minItems: 1
    items:
      type: object
      properties:
        ref:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#PathRef
        value:
          oneOf:
          - title: Number
            type: number
          - title: String
            type: string
      required:
      - ref
      - value
      additionalProperties: false
  setArrayValues:
    type: array
    minItems: 1
    items:
      type: object
      properties:
        ref:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#PathRef
        value:
          type: array
      required:
      - ref
      - value
      additionalProperties: false
  setModes:
    type: array
    minItems: 1
    items:
      type: object
      properties:
        ref:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#PathRef
        value:
          type: string
      required:
      - ref
      - value
      additionalProperties: false
  setConstraints:
    type: array
    minItems: 1
    items:
      allOf:
      - properties:
          ref:
            $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#PathRef
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#AnyConstraint
      required:
      - type
      - ref
      additionalProperties: true
  setStatus:
    type: array
    minItems: 1
    items:
      type: object
      properties:
        ref:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#PathRef
        value:
          type: string
          enum:
          - enabled
          - disabled
      required:
      - ref
      - value
      additionalProperties: false

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/settings/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/settings/schema.yaml)

## Sources

* [sensorml/schemas/json/Settings.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Settings.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/settings`

