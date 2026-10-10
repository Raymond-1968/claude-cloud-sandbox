# 06 — Architectural Decision 03: Platform Geometry, Production Object, and Placement Boundary

```text
DOCUMENT_CLASS =
    ARCHITECTURAL_DECISION_SUPPORT
    + HUMAN_ACCEPTED_DIRECTION

DECISION_ID =
    ARCHITECTURAL_DECISION_03

STATUS =
    HUMAN_ACCEPTED_DIRECTION
    NOT_IMPLEMENTATION_AUTHORIZATION

SEMANTIC_BASIS =
    05_CANONICAL_APPLICATION_SEMANTICS_BASELINE_V1.md
    semantic_registry_v1.yaml

RELATIONSHIP_TO_REVIEW =
    ADDENDUM_TO
    01_ACTUAL_PROJECT_RECONNAISSANCE.md
    02_SEMANTIC_AND_ARCHITECTURAL_ALIGNMENT_REVIEW.md
    03_FILE_FACTORY_MINIMUM_USEFUL_EXCAVATOR_CRITERIA.md
    04_PRODUCT_OPERATION_RECORD_AND_CANONICAL_SEMANTICS_REGISTRY.md
    05_CANONICAL_APPLICATION_SEMANTICS_BASELINE_V1.md
```

## 1. Decision summary

Impozitorium separates four concerns that were historically mixed inside modules:

```text
A. PDF structural facts and structural mutation

B. platform-owned generic geometry semantics

C. production-object semantics

D. placement / imposition semantics
```

The governing ownership law is:

```text
NO MODULE OWNS GENERIC PDF OR GEOMETRY SEMANTICS.

MODULE SAYS WHAT.
PLATFORM KNOWS HOW.
```

Operator-facing modules remain replaceable production capabilities. Removing, replacing, or versioning a module must not remove the platform's understanding of PDF structure, geometry, preservation, or output construction.

---

## 2. Platform ownership

### 2.1 PLATFORM.STRUCTURAL_PDF_CORE

Owns factual PDF structure and bounded structural mutation.

At minimum this includes:

```text
PDF page boxes
raw / inherited / effective box values
MediaBox origin
/Rotate
/UserUnit
content / resource structure
Optional Content preservation
OutputIntent / color-related structural preservation
bounded mutation
candidate writing
structural verification
```

It does not decide production meaning merely because it can read or write the PDF objects.

### 2.2 PLATFORM.GEOMETRY_CORE

"Platform Geometry Core" is the platform-owned semantic authority for generic geometry.

It owns:

```text
GEOMETRY.LAYOUT_BOX
GEOMETRY.FRAMEBOX
coordinate-space semantics
absolute ↔ working-frame transforms
orientation semantics
geometry descriptors
geometry diagnostics
normalization semantics
relationships between intrinsic page/object geometry
and platform working geometry
```

It is explicitly distinct from:

```text
MODULE.PAGE_GEOMETRY
PLATFORM.STRUCTURAL_PDF_CORE
```

The existing module named **Page Geometry** remains a module. It is not the owner of generic platform geometry semantics.

---

## 3. PDF boxes, layout_box, and Framebox

### 3.1 PDF page boxes

```text
PDF.BOX.MEDIA
PDF.BOX.CROP
PDF.BOX.BLEED
PDF.BOX.TRIM
PDF.BOX.ART
```

are PDF structural facts.

### 3.2 layout_box

```text
GEOMETRY.LAYOUT_BOX
```

is the source-derived canonical layout basis selected by the platform policy:

```text
TrimBox
→ ArtBox
→ CropBox
→ MediaBox
```

It is not itself a PDF box.

### 3.3 Framebox

```text
GEOMETRY.FRAMEBOX
```

is the platform-owned internal rectangular working/reference frame of the production object.

Hard distinctions:

```text
FRAMEBOX != PDF BOX

FRAMEBOX != LAYOUT_BOX

FRAMEBOX != FRAME_INTENT

FRAMEBOX != CLIP_REGION

FRAMEBOX != PRODUCTION_CONTOUR
```

These may coincide geometrically in a particular case without becoming semantically identical.

The initial Framebox may be derived from the layout_box through platform interpretation / normalization.

After an explicit accepted document-geometry operation, the current Framebox represents the current working geometry of the object.

---

## 4. Frame intent and Define Framebox

```text
GEOMETRY.FRAME_INTENT
```

is explicit operator- or machine-proposed intent to establish or modify the working frame.

It is not the Framebox itself.

The operator-facing **Define Framebox** capability expresses that intent through an explicit production operation.

Conceptually:

```text
FRAME_INTENT
    ↓
Define Framebox operation
    ↓
platform validation / admissibility
    ↓
PLATFORM.GEOMETRY_CORE
    ↓
current FRAMEBOX
    ↓
bounded structural materialization when required
```

