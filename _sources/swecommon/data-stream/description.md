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
- The DataStream example does not validate: the first field of `elementType` has no `name`, which is required. Possible resolution: add `"name": "time"` to the example.

## Known failing examples

1 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `datastream1.json`: The first field of `elementType` has no `name`, which is required (this is an example bug, not a schema bug).

## Examples

1 example(s) taken from the specification are included and validated against this schema.

