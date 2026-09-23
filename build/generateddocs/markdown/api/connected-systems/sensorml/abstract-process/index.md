
# AbstractProcess (Schema)

`ogc.api.connected-systems.sensorml.abstract-process` *v0.1*

AbstractProcess schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# AbstractProcess

Converted from [`sensorml/schemas/json/AbstractProcess.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/AbstractProcess.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.sensorml.abstract-process#FeatureList`:

- `FeatureList`
- `InputList`
- `OutputList`
- `ParameterList`
- `ModeChoice`
- `IOComponentChoice`

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `definition` | `string` |  | The type of process or system as a reference to a concept in an online ontology or dictionary. The value of the property must be a resolvable URI. |
| `typeOf` | `commonDefs.json#/$defs/XLink` |  | A reference to a base process from which this process inherits properties and constraints (e.g., original equipment manufacturer's model description, generic equation, etc.). |
| `configuration` | `Settings.json` |  | Value settings that further constrain the properties of the base process. |
| `featuresOfInterest` | `#/$defs/FeatureList` |  | A collection of sampling features or domain features relevant to the process (e.g., the Gulf of Mexico, the White House, the Atmosphere, a vehicle, etc.). |
| `inputs` | `#/$defs/InputList` |  | The list of process or system inputs. |
| `outputs` | `#/$defs/OutputList` |  | The list of process or system outputs. |
| `parameters` | `#/$defs/ParameterList` |  | The list of process or system parameters. |
| `modes` | `array` |  | A collection of parameters that can be set at once through the selection of a particular predefined mode. |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/described-object/schema.yaml
- properties:
    definition:
      description: The type of process or system as a reference to a concept in an
        online ontology or dictionary. The value of the property must be a resolvable
        URI.
      type: string
      format: uri
    typeOf:
      description: A reference to a base process from which this process inherits
        properties and constraints (e.g., original equipment manufacturer's model
        description, generic equation, etc.).
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    configuration:
      description: Value settings that further constrain the properties of the base
        process.
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/settings/schema.yaml
    featuresOfInterest:
      description: A collection of sampling features or domain features relevant to
        the process (e.g., the Gulf of Mexico, the White House, the Atmosphere, a
        vehicle, etc.).
      $ref: '#/$defs/FeatureList'
    inputs:
      description: The list of process or system inputs.
      $ref: '#/$defs/InputList'
    outputs:
      description: The list of process or system outputs.
      $ref: '#/$defs/OutputList'
    parameters:
      description: The list of process or system parameters.
      $ref: '#/$defs/ParameterList'
    modes:
      description: A collection of parameters that can be set at once through the
        selection of a particular predefined mode.
      type: array
      items:
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/mode/schema.yaml
$defs:
  FeatureList:
    type: array
    minItems: 1
    items:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    $anchor: FeatureList
  InputList:
    type: array
    minItems: 1
    items:
      $ref: '#/$defs/IOComponentChoice'
    $anchor: InputList
  OutputList:
    type: array
    minItems: 1
    items:
      $ref: '#/$defs/IOComponentChoice'
    $anchor: OutputList
  ParameterList:
    type: array
    minItems: 1
    items:
      $ref: '#/$defs/IOComponentChoice'
    $anchor: ParameterList
  ModeChoice:
    type: object
    properties:
      modes:
        type: array
        minItems: 1
        items:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/mode/schema.yaml
    $anchor: ModeChoice
  IOComponentChoice:
    oneOf:
    - title: DataComponent
      allOf:
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#SoftNamedProperty
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnyComponent
    - title: ObservableProperty
      allOf:
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#SoftNamedProperty
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#ObservableProperty
    $anchor: IOComponentChoice

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/abstract-process/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/abstract-process/schema.yaml)

## Sources

* [sensorml/schemas/json/AbstractProcess.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/AbstractProcess.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/abstract-process`