Exact mapping of Framebox into PDF page boxes remains governed by:

```text
POLICY.FRAME_MATERIALIZATION =
    NOT_YET_FINALIZED
```

No hidden second layout precedence chain is allowed.

Downstream consumers receive one canonical current working geometry result.

---

## 5. Observe and mutate are separate

Required law:

```text
OBSERVE != MUTATE
```

Reading geometry must not silently rewrite PDF structure.

Producer-specific repairs and historical heuristics must become explicit diagnostics and/or explicit repair operations rather than hidden side effects of geometry inspection.

Historical behavior such as Corel-specific correction may be valuable production knowledge, but the knowledge belongs to platform diagnostics/repair semantics, not to an opaque normalization side effect and not to an individual module.

---

## 6. Document transforms versus placement transforms

This distinction is canonical for the architecture.

### 6.1 GEOMETRY.DOCUMENT_TRANSFORM

A document transform changes the canonical working artifact or its intrinsic production geometry.

Examples include:

```text
rotation normalization
page-size change
Framebox change when structurally materialized
proportional or non-proportional content transformation
box mutation
geometry repair
bleed reconstruction that produces a new canonical working result
```

A document transform must not leave unresolved historical transforms for later modules to interpret.

Required law:

```text
NO UNRESOLVED DOCUMENT TRANSFORM
MAY ESCAPE INTO THE NEXT PRODUCTION OPERATION.
```

After an accepted document transform, the platform must treat the result as a new canonical working state and rebuild/re-evaluate the affected geometry and structural semantics.

### 6.2 GEOMETRY.PLACEMENT_TRANSFORM

A placement transform does not change the canonical source/working object.

It changes only one occurrence of that object in an imposition/output context.

Examples:

```text
180° rotation of a page in booklet imposition
90° / 270° rotation of a label on a sheet
arbitrary nesting rotation
translation on a sheet
placement scaling where explicitly allowed by production policy
```

Placement transforms may remain transforms until output construction.

They do not require pre-materializing a new source PDF merely because an instance is rotated or translated.

The placement-side model aligns conceptually with CIP4/XJDF PlacedObject and its placement CTM, while remaining explicitly separate from PDF graphics-state CTM semantics.

---

## 7. GUI and current working coordinates

The GUI must display the **current canonical working geometry**, not stale source geometry.

When a document transform changes the accepted working frame, subsequent rendering, measurement, rulers, overlays, and module interaction must use the new current geometry state.

The platform's human-readable working coordinate origin remains zero-based:

```text
[0, 0, width, height]
```

for the current working frame exposed to the GUI.

Source-derived layout_box remains preserved as provenance/structural interpretation where relevant; it is not allowed to keep the GUI anchored to obsolete geometry after an accepted document transform.

Placement transforms are an exception because they belong to output-sheet placement, not to mutation of the underlying Working Document.

---

## 8. ProductionObject

```text
PRODUCTION.PRODUCTION_OBJECT
```

is the platform representation of one placement-capable, semantically coherent production unit.

It is not equivalent to:

```text
Working Document
PDF page
Framebox
PlacedObject
CIP4 ContentObject
```

A ProductionObject references its source rather than necessarily being a separate PDF file.

Its source locator may eventually identify:

```text
WHOLE_PAGE
RECTANGULAR_SOURCE_REGION
future CONTOUR_SOURCE_REGION
```

A first implementation may support only WHOLE_PAGE.

Architecture must not make whole-page-only sourcing a permanent invariant.

---

## 9. ProductionObject content model

ProductionObject is not merely geometry around PDF content.

It is the smallest placement-capable semantic production unit whose internal production meanings remain distinguishable.

It may carry or reference:

```text
identity
source artifact / page / source region
provenance

intrinsic geometry
    Framebox
    optional ProductionContour
    bleed semantics
    orientation / intrinsic transform state

semantic content
    artwork
    technical / processing content
    contours
    marks
    other registered production components

color semantics
    process-color semantics
    ICC-related source semantics
    spot-color identity
    Separation / DeviceN semantics where applicable
    OutputIntent / related metadata where applicable

qualification / admissibility state
```

Shared movement does not imply semantic merging.

Artwork, technical content, contour information, spot-color semantics and other production components may move together while retaining independent identities.

---

## 10. ProductionContour and future nesting

```text
GEOMETRY.PRODUCTION_CONTOUR
```

remains provisional.

For rectangular workflows:

```text
Framebox may be sufficient
to describe the placement geometry.
```

For contour-nesting workflows:

```text
ProductionContour may define
the physical object shape used for fit/collision.

Framebox remains
the rectangular reference / bounding / placement frame.
```

Framebox is not made obsolete by future contour support.

Standards realization of cutting/folding/processing contours remains subject to ISO 19593 / CIP4 mapping and later technical-layer decisions.

---

