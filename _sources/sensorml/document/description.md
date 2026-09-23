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

