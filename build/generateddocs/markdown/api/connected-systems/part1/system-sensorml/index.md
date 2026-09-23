
# System (SensorML) (Schema)

`ogc.api.connected-systems.part1.system-sensorml` *v0.1*

A System (SensorML 3.0 JSON encoding): a sensor, actuator, platform, sampler or other asset that produces observations or receives commands, with its identity, type and relationships to other resources.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# System (SensorML)

Converted from [`api/part1/openapi/schemas/sensorml/system.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/system.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `definition` | `../common/uris.json#/$defs/SystemTypeUris` | yes |  |
| `links` | `../common/links.json` |  | Links to related resources |

## Examples

2 example(s) taken from the specification are included and validated against this schema.


## Examples

### Thermometer sensor sml
#### json
```json
{
  "type": "PhysicalSystem",
  "id": "123",
  "definition": "http://www.w3.org/ns/sosa/Sensor",
  "uniqueId": "urn:x-ogc:systems:001",
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
  "position": {
    "type": "Point",
    "coordinates": [41.8781, -87.6298]
  }
}
```


### Uav platform sml
#### json
```json
{
  "type": "PhysicalSystem",
  "id": "PLT412",
  "definition": "http://www.w3.org/ns/sosa/Platform",
  "uniqueId": "urn:x-usaf:systems:aircraft:101",
  "label": "Global Hawk 101",
  "description": "Example UAV platform",
  "typeOf": {
    "href": "https://data.example.org/api/procedures/ge4pjqq0hq6y?f=json",
    "uid": "urn:x-ngc:datasheets:uav:RQ-4B",
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
      "role": "http://sensorml.com/ont/swe/property/Operator",
      "organisationName": "Field Maintenance Corp."
    }
  ],
  "localReferenceFrames": [
    {
      "label": "Platform Frame",
      "description": "The platform frame is defined as the aircraft principal axes",
      "origin": "Center of gravity of the aircraft",
      "axes": [
        {
          "name": "x",
          "description": "Longitudinal or roll axis, parallel to the fuselage reference line, directed forward"
        },
        {
          "name": "y",
          "description": "Transverse or pitch axis, parallel to the line drawn from wingtip to wingtip, directed to the right of the aircraft when looking forward"
        },
        {
          "name": "z",
          "description": "Vertical or yaw axis, perpendicular to the wings and to the fuselage reference line, directed toward the bottom of the aircraft"
        }
      ]
    }
  ]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- oneOf:
  - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/simple-process/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/aggregate-process/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/physical-component/schema.yaml
  - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/physical-system/schema.yaml
- properties:
    definition:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/uris/schema.yaml#SystemTypeUris
    links:
      description: Links to related resources
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml
  required:
  - definition
  - uniqueId

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/system-sensorml/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/system-sensorml/schema.yaml)

## Sources

* [api/part1/openapi/schemas/sensorml/system.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/system.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/system-sensorml`

