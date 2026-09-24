
# TimeInstantOrNow (Schema)

`ogc.api.connected-systems.common.time-instant-or-now` *v0.1*

Time Instant

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# TimeInstantOrNow

Time Instant

Converted from [`common/timeInstantOrNow.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/common/timeInstantOrNow.json) in the OGC API - Connected Systems repository.

## Known issues in the source

This block is a faithful copy of the upstream file, which has the following mismatches with the examples of the specification (see `SCHEMA-FIXES.md`):

- Uses `oneOf`: the string `now` also matches the `date-time` branch unless `format` is asserted, so valid instances fail. Possible resolution: `anyOf`.


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Time Instant
oneOf:
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

