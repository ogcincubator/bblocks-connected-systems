
# AggregateProcess (Schema)

`ogc.api.connected-systems.sensorml.aggregate-process` *v0.1*

AggregateProcess schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# AggregateProcess

Converted from [`sensorml/schemas/json/AggregateProcess.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/AggregateProcess.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.sensorml.aggregate-process#ComponentList`:

- `ComponentList`
- `ConnectionList`

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"AggregateProcess"` |  |  |
| `components` | `#/$defs/ComponentList` |  | The list of sub-processes |
| `connections` | `#/$defs/ConnectionList` |  | The explicit definition of data links between outputs, inputs, and parameters of the components within an aggregate process. |

## Known failing examples

1 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `process_chain.json`: `DescribedObject` requires `uniqueId`, which embedded components/modes/processes in the example do not have.


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/abstract-process/schema.yaml
- properties:
    type:
      const: AggregateProcess
    components:
      description: The list of sub-processes
      $ref: '#/$defs/ComponentList'
    connections:
      description: The explicit definition of data links between outputs, inputs,
        and parameters of the components within an aggregate process.
      $ref: '#/$defs/ConnectionList'
$defs:
  ComponentList:
    type: array
    minItems: 1
    items:
      allOf:
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#SoftNamedProperty
      - oneOf:
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/simple-process/schema.yaml
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/aggregate-process/schema.yaml
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/physical-component/schema.yaml
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/physical-system/schema.yaml
        - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
          properties:
            type:
              const: Link
    $anchor: ComponentList
  ConnectionList:
    type: array
    minItems: 1
    items:
      type: object
      properties:
        source:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#PathRef
        destination:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#PathRef
      required:
      - source
      - destination
    $anchor: ConnectionList

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/aggregate-process/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/aggregate-process/schema.yaml)

## Sources

* [sensorml/schemas/json/AggregateProcess.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/AggregateProcess.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/aggregate-process`

