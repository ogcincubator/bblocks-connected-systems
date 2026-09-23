
# Document (Schema)

`ogc.api.connected-systems.sensorml.document` *v0.1*

Document schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Document

Converted from [`sensorml/schemas/json/Document.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Document.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `role` | `string` |  | Type of document (semantic link) |
| `name` | `string` | yes | Name of the document |
| `description` | `string` |  | Human readable description of the document |
| `link` | `commonDefs.json#/$defs/XLink` | yes | URI of the document (Favor a URL if the document is directly accessible online) |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  role:
    description: Type of document (semantic link)
    type: string
    format: uri
  name:
    description: Name of the document
    type: string
  description:
    description: Human readable description of the document
    type: string
  link:
    description: URI of the document (Favor a URL if the document is directly accessible
      online)
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
unevaluatedProperties: false
required:
- name
- link

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/document/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/document/schema.yaml)

## Sources

* [sensorml/schemas/json/Document.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Document.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/document`

