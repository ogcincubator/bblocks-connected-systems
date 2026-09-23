
# DataStream (Schema)

`ogc.api.connected-systems.part2.data-stream` *v0.1*

A DataStream: a time-ordered stream of observations produced by a System, describing the observed properties, result schema and formats. Observations are posted to and retrieved from it.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# DataStream

Converted from [`api/part2/openapi/schemas/json/dataStream.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/dataStream.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `system@link` | `../common/commonDefs.json#/$defs/Link` | yes | Link to the system producing the observations |
| `outputName` | `string` |  | Name of the system output feeding this datastream |
| `procedure@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the procedure used to acquire observations (only provided if all observations in the datastream share the same procedure) |
| `deployment@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the deployment during which the observations are/were collected (only provided if all observations in the datastream share the same deployment) |
| `featureOfInterest@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the ultimate feature of interest (only provided if all observations in the datastream share the same feature of interest) |
| `samplingFeature@link` | `../common/commonDefs.json#/$defs/Link` |  | Link to the sampling feature (only provided if all observations in the datastream share the same sampling feature) |
| `observedProperties` |  | yes |  |
| `phenomenonTime` |  | yes |  |
| `phenomenonTimeInterval` | `string` |  | An indication of how often feature of interest properties are observed |
| `resultTime` |  | yes |  |
| `resultTimeInterval` | `string` |  | An indication of how often observation results are produced |
| `type` | `string` |  |  |
| `resultType` |  | yes |  |
| `live` |  | yes |  |
| `schema` | `observationSchema.json` |  | Schema describing the content of observations in this datastream. The exact syntax of the schema depends on the encoding format. |
| `links` | `../common/commonDefs.json#/$defs/Links` |  | Other links to related resources |

## Examples

2 example(s) taken from the specification are included and validated against this schema.


## Examples

### Datastream simple
#### json
```json
{
  "id": "958tf25kjm2f6",
  "name": "Indoor Thermometer 001 - Living Room Temperature",
  "outputName": "temp",
  "system@link": {
    "href": "https://data.example.org/api/systems/123",
    "uid": "urn:x-ogc:systems:001"
  },
  "featureOfInterest@link": {
    "href": "https://data.example.org/api/collections/buildings/items/754",
    "title": "My House"
  },
  "samplingFeature@link": {
    "href": "https://data.example.org/api/samplingFeatures/4478",
    "title": "Thermometer Sampling Point"
  },
  "phenomenonTime": [
    "2020-06-29T14:32:00Z",
    "2022-06-29T19:37:00Z"
  ],
  "resultTime": [
    "2020-06-29T14:32:00Z",
    "2012-06-29T19:37:00Z"
  ],
  "observedProperties": [
    {
      "definition": "http://mmisw.org/ont/cf/parameter/air_temperature",
      "label": "Room Temperature",
      "description": "Ambient air temperature measured inside the room"
    }
  ],
  "resultType": "measure",
  "formats": [
    "application/json",
    "application/swe+json",
    "application/swe+csv",
    "application/x-protobuf"
  ],
  "live": true,
  "links": [
    {
      "rel" : "observations",
      "href" : "https://data.example.org/api/datastreams/958tf25kjm2f6/observations",
      "type" : "application/json"
    }
  ]
}
```


### Datastream
#### json
```json
{
  "id": "7dogt5gs8949s",
  "name": "Radiological Sensor RADIO003 - Wireless Link Status",
  "system@link": {
    "href": "https://data.example.org/api/systems/958tf25kjm2f6",
    "uid": "urn:x-ogc:systems:FF465",
    "outputName": "radio"
  },
  "featureOfInterest@link": {
    "href": "https://data.example.org/api/systems/4578",
    "uid": "urn:x-ogc:systems:FF465"
  },
  "phenomenonTime": [
    "2012-06-29T14:32:34Z",
    "2012-06-29T14:37:34Z"
  ],
  "resultTime": [
    "2012-06-29T14:32:34Z",
    "2012-06-29T14:37:34Z"
  ],
  "observedProperties": [
    {
      "definition": "http://sensorml.com/ont/isa/property/Link_Loss",
      "label": "Link Loss"
    },
    {
      "definition": "http://sensorml.com/ont/isa/property/Link_State",
      "label": "Link State"
    },
    {
      "definition": "http://sensorml.com/ont/isa/property/Range",
      "label": "Transmission Range"
    },
    {
      "definition": "http://sensorml.com/ont/isa/property/Receive_Power"
    },
    {
      "definition": "http://sensorml.com/ont/isa/property/Signal_Strength_Ratio"
    },
    {
      "definition": "http://sensorml.com/ont/isa/property/Transmit_Power"
    }
  ],
  "resultType": "record",
  "formats": [
    "application/json",
    "application/swe+json",
    "application/swe+csv",
    "application/swe+xml",
    "application/swe+binary"
  ],
  "live": true,
  "links": [
    {
      "rel" : "self",
      "href" : "https://data.example.org/api/datastreams/7dogt5gs8949s",
      "type" : "application/json"
    }, {
      "rel": "observations",
      "href": "https://api.georobotix.io/ogc/t18/api/datastreams/7dogt5gs8949s/observations",
      "type" : "application/json"
    }
  ]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/base-stream/schema.yaml
- properties:
    system@link:
      description: Link to the system producing the observations
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
      readOnly: true
    outputName:
      description: Name of the system output feeding this datastream
      type: string
    procedure@link:
      description: Link to the procedure used to acquire observations (only provided
        if all observations in the datastream share the same procedure)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    deployment@link:
      description: Link to the deployment during which the observations are/were collected
        (only provided if all observations in the datastream share the same deployment)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    featureOfInterest@link:
      description: Link to the ultimate feature of interest (only provided if all
        observations in the datastream share the same feature of interest)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    samplingFeature@link:
      description: Link to the sampling feature (only provided if all observations
        in the datastream share the same sampling feature)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    observedProperties:
      oneOf:
      - type: 'null'
      - description: List of observed properties included in this datastream
        type: array
        minItems: 1
        items:
          type: object
          properties:
            definition:
              type: string
              format: uri
            label:
              type: string
            description:
              type: string
      readOnly: true
    phenomenonTime:
      oneOf:
      - type: 'null'
      - description: Time extent spanning all phenomenon times of observations in
          this datastream
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
      readOnly: true
    phenomenonTimeInterval:
      description: An indication of how often feature of interest properties are observed
      type: string
      format: duration
    resultTime:
      oneOf:
      - type: 'null'
      - description: Time extent spanning all result times of observations in this
          datastream
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
      readOnly: true
    resultTimeInterval:
      description: An indication of how often observation results are produced
      type: string
      format: duration
    type:
      type: string
      enum:
      - status
      - observation
    resultType:
      oneOf:
      - type: 'null'
      - type: string
        enum:
        - measure
        - vector
        - record
        - coverage
        - complex
      readOnly: true
    live:
      oneOf:
      - type: 'null'
      - description: Flag indicating if the datastream is currently streaming data
        type: boolean
    schema:
      description: Schema describing the content of observations in this datastream.
        The exact syntax of the schema depends on the encoding format.
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/observation-schema/schema.yaml
      writeOnly: true
    links:
      description: Other links to related resources
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/links/schema.yaml
required:
- name
- system@link
- observedProperties
- phenomenonTime
- resultTime
- resultType
- live

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/data-stream/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part2/data-stream/schema.yaml)

## Sources

* [api/part2/openapi/schemas/json/dataStream.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/dataStream.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part2/data-stream`

