# OGC API - Connected Systems Building Blocks

Data models of the OGC API - Connected Systems standard and its underlying SWE Common 3.0 and SensorML 3.0 encodings, as reusable building blocks.


Draft conversion of the JSON schemas maintained in [opengeospatial/ogcapi-connected-systems](https://github.com/opengeospatial/ogcapi-connected-systems)
into building blocks. Scope is limited to data models (no OpenAPI paths/parameters, no XML encodings).
Semantic annotations (JSON-LD contexts) are not yet provided.


## Building Blocks

### `ogc.api.connected-systems.common.link` — Link

**Type:** schema

Link object following standard Web Linking conventions (see RFC5988 and RFC6690)

### `ogc.api.connected-systems.common.time-instant` — TimeInstant

**Type:** schema

Time Instant

### `ogc.api.connected-systems.part1.batch-delete` — Batch_delete

**Type:** schema

Request payload for batch deletion of resources, given as a list of resource URIs, local IDs or unique identifiers (UIDs).

### `ogc.api.connected-systems.part1.batch-response` — Batch_response

**Type:** schema

Response describing the outcome of a batch create, update or delete operation, reporting the per-item result of each request.

### `ogc.api.connected-systems.part1.uris` — Uris

**Type:** schema

Enumerations of the allowed type URIs (from the SSN/SOSA and Connected Systems vocabularies) for System, Deployment and Procedure features.

### `ogc.api.connected-systems.part2.command-status-code` — CommandStatusCode

**Type:** schema

Enumeration of the status codes a Command can report, such as pending, accepted, executing, completed, failed or rejected.

### `ogc.api.connected-systems.part2.command-schema-any-other` — CommandSchemaAnyOther

**Type:** schema

Command schema for any other command format, identified by `commandFormat` and carrying free-form schema properties.

### `ogc.api.connected-systems.part2.observation-schema-any-other` — ObservationSchemaAnyOther

**Type:** schema

Observation schema for any other observation format, identified by `obsFormat` and carrying free-form schema properties.

### `ogc.api.connected-systems.swecommon.abstract-swe-identifiable` — AbstractSweIdentifiable

**Type:** schema

Base substitution groups for all SWE Common objects with identification metadata

### `ogc.api.connected-systems.sensorml.pose` — Pose

**Type:** schema

A Pose object that can be either a GeoPose Basic instance of a relative pose.

### `ogc.api.connected-systems.swecommon.matrix` — Matrix

**Type:** schema

Implementation of ISO-11404 Array datatype. This defines an array of identical data components with a elementCount. Values are given as a block and can be encoded in different ways

### `ogc.api.connected-systems.sensorml.responsible-party` — ResponsibleParty

**Type:** schema

ResponsibleParty schema.

### `ogc.api.connected-systems.sensorml.legal-constraint` — LegalConstraint

**Type:** schema

LegalConstraint schema.

### `ogc.api.connected-systems.part1.links` — Links

**Type:** schema

Collection (array) of link objects pointing to related resources, following the OGC API Common link model.

### `ogc.api.connected-systems.part2.command-schema-protobuf` — CommandSchemaProtobuf

**Type:** schema

Command schema for the Protobuf format, describing command parameters using a Protobuf message definition.

### `ogc.api.connected-systems.part2.observation-schema-protobuf` — ObservationSchemaProtobuf

**Type:** schema

Observation schema for the Protobuf format, describing the observation record using a Protobuf message definition.

### `ogc.api.connected-systems.sensorml.contact-link` — ContactLink

**Type:** schema

ContactLink schema.

### `ogc.api.connected-systems.sensorml.document` — Document

**Type:** schema

Document schema.

### `ogc.api.connected-systems.common.time-instant-or-now` — TimeInstantOrNow

**Type:** schema

Time Instant

### `ogc.api.connected-systems.part2.observation` — Observation

**Type:** schema

An Observation: the result of observing a property of a feature of interest at a given time, produced by a System and stored in a DataStream.

### `ogc.api.connected-systems.swecommon.abstract-data-component` — AbstractDataComponent

**Type:** schema

Abstract base class for all data components

### `ogc.api.connected-systems.part1.deployed-system` — DeployedSystem (GeoJSON)

**Type:** schema

A deployed System (GeoJSON encoding, a profile of the OGC API - Features feature): a system as listed within a Deployment, tying it to its installation in that deployment.

### `ogc.api.connected-systems.part1.feature` — Feature (GeoJSON)

**Type:** schema

Generic GeoJSON feature used as the base of the Connected Systems feature resources, with local `id`, `geometry`, `bbox`, free-form `properties` and `links`.

### `ogc.api.connected-systems.common.time-period` — TimePeriod

**Type:** schema

Time Period

### `ogc.api.connected-systems.part2.observation-collection` — ObservationCollection

**Type:** schema

Paged collection of Observation resources as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.swecommon.abstract-simple-component` — AbstractSimpleComponent

**Type:** schema

AbstractSimpleComponent schema.

### `ogc.api.connected-systems.part1.deployed-system-array` — DeployedSystemArray (GeoJSON)

**Type:** schema

Bare JSON array of deployed System resources (GeoJSON encoding), used as the request payload for batch creation or update of several resources at once.

### `ogc.api.connected-systems.part1.procedure` — Procedure (GeoJSON)

**Type:** schema

A Procedure (GeoJSON encoding, a profile of the OGC API - Features feature): a specification of how observations are made or commands are executed, such as a sensor datasheet, method or protocol that systems implement.

### `ogc.api.connected-systems.part1.deployment` — Deployment (GeoJSON)

**Type:** schema

A Deployment (GeoJSON encoding, a profile of the OGC API - Features feature): the installation of one or more systems at a location and time, describing where and when they operate.

### `ogc.api.connected-systems.part1.sampling-feature` — SamplingFeature (GeoJSON)

**Type:** schema

A Sampling Feature (GeoJSON encoding): a feature such as a station, specimen or transect that is sampled or observed by systems, and serves as the feature of interest of observations; profile of the OGC API - Features feature.

### `ogc.api.connected-systems.part1.system` — System (GeoJSON)

**Type:** schema

A System (GeoJSON encoding, a profile of the OGC API - Features feature): a sensor, actuator, platform, sampler or other asset that produces observations or receives commands, with its identity, type and relationships to other resources.

### `ogc.api.connected-systems.part2.base-stream` — BaseStream

**Type:** schema

Properties shared by DataStream and ControlStream resources: local ID, name, description, valid time and the list of supported encoding formats.

### `ogc.api.connected-systems.part2.command` — Command

**Type:** schema

A Command: a request sent through a ControlStream to a System to perform an action, carrying its parameters, issue time and execution constraints.

### `ogc.api.connected-systems.part2.command-result` — CommandResult

**Type:** schema

A CommandResult: a result resource produced by the execution of a Command, linked to it by `command@id` and carrying inline data or a reference to the result.

### `ogc.api.connected-systems.swecommon.basic-types` — BasicTypes

**Type:** schema

BasicTypes schema.

### `ogc.api.connected-systems.swecommon.boolean` — Boolean

**Type:** schema

Scalar component used to express truth: True or False, 0 or 1

### `ogc.api.connected-systems.part1.deployed-system-collection` — DeployedSystemCollection (GeoJSON)

**Type:** schema

Paged collection of deployed System resources (GeoJSON encoding) as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.part1.procedure-array` — ProcedureArray (GeoJSON)

**Type:** schema

Bare JSON array of Procedure resources (GeoJSON encoding), used as the request payload for batch creation or update of several resources at once.

### `ogc.api.connected-systems.part1.deployment-array` — DeploymentArray (GeoJSON)

**Type:** schema

Bare JSON array of Deployment resources (GeoJSON encoding), used as the request payload for batch creation or update of several resources at once.

### `ogc.api.connected-systems.part1.sampling-feature-array` — SamplingFeatureArray (GeoJSON)

**Type:** schema

Bare JSON array of Sampling Feature resources (GeoJSON encoding), used as the request payload for batch creation or update.

### `ogc.api.connected-systems.part1.system-array` — SystemArray (GeoJSON)

**Type:** schema

Bare JSON array of System resources (GeoJSON encoding), used as the request payload for batch creation or update of several resources at once.

### `ogc.api.connected-systems.part2.command-collection` — CommandCollection

**Type:** schema

Paged collection of Command resources as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.part2.command-result-collection` — CommandResultCollection

**Type:** schema

Paged collection of CommandResult resources as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.part2.command-status` — CommandStatus

**Type:** schema

A CommandStatus report: the state of execution of a Command at a given report time, with status code, percent completion, message and any results.

### `ogc.api.connected-systems.swecommon.category` — Category

**Type:** schema

Scalar component used to represent a categorical value as a simple token identifying a term in a code space

### `ogc.api.connected-systems.swecommon.category-range` — CategoryRange

**Type:** schema

Pair of categorical values used to specify a range in an ordinal reference system (specified by the code space)

### `ogc.api.connected-systems.swecommon.count` — Count

**Type:** schema

Scalar component with integer representation used for a discrete counting value

### `ogc.api.connected-systems.swecommon.count-range` — CountRange

**Type:** schema

Integer pair used for specifying a count range

### `ogc.api.connected-systems.swecommon.data-record` — DataRecord

**Type:** schema

Implementation of ISO-11404 Record datatype. This allows grouping (sequence) of data components which can themselves be simple types, records, arrays or choices

### `ogc.api.connected-systems.swecommon.encodings` — Encodings

**Type:** schema

Encodings schema.

### `ogc.api.connected-systems.swecommon.geometry` — Geometry

**Type:** schema

Implementation of ISO-19107 geometry datatype. This allows embedding a geometry in a larger schema

### `ogc.api.connected-systems.swecommon.quantity` — Quantity

**Type:** schema

Scalar component with decimal representation and a unit of measure used to store value of a continuous quantity

### `ogc.api.connected-systems.swecommon.quantity-range` — QuantityRange

**Type:** schema

Decimal pair for specifying a quantity range with a unit of measure

### `ogc.api.connected-systems.swecommon.text` — Text

**Type:** schema

Free text component used to store comments or any other type of textual statement

### `ogc.api.connected-systems.swecommon.time` — Time

**Type:** schema

Scalar component used to represent a time quantity either as ISO 8601 (e.g., 2004-04-18T12:03:04.6Z) or as a duration relative to a time of reference

### `ogc.api.connected-systems.swecommon.time-range` — TimeRange

**Type:** schema

Time value pair for specifying a time range (can be a decimal or ISO 8601)

### `ogc.api.connected-systems.part1.procedure-collection` — ProcedureCollection (GeoJSON)

**Type:** schema

Paged collection of Procedure resources (GeoJSON encoding) as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.part1.deployment-collection` — DeploymentCollection (GeoJSON)

**Type:** schema

Paged collection of Deployment resources (GeoJSON encoding) as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.part1.sampling-feature-collection` — SamplingFeatureCollection (GeoJSON)

**Type:** schema

Paged collection of Sampling Feature resources (GeoJSON encoding) as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.part1.system-collection` — SystemCollection (GeoJSON)

**Type:** schema

Paged collection of System resources (GeoJSON encoding) as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.part2.command-status-collection` — CommandStatusCollection

**Type:** schema

Paged collection of CommandStatus reports as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.swecommon.data-choice` — DataChoice

**Type:** schema

Implementation of a choice of two or more Data Components (also called disjoint union)

### `ogc.api.connected-systems.swecommon.data-stream` — DataStream

**Type:** schema

Defines the structure of the element that will be repeated in the stream

### `ogc.api.connected-systems.swecommon.vector` — Vector

**Type:** schema

Implementation of a mathematical vector composed of a list of scalar coordinates expressed in the mandatory reference frame.

### `ogc.api.connected-systems.swecommon.swe-common` — SweCommon

**Type:** schema

SweCommon schema.

### `ogc.api.connected-systems.part2.command-schema-json` — CommandSchemaJson

**Type:** schema

Command schema for the JSON format (`application/json`), defining the `parametersSchema` and optional result and feasibility result schemas with SWE Common components.

### `ogc.api.connected-systems.part2.command-schema-swe` — CommandSchemaSwe

**Type:** schema

Command schema for SWE Common encodings (text, binary, etc.), giving the record schema and encoding rules of the command stream.

### `ogc.api.connected-systems.part2.data-stream-schema-def` — DataStreamSchemaDef

**Type:** schema

Schema definition of the observation record of a DataStream, describing phenomenon time, result time, feature of interest, result and parameters with SWE Common components.

### `ogc.api.connected-systems.part2.observation-schema-json` — ObservationSchemaJson

**Type:** schema

Observation schema for the JSON format (`application/json`), describing the observation result, parameters and related fields with SWE Common components.

### `ogc.api.connected-systems.part2.observation-schema-swe` — ObservationSchemaSwe

**Type:** schema

Observation schema for SWE Common encodings (text, binary, etc.), giving the record schema and the encoding rules of the observation stream.

### `ogc.api.connected-systems.sensorml.derived-property` — DerivedProperty

**Type:** schema

DerivedProperty schema.

### `ogc.api.connected-systems.swecommon.data-array` — DataArray

**Type:** schema

Implementation of ISO-11404 Array datatype. This defines an array of identical data components with a elementCount. Values are given as a block and can be encoded in different ways

### `ogc.api.connected-systems.part2.command-schema` — CommandSchema

**Type:** schema

Schema describing the content of commands in a ControlStream; the syntax depends on the command format (JSON, SWE, Protobuf or other).

### `ogc.api.connected-systems.part2.observation-schema` — ObservationSchema

**Type:** schema

Schema describing the content of observations in a DataStream; the syntax depends on the observation format (JSON, SWE, Protobuf or other).

### `ogc.api.connected-systems.part1.property-sensorml` — Property (SensorML)

**Type:** schema

A Property (SensorML 3.0 JSON encoding): a definition of an observable or controllable property (e.g. temperature, wind speed) that systems and procedures can reference.

### `ogc.api.connected-systems.sensorml.common-defs` — Common Definitions

**Type:** schema

Definitions shared by SensorML schemas: observable properties, terms, any-property and any-constraint unions, path references and time instant-or-period.

### `ogc.api.connected-systems.part2.control-stream` — ControlStream

**Type:** schema

A ControlStream: a channel through which commands are sent to a controllable System, describing the supported command parameters, result schema and formats.

### `ogc.api.connected-systems.part2.data-stream` — DataStream

**Type:** schema

A DataStream: a time-ordered stream of observations produced by a System, describing the observed properties, result schema and formats. Observations are posted to and retrieved from it.

### `ogc.api.connected-systems.part1.property-array-sensorml` — PropertyArray (SensorML)

**Type:** schema

Bare JSON array of Property resources (SensorML encoding), used as the request payload for batch creation or update.

### `ogc.api.connected-systems.sensorml.settings` — Settings

**Type:** schema

Settings schema.

### `ogc.api.connected-systems.part2.control-stream-collection` — ControlStreamCollection

**Type:** schema

Paged collection of ControlStream resources as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.part2.control-stream-create` — ControlStream_create

**Type:** schema

Create payload for a ControlStream: the ControlStream properties plus the required `schema` (command schema) describing the content of its commands.

### `ogc.api.connected-systems.part2.data-stream-collection` — DataStreamCollection

**Type:** schema

Paged collection of DataStream resources as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.part2.data-stream-create` — DataStream_create

**Type:** schema

Create payload for a DataStream: the DataStream properties plus the required `schema` (observation schema) describing the content of its observations.

### `ogc.api.connected-systems.part1.property-collection-sensorml` — PropertyCollection (SensorML)

**Type:** schema

Paged collection of Property resources (SensorML encoding) as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.sensorml.deployed-system` — DeployedSystem

**Type:** schema

DeployedSystem schema.

### `ogc.api.connected-systems.sensorml.event` — Event

**Type:** schema

A time tagged event with description and relevant property values.

### `ogc.api.connected-systems.part1.deployed-system-sensorml` — DeployedSystem (SensorML)

**Type:** schema

A deployed System (SensorML 3.0 JSON encoding): a system as listed within a Deployment, tying it to its installation in that deployment.

### `ogc.api.connected-systems.part2.system-event` — SystemEvent

**Type:** schema

A SystemEvent: a time-stamped event in the life of a System (e.g. calibration, maintenance, deployment or failure), stored as a feature-like record with links.

### `ogc.api.connected-systems.sensorml.described-object` — DescribedObject

**Type:** schema

DescribedObject schema.

### `ogc.api.connected-systems.part1.deployed-system-array-sensorml` — DeployedSystemArray (SensorML)

**Type:** schema

Bare JSON array of deployed System resources (SensorML encoding), used as the request payload for batch creation or update of several resources at once.

### `ogc.api.connected-systems.part2.system-event-collection` — SystemEventCollection

**Type:** schema

Paged collection of SystemEvent resources as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.sensorml.deployment` — Deployment

**Type:** schema

Deployment schema.

### `ogc.api.connected-systems.sensorml.mode` — Mode

**Type:** schema

Mode schema.

### `ogc.api.connected-systems.part1.deployed-system-collection-sensorml` — DeployedSystemCollection (SensorML)

**Type:** schema

Paged collection of deployed System resources (SensorML encoding) as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.part1.deployment-sensorml` — Deployment (SensorML)

**Type:** schema

A Deployment (SensorML 3.0 JSON encoding): the installation of one or more systems at a location and time, describing where and when they operate.

### `ogc.api.connected-systems.sensorml.abstract-process` — AbstractProcess

**Type:** schema

AbstractProcess schema.

### `ogc.api.connected-systems.part1.deployment-array-sensorml` — DeploymentArray (SensorML)

**Type:** schema

Bare JSON array of Deployment resources (SensorML encoding), used as the request payload for batch creation or update of several resources at once.

### `ogc.api.connected-systems.sensorml.abstract-physical-process` — AbstractPhysicalProcess

**Type:** schema

AbstractPhysicalProcess schema.

### `ogc.api.connected-systems.sensorml.simple-process` — SimpleProcess

**Type:** schema

SimpleProcess schema.

### `ogc.api.connected-systems.part1.deployment-collection-sensorml` — DeploymentCollection (SensorML)

**Type:** schema

Paged collection of Deployment resources (SensorML encoding) as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.sensorml.physical-system` — PhysicalSystem

**Type:** schema

PhysicalSystem schema.

### `ogc.api.connected-systems.sensorml.physical-component` — PhysicalComponent

**Type:** schema

PhysicalComponent schema.

### `ogc.api.connected-systems.sensorml.aggregate-process` — AggregateProcess

**Type:** schema

AggregateProcess schema.

### `ogc.api.connected-systems.part1.procedure-sensorml` — Procedure (SensorML)

**Type:** schema

A Procedure (SensorML 3.0 JSON encoding): a specification of how observations are made or commands are executed, such as a sensor datasheet, method or protocol that systems implement.

### `ogc.api.connected-systems.part1.system-sensorml` — System (SensorML)

**Type:** schema

A System (SensorML 3.0 JSON encoding): a sensor, actuator, platform, sampler or other asset that produces observations or receives commands, with its identity, type and relationships to other resources.

### `ogc.api.connected-systems.part1.procedure-array-sensorml` — ProcedureArray (SensorML)

**Type:** schema

Bare JSON array of Procedure resources (SensorML encoding), used as the request payload for batch creation or update of several resources at once.

### `ogc.api.connected-systems.part1.system-array-sensorml` — SystemArray (SensorML)

**Type:** schema

Bare JSON array of System resources (SensorML encoding), used as the request payload for batch creation or update of several resources at once.

### `ogc.api.connected-systems.part1.procedure-collection-sensorml` — ProcedureCollection (SensorML)

**Type:** schema

Paged collection of Procedure resources (SensorML encoding) as returned by list queries, with the items plus navigation `links`.

### `ogc.api.connected-systems.part1.system-collection-sensorml` — SystemCollection (SensorML)

**Type:** schema

Paged collection of System resources (SensorML encoding) as returned by list queries, with the items plus navigation `links`.

