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

