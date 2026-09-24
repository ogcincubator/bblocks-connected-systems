
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

4 of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:

- `sensor_datasheet_with_modes.json`: `DescribedObject` requires `uniqueId`, which embedded components/modes/processes in the example do not have.
- `sensor_instance_with_parent_and_frame.json`: `timeInstantOrNow` is a `oneOf`: the string `now` matches both the `const` and the `date-time` branch.
- `system_with_components_and_connections.json`: `timeInstantOrNow` is a `oneOf`: the string `now` matches both the `const` and the `date-time` branch.
- `weather_station_system.json`: `DescribedObject` requires `uniqueId`, which embedded components/modes/processes in the example do not have.

## Examples

8 example(s) taken from the specification are included and validated against this schema.


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


### Sensor datasheet with modes
#### json
```json
{
  "$schema": "../PhysicalSystem.json",
  "type": "PhysicalSystem",
  "definition": "http://www.w3.org/ns/sosa/ObservingProcedure",
  "uniqueId": "urn:x-org:sensors:S0001_modes",
  "label": "Sensor With Modes",
  "description": "Sensor with Modes: example where sensor modes can be changed externally and reported in the output",
  "validTime": [
    "2023-07-28T20:44:53.201495Z",
    "now"
  ],
  "inputs": [
    {
      "name": "radiation",
      "type": "ObservableProperty",
      "label": "Radiation",
      "definition": "http://sensorml.com/ont/swe/property/Radiation"
    }
  ],
  "parameters": [
    {
      "name": "settings",
      "type": "DataRecord",
      "fields": [
        {
          "name": "samplingRate",
          "type": "Quantity",
          "definition": "http://sensorml.com/ont/swe/property/SamplingRate",
          "label": "Sampling Rate",
          "updatable": false,
          "uom": {
            "code": "Hz"
          },
          "constraint": {
            "intervals": [
              [ 0.01, 10.0 ]
            ]
          }
        },
        {
          "name": "gain",
          "type": "Quantity",
          "definition": "http://sensorml.com/ont/swe/property/Gain",
          "label": "Gain",
          "updatable": false,
          "uom": {
            "code": "Hz"
          },
          "constraint": {
            "intervals": [
              [ 1.0, 2.5 ]
            ]
          }
        }
      ]
    }
  ],
  "modes": [
    {
      "name": "lowThreat",
      "type": "Mode",
      "label": "Low Threat Mode",
      "description": "Setting when nothing has been detected",
      "configuration": {
        "setValues": [
          {
            "ref": "parameters/settings/samplingRate",
            "value": "1e-1"
          },
          {
            "ref": "parameters/settings/gain",
            "value": "1.0"
          }
        ]
      }
    },
    {
      "id": "highThreat",
      "type": "Mode",
      "label": "High Threat Mode",
      "description": "Setting when something has been detected",
      "configuration": {
        "setValues": [
          {
            "ref": "parameters/settings/samplingRate",
            "value": "10.0"
          },
          {
            "ref": "parameters/settings/gain",
            "value": "2.5"
          }
        ]
      }
    }
  ]
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


### Sensor instance with parent and frame
#### json
```json
{
  "$schema": "../PhysicalSystem.json",
  "type": "PhysicalSystem",
  "id": "6p6978ufjont6",
  "uniqueId": "urn:android:device:c840ed110af5ddf6",
  "definition": "http://www.w3.org/ns/sosa/Sensor",
  "label": "Android Sensors [Galaxy S21 (Alex)]",
  "validTime": [
    "2023-05-28T12:00:00Z",
    "now"
  ],
  "attachedTo": {
    "href": "http://link/to/parent/sensor",
    "title": "Parent Sensor",
    "type": "application/sml+json"
  },
  "localReferenceFrame": {
    "id": "LOCAL_FRAME",
    "origin": "Center of the device screen",
    "axes": [
      {
        "name": "x",
        "description": "The X axis is in the plane of the screen and points to the right"
      },
      {
        "name": "y",
        "description": "The Y axis is in the plane of the screen and points up"
      },
      {
        "name": "z",
        "description": "The Z axis points towards the outside of the front face of the screen"
      }
    ]
  },
  "position": {
    "type": "Point",
    "coordinates": [-86.7228, 34.8038, 0]
  }
}
```


### System with components and connections
#### json
```json
{
  "$schema": "../PhysicalSystem.json",
  "type": "PhysicalSystem",
  "id": "qgqjt7276pa",
  "uniqueId": "urn:x-org:sensor:system:001",
  "definition": "http://www.w3.org/ns/ssn/System",
  "label": "Hierarchical System",
  "description": "Example of hierarchical system with components and connections",
  "validTime": [
    "2015-08-02T20:00:00Z",
    "now"
  ],
  "components": [
    {
      "name": "sensor1",
      "type": "SimpleProcess",
      "uniqueId": "urn:mysensor:002",
      "label": "Magnetometer",
      "description": "My sensor component, described inline",
      "typeOf": {
        "href": "https://data.example.com/link/to/procedure",
        "title": "HS45 Magnetometer"
      }
    },
    {
      "name": "sensor2",
      "href": "http://link/to/sensorml_doc.json",
      "title": "My Sensor"
    }
  ],
  "connections": [
    {
      "source": "components/sensor1/outputs/out",
      "destination": "outputs/out1"
    },
    {
      "source": "components/sensor2/outputs/out",
      "destination": "outputs/out2"
    }
  ]
}
```


### Weather station system
#### json
```json
{
  "$schema": "../PhysicalSystem.json",
  "type": "PhysicalSystem",
  "id": "2ev1rrr8dkeuu",
  "uniqueId": "urn:x-davis:station:vantagepro2",
  "definition": "http://www.w3.org/ns/sosa/Sensor",
  "label": "Davis Vantage Pro2 Weather Station",
  "description": "An industrial-grade weather station engineered to handle the harshest environments and deliver data with scientific precision, year after year. The Vantage Pro2 and Vantage Pro2 Plus offer the professional weather observer or serious weather enthusiast robust performance with a wide range of options and sensors.",
  "identifiers": [
    {
      "definition": "http://sensorml.com/ont/swe/property/ShortName",
      "label": "Short Name",
      "value": "Davis Vantage Pro2"
    },
    {
      "definition": "http://sensorml.com/ont/swe/property/LongName",
      "label": "Long Name",
      "value": "Davis Vantage Pro2 Weather Station"
    },
    {
      "definition": "http://sensorml.com/ont/swe/property/Manufacturer",
      "label": "Manufacturer Name",
      "value": "Davis Instruments"
    },
    {
      "definition": "http://sensorml.com/ont/swe/property/ModelNumber",
      "label": "Model Number",
      "value": "Vantage Pro2"
    }
  ],
  "classifiers": [
    {
      "definition": "http://sensorml.com/ont/swe/property/SensorType",
      "label": "Sensor Type",
      "value": "Weather Station"
    }
  ],
  "characteristics": [
    {
      "label": "Mechanical Characteristics (Console)",
      "characteristics": [
        {
          "type": "Quantity",
          "name": "weight",
          "definition": "http://qudt.org/vocab/quantitykind/Mass",
          "label": "Mass",
          "uom": {
            "code": "g"
          },
          "value": 850.0
        },
        {
          "type": "Quantity",
          "name": "length",
          "definition": "http://qudt.org/vocab/quantitykind/Length",
          "label": "Length",
          "uom": {
            "code": "mm"
          },
          "value": 245.0
        },
        {
          "type": "Quantity",
          "name": "width",
          "definition": "http://sensorml.com/ont/swe/property/Width",
          "label": "Width",
          "uom": {
            "code": "mm"
          },
          "value": 156.0
        },
        {
          "type": "Quantity",
          "name": "height",
          "definition": "http://sensorml.com/ont/swe/property/Height",
          "label": "Height",
          "uom": {
            "code": "mm"
          },
          "value": 41.0
        },
        {
          "type": "Category",
          "name": "material",
          "definition": "http://dbpedia.org/resource/Material",
          "label": "Housing Material",
          "value": "UV-resistant ABS plastic"
        }
      ]
    },
    {
      "label": "Mechanical Characteristics (Sensor Suite)",
      "characteristics": [
        {
          "type": "Quantity",
          "name": "weight",
          "definition": "http://qudt.org/vocab/quantitykind/Mass",
          "label": "Mass",
          "uom": {
            "code": "g"
          },
          "value": 850.0
        },
        {
          "type": "Quantity",
          "name": "length",
          "definition": "http://qudt.org/vocab/quantitykind/Length",
          "label": "Length",
          "uom": {
            "code": "mm"
          },
          "value": 356.0
        },
        {
          "type": "Quantity",
          "name": "width",
          "definition": "http://sensorml.com/ont/swe/property/Width",
          "label": "Width",
          "uom": {
            "code": "mm"
          },
          "value": 239.0
        },
        {
          "type": "Quantity",
          "name": "height",
          "definition": "http://sensorml.com/ont/swe/property/Height",
          "label": "Height",
          "uom": {
            "code": "mm"
          },
          "value": 368.0
        }
      ]
    },
    {
      "label": "Electrical Characteristics",
      "characteristics": [
        {
          "type": "Quantity",
          "name": "voltage",
          "definition": "http://qudt.org/vocab/quantitykind/Voltage",
          "label": "Input Voltage (DC)",
          "uom": {
            "code": "V"
          },
          "value": 5.0
        },
        {
          "type": "Quantity",
          "name": "current",
          "definition": "http://qudt.org/vocab/quantitykind/Current",
          "label": "Max Current",
          "uom": {
            "code": "mA"
          },
          "value": 10.0
        },
        {
          "type": "Text",
          "name": "if_type",
          "definition": "http://dbpedia.org/resource/Interface_(computing)",
          "label": "Interface Type",
          "value": "RS-232"
        }
      ]
    }
  ],
  "capabilities": [
    {
      "definition": "http://www.w3.org/ns/ssn/systems/OperatingRange",
      "label": "Operating Range",
      "capabilities": [
        {
          "type": "QuantityRange",
          "name": "temperature",
          "definition": "http://qudt.org/vocab/quantitykind/Temperature",
          "label": "Temperature Range",
          "uom": {
            "code": "Cel"
          },
          "value": [-40.0, 65.0]
        },
        {
          "type": "QuantityRange",
          "name": "humidity",
          "definition": "http://qudt.org/vocab/quantitykind/RelativeHumidity",
          "label": "Humidity Range",
          "uom": {
            "code": "%"
          },
          "value": [0.0, 100.0]
        }
      ]
    }
  ],
  "contacts": [
    {
      "role": "http://sensorml.com/ont/swe/property/Manufacturer",
      "organisationName": "Davis Instruments Corp.",
      "contactInfo": {
        "website": "https://www.davisinstruments.com",
        "phone": {
          "voice": "+1 (510) 732-7814"
        },
        "address": {
          "deliveryPoint": "3465 Diablo Avenue",
          "city": "Hayward",
          "postalCode": "94545",
          "administrativeArea": "CA",
          "country": "USA",
          "electronicMailAddress": "support@davisinstruments.com"
        }
      }
    }
  ],
  "documents": [
    {
      "role": "http://dbpedia.org/resource/Web_page",
      "name": "Product Web Site",
      "description": "Webpage with specs an other resources",
      "link": {
        "href": "https://www.davisinstruments.com/pages/vantage-pro2",
        "type": "text/html"
      }
    },
    {
      "role": "http://dbpedia.org/resource/Datasheet",
      "name": "Spec Sheet",
      "link": {
        "href": "https://cdn.shopify.com/s/files/1/0515/5992/3873/files/6152c_6162c_ss.pdf",
        "type": "application/pdf"
      }
    },
    {
      "role": "http://dbpedia.org/resource/Photograph",
      "name": "Photo",
      "link": {
        "href": "https://m.media-amazon.com/images/I/71rycLk7sFL.jpg",
        "type": "image/jpg"
      }
    }
  ],
  "components": [
    {
      "type": "PhysicalComponent",
      "name": "temp_sensor",
      "definition": "http://www.w3.org/ns/sosa/Sensor",
      "label": "Temperature Sensor",
      "identifiers": [
        {
          "definition": "http://sensorml.com/ont/swe/property/Manufacturer",
          "label": "Manufacturer Name",
          "value": "Davis Instruments"
        }
      ],
      "classifiers": [
        {
          "definition": "http://sensorml.com/ont/swe/property/SensorType",
          "label": "Sensor Type",
          "value": "Thermometer"
        }
      ],
      "capabilities": [
        {
          "definition": "http://www.w3.org/ns/ssn/systems/SystemCapability",
          "label": "Measurement Capabilities",
          "capabilities": [
            {
              "type": "QuantityRange",
              "name": "range",
              "definition": "http://www.w3.org/ns/ssn/systems/MeasurementRange",
              "label": "Measurement Range",
              "uom": {
                "code": "Cel"
              },
              "value": [-40.0, 60.0]
            },
            {
              "type": "Quantity",
              "name": "resolution",
              "definition": "http://www.w3.org/ns/ssn/systems/Resolution",
              "label": "Resolution",
              "uom": {
                "code": "Cel"
              },
              "value": 0.1
            },
            {
              "type": "Quantity",
              "name": "accuracy",
              "definition": "http://sensorml.com/ont/swe/property/AbsoluteAccuracy",
              "label": "Absolute Accuracy",
              "uom": {
                "code": "Cel"
              },
              "value": 0.3
            },
            {
              "type": "Quantity",
              "name": "samp_freq",
              "definition": "http://sensorml.com/ont/swe/property/SamplingFrequency",
              "label": "Sampling Frequency",
              "uom": {
                "code": "Hz"
              },
              "value": 0.1
            }
          ]
        }
      ],
      "inputs": [
        {
          "name": "temp",
          "type": "ObservableProperty",
          "definition": "http://mmisw.org/ont/cf/parameter/air_temperature",
          "label": "Air Temperature"
        }
      ]
    },
    {
      "type": "PhysicalComponent",
      "name": "press_sensor",
      "definition": "http://www.w3.org/ns/sosa/Sensor",
      "label": "Pressure Sensor",
      "identifiers": [
        {
          "definition": "http://sensorml.com/ont/swe/property/Manufacturer",
          "label": "Manufacturer Name",
          "value": "Davis Instruments"
        }
      ],
      "classifiers": [
        {
          "definition": "http://sensorml.com/ont/swe/property/SensorType",
          "label": "Sensor Type",
          "value": "Barometer"
        }
      ],
      "capabilities": [
        {
          "definition": "http://www.w3.org/ns/ssn/systems/SystemCapability",
          "label": "Measurement Capabilities",
          "capabilities": [
            {
              "type": "QuantityRange",
              "name": "range",
              "definition": "http://www.w3.org/ns/ssn/systems/MeasurementRange",
              "label": "Measurement Range",
              "uom": {
                "code": "hPa"
              },
              "value": [540.0, 1100.0]
            },
            {
              "type": "Quantity",
              "name": "resolution",
              "definition": "http://www.w3.org/ns/ssn/systems/Resolution",
              "label": "Resolution",
              "uom": {
                "code": "hPa"
              },
              "value": 0.1
            },
            {
              "type": "Quantity",
              "name": "accuracy",
              "definition": "http://sensorml.com/ont/swe/property/AbsoluteAccuracy",
              "label": "Absolute Accuracy",
              "uom": {
                "code": "hPa"
              },
              "value": 1.0
            },
            {
              "type": "Quantity",
              "name": "samp_freq",
              "definition": "http://sensorml.com/ont/swe/property/SamplingFrequency",
              "label": "Sampling Frequency",
              "uom": {
                "code": "Hz"
              },
              "value": 0.016
            }
          ]
        }
      ],
      "inputs": [
        {
          "name": "press",
          "type": "ObservableProperty",
          "definition": "http://mmisw.org/ont/cf/parameter/air_pressure",
          "label": "Air Pressure"
        }
      ]
    },
    {
      "type": "PhysicalComponent",
      "name": "hum_sensor",
      "definition": "http://www.w3.org/ns/sosa/Sensor",
      "label": "Humidity Sensor",
      "identifiers": [
        {
          "definition": "http://sensorml.com/ont/swe/property/Manufacturer",
          "label": "Manufacturer Name",
          "value": "Davis Instruments"
        }
      ],
      "classifiers": [
        {
          "definition": "http://sensorml.com/ont/swe/property/SensorType",
          "label": "Sensor Type",
          "value": "Hygrometer"
        }
      ],
      "capabilities": [
        {
          "definition": "http://www.w3.org/ns/ssn/systems/SystemCapability",
          "label": "Measurement Capabilities",
          "capabilities": [
            {
              "type": "QuantityRange",
              "name": "range",
              "definition": "http://www.w3.org/ns/ssn/systems/MeasurementRange",
              "label": "Measurement Range",
              "uom": {
                "code": "%"
              },
              "value": [1.0, 100.0]
            },
            {
              "type": "Quantity",
              "name": "resolution",
              "definition": "http://www.w3.org/ns/ssn/systems/Resolution",
              "label": "Resolution",
              "uom": {
                "code": "%"
              },
              "value": 1.0
            },
            {
              "type": "Quantity",
              "name": "accuracy",
              "definition": "http://sensorml.com/ont/swe/property/AbsoluteAccuracy",
              "label": "Absolute Accuracy",
              "uom": {
                "code": "%"
              },
              "value": 2.0
            },
            {
              "type": "Quantity",
              "name": "samp_freq",
              "definition": "http://sensorml.com/ont/swe/property/SamplingFrequency",
              "label": "Sampling Frequency",
              "uom": {
                "code": "Hz"
              },
              "value": 0.016
            }
          ]
        }
      ],
      "inputs": [
        {
          "name": "hum",
          "type": "ObservableProperty",
          "definition": "http://mmisw.org/ont/cf/parameter/relative_humidity",
          "label": "Relative Humidity"
        }
      ]
    },
    {
      "type": "PhysicalComponent",
      "name": "wind_sensor",
      "definition": "http://www.w3.org/ns/sosa/Sensor",
      "label": "Wind Sensor",
      "identifiers": [
        {
          "definition": "http://sensorml.com/ont/swe/property/Manufacturer",
          "label": "Manufacturer Name",
          "value": "Davis Instruments"
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
              "type": "QuantityRange",
              "name": "range",
              "definition": "http://www.w3.org/ns/ssn/systems/MeasurementRange",
              "label": "Measurement Range",
              "uom": {
                "code": "km/h"
              },
              "value": [1.0, 322.0]
            },
            {
              "type": "Quantity",
              "name": "resolution",
              "definition": "http://www.w3.org/ns/ssn/systems/Resolution",
              "label": "Resolution",
              "uom": {
                "code": "km/h"
              },
              "value": 1.0
            },
            {
              "type": "Quantity",
              "name": "accuracy",
              "definition": "http://sensorml.com/ont/swe/property/AbsoluteAccuracy",
              "label": "Absolute Accuracy",
              "uom": {
                "code": "km/h"
              },
              "value": 3.2
            },
            {
              "type": "Quantity",
              "name": "rel_accuracy",
              "definition": "http://sensorml.com/ont/swe/property/RelativeAccuracy",
              "label": "Relative Accuracy",
              "uom": {
                "code": "%"
              },
              "value": 0.5
            },
            {
              "type": "Quantity",
              "name": "samp_freq",
              "definition": "http://sensorml.com/ont/swe/property/SamplingFrequency",
              "label": "Sampling Frequency",
              "uom": {
                "code": "Hz"
              },
              "value": 0.4
            }
          ]
        },
        {
          "definition": "http://www.w3.org/ns/ssn/systems/SystemCapability",
          "label": "Direction Measurement Capabilities",
          "capabilities": [
            {
              "type": "QuantityRange",
              "name": "range",
              "definition": "http://www.w3.org/ns/ssn/systems/MeasurementRange",
              "label": "Measurement Range",
              "uom": {
                "code": "deg"
              },
              "value": [0.0, 360.0]
            },
            {
              "type": "Quantity",
              "name": "resolution",
              "definition": "http://www.w3.org/ns/ssn/systems/Resolution",
              "label": "Resolution",
              "uom": {
                "code": "deg"
              },
              "value": 1.0
            },
            {
              "type": "Quantity",
              "name": "accuracy",
              "definition": "http://sensorml.com/ont/swe/property/AbsoluteAccuracy",
              "label": "Absolute Accuracy",
              "uom": {
                "code": "deg"
              },
              "value": 3.0
            },
            {
              "type": "Quantity",
              "name": "samp_freq",
              "definition": "http://sensorml.com/ont/swe/property/SamplingFrequency",
              "label": "Sampling Frequency",
              "uom": {
                "code": "Hz"
              },
              "value": 0.4
            }
          ]
        }
      ],
      "inputs": [
        {
          "name": "hum",
          "type": "ObservableProperty",
          "definition": "http://mmisw.org/ont/cf/parameter/wind_speed",
          "label": "Wind Speed"
        }
      ]
    },
    {
      "type": "PhysicalComponent",
      "name": "rain_sensor",
      "definition": "http://www.w3.org/ns/sosa/Sensor",
      "label": "Rainfall Sensor",
      "identifiers": [
        {
          "definition": "http://sensorml.com/ont/swe/property/Manufacturer",
          "label": "Manufacturer Name",
          "value": "Davis Instruments"
        }
      ],
      "classifiers": [
        {
          "definition": "http://sensorml.com/ont/swe/property/SensorType",
          "label": "Sensor Type",
          "value": "Rain Gauge"
        }
      ],
      "capabilities": [
        {
          "definition": "http://www.w3.org/ns/ssn/systems/SystemCapability",
          "label": "Measurement Capabilities",
          "capabilities": [
            {
              "type": "QuantityRange",
              "name": "range",
              "definition": "http://www.w3.org/ns/ssn/systems/MeasurementRange",
              "label": "Measurement Range",
              "uom": {
                "code": "mm"
              },
              "value": [0.0, 999.8]
            },
            {
              "type": "Quantity",
              "name": "resolution",
              "definition": "http://www.w3.org/ns/ssn/systems/Resolution",
              "label": "Resolution",
              "uom": {
                "code": "mm"
              },
              "value": 0.2
            },
            {
              "type": "Quantity",
              "name": "accuracy",
              "definition": "http://sensorml.com/ont/swe/property/AbsoluteAccuracy",
              "label": "Absolute Accuracy",
              "uom": {
                "code": "mm"
              },
              "value": 0.2
            },
            {
              "type": "Quantity",
              "name": "rel_accuracy",
              "definition": "http://sensorml.com/ont/swe/property/RelativeAccuracy",
              "label": "Relative Accuracy",
              "uom": {
                "code": "%"
              },
              "value": 3.0
            },
            {
              "type": "Quantity",
              "name": "samp_freq",
              "definition": "http://sensorml.com/ont/swe/property/SamplingFrequency",
              "label": "Sampling Frequency",
              "uom": {
                "code": "Hz"
              },
              "value": 0.05
            }
          ]
        },
        {
          "definition": "http://www.w3.org/ns/ssn/systems/SystemCapability",
          "label": "Rate Measurement Capabilities",
          "capabilities": [
            {
              "type": "QuantityRange",
              "name": "range",
              "definition": "http://www.w3.org/ns/ssn/systems/MeasurementRange",
              "label": "Measurement Range",
              "uom": {
                "code": "mm/h"
              },
              "value": [0.0, 762.0]
            },
            {
              "type": "Quantity",
              "name": "resolution",
              "definition": "http://www.w3.org/ns/ssn/systems/Resolution",
              "label": "Resolution",
              "uom": {
                "code": "mm/h"
              },
              "value": 0.1
            },
            {
              "type": "Quantity",
              "name": "rel_accuracy",
              "definition": "http://sensorml.com/ont/swe/property/RelativeAccuracy",
              "label": "Relative Accuracy",
              "uom": {
                "code": "%"
              },
              "value": 5.0
            },
            {
              "type": "Quantity",
              "name": "samp_freq",
              "definition": "http://sensorml.com/ont/swe/property/SamplingFrequency",
              "label": "Sampling Frequency",
              "uom": {
                "code": "Hz"
              },
              "value": 0.05
            }
          ]
        }
      ],
      "inputs": [
        {
          "name": "rain",
          "type": "ObservableProperty",
          "definition": "http://mmisw.org/ont/cf/parameter/rainfall_amount",
          "label": "Rainfall Amount"
        }
      ]
    }
  ]
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

