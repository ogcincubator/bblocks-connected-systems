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

## Differences from the source

This block differs from the upstream file (which should be fixed there too):

- The DataStream example was fixed: the first field of `elementType` had no `name`, which is required.

## Examples

1 example(s) taken from the specification are included and validated against this schema.

