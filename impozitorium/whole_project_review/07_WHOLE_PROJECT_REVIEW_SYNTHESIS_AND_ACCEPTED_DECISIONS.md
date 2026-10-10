# 07 — Whole-Project Review Synthesis and Accepted Architectural Decisions

```text
DOCUMENT_CLASS =
    REVIEW_SYNTHESIS
    + HUMAN_ACCEPTED_ARCHITECTURAL_DIRECTION
    + EXECUTION_PRIORITY_CLARIFICATION

STATUS =
    REVIEW_PACKAGE_SYNTHESIS
    NOT_CANONICAL_PROJECT_POLICY_YET
    NOT_IMPLEMENTATION_AUTHORIZATION

EVIDENCE_BASIS =
    01_ACTUAL_PROJECT_RECONNAISSANCE.md
    02_SEMANTIC_AND_ARCHITECTURAL_ALIGNMENT_REVIEW.md
    03_FILE_FACTORY_MINIMUM_USEFUL_EXCAVATOR_CRITERIA.md
    04_PRODUCT_OPERATION_RECORD_AND_CANONICAL_SEMANTICS_REGISTRY.md
    05_CANONICAL_APPLICATION_SEMANTICS_BASELINE_V1.md
    semantic_registry_v1.yaml
    06_ARCHITECTURAL_DECISION_03_PLATFORM_GEOMETRY_PRODUCTION_OBJECT_AND_PLACEMENT_BOUNDARY.md
```

## 1. Purpose

This document consolidates the whole-project review after Human/Coordinator discussion and records which review conclusions were accepted, modified, rejected, or deferred.

It does not replace the underlying review artifacts.

It is the bridge between:

```text
independent review evidence
        ↓
Human / Coordinator decisions
        ↓
future canonicalization into Raymond-1968/Imposition_app
```

No canonical project files are modified by this document.

---

## 2. Overall review conclusion

```text
PROJECT_DIRECTION_LOST =
    NO

GREENFIELD_REWRITE_REQUIRED =
    NO

ARCHITECTURAL_CONVERGENCE_REQUIRED =
    YES

SEMANTIC_NORMALIZATION_REQUIRED =
    YES
    substantially begun

PRODUCT_SUBSTRATE_DIRECTION =
    SOUND

DEVELOPMENT_INFRASTRUCTURE =
    VALUABLE
    BUT MUST REMAIN SEPARATE FROM PRODUCT RUNTIME

IMPLEMENTATION_AUTHORIZED_BY_REVIEW =
    NO
```

The review established that Impozitorium has accumulated substantial accepted engineering in several divergent lines rather than a single integrated product line.

The central issue is therefore not absence of architecture.

The central issue is:

```text
accepted architecture and valuable code exist,
but ownership and integration are distributed
across divergent product, migration, laboratory,
and development-infrastructure lineages.
```

The project should converge deliberately rather than restart.

---

## 3. Accepted review strengths

The following findings are accepted.

### 3.1 Structural engine direction

```text
PDFium =
    rendering / preview boundary

pikepdf + qpdf =
    structural PDF reading / writing / mutation boundary

PyMuPDF =
    legacy / transitional production dependency
```

The migration remains capability-by-capability.

No silent fallback architecture is accepted as the target state.

### 3.2 Source and artifact safety

Accepted platform laws remain:

```text
SOURCE PDF IS SACRED

Working Document
Preview Result
Candidate / generated result
Final output / Save As

are distinct lifecycle concepts.
```

Platform File Management is retained as the product artifact/filesystem authority and should be completed rather than replaced.

### 3.3 HumanGate and evidence discipline

Human acceptance, independent review, bounded authority, STOP behavior and evidence-based publication remain core governance principles.

However, governance intensity should remain proportional to risk.

Living laboratories do not require platform-critical ceremony for every small iteration.

### 3.4 Laboratory semantics

Booklet Folding and Vector AutoBleed are accepted as valuable semantic and production-knowledge sources.

Their implementation is not automatically promoted.

The governing rule is:

```text
PRESERVE SEMANTICS
REIMPLEMENT OR ADAPT AGAINST PLATFORM CONTRACTS
WHEN PROMOTED
```

