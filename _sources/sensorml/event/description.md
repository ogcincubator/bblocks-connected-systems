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

