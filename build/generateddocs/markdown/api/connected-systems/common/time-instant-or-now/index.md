
# TimeInstantOrNow (Schema)

`ogc.api.connected-systems.common.time-instant-or-now` *v0.1*

Time Instant

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# TimeInstantOrNow

Time Instant

Converted from [`common/timeInstantOrNow.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/common/timeInstantOrNow.json) in the OGC API - Connected Systems repository.

## Differences from the source

This block differs from the upstream file (which should be fixed there too):

- Uses `anyOf` instead of `oneOf`: the string `now` also matches the `date-time` branch unless `format` is asserted, which made valid instances fail.


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Time Instant
anyOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-instant/schema.yaml
- type: string
  const: now

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-instant-or-now/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-instant-or-now/schema.yaml)

## Sources

* [common/timeInstantOrNow.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/common/timeInstantOrNow.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/common/time-instant-or-now`