---

## 4. Architectural Decision 01 — Product line and development-infrastructure boundary

### 4.1 Product substrate line of record

Accepted direction:

```text
PRODUCT_SUBSTRATE_LINE_OF_RECORD =
    engine-neutral / EN lineage

CURRENT REPRESENTATIVE =
    docs/oc6d2-b4-human-acceptance-01
    plus accepted engine-neutral predecessors
```

This means the EN lineage is the architectural basis for future product-substrate work.

It does NOT mean:

```text
EN contains all valuable product code

OW is obsolete

OC-line is obsolete

whole branches should be merged blindly
```

Product-relevant deltas from OW, OC, transfer and laboratory lines must be converged selectively.

### 4.2 Development infrastructure

The following form a separate development-infrastructure domain:

```text
File Factory
Orchestrator Operator Workplace
Stage 2C
Kandev integration
D01 and related control machinery
```

Hard boundary:

```text
PRODUCT RUNTIME DEPENDENCY
ON FILE FACTORY / DEVINFRA =
    FORBIDDEN
```

Reusable patterns may be adopted explicitly.

Domain-object reuse is forbidden by default.

### 4.3 Execution-priority correction to the architecture review

The recommendation in Review 02 to freeze File Factory expansion until a product vertical slice is NOT accepted as execution priority.

Accepted correction:

```text
FILE_FACTORY_STATUS =
    ACTIVE_PRIMARY_DEVELOPMENT_STREAM

PURPOSE =
    BUILD THE MULTI-AGENT DEVELOPMENT ACCELERATOR
    REQUIRED FOR SUSTAINABLE IMPOZITORIUM CONSTRUCTION

RETURN_TO_MAJOR_PRODUCT_IMPLEMENTATION =
    AFTER FILE_FACTORY REACHES
    MINIMUM_USEFUL_EXCAVATOR
    unless Human explicitly decides otherwise
```

The architectural separation remains intact.

Execution priority is independent of product ownership.

---

## 5. File Factory Minimum Useful Excavator gate

File Factory is not required to become commercially polished before it becomes useful.

Target:

```text
L2 =
    MINIMUM_USEFUL_EXCAVATOR
```

Required gate dimensions:

```text
A. MULTI_AGENT_EXECUTION
B. PARALLEL_WORK_UNITS
C. WORKSPACE_ISOLATION
D. AUTHORITY_BOUNDARIES
E. EVIDENCE_COLLECTION
F. INDEPENDENT_REVIEW_ROUTING
G. FAILURE / STOP SEMANTICS
H. RESTART / RECOVERY
I. HUMAN_GATE_SUMMARY
J. MULTI_MODEL_ROUTING
K. BASIC_COST_VISIBILITY
L. REAL_IMPOZITORIUM_PILOT
M. MEASURABLE_LEVERAGE
```

The governing KPI is leverage, not UI polish.

```text
L2_PASS =
    all required capabilities sufficient
    + real pilot pass
    + material reduction in Human coordination,
      frontier-model cost,
      and/or wall-clock delivery time
      without material correctness loss
```

---

## 6. Architectural Decision 02 — Product Operation Record and canonical semantics

### 6.1 Minimal Product Operation Record

Accepted direction:

```text
OPERATION RECORD =
    one minimal product-runtime fact
    describing a bounded operation over explicit artifacts
```

It owns:

```text
operation identity
operation kind/version
input artifact refs
parameters
policy reference
execution identity
diagnostics
admissibility outcome
output artifact refs
verification reference
provenance
```

It does not own artifact storage/lifecycle.

Platform File Management remains artifact authority.

### 6.2 Admissibility

Production admissibility is first-class.

The semantic classes include:

```text
PASS
PASS_WITH_WARNING
OPERATOR_ACCEPTED_DEVIATION
REPAIRED_AND_ACCEPTED
BLOCKED
UNKNOWN
```

Final enum names remain implementation-time detail.

Hard distinction:

```text
UNKNOWN != BLOCKED
UNKNOWN != PASS
```

### 6.3 Jobs and Agentic Layer

```text
FULL JOB SYSTEM =
    LATER

MINIMAL OPERATION / ARTIFACT LINEAGE =
    EARLIER

AGENTIC LAYER =
    LATER
```

