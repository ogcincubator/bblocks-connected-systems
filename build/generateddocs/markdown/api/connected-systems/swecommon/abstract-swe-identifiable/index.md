
# AbstractSweIdentifiable (Schema)

`ogc.api.connected-systems.swecommon.abstract-swe-identifiable` *v0.1*

Base substitution groups for all SWE Common objects with identification metadata

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# AbstractSweIdentifiable

Base substitution groups for all SWE Common objects with identification metadata

Converted from [`swecommon/schemas/json/AbstractSweIdentifiable.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/AbstractSweIdentifiable.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `label` | `string` |  | Human readable label for the object |
| `description` | `string` |  | Human readable description of the object |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Base substitution groups for all SWE Common objects with identification
  metadata
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AbstractSWE
- properties:
    label:
      description: Human readable label for the object
      type: string
      minLength: 1
    description:
      description: Human readable description of the object
      type: string
      minLength: 1

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-swe-identifiable/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-swe-identifiable/schema.yaml)

## Sources

* [swecommon/schemas/json/AbstractSweIdentifiable.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/AbstractSweIdentifiable.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/abstract-swe-identifiable`

