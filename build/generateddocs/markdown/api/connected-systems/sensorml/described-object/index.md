
# DescribedObject (Schema)

`ogc.api.connected-systems.sensorml.described-object` *v0.1*

DescribedObject schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# DescribedObject

Converted from [`sensorml/schemas/json/DescribedObject.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/DescribedObject.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.sensorml.described-object#CharacteristicList`:

- `CharacteristicList`
- `CapabilityList`

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | `string` | yes | Type of object |
| `id` | `string` |  | Local ID of the feature (e.g., locally unique on a server) |
| `description` | `string` |  | A textual description of the feature |
| `uniqueId` | `string` | yes | URI serving as the globally unique identifier of the feature (typically a URN) |
| `label` | `string` | yes | A human readable label for the feature |
| `lang` | `string` |  | Language of this document |
| `keywords` | `array` |  | Short keywords describing the context of this document to aid in discovery. |
| `identifiers` | `array` |  | Additional identifiers for the asset, useful for discovery (e.g., short name, mission id, model number, serial number, etc.). |
| `classifiers` | `array` |  | Classifiers for the asset, useful for discovery (e.g., process type, sensor type, intended application, etc.). |
| `validTime` | `commonDefs.json#/$defs/TimePeriod` |  |  |
| `securityConstraints` | `array` |  | Overall security tagging of process description; Individual tagging of properties can be done using extension properties. |
| `legalConstraints` | `array` |  | Legal constraints applied to this description (e.g., copyrights, legal use, etc.) |
| `characteristics` | `array` |  | Groups of characteristics applicable to this asset under various conditions |
| `capabilities` | `array` |  | Groups of capabilities applicable to this asset under various conditions |
| `contacts` | `array` |  | The list of contacts related to this asset |
| `documents` | `array` |  | Additional documentation about the asset |
| `history` | `array` |  | The list of events related to this asset |

## Differences from the source

This block differs from the upstream file (which should be fixed there too):

- `uniqueId` is no longer in `required`: embedded components, modes and inline processes in the specification examples do not have one. Top-level systems still require it in the Part 1 system schemas.


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
properties:
  type:
    description: Type of object
    type: string
  id:
    description: Local ID of the feature (e.g., locally unique on a server)
    type: string
    minLength: 1
  description:
    description: A textual description of the feature
    type: string
    minLength: 1
  uniqueId:
    description: URI serving as the globally unique identifier of the feature (typically
      a URN)
    type: string
    format: uri
  label:
    description: A human readable label for the feature
    type: string
    minLength: 1
  lang:
    description: Language of this document
    type: string
  keywords:
    description: Short keywords describing the context of this document to aid in
      discovery.
    type: array
    items:
      type: string
      minLength: 1
  identifiers:
    description: Additional identifiers for the asset, useful for discovery (e.g.,
      short name, mission id, model number, serial number, etc.).
    type: array
    items:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#Term
  classifiers:
    description: Classifiers for the asset, useful for discovery (e.g., process type,
      sensor type, intended application, etc.).
    type: array
    items:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#Term
  validTime:
    $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/time-period/schema.yaml
  securityConstraints:
    description: Overall security tagging of process description; Individual tagging
      of properties can be done using extension properties.
    type: array
    items:
      type: object
      properties:
        type:
          type: string
          format: uri
      required:
      - type
      additionalProperties: true
  legalConstraints:
    description: Legal constraints applied to this description (e.g., copyrights,
      legal use, etc.)
    type: array
    items:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/legal-constraint/schema.yaml
  characteristics:
    description: Groups of characteristics applicable to this asset under various
      conditions
    type: array
    items:
      $ref: '#/$defs/CharacteristicList'
  capabilities:
    description: Groups of capabilities applicable to this asset under various conditions
    type: array
    items:
      $ref: '#/$defs/CapabilityList'
  contacts:
    description: The list of contacts related to this asset
    type: array
    items:
      oneOf:
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/responsible-party/schema.yaml
      - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/contact-link/schema.yaml
  documents:
    description: Additional documentation about the asset
    type: array
    items:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/document/schema.yaml
  history:
    description: The list of events related to this asset
    type: array
    items:
      $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/event/schema.yaml
required:
- type
- label
$defs:
  CharacteristicList:
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-swe-identifiable/schema.yaml
    - type: object
      properties:
        definition:
          description: Semantic link to the definition of this group of capabilities
          type: string
          format: uri
        conditions:
          description: The conditions under which the characteristics apply
          type: array
          items:
            $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnySimpleComponent
        characteristics:
          description: The list of characteristics in this group
          type: array
          items:
            $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#AnyProperty
      required:
      - characteristics
    unevaluatedProperties: false
    $anchor: CharacteristicList
  CapabilityList:
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/abstract-swe-identifiable/schema.yaml
    - description: A group of capabilities.
      type: object
      properties:
        definition:
          description: Semantic link to the definition of this group of capabilities
          type: string
          format: uri
        conditions:
          description: The conditions under which the capabilities apply
          type: array
          items:
            $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/swe-common/schema.yaml#AnySimpleComponent
        capabilities:
          description: The list of capabilities in this group
          type: array
          items:
            $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/common-defs/schema.yaml#AnyProperty
      required:
      - capabilities
    unevaluatedProperties: false
    $anchor: CapabilityList

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/described-object/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/sensorml/described-object/schema.yaml)

## Sources

* [sensorml/schemas/json/DescribedObject.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/sensorml/schemas/json/DescribedObject.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/sensorml/described-object`

