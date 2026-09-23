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

