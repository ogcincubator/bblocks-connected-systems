
# BaseStream (Schema)

`ogc.api.connected-systems.part2.base-stream` *v0.1*

Properties shared by DataStream and ControlStream resources: local ID, name, description, valid time and the list of supported encoding formats.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# BaseStream

Converted from [`api/part2/openapi/schemas/json/baseStream.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/baseStream.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | yes | Local resource ID. If set on creation, the server may ignore it. |
| `name` | `string` | yes | Human readable name of the resource |
| `description` | `string` |  | Human readable description of the resource |
| `validTime` | `../common/commonDefs.json#/$defs/TimePeriod` |  | Validity period of the resource |
| `formats` | `array` | yes | List of available formats |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  id:
    description: Local resource ID. If set on creation, the server may ignore it.
    type: string
    minLength: 1
    readOnly: true
  name:
    description: Human readable name of the resource
    type: string
    minLength: 1
  description:
    description: Human readable description of the resource
    type: string
    minLength: 1
  validTime:
    description: Validity period of the resource
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
  formats:
    description: List of available formats
    type: array
    minItems: 1
    items:
      type: string
    readOnly: true
required:
- id
- name
- formats

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/base-stream/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/base-stream/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/baseStream.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/baseStream.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/base-stream`

