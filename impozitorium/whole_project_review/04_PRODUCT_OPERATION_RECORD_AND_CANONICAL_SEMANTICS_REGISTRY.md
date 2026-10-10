# 04 — Product Operation Record and Canonical Semantics Registry

```text
DOCUMENT_CLASS =
    ARCHITECTURAL_DECISION_SUPPORT
    + SEMANTIC_GOVERNANCE

STATUS =
    HUMAN_ACCEPTED_DIRECTION
    NOT_IMPLEMENTATION_AUTHORIZATION

RELATIONSHIP_TO_REVIEW =
    ADDENDUM_TO
    01_ACTUAL_PROJECT_RECONNAISSANCE.md
    02_SEMANTIC_AND_ARCHITECTURAL_ALIGNMENT_REVIEW.md
    03_FILE_FACTORY_MINIMUM_USEFUL_EXCAVATOR_CRITERIA.md
```

## 1. Purpose

Impozitorium is expected to accumulate many production capabilities, operations, diagnostics, artifact types, technical objects, policy concepts and future agent-visible actions.

Without a shared semantic discipline, each module can independently invent names and meanings for similar concepts. That creates semantic debt even when the code itself is modular.

This decision therefore couples two lightweight architectural foundations:

```text
A. MINIMAL PRODUCT OPERATION RECORD

B. CANONICAL PRODUCT SEMANTICS REGISTRY
```

The Operation Record is a runtime contract.

The Semantics Registry is the authoritative vocabulary used by the runtime contract, modules, GUI, Jobs, batch surfaces and future agents.

Neither is a workflow engine.

---

## 2. Decision

```text
ARCHITECTURAL_DECISION_02 =
    MINIMAL_PRODUCT_OPERATION_RECORD
    + CANONICAL_PRODUCT_SEMANTICS_REGISTRY

IMPLEMENTATION_AUTHORIZATION =
    NONE

FULL_OPERATION_FRAMEWORK =
    NOT_AUTHORIZED

FULL_JOB_SYSTEM =
    NOT_AUTHORIZED

AGENTIC_LAYER =
    NOT_AUTHORIZED
```

---

## 3. Minimal Product Operation Record

The product needs one common way to record that a bounded operation was applied to explicit artifacts.

The record must not duplicate Platform File Management.

### Operation Record owns

```text
operation identity
operation kind + version
input artifact references
parameters
policy profile reference
execution identity
diagnostics
admissibility outcome
output artifact references
verification reference
provenance
```

### Platform File Management owns

```text
artifact identity
storage
candidate lifecycle
verification receipts
managed staging
promotion
current pointer
filesystem safety
```

Required law:

```text
OPERATION RECORD != FILE MANAGEMENT
OPERATION RECORD != JOB
OPERATION RECORD != FILE FACTORY WORKUNIT
OPERATION RECORD != GUI COMMAND
```

A future Job may compose Operation Records, but Operation Records must be useful before Jobs exist.

---

## 4. Minimum Operation Record shape

The exact schema is not decided by this document.

The minimum semantic content is:

```text
OperationRecord

identity
    operation_id
    operation_kind
    operation_version

inputs
    artifact_refs

intent
    parameters
    policy_profile_ref

execution
    engine_identity
    writer_identity
    execution_status

diagnostics
    stable diagnostic codes
    severity
    structured details

admissibility
    outcome
    actor where relevant
    reason where relevant

outputs
    artifact_refs

verification
    verification_ref / result

provenance
    timestamps
    implementation identity
    environment identity where required
```

Domain-specific parameters remain domain-specific.

The common record must not flatten important domain meaning.

Required law:

```text
EVERY FUTURE PRODUCTION CAPABILITY
MUST BE ABLE TO EXPRESS ITS EXECUTION
AS AN OPERATION RECORD
WITHOUT LOSING DOMAIN-SPECIFIC DETAIL.
```

---

## 5. Admissibility is first-class

Real print production is not purely binary valid/invalid processing.

The platform must be able to represent distinctions such as:

```text
PASS

PASS_WITH_WARNING

OPERATOR_ACCEPTED_DEVIATION

REPAIRED_AND_ACCEPTED

BLOCKED

UNKNOWN
```

These are semantic classes, not yet final enum names.

Important distinction:

```text
UNKNOWN != BLOCKED
UNKNOWN != PASS
```

The architecture must preserve the difference between:

