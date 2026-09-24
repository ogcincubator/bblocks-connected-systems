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

