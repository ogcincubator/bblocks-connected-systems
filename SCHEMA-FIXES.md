# Differences from the upstream schemas

The blocks in `_sources/` are generated copies of the JSON schemas in
[opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems)
by `tools/convert.py`. Beyond mechanical changes (`$ref`s to `bblocks://` URIs, `$anchor` added to every
`$defs` entry), the blocks are **faithful copies** of the upstream schemas: the problems below are deliberately
**not fixed**, so that the specification's own examples that fail against the schemas are visible. Each such example
is included as a negative test (`tests/spec-*-fail.json`, 42 in total), which passes only while the problem exists,
and is listed in the block's `description.md` under "Known failing examples". All 110 blocks therefore pass
validation, and the failures can be seen in the test report.

In several cases it is **not known whether the schema or the example is wrong**, so the changes below are only
possible resolutions to be discussed upstream. `python3 tools/convert.py --fixed` regenerates the register with them
applied (10 of the 42 negative tests then become regular examples, and all blocks still pass), which shows that they
would resolve the mismatches.

## Mismatches between schemas and examples

Possible schema changes (not applied); for 3 and 4 the examples could be changed instead.

| # | Upstream file | Possible change | Reason |
|---|---|---|---|
| 1 | `swecommon/schemas/json/basicTypes.json` `DateTimeNumberOrSpecial` | `oneOf` → `anyOf` | Strings such as `+Infinity` match both branches (date-time and special number) unless `format` is asserted, so valid values fail `oneOf`. |
| 2 | `common/timeInstantOrNow.json` | `oneOf` → `anyOf` | The string `now` also matches the `date-time` branch unless `format` is asserted; spec examples with `"now"` fail. |
| 3 | `sensorml/schemas/json/DescribedObject.json` | `uniqueId` removed from `required` | Embedded components, modes and inline processes in the spec examples (`weather_station_system.json`, `process_chain.json`, `sensor_datasheet_with_modes.json`) have no `uniqueId`. Top-level systems still require it in the Part 1 system schemas. |
| 4 | `api/part1/openapi/schemas/common/uris.json` `ProcedureTypeUris` | added `http://www.w3.org/ns/ssn-system/SensorKind` | Used as `featureType` / `definition` in the spec's procedure examples (`sensor-datasheet-*.json`, `ins-sensor-sml.json`). Alternative: change the examples. |

Also checked against the upstream schemas directly: mismatches 2 and 3 are reproducible there (upstream examples fail
validation with the upstream schemas).

## Example that does not validate

This one is most likely an example bug (a required member is missing); not changed.

| Example | Possible change |
|---|---|
| `swecommon/schemas/json/examples/spec/datastream1.json` | Add `"name": "time"` to the first field of `elementType` (`name` is required by `SoftNamedProperty`). |

## Other known failing examples

The 10 examples affected by the mismatches above are listed, with the reason, in `tools/excluded_examples.json` (entries
marked `fixed`). These further upstream examples do not validate against the corresponding schema either, and would
need a schema redesign or changes to the examples:

- **Request payloads vs. response schemas** (Part 2: observation `*-create`, command, command-result, command-status
  inline results, data-stream / control-stream `*-create`, datastream-external-link-edr): the schemas describe
  the response representation and mark `id`, `live`, `system@link`... as `readOnly` *and* `required`. Plain JSON
  Schema validation does not ignore readOnly properties the way OpenAPI request validation does. A proper
  fix is to model create/update payloads as separate schemas.
- **Property examples** (`api/part1/openapi/examples/properties/*.json`): use `id` but no `uniqueId`, which the
  property schema requires.

## Findings: the "link" schema is not the shared link it appears to be

`common/link.json` looks like the OGC API link object used almost everywhere else in OGC API standards, and it was
expected to be replaceable by the shared building block `ogc.ogc-utils.json-link` (used by OGC API - Features,
Records, Processes, STAC, JSON-FG, ...). Trying that in this register showed the two are **not compatible**, even
though they look the same at a glance. This is exactly the kind of divergence that is invisible when each
specification copies its own schema and that reusable, validated blocks surface.

| Aspect | Connected Systems `common/link.json` | `ogc.ogc-utils.json-link` |
|---|---|---|
| Required members | `href` only | `href` **and `rel`** |
| `href` format | `uri` | `uri-reference` |
| Extra members | `uid`, `rt`, `if` (RFC 6690) | `anchor`, `length` |
| `hreflang` / `title` | pattern / `minLength: 1` | unconstrained |
| JSON-LD context | none | maps to Web Annotation (`oa:`) / `dct:` |

