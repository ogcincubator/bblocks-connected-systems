
# Boolean (Schema)

`ogc.api.connected-systems.swecommon.boolean` *v0.1*

Scalar component used to express truth: True or False, 0 or 1

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Boolean

Scalar component used to express truth: True or False, 0 or 1

Converted from [`swecommon/schemas/json/Boolean.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Boolean.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"Boolean"` | yes |  |
| `value` | `boolean` |  |  |

## Examples

2 example(s) taken from the specification are included and validated against this schema.


## Examples

### Boolean1
#### json
```json
{
  "type": "Boolean",
  "definition": "http://sweet.jpl.nasa.gov/2.0/physDynamics.owl#Motion",
  "label": "Motion Detected",
  "description": "True when motion was detected in the room",
  "value": true
}
```


### Boolean2
#### json
```json
{
  "type": "Boolean",
  "definition": "http://mmisw.org/ont/q2o/test/timeContinuityTest",
  "label": "Time Continuity Test",
  "description": "Set to true to enable time continuity test"
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Scalar component used to express truth: True or False, 0 or 1'
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml
- properties:
    type:
      const: Boolean
    value:
      type: boolean
  required:
  - type
  - definition
  - label

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/boolean/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/boolean/schema.yaml)

## Sources

* [swecommon/schemas/json/Boolean.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Boolean.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/boolean`

