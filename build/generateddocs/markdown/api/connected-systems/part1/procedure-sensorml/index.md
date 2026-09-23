
# Procedure (SensorML) (Schema)

`ogc.api.connected-systems.part1.procedure-sensorml` *v0.1*

A Procedure (SensorML 3.0 JSON encoding): a specification of how observations are made or commands are executed, such as a sensor datasheet, method or protocol that systems implement.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Procedure (SensorML)

Converted from [`api/part1/openapi/schemas/sensorml/procedure.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/procedure.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `definition` | `../common/uris.json#/$defs/ProcedureTypeUris` | yes |  |
| `position` |  |  |  |
| `links` | `../common/links.json` |  | Links to related resources |

## Examples

2 example(s) taken from the specification are included and validated against this schema.


## Examples

### Ins sensor sml
#### json
```json
{
  "type": "PhysicalSystem",
  "id": "INS001",
  "definition": "http://www.w3.org/ns/ssn-system/SensorKind",
  "uniqueId": "urn:x-vectornav:sensor:vn200",
  "label": "VectorNav VN-200",
  "description": "Datasheet of VN-200 GNSS-aided inertial navigation system",
  "identifiers": [
    {
      "definition": "http://sensorml.com/ont/swe/property/ModelNumber",
      "label": "Model Number",
      "value": "VN-200"
    }
  ],
  "classifiers": [
    {
      "definition": "http://sensorml.com/ont/swe/property/SensorType",
      "label": "Sensor Type",
      "value": "Inertial Navigation System"
    }
  ],
  "contacts": [
    {
      "role": "http://sensorml.com/ont/swe/property/Manufacturer",
      "organisationName": "VectorNav"
    }
  ],
  "capabilities": [
    {
      "definition": "http://www.w3.org/ns/ssn/systems/SystemCapability",
      "label": "Heading Measurement Capabilities",
      "capabilities": [
        {
          "name": "range",
          "type": "QuantityRange",
          "definition": "http://www.w3.org/ns/ssn/systems/MeasurementRange",
          "label": "Measurement Range",
          "uom": {
            "code": "deg"
          },
          "value": [-180.0,180.0]
        },
        {
          "name": "resolution",
          "type": "Quantity",
          "definition": "http://www.w3.org/ns/ssn/systems/Resolution",
          "label": "Resolution",
          "uom": {
            "code": "deg"
          },
          "value": 0.001
        },
        {
          "name": "accuracy",
          "type": "Quantity",
          "definition": "http://sensorml.com/ont/swe/property/AbsoluteAccuracy",
          "label": "Absolute Accuracy (1σ)",
          "uom": {
            "code": "deg"
          },
          "value": 0.2
        }
      ]
    },
    {
      "definition": "http://www.w3.org/ns/ssn/systems/SystemCapability",
      "label": "Pitch Measurement Capabilities",
      "capabilities": [
        {
          "name": "range",
          "type": "QuantityRange",
          "definition": "http://www.w3.org/ns/ssn/systems/MeasurementRange",
          "label": "Measurement Range",
          "uom": {
            "code": "deg"
          },
          "value": [-90.0,90.0]
        },
        {
          "name": "resolution",
          "type": "Quantity",
          "definition": "http://www.w3.org/ns/ssn/systems/Resolution",
          "label": "Resolution",
          "uom": {
            "code": "deg"
          },
          "value": 0.001
        },
        {
          "name": "accuracy",
          "type": "Quantity",
          "definition": "http://sensorml.com/ont/swe/property/AbsoluteAccuracy",
          "label": "Absolute Accuracy (1σ)",
          "uom": {
            "code": "deg"
          },
          "value": 0.03
        }
      ]
    },
    {
      "definition": "http://www.w3.org/ns/ssn/systems/SystemCapability",
      "label": "Roll Measurement Capabilities",
      "capabilities": [
        {
          "name": "range",
          "type": "QuantityRange",
          "definition": "http://www.w3.org/ns/ssn/systems/MeasurementRange",
          "label": "Measurement Range",
          "uom": {
            "code": "deg"
          },
          "value": [-180.0,180.0]
        },
        {
          "name": "resolution",
          "type": "Quantity",
          "definition": "http://www.w3.org/ns/ssn/systems/Resolution",
          "label": "Resolution",
          "uom": {
            "code": "deg"
          },
          "value": 0.001
        },
        {
          "name": "accuracy",
          "type": "Quantity",
          "definition": "http://sensorml.com/ont/swe/property/AbsoluteAccuracy",
          "label": "Absolute Accuracy (1σ)",
          "uom": {
            "code": "deg"
          },
          "value": 0.03
        }
      ]
    }
  ],
  "components": [
    {
      "name": "accel",
      "type": "PhysicalSystem",
      "definition": "http://www.w3.org/ns/sosa/Sensor",
      "uniqueId": "urn:x-vectornav:sensor:vn200:accel",
      "label": "Accelerometer",
      "description": "3-axis accelerometer"
    },
    {
      "name": "gyro",
      "type": "PhysicalSystem",
      "definition": "http://www.w3.org/ns/sosa/Sensor",
      "uniqueId": "urn:x-vectornav:sensor:vn200:gyro",
      "label": "Gyroscope",
      "description": "3-axis gyroscope"
    },
    {
      "name": "mag",
      "type": "PhysicalSystem",
      "definition": "http://www.w3.org/ns/sosa/Sensor",
      "uniqueId": "urn:x-vectornav:sensor:vn200:mag",
      "label": "Magnetometer",
      "description": "3-axis magnetometer"
    }
  ]
}
```


### Sensor datasheet sml
#### json
```json
{
  "type": "PhysicalComponent",
  "id": "iv3f2kcq27gfi",
  "definition": "http://www.w3.org/ns/ssn-system/SensorKind",
  "uniqueId": "urn:osh:sensors:saildrone:S0004",
  "label": "3D Ultrasonic Anemometer",
  "description": "Precision 3-axis ultrasonic anemometer",
  "identifiers": [
    {
      "definition": "http://sensorml.com/ont/swe/property/Manufacturer",
      "label": "Manufacturer Name",
      "value": "Gill"
    },
    {
      "definition": "http://sensorml.com/ont/swe/property/ModelNumber",
      "label": "Model Number",
      "value": "WindMaster"
    }
  ],
  "classifiers": [
    {
      "definition": "http://sensorml.com/ont/swe/property/SensorType",
      "label": "Sensor Type",
      "value": "Anemometer"
    }
  ],
  "capabilities": [
    {
      "definition": "http://www.w3.org/ns/ssn/systems/SystemCapability",
      "label": "Speed Measurement Capabilities",
      "capabilities": [
        {
          "name": "range",
          "type": "QuantityRange",
          "definition": "http://www.w3.org/ns/ssn/systems/MeasurementRange",
          "label": "Measurement Range",
          "uom": {
            "code": "m/s"
          },
          "value": [0.0,50.0]
        },
        {
          "name": "resolution",
          "type": "Quantity",
          "definition": "http://www.w3.org/ns/ssn/systems/Resolution",
          "label": "Resolution",
          "uom": {
            "code": "m/s"
          },
          "value": 0.01
        },
        {
          "name": "accuracy",
          "type": "Quantity",
          "definition": "http://sensorml.com/ont/swe/property/RelativeAccuracy",
          "label": "Relative Accuracy",
          "uom": {
            "code": "%"
          },
          "value": 1.5
        }
      ]
    }
  ],
  "links": [
    {
      "href" : "https://data.example.org/api/procedures/iv3f2kcq27gfi?f=sml",
      "rel" : "self",
      "type" : "application/sml+json",
      "title" : "this document"
    }, {
      "href" : "https://data.example.org/api/procedures/iv3f2kcq27gfi?f=json",
      "rel" : "alternate",
      "type" : "application/geo+json",
      "title" : "this resource as GeoJSON"
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
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/uris/schema.yaml#ProcedureTypeUris
    position:
      not: {}
    links:
      description: Links to related resources
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml
  required:
  - definition
  - uniqueId

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/procedure-sensorml/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/procedure-sensorml/schema.yaml)

## Sources

* [api/part1/openapi/schemas/sensorml/procedure.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/sensorml/procedure.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/procedure-sensorml`