- compliant result;
- warned but acceptable result;
- deliberate operator-accepted deviation;
- repaired and reverified result;
- prohibited result;
- result whose admissibility cannot be proven.

Operator acceptance must be recorded as product evidence, not remain only in GUI state.

---

## 6. GUI role

GUI is a consumer and presenter of operations.

GUI may:

- collect operator intent;
- display diagnostics;
- preview proposed changes;
- request an operation;
- present admissibility choices;
- record explicit Human decisions.

GUI must not become the owner of:

- structural PDF mutation semantics;
- operation semantics;
- artifact lifecycle;
- geometry policy.

---

## 7. File Factory relationship

File Factory domain objects are not product runtime objects.

```text
FILE_FACTORY_DOMAIN_OBJECT_REUSE =
    FORBIDDEN_BY_DEFAULT

FILE_FACTORY_PATTERN_REUSE =
    ALLOWED_AFTER_EXPLICIT_ADOPTION
```

Patterns that may be useful include:

- request identity;
- idempotency;
- replay classification;
- bounded authority;
- incident semantics;
- unknown-side-effect STOP behavior;
- evidence routing.

Adoption must be deliberate and product-specific.

---

## 8. Canonical Product Semantics Registry

The platform requires one authoritative registry for significant product concepts.

Initial semantic families include:

```text
operation_kind
artifact_kind
geometry_concept
technical_object_kind
diagnostic_code
admissibility_outcome
policy_kind
production_intent_field
verification_kind
```

The registry is intended to prevent semantic duplication and name drift across modules.

It is not a heavy ontology engine.

A first implementation may be as small as:

```text
one authoritative YAML / JSON / Python registry
+ one short normative document
+ validation tests
```

---

## 9. Registry entry model

A meaningful canonical concept should be able to record:

```text
canonical_id
canonical_name
definition
domain
semantic_class
source / standard basis
aliases
deprecated_aliases
relationships
implementation_owner
status
```

Not every field must be required for every concept.

The goal is semantic identity, not bureaucratic completeness.

---

## 10. Semantic classes

At minimum, terms should distinguish:

```text
STANDARD_TERM
PLATFORM_TERM
MODULE_OR_DOMAIN_TERM
```

Example:

```text
TrimBox
    STANDARD_TERM

layout_box
    PLATFORM_TERM

booklet creep / lap semantics
    PRODUCTION_DOMAIN_TERM
    unless an applicable standard provides the canonical terminology
```

Platform-specific concepts are allowed.

They must be explicitly identified as platform semantics rather than accidentally treated as industry-standard terms.

---

## 11. Semantic source priority

When defining a new canonical concept, terminology should be sourced in this order:

```text
1. APPLICABLE INTERNATIONAL / INDUSTRY STANDARD

2. ESTABLISHED PRODUCTION-DOMAIN TERMINOLOGY

3. EXISTING ACCEPTED IMPOZITORIUM PLATFORM TERMINOLOGY

4. NEW IMPOZITORIUM EXTENSION
   only when no suitable existing term exists
```

Relevant standard families may include, where applicable:

- ISO PDF standards and production standards;
- PDF/X-related terminology;
- ISO 19593 and technical production layer semantics;
- ICC / ICCmax terminology;
- CIP4 / JDF / XJDF terminology;
- other applicable printing, color, finishing or document-production standards.

This document does not assert the exact meaning of any external standard term.

Standard alignment must be researched and cited when individual semantic entries are defined.

---

## 12. No silent semantic invention

Required laws:

```text
NO NEW CANONICAL TERM
WITHOUT CHECKING THE EXISTING REGISTRY

NO DUPLICATE CANONICAL IDENTITY
FOR THE SAME CONCEPT

NO SINGLE CANONICAL TERM
FOR MULTIPLE UNRELATED CONCEPTS
WITHOUT EXPLICIT NAMESPACE
```

Modules may have local implementation names, but public product semantics must map to the canonical registry.

---

## 13. Namespacing overloaded terms

Several current project terms are already overloaded.

The registry must explicitly separate concepts such as:

```text
GOVERNANCE.HUMAN_ACCEPTANCE

ARTIFACT.ADMISSION

PRODUCTION.ADMISSIBILITY
```

and:

```text
GIT.PUBLICATION

ARTIFACT.PROMOTION

OUTPUT.SAVE_AS
```

Likewise, future use of terms such as:

