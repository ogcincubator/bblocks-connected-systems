
# Text (Schema)

`ogc.api.connected-systems.swecommon.text` *v0.1*

Free text component used to store comments or any other type of textual statement

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Text

Free text component used to store comments or any other type of textual statement

Converted from [`swecommon/schemas/json/Text.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Text.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"Text"` | yes |  |
| `constraint` | `basicTypes.json#/$defs/AllowedTokens` |  |  |
| `nilValues` | `basicTypes.json#/$defs/NilValuesText` |  |  |
| `value` | `string` |  |  |

## Examples

5 example(s) taken from the specification are included and validated against this schema.


## Examples

### AllowedTokens1
#### json
```json
{
  "type": "Text",
  "definition": "http://sensorml.com/ont/swe/property/ModelNumber",
  "label": "Model Number",
  "constraint": {
    "pattern": "^[0-9][A-Z]{3}[0-9]{2}S1$"
  }
}
```


### Nil values3
#### json
```json
{
  "type": "Text",
  "definition": "http://sensorml.com/ont/x-swe/property/VehicleRegistrationNumber",
  "label": "License Plate",
  "nilValues": [
    { "reason": "http://www.opengis.net/def/nil/OGC/0/Missing", "value": "Missing" },
    { "reason": "http://www.opengis.net/def/nil/OGC/0/Unknown", "value": "Unknown" }
  ]
}
```


### Text1
#### json
```json
{
  "type": "Text",
  "definition": "http://sensorml.com/ont/swe/property/Manufacturer",
  "label": "Manufacturer",
  "value": "Ocean Devices, Inc."
}
```


### Text2
#### json
```json
{
  "type": "Text",
  "definition": "http://sensorml.com/ont/x-swe/property/VehicleRegistrationNumber",
  "label": "License Plate",
  "value": "45ER-EJK-235"
}
```


### Text3
#### json
```json
{
  "type": "Text",
  "definition": "http://sensorml.com/ont/x-swe/property/VehicleRegistrationNumber",
  "label": "License Plate",
  "constraint": {
    "pattern": "^[0-9][A-Z]{4}-[A-Z]{3}-[0-9]{3}$"
  }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Free text component used to store comments or any other type of textual
  statement
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml
- properties:
    type:
      const: Text
    constraint:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AllowedTokens
    nilValues:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#NilValuesText
    value:
      type: string
  required:
  - type
  - definition
  - label

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/text/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/text/schema.yaml)

## Sources

* [swecommon/schemas/json/Text.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/Text.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/text`

