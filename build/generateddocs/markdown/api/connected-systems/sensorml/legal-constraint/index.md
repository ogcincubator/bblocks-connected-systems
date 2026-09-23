
# LegalConstraint (Schema)

`ogc.api.connected-systems.sensorml.legal-constraint` *v0.1*

LegalConstraint schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# LegalConstraint

Converted from [`sensorml/schemas/json/LegalConstraint.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/LegalConstraint.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.sensorml.legal-constraint#CodeListValue`:

- `CodeListValue`

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `useLimitations` | `array` |  |  |
| `accessConstraints` | `array` |  |  |
| `useConstraints` | `array` |  |  |
| `otherConstraints` | `array` |  |  |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  useLimitations:
    type: array
    items:
      type: string
  accessConstraints:
    type: array
    items:
      $ref: '#/$defs/CodeListValue'
  useConstraints:
    type: array
    items:
      $ref: '#/$defs/CodeListValue'
  otherConstraints:
    type: array
    items:
      type: string
$defs:
  CodeListValue:
    type: object
    properties:
      codeSpace:
        type: string
        format: uri
      value:
        type: string
    additionalProperties: false
    $anchor: CodeListValue

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/legal-constraint/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/legal-constraint/schema.yaml)

## Sources

* [sensorml/schemas/json/LegalConstraint.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/LegalConstraint.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/legal-constraint`

