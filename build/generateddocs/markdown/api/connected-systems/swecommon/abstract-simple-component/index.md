
# AbstractSimpleComponent (Schema)

`ogc.api.connected-systems.swecommon.abstract-simple-component` *v0.1*

AbstractSimpleComponent schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# AbstractSimpleComponent

Converted from [`swecommon/schemas/json/AbstractSimpleComponent.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/AbstractSimpleComponent.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `referenceFrame` | `string` |  | Frame of reference (usually temporal or spatial) with respect to which the value of the component is expressed. A reference frame anchors a value to a real world datum. |
| `axisID` | `string` |  | Specifies the reference axis (refer to CRS axisID). The reference frame URI should also be specified unless it is inherited from parent Vector |
| `nilValues` |  |  | Defines reserved values with special meaning (e.g., missing, out-of-range, etc.) |
| `constraint` |  |  |  |
| `value` |  |  | Inline value(s) for the component. This property is optional to enable structure to act as a schema for values provided separately (e.g., in a datastream) |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-data-component/schema.yaml
- properties:
    referenceFrame:
      description: Frame of reference (usually temporal or spatial) with respect to
        which the value of the component is expressed. A reference frame anchors a
        value to a real world datum.
      type: string
      format: uri-reference
    axisID:
      description: Specifies the reference axis (refer to CRS axisID). The reference
        frame URI should also be specified unless it is inherited from parent Vector
      type: string
      minLength: 1
    nilValues:
      description: Defines reserved values with special meaning (e.g., missing, out-of-range,
        etc.)
    constraint: {}
    value:
      description: Inline value(s) for the component. This property is optional to
        enable structure to act as a schema for values provided separately (e.g.,
        in a datastream)

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml)

## Sources

* [swecommon/schemas/json/AbstractSimpleComponent.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/AbstractSimpleComponent.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/abstract-simple-component`