## 11. Placement readiness

An imposition module must not receive a raw Working Document and independently decide whether it is safe to place.

A ProductionObject becomes placement-ready only when the platform can establish sufficient intrinsic stability.

Conceptually:

```text
PLACEMENT_READY requires:

    canonical intrinsic geometry known

    current Framebox valid

    required document transforms resolved

    no unresolved source-geometry transform state

    relevant structural semantics preserved

    required technical / processing content identifiable

    required Optional Content semantics preserved

    required color semantics preserved

    structural warnings classified

    artifact/source reference stable
```

Final runtime enum/status naming is not decided here.

---

## 12. Module boundary

A production module receives placement-ready ProductionObjects.

It may own:

```text
production-specific algorithm
operation parameters
arrangement strategy
domain-specific admissibility rules
interactive controls specific to its task
```

It must not own:

```text
generic PDF box interpretation
generic geometry normalization
generic rotation repair
generic structural PDF rebuilding
generic Optional Content preservation
generic color-semantic preservation
artifact lifecycle
```

Examples:

### Vector AutoBleed

Owns:

```text
bleed-construction mathematics
source-sampling strategy
bleed-specific sanitation policy
explicit raster fallback semantics
VAB-specific diagnostics
```

Does not own generic PDF normalization, raw box interpretation, rotation repair, Optional Content preservation mechanics, or generic structural rebuild.

### Step & Repeat / N-up / Cut Stack / Booklet / Nesting

Own arrangement logic.

They consume platform-owned intrinsic object geometry and emit placement intent.

They do not redefine what Framebox, PDF boxes, spot colors, or structural preservation mean.

---

## 13. Placement / imposition model

The standards-aligned conceptual direction is:

```text
INTRINSIC / SOURCE SIDE

Working Document
    ↓
Platform Structural PDF Core
    +
Platform Geometry Core
    ↓
ProductionObject
    Framebox
    optional ProductionContour
    bleed
    semantic content
    color semantics
    preservation state

            ↓ imposition algorithm

PLACEMENT SIDE

CIP4-aligned Layout / Sheet / Surface
    ↓
PlacedObject
    placement CTM
    placement ClipBox / related placement geometry
    trimming projection as applicable
    ↓
ContentObject OR MarkObject payload

            ↓

output construction
```

This is a conceptual mapping, not a claim that the Impozitorium runtime must directly serialize JDF/XJDF structures.

---

## 14. Synchronous placement of semantic components

Required law:

```text
PLACEMENT TRANSFORM APPLIES
TO THE PRODUCTION OBJECT
AS A SEMANTIC UNIT.
```

For example, in contour nesting:

```text
ProductionContour drives fit/collision,
but the platform places the whole ProductionObject.

Artwork travels with the contour.

Technical/processing components travel synchronously.

Spot-color and layer semantics remain identifiable.
```

Modules must not independently rotate/move artwork, contour, marks and technical content as unrelated objects unless the production operation explicitly defines such a relationship.

---

## 15. Output projections

A composed production result may have more than one output purpose.

Conceptually:

```text
ONE PRODUCTION COMPOSITION
        ↓
OUTPUT-SPECIFIC PROJECTION
        ↓
PRINT OUTPUT
POSTPRESS / CUTTING OUTPUT
PROOF / INSPECTION OUTPUT
other future outputs
```

Print output and postpress output may include different semantic components while preserving shared geometry and identities.

Exact output-projection architecture is not finalized by this decision.

Technical-layer realization, ISO 19593 processing-step representation, and device-specific postpress export remain later decisions.

---

## 16. Color preservation invariant

Color management is a separate future architectural decision.

This decision establishes only the preservation boundary required now.

```text
COLOR MANAGEMENT ARCHITECTURE =
    REQUIRED PLATFORM CONCERN
    SEPARATE FUTURE DECISION

CURRENT LAW =
    STRUCTURAL OR GEOMETRIC TRANSFORMATION
    MUST NOT SILENTLY CHANGE COLOR SEMANTICS.
```

ProductionObject therefore carries/references color semantics that must survive document transformation and placement.

At minimum this includes preserving, where present and in scope:

```text
process-color meaning
embedded profile relationships
ICCBased semantics
Separation / DeviceN semantics
spot-color identities
OutputIntent-related structural information
```

No implicit color conversion is authorized by this decision.

Preview/display color transformation and production-output color conversion are explicitly separate future concerns.

A later architecture decision will define:

```text
source characterization
ICC / iccMAX policy
preview / soft-proof transform
rendering intents
output conversion
spot-color handling
PDF/X / OutputIntent policy
boundary with printer / DFE / RIP color management
```

---

## 17. First vertical-slice implication

The future first end-to-end platform slice should prove the boundary rather than merely add another button.

Conceptually it should demonstrate:

