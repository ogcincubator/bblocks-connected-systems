# OGC API - Connected Systems building blocks

[OGC Blocks](https://opengeospatial.github.io/bblocks/) conversion of the **data models** of
[OGC API - Connected Systems](https://github.com/opengeospatial/ogcapi-connected-systems) and the
encodings it builds on. This is a draft: the schemas are generated from the upstream JSON schemas and
have no semantic annotations (JSON-LD contexts) yet.

| Directory in `_sources/` | Contents |
|---|---|
| `swecommon/` | SWE Common 3.0 JSON data components, encodings and basic types |
| `sensorml/` | SensorML 3.0 JSON (systems, components, processes, deployments, ...) |
| `common/` | Shared time and link schemas |
| `part1/` | Part 1 (Feature resources): GeoJSON and SensorML encodings of systems, deployments, procedures, sampling features, properties |
| `part2/` | Part 2 (Dynamic data): datastreams, observations, control streams, commands, system events |

Out of scope: OpenAPI paths/parameters/responses and the XML encodings.

## Regenerating

`tools/convert.py` converts the upstream schemas (expects the upstream repository next to this one) into
`_sources/`. See [SCHEMA-FIXES.md](SCHEMA-FIXES.md) for the differences from the upstream schemas, which are
candidates for backporting.

Build locally with `./build.sh` (requires Docker) and browse the result with `./view.sh`.
