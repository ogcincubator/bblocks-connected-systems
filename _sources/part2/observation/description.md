<!-- generated -->
# Observation

Converted from [`api/part2/openapi/schemas/json/observation.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observation.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | yes | Local ID of the observation |
| `datastream@id` | `string` | yes | Local ID of the datastream that the observation is part of |
| `samplingFeature@id` | `string` |  | Local ID of the sampling feature that is the target of the observation |
| `procedure@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the procedure/method used to make the observation |
| `phenomenonTime` | `../common/commonDefs.json#/$defs/TimeInstant` |  | Time at which the observation result is a valid estimate of the sampling feature property(ies). Defaults to the same value as `resultTime`. |
| `resultTime` | `../common/commonDefs.json#/$defs/TimeInstant` | yes | Time at which the observation result was generated. |
| `parameters` | `object` |  | Parameters of the observation. Must be valid according to the parameters schema provided in the datastream metadata. |
| `result` |  |  | Result of the observation. Must be valid according to the result schema provided in the datastream metadata. |
| `result@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to external result data (e.g., large raster dataset served by a tiling service) |

## Examples

6 example(s) taken from the specification are included and validated against this schema.

