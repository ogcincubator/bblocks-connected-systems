
# AbstractPhysicalProcess (Schema)

`ogc.api.connected-systems.sensorml.abstract-physical-process` *v0.1*

AbstractPhysicalProcess schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# AbstractPhysicalProcess

Converted from [`sensorml/schemas/json/AbstractPhysicalProcess.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/AbstractPhysicalProcess.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.sensorml.abstract-physical-process#SpatialFrame`:

- `SpatialFrame`: A general spatial Cartesian Reference Frame where the axes and origin will be defined textually relative to a physical component.
- `TemporalFrame`: A general temporal frame such as a mission start time or timer start time. The origin should just describe context of the start of time (e.g., start of local timer).
- `Position`

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `attachedTo` | `commonDefs.json#/$defs/XLink` |  | References the physical component or system (e.g., platform) to which to which this component or system is attached. |
| `localReferenceFrames` | `array` |  | A list of spatial reference frames, attached to the physical component itself. |
| `localTimeFrames` | `array` |  | Supports local time reference frames such as "time past mission start". Note that units are handled in timePosition so they are not specified in the TemporalFrame. |
| `position` | `#/$defs/Position` |  | Provides positional information relating the component's spatial reference frame to an external spatial reference frame. |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
allOf:
- $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/abstract-process/schema.yaml
- properties:
    attachedTo:
      description: References the physical component or system (e.g., platform) to
        which to which this component or system is attached.
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    localReferenceFrames:
      description: A list of spatial reference frames, attached to the physical component
        itself.
      type: array
      items:
        $ref: '#/$defs/SpatialFrame'
    localTimeFrames:
      description: Supports local time reference frames such as "time past mission
        start". Note that units are handled in timePosition so they are not specified
        in the TemporalFrame.
      type: array
      items:
        $ref: '#/$defs/TemporalFrame'
    position:
      description: Provides positional information relating the component's spatial
        reference frame to an external spatial reference frame.
      $ref: '#/$defs/Position'
$defs:
  SpatialFrame:
    description: A general spatial Cartesian Reference Frame where the axes and origin
      will be defined textually relative to a physical component.
    type: object
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-swe-identifiable/schema.yaml
    - properties:
        origin:
          description: A textual description of the origin of the reference frame
            relative to the physical device (e.g., "the origin is at the point of
            attachment of the sensor to the platform").
          type: string
        axes:
          description: Axis with name attribute and a textual description of the relationship
            of the axis to the physical device; the order of the axes listed determines
            their relationship according to the right-handed rule (e.g., axis 1 cross
            axis 2 = axis 3).
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              description:
                type: string
            required:
            - name
            - description
      required:
      - origin
      - axes
    unevaluatedProperties: false
    $anchor: SpatialFrame
  TemporalFrame:
    description: A general temporal frame such as a mission start time or timer start
      time. The origin should just describe context of the start of time (e.g., start
      of local timer).
    type: object
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-swe-identifiable/schema.yaml
    - properties:
        origin:
          type: string
      required:
      - origin
    unevaluatedProperties: false
    $anchor: TemporalFrame
  Position:
    oneOf:
    - title: by Text
      description: A textual description of where the system is located (e.g., a building
        name, a room number, etc.)
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/text/schema.yaml
    - title: by Point
      $ref: https://geojson.org/schema/Point.json
    - title: by Pose
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/pose/schema.yaml
    - title: by Process
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/abstract-process/schema.yaml
    - title: by Datastream
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml
    - title: by Location Vector
      deprecated: true
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/vector/schema.yaml
    - title: by Position (DataRecord)
      deprecated: true
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-record/schema.yaml
    - title: by Trajectory (DataArray)
      deprecated: true
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/data-array/schema.yaml
    $anchor: Position

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/abstract-physical-process/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/abstract-physical-process/schema.yaml)

## Sources

* [sensorml/schemas/json/AbstractPhysicalProcess.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/AbstractPhysicalProcess.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/abstract-physical-process`

