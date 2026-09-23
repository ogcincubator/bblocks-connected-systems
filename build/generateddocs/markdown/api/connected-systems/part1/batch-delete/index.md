
# Batch_delete (Schema)

`ogc.api.connected-systems.part1.batch-delete` *v0.1*

Request payload for batch deletion of resources, given as a list of resource URIs, local IDs or unique identifiers (UIDs).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Batch_delete

List of resource URIs, local IDs or UIDs

Converted from [`api/part1/openapi/schemas/common/batch_delete.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/common/batch_delete.json) in the OGC API - Connected Systems repository.


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Batch Delete Request
description: List of resource URIs, local IDs or UIDs
type: array
minItems: 1
items:
  type: string

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/batch-delete/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/batch-delete/schema.yaml)

## Sources

* [api/part1/openapi/schemas/common/batch_delete.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/common/batch_delete.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/batch-delete`