What happened when `part1/links` (the resource `links` arrays) was switched to `json-link`:

- **Validation:** the specification's own `systemEvent.json` example has a link without `rel`
  (`{"href": ..., "type": ..., "title": ...}`) and no longer validates.
- **Scope of the mismatch:** about half of the objects with an `href` in the specification examples have no `rel`.
  Nearly all are *reference links* rather than Web Links: `system@link`, `typeOf`, `sampledFeature@link`,
  `platform@link`, `uom`, ... . In those a `rel` is meaningless, so the SensorML and API reference links
  cannot use `json-link` without relaxing it upstream.
- **Semantic uplift:** `json-link` carries a JSON-LD context, so every block that reaches it gets uplifted. While
  the rest of the register has no semantic annotations, the examples of 5 more blocks (`part1/system-sensorml`,
  `procedure-sensorml`, `deployment-sensorml`, `part2/data-stream`, `control-stream`) uplift to **empty RDF**, which
  the postprocessor reports as an error (104 of 110 blocks passed).
- **Not an issue:** the GeoJSON `Feature`/`FeatureCollection` blocks already require `rel` in `links` (via
  `json-link`), so for GeoJSON resources the effective constraint was already the stricter one, and the local link
  only added `uid`/`rt`/`if` and the `hreflang`/`title` constraints.

Possible resolutions upstream (none applied here):

1. Split the concept: keep a Web Link (`rel` required, aligned with `json-link`) for `links` arrays, and a separate
   *reference link* type (no `rel`) for `@link` properties, `typeOf`, etc.
2. Or make `rel` optional in `json-link` (a change that affects every register that depends on it).
3. Fix the `systemEvent` example (add `rel`), and decide whether `uid`/`rt`/`if` and the `hreflang` pattern
   belong in a shared link block.

The local `common/link` block is therefore kept, and it is deliberately documented as a divergent link model. To be
revisited when semantic annotations are added.

## Findings: overlaps with blocks in other registers

Checked against the blocks published by the OGC meta-registry (2026-09-24). Only schemas were compared; none of
the overlaps below is resolved here, since bridging them is a matter for semantic annotations.

- **SWE Common and SensorML:** no equivalent blocks exist anywhere, so the `swecommon/` and `sensorml/` blocks are
  the first ones for these models. No overlap.
- **Time:** `common/time-period` is a 2-element array of RFC 3339 `date-time` strings (or `now`), while the
  Records (`ogc.api.records.v1.schemas.time`) and JSON-FG (`ogc.geo.json-fg.time`) blocks use an object
  (`date` / `timestamp` / `interval`) with UTC-only timestamps and `..` for open ends. Same concept, different shapes
  and open-end conventions (`now` vs `..`); they are not interchangeable.
- **SOSA (`ogc.sosa.*`):** Part 1 systems, deployments and sampling features and the Part 2 observations correspond
  to `sosa:System`/`Sensor`/`Platform`, `Deployment`, `Sample` and `Observation`, but with a different property model:
  SOSA relations are `object | string` values (`deployedSystem`, `hasFeatureOfInterest`), whereas Connected Systems
  uses `*@link` link objects (`system@link`, `samplingFeature@link`, `datastream@id`); SOSA deployments have
  `startTime`/`endTime`, Connected Systems uses `validTime`. Only the `phenomenonTime` and `resultTime` names coincide.
- **SensorThings (`ogc.api.sta.*`):** `Datastream` and `Observation` are the closest functional counterparts of the
  Part 2 data stream and observation. Naming differs (`@iot.id`, `*@iot.navigationLink`), and the STA schemas are
  JSON Schema draft-04, while Connected Systems uses 2020-12.

These are three models of the same domain (SOSA/SSN, SensorThings, Connected Systems) that a shared building block
register makes directly comparable; they can only be connected through semantics.

## Deliberate non-changes

- Circular references (`DataRecord` ↔ `swe-common#AnyComponent`, etc.) are kept as they are; the postprocessor
  reports them as (experimental) circular dependencies. `basic-types#ElementCount` extends
  `abstract-simple-component`, which creates an additional cycle between the abstract SWE blocks. The cycles are
  harmless for validation, but they show that the SWE Common (and, by extension, SensorML) schemas could be made
  more modular: the abstract base components and the concrete component unions (`AnyComponent`, ...) currently
  reference each other, so no part can be reused in isolation.
