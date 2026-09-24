
# DataStream (Schema)

`ogc.api.connected-systems.swecommon.data-stream` *v0.1*

Defines the structure of the element that will be repeated in the stream

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# DataStream

Defines the structure of the element that will be repeated in the stream

Converted from [`swecommon/schemas/json/DataStream.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/DataStream.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"DataStream"` | yes |  |
| `elementType` |  | yes | Definition and structure of one stream element |
| `encoding` |  | yes | Method used to encode the stream values |
| `values` | `basicTypes.json#/$defs/AssociationAttributeGroup` |  | Encoded values for the stream (can be out of band) |

## Known issues in the source

This block is a faithful copy of the upstream file, which has the following mismatches with the examples of the specification (see `SCHEMA-FIXES.md`):

- The DataStream example does not validate: the first field of `elementType` has no `name`, which is required. Possible resolution: add `"name": "time"` to the example.

## Known failing examples

1 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `datastream1.json`: The first field of `elementType` has no `name`, which is required (this is an example bug, not a schema bug).


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Defines the structure of the element that will be repeated in the stream
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-swe-identifiable/schema.yaml
- properties:
    type:
      const: DataStream
    elementType:
      description: Definition and structure of one stream element
      allOf:
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#SoftNamedProperty
      - oneOf:
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AssociationAttributeGroup
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
    encoding:
      description: Method used to encode the stream values
      oneOf:
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#BinaryEncoding
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#TextEncoding
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#XMLEncoding
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml#JSONEncoding
    values:
      description: Encoded values for the stream (can be out of band)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AssociationAttributeGroup
  required:
  - type
  - elementType
  - encoding

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-stream/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-stream/schema.yaml)

## Sources

* [swecommon/schemas/json/DataStream.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/DataStream.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/data-stream`