```text
Working Document
→ structural/geometry inspection
→ current Framebox
→ operator FrameIntent where applicable
→ explicit operation
→ document transform when required
→ structural candidate
→ verification
→ rebuilt current geometry
→ PDFium preview
→ artifact admission / Working Document
→ Save As
```

Manual Trim and Define Framebox are suitable candidate surfaces because they exercise geometry, structural mutation, verification and operator intent.

The exact implementation task is not authorized by this document.

---

## 18. Legacy migration implication

```text
preflight/core.py::normalize_boxes
```

and similar legacy paths remain transitional compatibility behavior, not the future semantic authority.

Useful producer-specific knowledge must be extracted rather than discarded.

Migration principle:

```text
LEGACY HIDDEN HEURISTIC
    ↓
named diagnostic / policy / repair semantics
    ↓
Platform Geometry Core / Structural PDF Core
```

The legacy path is retired only after equivalent required production behavior is explicitly preserved and qualified.

---

## 19. Open items

This decision intentionally leaves open:

```text
POLICY.FRAME_MATERIALIZATION
    exact mapping between Framebox and PDF structural page boxes

GEOMETRY.PRODUCTION_CONTOUR
    final contour domain model and standards realization

PRODUCTION.PRODUCTION_OBJECT
    exact runtime schema and source-region implementation

PLACEMENT_READY
    exact state/enum and verification profile

OUTPUT PROJECTIONS
    runtime representation and policy

TECHNICAL LAYERS
    exact ISO 19593 / Optional Content realization

COLOR MANAGEMENT
    full ICC / iccMAX architecture
```

These are bounded future decisions, not reasons to return generic PDF semantics to modules.

---

## 20. Human decision

```text
ARCHITECTURAL_DECISION_03 =
    ACCEPTED_DIRECTION

PLATFORM.STRUCTURAL_PDF_CORE =
    OWNS PDF STRUCTURE
    + SAFE STRUCTURAL MUTATION
    + STRUCTURAL PRESERVATION / VERIFICATION

PLATFORM.GEOMETRY_CORE =
    SINGLE OWNER OF GENERIC PLATFORM GEOMETRY SEMANTICS

MODULE.PAGE_GEOMETRY =
    MODULE
    NOT PLATFORM GEOMETRY AUTHORITY

GEOMETRY.LAYOUT_BOX =
    SOURCE-DERIVED LAYOUT BASIS

GEOMETRY.FRAMEBOX =
    PLATFORM-OWNED CURRENT RECTANGULAR WORKING FRAME

GEOMETRY.FRAME_INTENT =
    INTENT TO ESTABLISH / MODIFY FRAMEBOX

DOCUMENT_TRANSFORM =
    MUST MATERIALIZE / RESOLVE BEFORE NEXT PRODUCTION OPERATION

PLACEMENT_TRANSFORM =
    MAY REMAIN A PLACEMENT TRANSFORM UNTIL OUTPUT CONSTRUCTION

PRODUCTION.PRODUCTION_OBJECT =
    SEMANTICALLY COHERENT PLACEMENT-CAPABLE PRODUCTION UNIT

PRODUCTION.PLACED_OBJECT =
    PLACEMENT OCCURRENCE IN LAYOUT / SHEET / SURFACE SPACE

MODULE_OWNERSHIP =
    DOMAIN-SPECIFIC ALGORITHM ONLY

GENERIC PDF / GEOMETRY OWNERSHIP BY MODULE =
    FORBIDDEN

COLOR_SEMANTICS =
    PRESERVATION_REQUIRED

COLOR_MANAGEMENT_POLICY =
    SEPARATE FUTURE DECISION

IMPLEMENTATION_AUTHORIZATION =
    NONE
```

---

## 21. Core invariants

```text
I1  SOURCE PDF IS SACRED.

I2  OBSERVE != MUTATE.

I3  MODULE SAYS WHAT; PLATFORM KNOWS HOW.

I4  NO MODULE OWNS GENERIC PDF / GEOMETRY SEMANTICS.

I5  TrimBox / ArtBox / CropBox / MediaBox selection produces layout_box;
    layout_box is not a PDF box.

I6  Framebox is the current rectangular working frame;
    it is not TrimBox, layout_box, frame intent, clip region, or contour.

I7  No unresolved document transform crosses an operation boundary.

I8  Placement transforms do not mutate the canonical production object.

I9  ProductionObject is intrinsic; PlacedObject is extrinsic.

I10 Placement acts on the ProductionObject as a semantic unit.

I11 Shared movement does not merge artwork, technical, contour, or color semantics.

I12 Structural/geometric transformations must not silently change color semantics.

I13 ProductionContour may extend object geometry beyond rectangles;
    Framebox remains a valid rectangular reference.

I14 Downstream modules consume one canonical current geometry state.

I15 Standards-first semantic governance remains mandatory for new terms.
```
