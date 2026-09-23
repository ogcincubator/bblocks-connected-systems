
# Event (Schema)

`ogc.api.connected-systems.sensorml.event` *v0.1*

A time tagged event with description and relevant property values.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Event

A time tagged event with description and relevant property values.

Converted from [`sensorml/schemas/json/Event.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Event.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `definition` | `string` |  | Type of event (semantic link) |
| `identifiers` | `array` |  | Additional identifiers for the event, useful for discovery. |
| `classifiers` | `array` |  | Additional classifiers for the event, useful for discovery. |
| `contacts` | `array` |  | The list of contacts relevant to this event |
| `documentation` | `array` |  | Additional documentation relevant to this event |
| `time` | `commonDefs.json#/$defs/TimeInstantOrPeriod` | yes | Time of the event |
| `properties` | `array` |  | A list of additional properties of interest to the event (e.g., calibration values, condition category, error codes, etc). |
| `configuration` | `Settings.json` |  | Configuration settings adjusted during the event. |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: A time tagged event with description and relevant property values.
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-swe-identifiable/schema.yaml
- properties:
    definition:
      description: Type of event (semantic link)
      type: string
      format: uri
    identifiers:
      description: Additional identifiers for the event, useful for discovery.
      type: array
      items:
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#Term
    classifiers:
      description: Additional classifiers for the event, useful for discovery.
      type: array
      items:
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#Term
    contacts:
      description: The list of contacts relevant to this event
      type: array
      items:
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/responsible-party/schema.yaml
    documentation:
      description: Additional documentation relevant to this event
      type: array
      items:
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/document/schema.yaml
    time:
      description: Time of the event
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#TimeInstantOrPeriod
    properties:
      description: A list of additional properties of interest to the event (e.g.,
        calibration values, condition category, error codes, etc).
      type: array
      items:
        $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#AnyProperty
    configuration:
      description: Configuration settings adjusted during the event.
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/settings/schema.yaml
  required:
  - label
  - time

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/event/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/event/schema.yaml)

## Sources

* [sensorml/schemas/json/Event.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Event.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/event`

