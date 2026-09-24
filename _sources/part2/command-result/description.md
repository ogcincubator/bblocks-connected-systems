<!-- generated -->
# CommandResult

Converted from [`api/part2/openapi/schemas/json/commandResult.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandResult.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | yes | Local identifier of the result resource |
| `command@id` | `string` | yes | Local identifier of the command that this result is associated to |

## Known failing examples

3 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `command-result-datastream.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.
- `command-result-inline.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.
- `command-result-single-obs.json`: Request payload validated against the response schema: `readOnly` properties (`id`, `live`, `system@link`...) are `required`.

## Examples

3 example(s) taken from the specification are included and validated against this schema.

