<!-- generated -->
# BasicTypes

Converted from [`swecommon/schemas/json/basicTypes.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/basicTypes.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.swecommon.basic-types#AbstractSWE`:

- `AbstractSWE`: Base substitution groups for all SWE Common objects other than value objects
- `UnitReference`
- `AllowedTokens`: Defines permitted values for the component, as an enumerated list of tokens or a regular expression pattern
- `AllowedValues`: Defines the permitted values for the component as an enumerated list and/or a list of inclusive ranges
- `AllowedTimes`: Defines the permitted values for the component, as a time range or an enumerated list of time values
- `NilValuesText`
- `NilValuesInteger`
- `NilValuesNumber`
- `NilValuesTime`
- `SoftNamedProperty`
- `NameToken`
- `AssociationAttributeGroup`
- `NumberOrSpecial`
- `DateTimeNumberOrSpecial`
- `ElementCount`
- `EncodedValues`

## Differences from the source

This block differs from the upstream file (which should be fixed there too):

- `DateTimeNumberOrSpecial` uses `anyOf` instead of `oneOf`: with `oneOf`, the strings `NaN`/`Infinity` etc. match both branches unless `format: date-time` is asserted, which makes valid instances fail.

