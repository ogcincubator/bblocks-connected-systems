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