```text
job
operation
action
repair
normalize
sanitize
transform
commit
promote
publish
accept
```

must be semantically disambiguated.

Human readers and agents must not be expected to infer the intended meaning from context when a stable namespace can make it explicit.

---

## 14. Geometry terminology

Geometry is a high-risk semantic domain.

The registry must distinguish standardized PDF page boxes from platform semantics.

For example:

```text
MediaBox
CropBox
BleedBox
TrimBox
ArtBox
    = standard PDF page-box concepts

layout_box
    = IMPOZITORIUM PLATFORM SEMANTIC
      derived from standard PDF boxes by accepted policy

operator frame intent
    = product semantic
      final canonical materialization policy NOT_DECIDED
```

The Semantics Registry must not create a second geometry authority.

Page Geometry remains the semantic owner of canonical geometry behavior.

---

## 15. Technical-object terminology

The same registry principle applies to:

- crop / trim / cut marks;
- fold marks;
- collating marks;
- registration marks;
- service text;
- signature labels;
- numbering;
- plotter / cutter geometry;
- finishing contours.

Before defining a new platform term, the applicable standards and established production terminology must be checked.

If the platform introduces an extension, it must be marked as such.

Exact PDF structural realization, including OCG or later standards-aligned technical-layer representation, remains a separate architectural decision.

---

## 16. Registry validation

At minimum, automated validation should eventually prove:

```text
canonical IDs are unique
canonical names are unique within their namespace
aliases do not collide ambiguously
deprecated aliases resolve to one canonical concept
operation kinds are registered once
diagnostic codes are unique
semantic class is explicit
platform extensions are distinguishable from standard terms
```

Implementation of these tests is not authorized by this document.

---

## 17. Relationship to Jobs and Agentic Layer

The semantics registry becomes more important as interaction surfaces multiply.

A future Job may be modeled as:

```text
production intent
+
ordered / related Operation Records
```

A future agent must call the same canonical operations as GUI or batch.

Therefore:

```text
GUI
CLI / BATCH
JOBS
AGENT

must use the same canonical semantic identities
for the same production concepts.
```

Agents must not invent their own synonyms for product actions.

---

## 18. Scope restraint

This decision intentionally does not authorize:

```text
OperationManager
OperationScheduler
OperationGraph
OperationBus
OperationRuntimeFramework
OperationPluginSystem
full Job engine
agent runtime
standards implementation
ISO 19593 implementation
semantic database service
ontology server
```

The current requirement is:

```text
SMALL RUNTIME CONTRACT
+
SMALL AUTHORITATIVE SEMANTICS REGISTRY
+
CLEAR STANDARD-SOURCING DISCIPLINE
```

---

## 19. Human decision

```text
DECISION =
    ACCEPTED_DIRECTION

MINIMAL_PRODUCT_OPERATION_RECORD =
    REQUIRED

ADMISSIBILITY =
    FIRST_CLASS_PRODUCT_CONCEPT

CANONICAL_PRODUCT_SEMANTICS_REGISTRY =
    REQUIRED

SEMANTIC_SOURCE_PRIORITY =
    STANDARD_FIRST
    DOMAIN_SECOND
    ACCEPTED_PLATFORM_TERMS_THIRD
    NEW_PLATFORM_EXTENSION_LAST

SEMANTIC_DUPLICATION =
    NOT_ALLOWED

STANDARD_ALIGNMENT =
    MUST_BE VERIFIED WHEN TERMS ARE REGISTERED

RUNTIME_FRAMEWORK_EXPANSION =
    NOT_AUTHORIZED

IMPLEMENTATION_AUTHORIZATION =
    NONE
```

---

## 20. Decision summary

```text
OPERATION RECORD =
    MINIMAL PRODUCT-RUNTIME EXECUTION FACT

SEMANTICS REGISTRY =
    AUTHORITATIVE PRODUCT VOCABULARY

PFM =
    ARTIFACT AUTHORITY

PAGE GEOMETRY =
    GEOMETRY SEMANTIC AUTHORITY

FILE FACTORY =
    DEVELOPMENT INFRASTRUCTURE
    NOT PRODUCT DOMAIN MODEL

JOBS =
    LATER

AGENTIC LAYER =
    LATER

PRIMARY SEMANTIC LAW =
    ONE CONCEPT
    ONE CANONICAL IDENTITY
    EXPLICIT SOURCE
    NO SILENT DUPLICATION
```
