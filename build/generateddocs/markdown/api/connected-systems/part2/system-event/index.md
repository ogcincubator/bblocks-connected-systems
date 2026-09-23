
# SystemEvent (Schema)

`ogc.api.connected-systems.part2.system-event` *v0.1*

A SystemEvent: a time-stamped event in the life of a System (e.g. calibration, maintenance, deployment or failure), stored as a feature-like record with links.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# SystemEvent

Converted from [`api/part2/openapi/schemas/json/systemEvent.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/systemEvent.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` |  |  |  |
| `links` | `../common/commonDefs.json#/$defs/Links` |  | Links to related resources |

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### SystemEvent
#### json
```json
{
  "id": "e5ce3b97-0fe2-4f92-a631-4bba0bd82fb1",
  "label": "Deployment",
  "definition": "https://vocab.nerc.ac.uk/collection/W03/current/W030002/",
  "time": "2015-10-12T12:02:00.000Z",
  "documentation": [
    {
      "name": "log",
      "link": {
        "href": "http://trios.de/lisa3075_installation.log"
      }
    }
  ],
  "links": [
    {
      "href": "https://data.example.com/link/to/resource",
      "type": "application/json",
      "title": "Resource Name"
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/event/schema.yaml
- properties:
    id:
      readOnly: true
    links:
      description: Links to related resources
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml
  required:
  - definition
  - label
  - time

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/system-event/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/system-event/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/systemEvent.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/systemEvent.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/system-event`