Future GUI, batch, Jobs and agent surfaces must use the same canonical operations.

---

## 7. Semantic governance breakthrough

The review exposed that architecture discussion itself was becoming unsafe because key terms were overloaded.

The project therefore adopts:

```text
CANONICAL PRODUCT SEMANTICS REGISTRY =
    REQUIRED

SEMANTIC SOURCE PRIORITY =
    1. applicable international / industry standard
    2. established production-domain terminology
    3. accepted Impozitorium terminology
    4. new Impozitorium extension only where required
```

The registry is machine-readable and Human-readable.

Current semantic baseline contains:

```text
semantic_registry_v1.yaml
05_CANONICAL_APPLICATION_SEMANTICS_BASELINE_V1.md
```

Important disambiguations now include:

```text
MODULE.PAGE_GEOMETRY
    != PLATFORM.GEOMETRY_CORE

GOVERNANCE.HUMAN_ACCEPTANCE
    != ARTIFACT.ADMISSION
    != PRODUCTION.ADMISSIBILITY_OUTCOME

GOVERNANCE.REPOSITORY_PUBLICATION
    != ARTIFACT.PROMOTION
    != UI.SAVE_AS

PRODUCTION.JOB
    != DEVINFRA.FILE_FACTORY_JOB
```

Bare ambiguous terms must not silently resolve to one meaning.

The registry is expected to continue evolving.

Evolution is acceptable only without methodological contradiction.

---

## 8. Standards-first geometry / imposition mapping

Current standards-aligned direction includes:

```text
ISO 32000-2
    PDF structural semantics

ISO 19593-1:2026
    processing-step / production-processing semantics in PDF

CIP4 JDF / XJDF
    print-production intent, layout, sheet/surface,
    placed-object and mark/content placement semantics
```

Current accepted mappings include:

```text
PRODUCTION.PLACED_OBJECT
    ↔ CIP4/XJDF PlacedObject

PRODUCTION.CONTENT_OBJECT
    ↔ CIP4 ContentObject payload

PRODUCTION.MARK_OBJECT
    ↔ CIP4 MarkObject payload

GEOMETRY.PLACEMENT_TRANSFORM
    related to CIP4 PlacedObject CTM

PDF.CTM
    distinct PDF graphics-state concept
```

Impozitorium extensions retained where no demonstrated equivalent exists include:

```text
GEOMETRY.LAYOUT_BOX
GEOMETRY.FRAMEBOX
GEOMETRY.FRAME_INTENT
GEOMETRY.CLIP_REGION
GEOMETRY.PRODUCTION_CONTOUR (provisional)
GEOMETRY.DOCUMENT_TRANSFORM
PRODUCTION.PRODUCTION_OBJECT (provisional)
TECHNICAL_OBJECT.TECHNICAL_OBJECT
```

Needs-standard-review is a valid registry state, not a registry defect.

---

## 9. Architectural Decision 03 — Platform Geometry, ProductionObject, placement boundary

### 9.1 Ownership

Accepted direction:

```text
PLATFORM.STRUCTURAL_PDF_CORE =
    owns raw PDF structure
    + bounded structural mutation
    + preservation / verification

PLATFORM.GEOMETRY_CORE =
    owns generic platform geometry semantics

MODULE.PAGE_GEOMETRY =
    module
    not geometry authority
```

Hard law:

```text
NO MODULE OWNS GENERIC PDF / GEOMETRY SEMANTICS.

MODULE SAYS WHAT.
PLATFORM KNOWS HOW.
```

### 9.2 layout_box

```text
GEOMETRY.LAYOUT_BOX
```

is selected from source PDF structure by:

```text
TrimBox
→ ArtBox
→ CropBox
→ MediaBox
```

It is the source-derived layout basis.

### 9.3 Framebox

```text
GEOMETRY.FRAMEBOX
```

is the platform-owned current rectangular working/reference frame of the production object.

It is not equivalent to:

```text
TrimBox
layout_box
FrameIntent
ClipRegion
ProductionContour
```

### 9.4 Frame intent

```text
GEOMETRY.FRAME_INTENT
```

