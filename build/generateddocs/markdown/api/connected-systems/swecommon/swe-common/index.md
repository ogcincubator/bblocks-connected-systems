
# SweCommon (Schema)

`ogc.api.connected-systems.swecommon.swe-common` *v0.1*

SweCommon schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# SweCommon

Converted from [`swecommon/schemas/json/sweCommon.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/sweCommon.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.swecommon.swe-common#AnyComponent`:

- `AnyComponent`
- `AnySimpleComponent`
- `AnyScalarComponent`


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$defs:
  AnyComponent:
    oneOf:
    - $ref: '#/$defs/AnySimpleComponent'
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-record/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/vector/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-array/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/matrix/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-choice/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/geometry/schema.yaml
    $anchor: AnyComponent
  AnySimpleComponent:
    oneOf:
    - $ref: '#/$defs/AnyScalarComponent'
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/count-range/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/quantity-range/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/time-range/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/category-range/schema.yaml
    $anchor: AnySimpleComponent
  AnyScalarComponent:
    oneOf:
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/boolean/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/count/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/quantity/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/time/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/category/schema.yaml
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/text/schema.yaml
    $anchor: AnyScalarComponent
oneOf:
- $ref: '#/$defs/AnyComponent'
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-stream/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml)

## Sources

* [swecommon/schemas/json/sweCommon.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/sweCommon.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/swe-common`

