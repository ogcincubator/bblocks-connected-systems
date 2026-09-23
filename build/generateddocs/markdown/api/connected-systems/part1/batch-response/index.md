
# Batch_response (Schema)

`ogc.api.connected-systems.part1.batch-response` *v0.1*

Response describing the outcome of a batch create, update or delete operation, reporting the per-item result of each request.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Batch_response

Batch Operation Response

Converted from [`api/part1/openapi/schemas/common/batch_response.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/common/batch_response.json) in the OGC API - Connected Systems repository.


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Batch Operation Response
type: array
minItems: 1
items:
  type: object
  properties:
    id:
      description: Identifier of resource as provided in request
      type: string
    status:
      description: HTTP status code
      type: integer
    location:
      description: URL of created resource (equivalent to HTTP Location header), only
        provided on create
      type: string
      format: uri
    error:
      description: An optional error message
      type: string
  required:
  - id
  - status

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/batch-response/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/batch-response/schema.yaml)

## Sources

* [api/part1/openapi/schemas/common/batch_response.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/common/batch_response.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/batch-response`

