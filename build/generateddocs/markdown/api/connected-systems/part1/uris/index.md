
# Uris (Schema)

`ogc.api.connected-systems.part1.uris` *v0.1*

Enumerations of the allowed type URIs (from the SSN/SOSA and Connected Systems vocabularies) for System, Deployment and Procedure features.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Uris

Converted from [`api/part1/openapi/schemas/common/uris.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/common/uris.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.part1.uris#SystemTypeUris`:

- `SystemTypeUris`
- `DeploymentTypeUris`
- `ProcedureTypeUris`

## Known issues in the source

This block is a faithful copy of the upstream file, which has the following mismatches with the examples of the specification (see `SCHEMA-FIXES.md`):

- `ProcedureTypeUris` does not allow `http://www.w3.org/ns/ssn-system/SensorKind`, which the specification's own procedure examples use as `featureType`/`definition`. Possible resolution: add it (or change the examples).


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$defs:
  SystemTypeUris:
    type: string
    enum:
    - http://www.w3.org/ns/sosa/Sensor
    - http://www.w3.org/ns/sosa/Actuator
    - http://www.w3.org/ns/sosa/Platform
    - http://www.w3.org/ns/sosa/Sampler
    - http://www.w3.org/ns/sosa/System
    - sosa:Sensor
    - sosa:Actuator
    - sosa:Platform
    - sosa:Sampler
    - sosa:System
    $anchor: SystemTypeUris
  DeploymentTypeUris:
    type: string
    enum:
    - http://www.w3.org/ns/sosa/Deployment
    - sosa:Deployment
    $anchor: DeploymentTypeUris
  ProcedureTypeUris:
    type: string
    enum:
    - http://www.w3.org/ns/sosa/Procedure
    - http://www.w3.org/ns/sosa/ObservingProcedure
    - http://www.w3.org/ns/sosa/SamplingProcedure
    - http://www.w3.org/ns/sosa/ActuatingProcedure
    - http://www.w3.org/ns/sosa/System
    - http://www.w3.org/ns/sosa/Sensor
    - http://www.w3.org/ns/sosa/Actuator
    - http://www.w3.org/ns/sosa/Sampler
    - http://www.w3.org/ns/sosa/Platform
    - sosa:Procedure
    - sosa:ObservingProcedure
    - sosa:SamplingProcedure
    - sosa:ActuatingProcedure
    - sosa:System
    - sosa:Sensor
    - sosa:Actuator
    - sosa:Sampler
    - sosa:Platform
    $anchor: ProcedureTypeUris

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/uris/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/part1/uris/schema.yaml)

## Sources

* [api/part1/openapi/schemas/common/uris.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part1/openapi/schemas/common/uris.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/part1/uris`

