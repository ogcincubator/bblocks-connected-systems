
# Property (SensorML) (Schema)

`ogc.api.connected-systems.part1.property-sensorml` *v0.1*

A Property (SensorML 3.0 JSON encoding): a definition of an observable or controllable property (e.g. temperature, wind speed) that systems and procedures can reference.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Property (SensorML)

Converted from [`api/part1/openapi/schemas/sensorml/property.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/property.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `links` | `../common/links.json` |  | Links to related resources |

## Known failing examples

9 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `air-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `avg-cpu-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `combustion-chamber-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `daily-avg-air-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `engine-power.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `engine-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `received-rf-power-xband.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `received-rf-power.json`: Example has `id` but no `uniqueId`, which the property schema requires.
- `water-temp.json`: Example has `id` but no `uniqueId`, which the property schema requires.

## Examples

9 example(s) taken from the specification are included and validated against this schema.


## Examples

### Air temp
#### json
```json
{
  "id": "AirTemp",
  "label": "Air Temperature",
  "description": "Temperature of the air under cover",
  "baseProperty": "http://qudt.org/vocab/quantitykind/Temperature",
  "objectType": "http://dbpedia.org/resource/Atmosphere"
}
```


### Avg cpu temp
#### json
```json
{
  "id": "AverageCpuTemp",
  "label": "Average CPU Temp",
  "description": "Hourly average of the CPU temperature",
  "baseProperty": "http://qudt.org/vocab/quantitykind/Temperature",
  "objectType": "http://dbpedia.org/resource/Central_processing_unit",
  "statistic": "http://sensorml.com/ont/x-stats/HourlyMean"
}
```


### Combustion chamber temp
#### json
```json
{
  "id": "CombustionTemp",
  "label": "Combustion Temp",
  "description": "Temperature measured inside the combustion chamber",
  "baseProperty": "http://qudt.org/vocab/quantitykind/Temperature",
  "objectType": "http://dbpedia.org/resource/Combustion_chamber"
}
```


### Daily avg air temp
#### json
```json
{
  "id": "DailyAverageAirTemp",
  "label": "Daily Average Temperature",
  "description": "Average temperature computed over a 24-hour calendar day, starting at midnight local time at the measurement location",
  "baseProperty": "http://mmisw.org/ont/cf/parameter/air_temperature",
  "statistic": "http://sensorml.com/ont/x-stats/DailyMean"
}
```


### Engine power
#### json
```json
{
  "id": "EnginePower",
  "label": "Engine Power",
  "description": "Mechanical power produced by the engine",
  "baseProperty": "http://qudt.org/vocab/quantitykind/Power",
  "objectType": "http://dbpedia.org/resource/Engine"
}
```


### Engine temp
#### json
```json
{
  "id": "EngineTemp",
  "label": "Engine Temp",
  "description": "Temperature of the engine oil, measured at the bottom of the engine block",
  "baseProperty": "http://qudt.org/vocab/quantitykind/Temperature",
  "objectType": "http://dbpedia.org/resource/Engine"
}
```


### Received rf power xband
#### json
```json
{
  "id": "RFPower_Received_XBand",
  "baseProperty": "http://qudt.org/vocab/quantitykind/RF-Power",
  "label": "Received RF Power (XBand)",
  "description": "RF Power received in band X",
  "qualifiers": [
    {
      "type": "Category",
      "definition": "http://qudt.org/vocab/quantitykind/Frequency",
      "label": "Frequency Band",
      "value": "http://sensorml.com/ont/swe/spectrum/IEEE/X_band"
    }
  ]
}
```


### Received rf power
#### json
```json
{
  "id": "RFPower_Received_620-720",
  "baseProperty": "http://qudt.org/vocab/quantitykind/RF-Power",
  "label": "Received RF Power",
  "description": "RF Power received in band 620-720 MHz",
  "qualifiers": [
    {
      "type": "QuantityRange",
      "definition": "http://qudt.org/vocab/quantitykind/Frequency",
      "label": "Frequency Range",
      "uom": { "code": "MHz" },
      "value": [620.0, 720.0]
    }
  ]
}
```


### Water temp
#### json
```json
{
  "id": "SeaWaterTemp",
  "label": "Seawater Temperature",
  "description": "Temperature of the sea surface water",
  "baseProperty": "http://qudt.org/vocab/quantitykind/Temperature",
  "objectType": "http://dbpedia.org/resource/Seawater"
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/derived-property/schema.yaml
- properties:
    links:
      description: Links to related resources
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml
  required:
  - uniqueId

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/property-sensorml/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/property-sensorml/schema.yaml)

## Sources

* [api/part1/openapi/schemas/sensorml/property.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/property.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/property-sensorml`

