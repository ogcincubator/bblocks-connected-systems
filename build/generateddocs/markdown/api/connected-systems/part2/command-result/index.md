
# CommandResult (Schema)

`ogc.api.connected-systems.part2.command-result` *v0.1*

A CommandResult: a result resource produced by the execution of a Command, linked to it by `command@id` and carrying inline data or a reference to the result.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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


## Examples

### Command result datastream
#### json
```json
{
  "datastream@link": {
    "href": "https://data.example.org/api/datastreams/445ssdf55",
    "title": "Plume Simulation Data",
    "type": "application/json"
  }
}
```


### Command result inline
#### json
```json
{
  "data": {
    "mean": "10.51",
    "stdev": "1.23"
  }
}
```


### Command result single obs
#### json
```json
{
  "observation@link": {
    "href": "https://data.example.org/api/observations/gss45sdf413s387g49445ssdf55?f=json",
    "title": "Satellite Image",
    "type": "application/json"
  }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  id:
    description: Local identifier of the result resource
    type: string
    minLength: 1
    readOnly: true
  command@id:
    description: Local identifier of the command that this result is associated to
    type: string
    minLength: 1
    readOnly: true
required:
- id
- command@id
oneOf:
- title: Inline result
  properties:
    id: {}
    command@id: {}
    data:
      description: Inline JSON data encoded according to the control stream result
        schema
  required:
  - data
- title: Link to a single observation
  properties:
    id: {}
    command@id: {}
    observation@link:
      description: Link to an observation resulting from the execution of the command
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
  required:
  - observation@link
- title: Link to a set of observations
  properties:
    id: {}
    command@id: {}
    observationSet@link:
      description: Link to a set of observations resulting from the execution of the
        command
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
  required:
  - observationSet@link
- title: Link to a datastream
  properties:
    id: {}
    command@id: {}
    datastream@link:
      description: Link to a datastream containing observations resulting from the
        execution of the command
      allOf:
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
      - properties:
          resultTime:
            description: Time range during which the resulting observations were generated
              (If not provided, the entire datastream is assumed to be the result)
            $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
  required:
  - datastream@link
- title: Link to an external dataset
  properties:
    id: {}
    command@id: {}
    external@link:
      description: Link to an external dataset containing the result(s) of the command
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
  required:
  - external@link

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-result/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/command-result/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/commandResult.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/commandResult.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/command-result`

