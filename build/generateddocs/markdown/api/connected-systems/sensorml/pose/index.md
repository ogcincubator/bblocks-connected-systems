
# Pose (Schema)

`ogc.api.connected-systems.sensorml.pose` *v0.1*

A Pose object that can be either a GeoPose Basic instance of a relative pose.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Pose

A Pose object that can be either a GeoPose Basic instance of a relative pose.

Converted from [`sensorml/schemas/json/Pose.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Pose.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.sensorml.pose#PositionGeo`:

- `PositionGeo`: Geographic position in EPSG:4979 CRS (WGS84)
- `PositionXYZ`: Cartesian position expressed in the specified reference frame
- `AnglesYPR`: Euler angles, with yaw, pitch and roll rotations about the local (rotated) axes Z, Y, and X respectively, applied in that order
- `Quaternion`: Quaternion orientation expressed in the specified reference frame


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: A Pose object that can be either a GeoPose Basic instance of a relative
  pose.
oneOf:
- type: object
  title: GeoPose YPR
  description: 'Basic-YPR: Basic GeoPose using yaw, pitch, and roll to specify orientation'
  properties:
    type:
      const: GeoPose
    ltpReferenceFrame:
      type: string
      format: uri
    position:
      $ref: '#/$defs/PositionGeo'
    angles:
      $ref: '#/$defs/AnglesYPR'
  required:
  - type
  - position
  - angles
- type: object
  title: GeoPose Quaternion
  description: 'Basic-Quaternion: Basic GeoPose using quaternion to specify orientation'
  properties:
    type:
      const: GeoPose
    ltpReferenceFrame:
      type: string
      format: uri
    position:
      $ref: '#/$defs/PositionGeo'
    quaternion:
      $ref: '#/$defs/Quaternion'
  required:
  - type
  - position
  - quaternion
- type: object
  title: Relative Pose YPR
  description: 'Relative-YPR: Relative pose using yaw, pitch, and roll to specify
    orientation'
  properties:
    type:
      const: RelativePose
    referenceFrame:
      type: string
      format: uri
    position:
      $ref: '#/$defs/PositionXYZ'
    angles:
      $ref: '#/$defs/AnglesYPR'
  required:
  - type
  - referenceFrame
  - position
  - angles
- type: object
  title: Relative Pose Quaternion
  description: 'Relative-Quaternion: Relative pose using quaternion to specify orientation'
  properties:
    type:
      const: RelativePose
    referenceFrame:
      type: string
      format: uri
    position:
      $ref: '#/$defs/PositionXYZ'
    quaternion:
      $ref: '#/$defs/Quaternion'
  required:
  - type
  - referenceFrame
  - position
  - quaternion
$defs:
  PositionGeo:
    description: Geographic position in EPSG:4979 CRS (WGS84)
    properties:
      lat:
        type: number
      lon:
        type: number
      h:
        type: number
    required:
    - lat
    - lon
    - h
    $anchor: PositionGeo
  PositionXYZ:
    description: Cartesian position expressed in the specified reference frame
    properties:
      x:
        description: Distance along the X axis, in meters
        type: number
      y:
        description: Distance along the Y axis, in meters
        type: number
      z:
        description: Distance along the Z axis, in meters
        type: number
    required:
    - x
    - y
    - z
    $anchor: PositionXYZ
  AnglesYPR:
    description: Euler angles, with yaw, pitch and roll rotations about the local
      (rotated) axes Z, Y, and X respectively, applied in that order
    properties:
      yaw:
        description: Yaw angle about Z axis, in degrees
        type: number
      pitch:
        description: Pitch angle about Y axis, in degrees
        type: number
      roll:
        description: Roll angle about X axis, in degrees
        type: number
    required:
    - yaw
    - pitch
    - roll
    $anchor: AnglesYPR
  Quaternion:
    description: Quaternion orientation expressed in the specified reference frame
    properties:
      x:
        type: number
      y:
        type: number
      z:
        type: number
      w:
        type: number
    required:
    - x
    - y
    - z
    - w
    $anchor: Quaternion

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/pose/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/pose/schema.yaml)

## Sources

* [sensorml/schemas/json/Pose.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/Pose.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/pose`

