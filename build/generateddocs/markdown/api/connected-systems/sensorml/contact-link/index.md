
# ContactLink (Schema)

`ogc.api.connected-systems.sensorml.contact-link` *v0.1*

ContactLink schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# ContactLink

Converted from [`sensorml/schemas/json/ContactLink.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/ContactLink.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `role` | `string` |  | Role of the contact |
| `name` | `string` | yes | Name of the contact |
| `link` | `commonDefs.json#/$defs/XLink` | yes | Link to complete contact information |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  role:
    description: Role of the contact
    type: string
    format: uri
  name:
    description: Name of the contact
    type: string
  link:
    description: Link to complete contact information
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
unevaluatedProperties: false
required:
- name
- link

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/contact-link/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/contact-link/schema.yaml)

## Sources

* [sensorml/schemas/json/ContactLink.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/ContactLink.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/contact-link`

