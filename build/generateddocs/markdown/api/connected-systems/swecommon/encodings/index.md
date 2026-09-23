
# Encodings (Schema)

`ogc.api.connected-systems.swecommon.encodings` *v0.1*

Encodings schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

<!-- generated -->
# Encodings

Converted from [`swecommon/schemas/json/encodings.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/encodings.json) in the OGC API - Connected Systems repository.

## Definitions

The following definitions can be referenced individually using their anchor, e.g. `bblocks://ogc.api.connected-systems.swecommon.encodings#AbstractEncoding`:

- `AbstractEncoding`
- `TextEncoding`: Parameters of the text encoding method
- `JSONEncoding`: Parameters of the JSON encoding method
- `XMLEncoding`: Parameters of the XML encoding method
- `BinaryEncoding`: Parameters of the binary encoding method
- `Block`: Binary encoding parameters used to encode a block of values at once. This is used for encrypting or compressing a complete array of values for instance
- `Component`: Binary encoding parameters used for encoding a single data component


## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$defs:
  AbstractEncoding:
    type: object
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AbstractSWE
    - properties: {}
    $anchor: AbstractEncoding
  TextEncoding:
    description: Parameters of the text encoding method
    type: object
    allOf:
    - $ref: '#/$defs/AbstractEncoding'
    - properties:
        type:
          const: TextEncoding
        collapseWhiteSpaces:
          description: Indicates whether white spaces (i.e., space, tab, CR, LF) should
            be collapsed with separators when parsing the data stream
          type: boolean
        decimalSeparator:
          description: Character used as the decimal separator
          type: string
          minLength: 1
        tokenSeparator:
          description: Character sequence used as the token separator (i.e., between
            two successive values)
          type: string
          minLength: 1
        blockSeparator:
          description: Character sequence used as the block separator (i.e., between
            two successive blocks in the data set. The end of a block is reached once
            all values from the data tree have been encoded once)
          type: string
          minLength: 1
      required:
      - type
      - tokenSeparator
      - blockSeparator
    $anchor: TextEncoding
  JSONEncoding:
    description: Parameters of the JSON encoding method
    type: object
    allOf:
    - $ref: '#/$defs/AbstractEncoding'
    - properties:
        type:
          const: JSONEncoding
        recordsAsArrays:
          type: boolean
          default: false
          description: If true, DataRecord values are encoded as JSON arrays instead
            of JSON objects
        vectorsAsArrays:
          type: boolean
          default: false
          description: If true, Vector values are encoded as JSON arrays instead of
            JSON objects
      required:
      - type
    $anchor: JSONEncoding
  XMLEncoding:
    description: Parameters of the XML encoding method
    type: object
    allOf:
    - $ref: '#/$defs/AbstractEncoding'
    - properties:
        type:
          const: XMLEncoding
        namespace:
          type: string
          format: uri
      required:
      - type
    $anchor: XMLEncoding
  BinaryEncoding:
    description: Parameters of the binary encoding method
    type: object
    allOf:
    - $ref: '#/$defs/AbstractEncoding'
    - properties:
        type:
          const: BinaryEncoding
        byteOrder:
          description: Byte order convention used to encode this binary data (big
            endian = most significant byte first, MSB or little endian = least significant
            byte first, LSB)
          type: string
          enum:
          - bigEndian
          - littleEndian
        byteEncoding:
          description: Byte encoding method used to encode the binary data (raw or
            base 64)
          type: string
          enum:
          - base64
          - raw
        byteLength:
          description: Total length in bytes of the binary stream (if known in advance)
          type: integer
        members:
          description: Each member contains detailed parameters for encoding a scalar
            value or a block of values
          type: array
          minItems: 1
          items:
            oneOf:
            - $ref: '#/$defs/Component'
            - $ref: '#/$defs/Block'
      required:
      - type
      - byteOrder
      - byteEncoding
      - members
    $anchor: BinaryEncoding
  Block:
    description: Binary encoding parameters used to encode a block of values at once.
      This is used for encrypting or compressing a complete array of values for instance
    type: object
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AbstractSWE
    - properties:
        type:
          const: Block
        compression:
          description: Name of the compression method used to encrypt the block of
            values described by the referenced data component
          type: string
          format: uri
        encryption:
          description: Name of the encryption method used to encrypt the block of
            values described by the referenced data component
          type: string
          format: uri
        paddingBytes-after:
          description: Number of padding bytes present in the stream after this binary
            block
          type: integer
        paddingBytes-before:
          description: Number of padding bytes present in the stream before this binary
            block
          type: integer
        byteLength:
          description: Length in byte of this binary block (if known in advance)
          type: integer
        ref:
          description: Reference to the aggregate data component that this binary
            block encoding settings apply to
          type: string
      required:
      - type
      - ref
    $anchor: Block
  Component:
    description: Binary encoding parameters used for encoding a single data component
    type: object
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/basic-types/schema.yaml#AbstractSWE
    - properties:
        type:
          const: Component
        encryption:
          description: Name of the encryption method used to encrypt the value of
            this field
          type: string
          format: uri
        significantBits:
          description: Number of significant bits actually used for a binary encoded
            numerical value (all remaining bits shall be set to 0)
          type: integer
        bitLength:
          type: integer
        byteLength:
          description: Byte length of this field when a custom data type is used
          type: integer
        dataType:
          description: Binary data type used to encode the value(s) of the referenced
            data component
          type: string
          format: uri
        ref:
          description: Reference to the data component that these binary encoding
            settings apply to
          type: string
      required:
      - type
      - dataType
      - ref
    $anchor: Component
oneOf:
- $ref: '#/$defs/TextEncoding'
- $ref: '#/$defs/XMLEncoding'
- $ref: '#/$defs/JSONEncoding'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-connected-systems/build/annotated/api/connected-systems/swecommon/encodings/schema.yaml)

## Sources

* [swecommon/schemas/json/encodings.json in opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/swecommon/schemas/json/encodings.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-connected-systems](https://github.com/ogcincubator/bblocks-connected-systems)
* Path: `_sources/swecommon/encodings`

