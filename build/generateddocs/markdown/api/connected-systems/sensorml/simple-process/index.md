
# SimpleProcess (Schema)

`ogc.api.connected-systems.sensorml.simple-process` *v0.1*

SimpleProcess schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# SimpleProcess

Converted from [`sensorml/schemas/json/SimpleProcess.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/SimpleProcess.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.sensorml.simple-process#ProcessMethod`:

- `ProcessMethod`

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"SimpleProcess"` |  |  |
| `method` | `#/$defs/ProcessMethod` |  |  |

## Examples

1 example(s) taken from the specification are included and validated against this schema.


## Examples

### Simple process
#### json
```json
{
  "$schema": "../../SimpleProcess.json",
  "type": "SimpleProcess",
  "uniqueId": "urn:x-org:process:windchill:001",
  "label": "Wind Chill Process",
  "description": "A simple process for taking temperature and wind speed and determining wind chill.",
  "inputs": [
    {
      "name": "temp",
      "type": "Quantity",
      "definition": "http://mmisw.org/ont/cf/parameter/air_temperature",
      "label": "Air Temperature",
      "uom": { "code": "Cel", "symbol": "°C" }
    },
    {
      "name": "wind",
      "type": "Quantity",
      "definition": "http://mmisw.org/ont/cf/parameter/wind_speed",
      "label": "Wind Speed",
      "uom": { "code": "km/h" }
    }
  ],
  "outputs": [
    {
      "name": "wind_chill",
      "type": "Quantity",
      "definition": "http://mmisw.org/ont/cf/parameter/wind_chill_of_air_temperature",
      "label": "Wind Chill Factor",
      "uom": { "code": "Cel", "symbol": "°C" }
    }
  ],
  "method": {
    "description": "The formula used to compute windchill is:\nTwc = 13.12 + 0.6215*Ta - 11.37*v^0.16 + 0.3965*Ta*v^0.16, where\nTwc is the wind chill index on the Celsius temperature scale;\nTa is the air temperature in degrees Celsius;\nv is the wind speed at 10 m AGL, in km/h"
  }
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
      const: SimpleProcess
    method:
      $ref: '#/$defs/ProcessMethod'
$defs:
  ProcessMethod:
    type: object
    properties:
      algorithm:
        title: A description of the algorithm using a machine readable language, either
          inline or by reference
      description:
        title: A description of the method in natural language
        type: string
    $anchor: ProcessMethod

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/simple-process/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/simple-process/schema.yaml)

## Sources

* [sensorml/schemas/json/SimpleProcess.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/SimpleProcess.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/simple-process`

