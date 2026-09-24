<!-- generated -->
# ControlStream_create

Converted from [`api/part2/openapi/schemas/json/controlStream_create.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/controlStream_create.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `schema` | `commandSchema.json` | yes | Schema describing the content of commands in this control stream. The exact syntax of the schema depends on the encoding format. |

## Known failing examples

1 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `controlstream-ptz-create.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.

## Examples

1 example(s) taken from the specification are included and validated against this schema.

