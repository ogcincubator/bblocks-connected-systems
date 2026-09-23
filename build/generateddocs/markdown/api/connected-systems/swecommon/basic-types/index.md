
# BasicTypes (Schema)

`ogc.api.connected-systems.swecommon.basic-types` *v0.1*

BasicTypes schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$defs:
  AbstractSWE:
    $schema: https://json-schema.org/draft/2020-12/schema
    description: Base substitution groups for all SWE Common objects other than value
      objects
    type: object
    properties:
      id:
        description: The ID of the object, referenceable using a URI fragment
        type: string
        minLength: 1
    $anchor: AbstractSWE
  UnitReference:
    type: object
    properties:
      label:
        description: A human readable label for the unit
        type: string
        minLength: 1
      symbol:
        description: The preferred unit symbol to use when presenting the data in
          a UI (use the UCUM code instead if no symbol is provided)
        type: string
        minLength: 1
      code:
        type: string
        minLength: 1
      href:
        type: string
        format: uri
    anyOf:
    - title: UCUM Code
      required:
      - code
    - title: URI
      required:
      - href
    unevaluatedProperties: false
    $anchor: UnitReference
  AllowedTokens:
    description: Defines permitted values for the component, as an enumerated list
      of tokens or a regular expression pattern
    type: object
    oneOf:
    - title: Enum Values
      properties:
        type:
          const: AllowedTokens
        values:
          type: array
          minItems: 1
          items:
            type: string
            minLength: 1
      required:
      - values
    - title: Regex Pattern
      properties:
        type:
          const: AllowedTokens
        pattern:
          type: string
          format: regex
          minLength: 1
      required:
      - pattern
    $anchor: AllowedTokens
  AllowedValues:
    description: Defines the permitted values for the component as an enumerated list
      and/or a list of inclusive ranges
    type: object
    properties:
      type:
        const: AllowedValues
      values:
        type: array
        minItems: 1
        items:
          $ref: '#/$defs/NumberOrSpecial'
      intervals:
        type: array
        minItems: 1
        items:
          type: array
          minItems: 2
          maxItems: 2
          items:
            $ref: '#/$defs/NumberOrSpecial'
      significantFigures:
        type: integer
        minimum: 1
        maximum: 40
    anyOf:
    - title: Enum Values
      required:
      - values
    - title: Intervals
      required:
      - intervals
    $anchor: AllowedValues
  AllowedTimes:
    description: Defines the permitted values for the component, as a time range or
      an enumerated list of time values
    type: object
    properties:
      type:
        const: AllowedTimes
      values:
        type: array
        minItems: 1
        items:
          $ref: '#/$defs/DateTimeNumberOrSpecial'
      intervals:
        type: array
        items:
          type: array
          minItems: 2
          maxItems: 2
          items:
            $ref: '#/$defs/DateTimeNumberOrSpecial'
      significantFigures:
        type: integer
        minimum: 1
        maximum: 40
    anyOf:
    - title: Enum Values
      required:
      - values
    - title: Intervals
      required:
      - intervals
    $anchor: AllowedTimes
  NilValuesText:
    type: array
    minItems: 1
    items:
      type: object
      properties:
        reason:
          description: The reason for using the reserved value
          type: string
          format: uri
        value:
          description: The reserved value itself
          type: string
      required:
      - reason
      - value
      additionalProperties: false
    $anchor: NilValuesText
  NilValuesInteger:
    type: array
    minItems: 1
    items:
      type: object
      properties:
        reason:
          description: The reason for using the reserved value
          type: string
          format: uri
        value:
          description: The reserved value itself
          type: integer
      required:
      - reason
      - value
      additionalProperties: false
    $anchor: NilValuesInteger
  NilValuesNumber:
    type: array
    minItems: 1
    items:
      type: object
      properties:
        reason:
          description: The reason for using the reserved value
          type: string
          format: uri
        value:
          description: The reserved value itself
          $ref: '#/$defs/NumberOrSpecial'
      required:
      - reason
      - value
      additionalProperties: false
    $anchor: NilValuesNumber
  NilValuesTime:
    type: array
    minItems: 1
    items:
      type: object
      properties:
        reason:
          description: The reason for using the reserved value
          type: string
          format: uri
        value:
          description: The reserved value itself
          $ref: '#/$defs/DateTimeNumberOrSpecial'
      required:
      - reason
      - value
      additionalProperties: false
    $anchor: NilValuesTime
  SoftNamedProperty:
    type: object
    properties:
      name:
        $ref: '#/$defs/NameToken'
    required:
    - name
    $anchor: SoftNamedProperty
  NameToken:
    type: string
    minLength: 1
    pattern: ^[A-Za-z][A-Za-z0-9_\-]*$
    $anchor: NameToken
  AssociationAttributeGroup:
    type: object
    properties:
      href:
        type: string
        format: uri-reference
      role:
        type: string
        format: uri
      arcrole:
        type: string
        format: uri
      title:
        type: string
        minLength: 1
    required:
    - href
    $anchor: AssociationAttributeGroup
  NumberOrSpecial:
    oneOf:
    - title: Number
      type: number
    - title: Special Value
      type: string
      enum:
      - NaN
      - Infinity
      - +Infinity
      - -Infinity
    $anchor: NumberOrSpecial
  DateTimeNumberOrSpecial:
    $anchor: DateTimeNumberOrSpecial
    anyOf:
    - title: Date/Time
      type: string
      format: date-time
    - $ref: '#/$defs/NumberOrSpecial'
  ElementCount:
    type: object
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-simple-component/schema.yaml
    - properties:
        constraint:
          $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AllowedValues
        value:
          description: Value is optional, to enable structure to act as a schema for
            values provided using other encodings
          type: integer
    $anchor: ElementCount
  EncodedValues:
    oneOf:
    - type: array
    - $ref: '#/$defs/AssociationAttributeGroup'
    $anchor: EncodedValues

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml)

## Sources

* [swecommon/schemas/json/basicTypes.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/basicTypes.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/basic-types`

