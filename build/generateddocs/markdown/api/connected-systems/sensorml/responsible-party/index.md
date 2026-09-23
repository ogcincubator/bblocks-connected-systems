
# ResponsibleParty (Schema)

`ogc.api.connected-systems.sensorml.responsible-party` *v0.1*

ResponsibleParty schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ResponsibleParty

Converted from [`sensorml/schemas/json/ResponsibleParty.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/ResponsibleParty.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.sensorml.responsible-party#Contact`:

- `Contact`
- `Phone`
- `Address`

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `individualName` | `string` |  |  |
| `organisationName` | `string` |  |  |
| `positionName` | `string` |  |  |
| `contactInfo` | `#/$defs/Contact` |  |  |
| `role` | `string` | yes |  |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  individualName:
    type: string
  organisationName:
    type: string
  positionName:
    type: string
  contactInfo:
    $ref: '#/$defs/Contact'
  role:
    type: string
    format: uri
unevaluatedProperties: false
required:
- role
oneOf:
- title: Individual
  required:
  - individualName
- title: Organization
  required:
  - organisationName
$defs:
  Contact:
    type: object
    properties:
      phone:
        $ref: '#/$defs/Phone'
      address:
        $ref: '#/$defs/Address'
      website:
        type: string
      hoursOfService:
        type: string
      contactInstructions:
        type: string
    unevaluatedProperties: false
    $anchor: Contact
  Phone:
    type: object
    properties:
      voice:
        type: string
      facsimile:
        type: string
    unevaluatedProperties: false
    $anchor: Phone
  Address:
    type: object
    properties:
      deliveryPoint:
        type: string
      city:
        type: string
      administrativeArea:
        type: string
      postalCode:
        type: string
      country:
        type: string
      electronicMailAddress:
        type: string
        format: email
    unevaluatedProperties: false
    $anchor: Address

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/responsible-party/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/responsible-party/schema.yaml)

## Sources

* [sensorml/schemas/json/ResponsibleParty.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/ResponsibleParty.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/responsible-party`

