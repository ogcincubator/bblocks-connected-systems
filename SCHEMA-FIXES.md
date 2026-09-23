# Differences from the upstream schemas

The blocks in `_sources/` are generated copies of the JSON schemas in
[opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems)
by `tools/convert.py`. Beyond mechanical changes (`$ref`s to `bblocks://` URIs, `$anchor` added to every
`$defs` entry), the following differences were introduced. Most fix inconsistencies between the schemas
and the specification's own examples and are candidates to be **backported upstream**.

Every affected block lists its differences in its `description.md`.

## Schema changes

| # | Upstream file | Change | Reason |
|---|---|---|---|
| 1 | `swecommon/schemas/json/basicTypes.json` `DateTimeNumberOrSpecial` | `oneOf` → `anyOf` | Strings such as `+Infinity` match both branches (date-time and special number) unless `format` is asserted, so valid values fail `oneOf`. |
| 2 | `common/timeInstantOrNow.json` | `oneOf` → `anyOf` | The string `now` also matches the `date-time` branch unless `format` is asserted; spec examples with `"now"` fail. |
| 3 | `sensorml/schemas/json/DescribedObject.json` | `uniqueId` removed from `required` | Embedded components, modes and inline processes in the spec examples (`weather_station_system.json`, `process_chain.json`, `sensor_datasheet_with_modes.json`) have no `uniqueId`. Top-level systems still require it in the Part 1 system schemas. |
| 4 | `api/part1/openapi/schemas/common/uris.json` `ProcedureTypeUris` | added `http://www.w3.org/ns/ssn-system/SensorKind` | Used as `featureType` / `definition` in the spec's procedure examples (`sensor-datasheet-*.json`, `ins-sensor-sml.json`). Alternative: change the examples. |

Also checked against the upstream schemas directly: fixes 2 and 3 are reproducible there (upstream examples fail
validation without them).

## Example changes

| Example | Change |
|---|---|
| `swecommon/schemas/json/examples/spec/datastream1.json` | Added `"name": "time"` to the first field of `elementType` (`name` is required by `SoftNamedProperty`). |

## Examples excluded

These upstream examples do not validate against the corresponding schema and were left out (listed in
`tools/excluded_examples.json`):

- **Request payloads vs. response schemas** (Part 2: observation `*-create`, command, command-result, command-status
  inline results, data-stream / control-stream `*-create`, datastream-external-link-edr): the schemas describe
  the response representation and mark `id`, `live`, `system@link`... as `readOnly` *and* `required`. Plain JSON
  Schema validation does not ignore readOnly properties the way OpenAPI request validation does. A proper
  fix is to model create/update payloads as separate schemas.
- **Property examples** (`api/part1/openapi/examples/properties/*.json`): use `id` but no `uniqueId`, which the
  property schema requires.

## Deliberate non-changes

- `common/link.json` was **not** replaced by the OGC API JSON link block (`ogc.ogc-utils.json-link`): the
  latter requires `rel` (SensorML `typeOf`/`attachedTo`/... links have none) and its JSON-LD context makes
  the semantic uplift of SensorML examples produce empty RDF, which the postprocessor reports as an error. To be
  revisited when semantic annotations are added.
- Circular references (`DataRecord` ↔ `swe-common#AnyComponent`, etc.) are kept as they are; the postprocessor
  reports them as (experimental) circular dependencies. `basic-types#ElementCount` extends
  `abstract-simple-component`, which creates an additional cycle between the abstract SWE blocks.
