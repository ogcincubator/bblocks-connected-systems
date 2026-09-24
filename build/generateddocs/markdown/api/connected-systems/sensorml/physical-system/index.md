
# PhysicalSystem (Schema)

`ogc.api.connected-systems.sensorml.physical-system` *v0.1*

PhysicalSystem schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# PhysicalSystem

Converted from [`sensorml/schemas/json/PhysicalSystem.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/PhysicalSystem.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"PhysicalSystem"` |  |  |
| `components` | `AggregateProcess.json#/$defs/ComponentList` |  | The list of sub-components |
| `connections` | `AggregateProcess.json#/$defs/ConnectionList` |  |  |

## Known failing examples

4 example(s) taken from the specification do **not** validate against this schema. They are included as negative tests (`tests/spec-*-fail.json`), which pass only while the problem persists:

- `sensor_datasheet_with_modes.json`: `DescribedObject` requires `uniqueId`, which embedded components/modes/processes in the example do not have.
- `sensor_instance_with_parent_and_frame.json`: `timeInstantOrNow` is a `oneOf`: the string `now` matches both the `const` and the `date-time` branch.
- `system_with_components_and_connections.json`: `timeInstantOrNow` is a `oneOf`: the string `now` matches both the `const` and the `date-time` branch.
- `weather_station_system.json`: `DescribedObject` requires `uniqueId`, which embedded components/modes/processes in the example do not have.

## Examples

4 example(s) taken from the specification are included and validated against this schema.


## Examples

### Physical system instance
#### json
```json
{
  "$schema": "../../PhysicalSystem.json",
  "type": "PhysicalSystem",
  "definition": "http://www.w3.org/ns/sosa/Sensor",
  "uniqueId": "urn:x-meteofrance:stations:davis:WS00010",
  "label": "Meteo France Weather Station WS00010",
  "typeOf": {
    "href": "http://example.org/api/procedures/2ev1rrr8dkeuu",
    "uid": "urn:x-davis:station:vantagepro2",
    "type": "application/sml+json"
  },
  "contacts": [
    {
      "role": "http://sensorml.com/ont/swe/property/Operator",
      "organisationName": "Meteo France",
      "contactInfo": {
        "website": "https://www.meteo.fr",
        "phone": {
          "voice": "+33 5 61 07 80 80"
        },
        "address": {
          "deliveryPoint": "42 avenue Gaspard-Coriolis",
          "city": "TOULOUSE",
          "postalCode": "31057 Cedex 1",
          "country": "France"
        }
      }
    }
  ],
  "position": {
    "type": "Point",
    "coordinates": [
      1.35997,
      43.637788
    ]
  }
}
```


### Sensor instance with config
#### json
```json
{
  "$schema": "../PhysicalSystem.json",
  "type": "PhysicalSystem",
  "id": "123",
  "definition": "http://www.w3.org/ns/sosa/Sensor",
  "uniqueId": "urn:x-org:systems:001",
  "label": "Outdoor Thermometer 001",
  "description": "Digital thermometer located on first floor window 1",
  "typeOf": {
    "href": "https://data.example.org/api/procedures/TP60S?f=sml",
    "uid": "urn:x-myorg:datasheets:ThermoPro:TP60S:v001",
    "title": "ThermoPro TP60S",
    "type" : "application/sml+json"
  },
  "identifiers": [
    {
      "definition": "http://sensorml.com/ont/swe/property/SerialNumber",
      "label": "Serial Number",
      "value": "0123456879"
    }
  ],
  "contacts": [
    {
      "role": "http://sensorml.com/ont/swe/roles/Operator",
      "organisationName": "Field Maintenance Corp."
    }
  ],
  "configuration": {
    "setValues": [
      {
        "ref": "parameters/gain",
        "value": 1.6
      },
      {
        "ref": "parameters/offset",
        "value": -0.3
      }
    ],
    "setArrayValues": [
      {
        "ref": "parameters/calCoefs",
        "value": [1.6, 2.8, 0.035]
      }
    ],
    "setModes": [
      {
        "ref": "modes/OPERATING_MODES",
        "value": "TEST"
      }
    ],
    "setConstraints": [
      {
        "type": "AllowedValues",
        "ref": "inputs/temperature",
        "intervals": [[-100, 230.0]]
      },
      {
        "type": "AllowedTokens",
        "ref": "parameters/tag",
        "pattern": "[a-zA-Z0-9]"
      }
    ]
  },
  "position": {
    "type": "Point",
    "coordinates": [41.8781, -87.6298]
  }
}
```


### Sensor instance with geojson location
#### json
```json
{
  "$schema": "../PhysicalSystem.json",
  "type": "PhysicalSystem",
  "definition": "http://www.w3.org/ns/sosa/Sensor",
  "uniqueId": "urn:x-org:sensors:001",
  "label": "Sensor with GeoJson location",
  "position": {
    "type": "Point",
    "coordinates": [41.8781, -87.6298]
  }
}
```


### Sensor instance with geopose quat
#### json
```json
{
  "$schema": "../PhysicalSystem.json",
  "type": "PhysicalSystem",
  "definition": "http://www.w3.org/ns/sosa/Sensor",
  "uniqueId": "urn:x-org:sensors:001",
  "label": "Sensor with GeoPose",
  "position": {
    "type": "GeoPose",
    "position": {
      "lat": 47.7,
      "lon": -122.3,
      "h": 11.5
    },
    "quaternion": {
      "x": 0.22876396167290736,
      "y": -0.038868031178080464,
      "z": 0.16293209735513692,
      "w": -0.9589626987758765
    }
  }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/abstract-physical-process/schema.yaml
- properties:
    type:
      const: PhysicalSystem
    components:
      description: The list of sub-components
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/aggregate-process/schema.yaml#ComponentList
    connections:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/aggregate-process/schema.yaml#ConnectionList

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/physical-system/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/physical-system/schema.yaml)

## Sources

* [sensorml/schemas/json/PhysicalSystem.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/PhysicalSystem.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/physical-system`