is operator- or machine-proposed intent to establish or modify Framebox.

Define Framebox is an operator-facing operation/capability over platform-owned geometry semantics.

Exact structural materialization remains open.

---

## 10. Document transform versus placement transform

This distinction is accepted as a core architectural law.

### Document transform

Changes the canonical working artifact or intrinsic object geometry.

Examples:

```text
rotation normalization
page-size change
Framebox materialization
content scaling
box mutation
geometry repair
bleed reconstruction producing a new canonical result
```

Required invariant:

```text
NO UNRESOLVED DOCUMENT TRANSFORM
MAY ESCAPE INTO THE NEXT PRODUCTION OPERATION.
```

### Placement transform

Changes only one placement occurrence in imposition/output space.

Examples:

```text
180° booklet-page rotation
90° / 270° label placement
arbitrary nesting angle
sheet translation
placement scaling when explicitly admissible
```

Placement transforms may remain transforms until output construction.

They do not require materializing a new source PDF merely because the placement rotates or translates the object.

---

## 11. ProductionObject

```text
PRODUCTION.PRODUCTION_OBJECT
```

is the platform representation of one placement-capable, semantically coherent production unit.

It is intrinsic.

It is not equivalent to:

```text
Working Document
PDF Page
Framebox
PlacedObject
CIP4 ContentObject
```

Its source may eventually be:

```text
WHOLE_PAGE
RECTANGULAR_SOURCE_REGION
future CONTOUR_SOURCE_REGION
```

V1 may support WHOLE_PAGE only.

ProductionObject is semantic; it is not required to be a separately materialized PDF file.

---

## 12. ProductionObject semantic coherence

ProductionObject may carry/reference:

```text
source identity
provenance

Framebox
optional ProductionContour
bleed semantics
orientation / intrinsic geometry state

artwork
technical / processing content
contours
marks

color semantics
spot-color identity
Separation / DeviceN semantics
ICC-related source semantics
OutputIntent-related structural information

qualification / admissibility state
```

Shared movement does not imply semantic merging.

Artwork, technical content, contours and color semantics remain individually identifiable.

---

## 13. Placement readiness

An imposition module receives placement-ready ProductionObjects, not raw PDFs that it must normalize itself.

Conceptually placement-ready requires:

```text
canonical intrinsic geometry known
Framebox valid
document transforms resolved
source geometry stable
required structural semantics preserved
technical / processing content identifiable
Optional Content semantics preserved where required
color semantics preserved
warnings classified
artifact/source reference stable
```

Exact runtime status/enum remains open.

---

## 14. Placement / imposition boundary

Accepted conceptual direction:

```text
INTRINSIC SIDE

Working Document
→ Structural PDF Core
→ Platform Geometry Core
→ ProductionObject

        ↓ production-module arrangement algorithm

PLACEMENT SIDE

Layout / Sheet / Surface
→ PlacedObject
→ placement transform / CTM
→ ContentObject OR MarkObject payload
→ output construction
```

The production module owns arrangement strategy.

The platform owns:

```text
intrinsic geometry representation
placement representation
sheet/surface coordinate semantics
structural PDF output materialization
```

---

## 15. Contour nesting direction

Rectangular workflows may use Framebox as sufficient placement geometry.

Contour nesting may use:

```text
GEOMETRY.PRODUCTION_CONTOUR
```

for fit/collision while Framebox remains the rectangular reference/bounding frame.

The platform must not require a future rewrite of placement semantics merely because the object ceases to be rectangular.

---

## 16. Technical / processing content

Technical objects and processing semantics must remain structurally and semantically distinguishable from artwork.

Current direction:

```text
common technical-object representation
+
operation-specific production policy
```

Exact PDF realization remains open.

ISO 19593 processing-step representation and Optional Content are strong relevant standards/mechanisms but are not yet fixed as the only implementation.

---

## 17. Color-preservation boundary

Full color management is explicitly deferred to a separate future architectural decision.

However Decision 03 establishes:

```text
STRUCTURAL OR GEOMETRIC TRANSFORMATION
MUST NOT SILENTLY CHANGE COLOR SEMANTICS.
```

At minimum preserve, where present and in scope:

