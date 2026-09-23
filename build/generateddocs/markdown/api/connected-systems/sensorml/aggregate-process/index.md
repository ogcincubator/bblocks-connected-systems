
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

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### Process chain
#### json
```json
{
  "$schema": "../../AggregateProcess.json",
  "type": "AggregateProcess",
  "uniqueId": "urn:x-ogc:process-chain:001",
  "label": "Simple Process Chain",
  "description": "A simple process chain that applies a linear transformation and clips the value to a threshold.",
  "inputs": [
    {
      "name": "valueIn",
      "type": "Quantity",
      "definition": "http://sensorml.com/ont/swe/property/DN",
      "label": "Input Value",
      "uom": { "href": "http://www.opengis.net/def/nil/OGC/0/unknown" }
    }
  ],
  "outputs": [
    {
      "name": "valueOut",
      "type": "Quantity",
      "definition": "http://sensorml.com/ont/swe/property/DN",
      "label": "Output Value",
      "uom": { "href": "http://www.opengis.net/def/nil/OGC/0/unknown" }
    }
  ],
  "components": [
    {
      "name": "scale",
      "type": "SimpleProcess",
      "label": "Linear Transform 01",
      "typeOf": {
        "href": "http://example.org/processlib/linearTransform.json",
        "uid": "urn:x-org:process:LinearTransform:v1.0",
        "title": "Linear Transform"
      },
      "configuration": {
        "setValues": [
          { "ref": "parameters/slope", "value": 2.3 },
          { "ref": "parameters/intercept", "value": 1.76 }
        ]
      }
    },
    {
      "name": "clip",
      "type": "SimpleProcess",
      "label": "Threshold Clipper 01",
      "typeOf": {
        "href": "http://example.org/processlib/thresholdClipper.json",
        "uid": "urn:x-org:process:ThresholdClipper:v1.0",
        "title": "Threshold Clip"
      },
      "configuration": {
        "setValues": [
          { "ref": "parameters/threshold", "value": 15.0 }
        ]
      }
    }
  ],
  "connections": [
    { "source": "inputs/valueIn", "destination": "components/scale/inputs/x" },
    { "source": "components/scale/outputs/y", "destination": "components/clip/inputs/valueIn" },
    { "source": "components/clip/outputs/passValue", "destination": "outputs/valueOut" }
  ]
}
```

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

