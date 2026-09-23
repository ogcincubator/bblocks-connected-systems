
# Link (Schema)

`ogc.api.connected-systems.common.link` *v0.1*

Link object following standard Web Linking conventions (see RFC5988 and RFC6690)

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Link

Link object following standard Web Linking conventions (see RFC5988 and RFC6690)

Converted from [`common/link.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/common/link.json) in the OGC API - Connected Systems repository.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `href` | `string` | yes | URL of target resource |
| `rel` | `string` |  | Link relation type |
| `type` | `string` |  | Media type of target resource |
| `hreflang` | `string` |  | Language tag of target resource (2-letter language code, followed by optional 2-letter region code) |
| `title` | `string` |  | Title of target resource |
| `uid` | `string` |  | Unique identifier of target resource |
| `rt` | `string` |  | Semantic type of target resource (RFC 6690) |
| `if` | `string` |  | Interface used to access target resource (RFC 6690) |


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Link
description: Link object following standard Web Linking conventions (see RFC5988 and
  RFC6690)
type: object
required:
- href
properties:
  href:
    description: URL of target resource
    type: string
    format: uri
    examples:
    - https://data.example.com/link/to/resource
  rel:
    description: Link relation type
    type: string
    examples:
    - alternate
    - self
    - http://www.opengis.net/def/rel/ogc/1.0/conformance
  type:
    description: Media type of target resource
    type: string
    examples:
    - application/json
    - image/tiff; application=geotiff
  hreflang:
    description: Language tag of target resource (2-letter language code, followed
      by optional 2-letter region code)
    type: string
    minLength: 1
    pattern: ^([a-z]{2}(-[A-Z]{2})?)|x-default$
    examples:
    - en-US
    - fr-FR
    - de
  title:
    description: Title of target resource
    type: string
    minLength: 1
    examples:
    - Resource Name
  uid:
    description: Unique identifier of target resource
    type: string
    format: uri
    examples:
    - urn:x-org:resourceType:0001
  rt:
    description: Semantic type of target resource (RFC 6690)
    type: string
    format: uri
    examples:
    - http://www.example.org/uri/of/concept
  if:
    description: Interface used to access target resource (RFC 6690)
    type: string
    format: uri
    examples:
    - http://www.opengis.net/spec/spec-id/version

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/common/link/schema.yaml)

## Sources

* [common/link.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/common/link.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/common/link`