```text
process-color meaning
embedded profile relationships
ICCBased semantics
Separation / DeviceN semantics
spot-color identity
OutputIntent-related information
```

No implicit color conversion is authorized.

Future dedicated decision:

```text
COLOR MANAGEMENT / ICC ARCHITECTURE
```

will address preview/soft proof, output conversion, ICC/iccMAX, rendering intents, PDF/X/OutputIntent, spot handling, and the boundary with closed printer/DFE/RIP color management.

---

## 18. Review recommendations accepted with modification

### Accepted substantially

```text
EN-line as product-substrate basis
PFM keep-and-complete
pikepdf/qpdf structural ownership
PDFium render ownership
Operation Record before broad module migration
Jobs later than operation/artifact lineage
Agentic Layer later than Jobs
lab semantics preserved rather than direct code transplant
technical-object common representation
governance proportionality
```

### Accepted with modification

```text
"Page Geometry as single geometry authority"
    → corrected to PLATFORM.GEOMETRY_CORE as authority;
      MODULE.PAGE_GEOMETRY remains a module.

"Create Booklet + Booklet Folding = merge"
    → corrected to convergence on a shared booklet/signature domain;
      final module/UI/operation relationship NOT_DECIDED.

"technical objects use OCG"
    → corrected to structurally separable semantic identity;
      exact PDF realization NOT_DECIDED.

"Define Framebox overrides layout_box"
    → corrected: FrameIntent and Framebox are explicit platform semantics;
      no hidden competing precedence chain.
```

### Review recommendation not accepted as execution priority

```text
freeze File Factory major work until product vertical slice
```

Replaced by:

```text
File Factory remains active primary development stream
until Minimum Useful Excavator L2 is achieved.
```

---

## 19. Explicitly deferred architecture

The following remain intentionally open:

```text
exact Git convergence strategy
exact Framebox → PDF-box materialization policy
exact ProductionObject runtime schema
final contour model
technical-layer PDF realization
full output-projection model
full product Job system
Agentic Layer
external API / commercial shell
full Color Management / ICC architecture
cross-volume PFM qualification unless needed
```

Deferral does not mean absence of ownership.

Generic PDF, geometry, artifact and semantic ownership stays at the platform level.

---

## 20. Current execution priority

```text
PRIMARY ACTIVE STREAM =
    FILE FACTORY

TARGET =
    MINIMUM_USEFUL_EXCAVATOR L2

MAJOR PRODUCT IMPLEMENTATION =
    DEFERRED UNTIL L2
    unless Human explicitly changes priority

ARCHITECTURAL / SEMANTIC WORK =
    MAY CONTINUE AS NEEDED
    to prevent future rework
```

The whole-project review is therefore not an instruction to abandon File Factory.

It provides the product architecture that File Factory will later help construct.

---

## 21. Next canonicalization step

The review package remains non-canonical evidence and decision support.

After Human/Coordinator completion of the review synthesis:

```text
claude-cloud-sandbox
    review evidence + decision support
        ↓
Human / Coordinator final reconciliation
        ↓
Raymond-1968/Imposition_app
    canonical architectural decision record
    updated project routing
    accepted execution priority
    references back to review artifacts
```

The future canonical record should summarize decisions rather than copy the entire review package.

---

## 22. Review-package conclusion

```text
WHOLE_PROJECT_REVIEW =
    SUBSTANTIALLY COMPLETE

FACTUAL_RECONSTRUCTION =
    COMPLETE FOR REVIEW BASIS

ARCHITECTURAL_ALIGNMENT_REVIEW =
    COMPLETE

SEMANTIC BASELINE =
    ESTABLISHED

ARCHITECTURAL_DECISION_01 =
    ACCEPTED_DIRECTION

FILE_FACTORY_L2_GATE =
    ACCEPTED_DIRECTION

ARCHITECTURAL_DECISION_02 =
    ACCEPTED_DIRECTION

ARCHITECTURAL_DECISION_03 =
    ACCEPTED_DIRECTION

IMPLEMENTATION AUTHORIZATION =
    NONE

NEXT PHASE =
    COMPLETE REVIEW CANONICALIZATION
    + CONTINUE FILE FACTORY TOWARD L2
```
