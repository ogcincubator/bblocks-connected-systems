<!-- generated -->
# DataStream

Converted from [`api/part2/openapi/schemas/json/dataStream.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/dataStream.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `system@link` | `../common/commonDefs.json#/$defs/Link` | yes | Link to the system producing the observations |
| `outputName` | `string` |  | Name of the system output feeding this datastream |
| `procedure@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the procedure used to acquire observations (only provided if all observations in the datastream share the same procedure) |
| `deployment@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the deployment during which the observations are/were collected (only provided if all observations in the datastream share the same deployment) |
| `featureOfInterest@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the ultimate feature of interest (only provided if all observations in the datastream share the same feature of interest) |
| `samplingFeature@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the sampling feature (only provided if all observations in the datastream share the same sampling feature) |
| `observedProperties` |  | yes |  |
| `phenomenonTime` |  | yes |  |
| `phenomenonTimeInterval` | `string` |  | An indication of how often feature of interest properties are observed |
| `resultTime` |  | yes |  |
| `resultTimeInterval` | `string` |  | An indication of how often observation results are produced |
| `type` | `string` |  |  |
| `resultType` |  | yes |  |
| `live` |  | yes |  |
| `schema` | `observationSchema.json` |  | Schema describing the content of observations in this datastream. The exact syntax of the schema depends on the encoding format. |
| `links` | `../common/commonDefs.json#/$defs/Links` |  | Other links to related resources |

## Known failing examples

1 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `datastream-external-link-edr.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.

## Examples

2 example(s) taken from the specification are included and validated against this schema.

