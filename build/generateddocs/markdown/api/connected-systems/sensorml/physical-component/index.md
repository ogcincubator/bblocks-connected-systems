
# PhysicalComponent (Schema)

`ogc.api.connected-systems.sensorml.physical-component` *v0.1*

PhysicalComponent schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# PhysicalComponent

Converted from [`sensorml/schemas/json/PhysicalComponent.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/PhysicalComponent.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `"PhysicalComponent"` |  |  |
| `method` | `SimpleProcess.json#/$defs/ProcessMethod` |  |  |

## Examples

2 example(s) taken from the specification are included and validated against this schema.


## Examples

### Physical component
#### json
```json
{
  "$schema": "../../PhysicalComponent.json",
  "type": "PhysicalComponent",
  "definition": "http://www.w3.org/ns/sosa/Sensor",
  "uniqueId": "urn:x-org:systems:001",
  "label": "Outdoor Thermometer 001",
  "description": "Digital thermometer located on first floor window 1",
  "typeOf": {
    "href": "https://data.example.org/api/procedures/TP60S?f=sml",
    "title": "ThermoPro TP60S",
    "type" : "application/sml+json"
  },
  "position": {
    "type": "Point",
    "coordinates": [41.8781, -87.6298]
  }
}
```


### Sensor instance with geopose ypr
#### json
```json
{
  "$schema": "../PhysicalComponent.json",
  "type": "PhysicalComponent",
  "definition": "http://www.w3.org/ns/sosa/Sensor",
  "uniqueId": "urn:x-org:sensors:001",
  "label": "Sensor with GeoPose",
  "position": {
    "type": "GeoPose",
    "ltpReferenceFrame": "http://www.opengis.net/def/cs/OGC/0/NED",
    "position": {
      "lat": 47.7,
      "lon": -122.3,
      "h": 11.5
    },
    "angles": {
      "yaw": 5.946590591427664,
      "pitch": -0.4683537318018044,
      "roll": 0.0
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
      const: PhysicalComponent
    method:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/simple-process/schema.yaml#ProcessMethod

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/physical-component/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/physical-component/schema.yaml)

## Sources

* [sensorml/schemas/json/PhysicalComponent.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/PhysicalComponent.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/physical-component`

