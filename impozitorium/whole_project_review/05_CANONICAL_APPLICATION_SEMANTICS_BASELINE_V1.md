# 05 — Canonical Application Semantics Baseline V1

```text
TASK_ID =
    IMPOZITORIUM_CANONICAL_APPLICATION_SEMANTICS_BASELINE_V1_01

DOCUMENT_CLASS =
    SEMANTIC_GOVERNANCE_BASELINE_CANDIDATE
    NOT_IMPLEMENTATION_AUTHORIZATION

COMPANION_REGISTRY =
    impozitorium/whole_project_review/semantic_registry_v1.yaml

REVIEW_SOURCE =
    Raymond-1968/Imposition_app-review-mirror (read-only)

CANONICAL_REPOSITORY_ACCESSED =
    NO

STATUS =
    PENDING_HUMAN_AND_COORDINATOR_REVIEW
```

---

## Revision note — Bounded Correction 01

```text
CORRECTION_SCOPE =
    Framebox semantics                                   (§9, GEOMETRY.FRAMEBOX)
    frame intent separation                              (§9, GEOMETRY.FRAME_INTENT)
    layout_box -> Framebox relationship                  (§9.2)
    future contour relationship                          (§9, GEOMETRY.PRODUCTION_CONTOUR)
    Platform Geometry Core naming/ownership              (§9, §18, §20 R13, §21)
    clip-region clarification                            (§9, GEOMETRY.CLIP_REGION)
    trim-mark / crop-mark deprecation rollback           (§5 K-16, §13, §19)

ARCHITECTURAL_RECOMMENDATIONS_ADDED = NONE
NEW_ARTIFACTS = NONE
```

Registry effect: `GEOMETRY.OPERATOR_FRAME_INTENT` is replaced by two
entries, `GEOMETRY.FRAMEBOX` and `GEOMETRY.FRAME_INTENT` (158 → 159 entries).
`PLATFORM.GEOMETRY_CORE` changes from NEEDS_HUMAN_DECISION to CANONICAL_V1
(display name "Platform Geometry Core"). `TECHNICAL_OBJECT.TRIM_MARK` changes
from PROVISIONAL to NEEDS_STANDARD_REVIEW, and "crop mark" is no longer a
deprecated alias.

## Revision note — Standards Mapping Pass 01

```text
SCOPE         = geometry, imposition, placement, sheet/surface, technical marks,
                finished-product geometry (see section "Standards Mapping —
                Geometry and Imposition Pass 01", after §16)
NEW_ENTRIES   = 10   (159 → 169)
RENAMES       = NONE
NEW_DEPRECATED_ALIASES = PlacedInstance, SheetComposition (both resolve to CIP4-based entries)
NEW_AMBIGUOUS_TERMS    = CTM, content object   ("layout" extended)
ACCESS_LIMITATION = iso.org, pdfa.org and cip4.org were not reachable from this
                    environment (egress policy); CIP4 and ISO evidence comes from
                    search-result summaries of the cited documents.
```

---

## 1. Purpose and authority

The whole-project review found that Impozitorium has no single canonical
vocabulary. The clearest symptom is **"Page Geometry"**. It already names a
module (`doc/page_geometry_module_charter.md`). It is also used for that
module's backend "engine" (`doc/size_and_crop_module_intent.md`), for the
`PageGeometry` value object in code, and, in reviews `02` and `04`, for the
platform geometry ownership domain. Architectural Decision 03 is paused on
this.

This baseline:

- inventories the language the project actually uses (§4);
- records material collisions (§5);
- fixes a namespace model and semantic classes (§6, §7);
- registers 159 concepts with explicit status (`semantic_registry_v1.yaml`);
- separates what can be canonized now from what needs Human decision or
  standard review (§18).

**Authority.** This document is a baseline *candidate*. It acquires
authority only through Human acceptance. It renames no code, no class, no
GUI label and no file. Existing code identifiers stay as they are and are
mapped to canonical identities through aliases.

---

## 2. Method and evidence basis

1. **Inventory (Pass A).** Counted 82 search terms across five branches of
   the review mirror: OW-line tip, EN-line tip, OC-line, Booklet Folding
   Lab, Vector AutoBleed Lab. Read the defining documents and code for each
   high-traffic or ambiguous term.
2. **Collision audit (Pass B).** Every term with more than one observed
   meaning, or more than one name for one meaning, was traced to evidence
   (§5).
3. **Classification and namespaces (Passes C, D).**
4. **Standards alignment (Pass E).** Bounded external verification (§16).
   Normative standard texts (ISO 32000-2, ISO 15930, ISO 19593-1, ICC,
   CIP4 JDF/XJDF) were **not** accessed; alignment is stated only to the
   level the sources support.
5. **Registry.** The registry was generated from one source of truth and
   validated for: unique `canonical_id`; unique name within a namespace; no
   alias resolving to two entries (case-insensitive); no ambiguous bare term
   registered as a resolvable alias; no dangling references; every entry
   carrying an explicit status and source basis. Two generations produced
   byte-identical output (deterministic).

Inputs: `01`–`04` in this workspace (not modified), the review mirror, and
the external sources listed in the registry `sources` section.

---

## 3. Semantic source priority

Applied as accepted in `04 §11`:

```text
1. APPLICABLE INTERNATIONAL / INDUSTRY STANDARD
2. ESTABLISHED PRODUCTION-DOMAIN TERMINOLOGY
3. EXISTING HUMAN-ACCEPTED IMPOZITORIUM TERMINOLOGY
4. NEW IMPOZITORIUM EXTENSION (only where nothing adequate exists)
```

Repository usage is **evidence of usage, not canonicity**. Examples:
`normalize_boxes` is frequent but encodes legacy behavior, so it is registered
as `LEGACY`. `PageGeometry` is a class name, but the concept it carries needs a
non-colliding canonical name.

---

## 4. Semantic inventory summary

Approximate occurrence counts in `*.py` and `*.md` (case-insensitive; OW-line
tip ≈ EN-line tip unless noted). They show where language load sits, not
correctness.

| Family | Term (count, OW / EN) | Observation |
|---|---|---|
| PDF boxes | TrimBox 1988/1959, MediaBox 1654/1563, BleedBox 857/818, CropBox 593/584, ArtBox 371/267 | standard terms, heavily used |
| Geometry | Page Geometry 1625/1849, PageGeometry 781/1087, layout_box 923/835, canvas 391/379, bbox 221/241, clip* 131/218, working/object/production geometry ≤ 53 | "Page Geometry" dominates and is overloaded |
| Geometry | Framebox / FrameBox / frame box **0** on every branch | product concept not yet in repository |
| Geometry | content extent **0** | not used |
| Transform verbs | normaliz* 1826/1891, repair 1227/1140, reconstruct 1209/528, promot* 1755/2879, sanitiz* 110/113, postflight 35/107 | several meanings each (§5) |
| Artifacts | artifact 19729/19412, candidate 14940/14081, Save As 2170/2293, Working Document 1822/1898, Preview Result 952/978, Generated Result 349/445, Source PDF 675/689 | lifecycle words well established |
| Runtime/governance | evidence 20571/15863, action 13592/11900, acceptance 9874/8040, operation 8275/5973, manifest 8246/8329, Job 5811/782, Controller 3972/96, receipt 3668/3908, publication 3035/472, admission 2477/8, incident 2148/9, WorkUnit 918/0, admissib* 75/102 | OW-line counts are dominated by File Factory text |
| Production | Step & Repeat 5332, imposition 2056, PreCollate 1322, creep 968, lap 375, N-up 225, Cut Stack 185, Size & Crop 44 | |
| Technical objects | cut mark 991, trim mark 95, fold mark 78, registration mark 67, crop mark 63, finishing contour 47, slug 30, plotter 4; collating mark / service text / signature label 0 on main lines, present only in Booklet Folding Lab | mark vocabulary fragmented |
| Standards | OCG 507/532, ICC 317/18, OCMD 12/26, OutputIntent 4/1, JDF/XJDF 0, ISO 19593 0 (1 in Booklet lab) | standards language mostly absent beyond PDF/OC |
| Dev infrastructure | Operator Workplace 134/0, Kandev, WorkUnit, D01 | OW-line only |

Additional significant terms discovered: *Size & Crop*, *target canvas*,
*generated result profile*, *verification profile*, *Gate* (PDFium Gate A–D,
Compatibility Gate, HumanGate), *Stage* (Operator Workplace Stage 5, Page
Geometry Stage 8, Stage 2C), *D1/D2/D01/D-01*, *signature* (folded section vs
technical job signature), *chunk*, *PreCollate*, *known bad / unknown bad*,
*salvage mode*.

`SEMANTIC_TERMS_INVENTORIED = 82 searched terms` (plus the 13 discovered terms
listed above).

---

## 5. Collision audit

Status: **C** = `CANONICALIZABLE_NOW`, **A** = `NEEDS_ARCHITECTURAL_DECISION`,
**S** = `NEEDS_STANDARD_REVIEW`. The registry's `ambiguous_terms` section
lists the bare words below that must always be qualified.

| # | Term | Meaning A | Meaning B (and more) | Evidence | Risk | Status |
|---|---|---|---|---|---|---|
| K-01 | Page Geometry | module (charter) | module's "engine" (Size & Crop intent); `PageGeometry` value object; platform geometry domain (`02`, `04 §14, §20`) | charter, size_and_crop intent, `engine_neutral_geometry.py`, `04` | Decision 03 cannot be stated unambiguously | C (`MODULE.PAGE_GEOMETRY` vs `PLATFORM.GEOMETRY_CORE` "Platform Geometry Core") |
| K-02 | Size & Crop vs Page Geometry | operator-facing module | label of the Page Geometry module? | `size_and_crop_module_intent.md`, index rows | duplicate module identity | **A** |
| K-03 | Job | File Factory JobKind | product Job (design); "job signature" | `canonical_core/types.py`, `04 §17` | dev-infra semantics leak into product | C |
| K-04 | Operator Workplace | development orchestrator workplace | prepress operator GUI | Orchestrator contract, prompt usage | wrong system addressed | C (devinfra keeps it; product name pending) |
| K-05 | acceptance | Human acceptance | working-document (artifact) acceptance; operator-accepted deviation | Agent Hierarchy, `working_document_acceptance.py`, `04 §5` | governance vs runtime confusion | C |
| K-06 | admission | artifact admission (`04`) | File Factory review admission | `04 §13`, `review_context_admission.py` | same | C |
| K-07 | admissibility vs admission | production judgment | lifecycle decision | `04 §5`, `04 §13` | conflated outcomes | C |
| K-08 | publication / publish | Git/repository publication | artifact promotion; Save As | Agent Hierarchy, PFM | false belief that output is "published" | C |
| K-09 | promotion | PFM filesystem promotion | lab-to-platform promotion | PFM, `02 §16` | | C |
| K-10 | commit | Git commit | Generated Result Commit; receipt commit (Transaction A) | PFM, File Factory | | C |
| K-11 | OC | Optional Content | OC-6B*/6D* File Management lifecycle milestones | `01 C-16` | scope confusion | C |
| K-12 | D1 / D01 / D-01 / D2 | engine decision D-01 | D01 kernel driver; OC-6D1 step; PDFium Gate D sub-step D2 | EN decisions, OW driver, EN index, OW commits | wrong document/branch | C (always prefix) |
| K-13 | normalize | `normalize_boxes` GUI zeroing | rotation normalization; "Normalize-to-Zero" note; `normalizer/` direction; Page Geometry "canvas geometry normalization" | `core.py`, `rotation_normalizer.py`, readme notes, charter | hides legacy drift; vague operation class | C |
| K-14 | crop | CropBox | content crop in Size & Crop / `SourceCropSpec`; "crop marks" | standards, PG transform, marks | CropBox mistaken for finishing | C |
| K-15 | trim | TrimBox | Manual Trim module; trimming; trim marks | | Manual Trim edits more than TrimBox | C |
| K-16 | cut / crop / trim mark | cut-mark registry umbrella | domain synonyms crop/trim mark; JDF CutMark | `cut_mark_profile_registry.py`, domain | several names; whether trim mark and crop mark are one object is itself unverified | **S** (trim/crop relationship; no deprecation) |
| K-17 | signature | folded section (booklet) | technical job signature label | Booklet lab, `signature_profile_registry` | severe in booklet + label work | C |
| K-18 | profile | ICC profile | generated-result, verification, policy, cut-mark, signature profile | ICC, EN registry, registries | | C |
| K-19 | layout | layout box / layout space | Step & Repeat `layout` dict; JDF Layout; Qt layouts | `page_geometry.py`, `step_repeat/backend/engine.py` | | C |
| K-20 | canvas | Page Geometry target canvas | GUI preview canvas; imposed sheet | `TargetCanvasSpec`, VAB `preview_canvas.py` | | C |
| K-21 | candidate | artifact candidate | governance candidate (local candidate, blueprint candidate, Kandev candidate) | PFM, governance records | | C |
| K-22 | Preview Result / Generated Result / candidate | three lifecycle words | possibly one concept at two stages | legacy GUI vs EN PFM | lifecycle model split | **A** |
| K-23 | review | governance independent review | File Factory REVIEW job; operation verification | | | C |
| K-24 | Gate | HumanGate | PDFium Gate A–D; Compatibility Gate; Rotation Compatibility Gate | | | C (always qualify) |
| K-25 | Stage | Operator Workplace Stage 5 | Page Geometry Stage 7/8; Stage 2C | | | C (always qualify) |
| K-26 | evidence | governance evidence package | File Factory EvidenceKind; operation provenance | | | C |
| K-27 | bounding box / BBox | PDF form XObject BBox (standard) | computed content bounds | ISO 32000 XObject, analysis | standard key misread | C |
| K-28 | Framebox / frame intent | platform working frame (`GEOMETRY.FRAMEBOX`) | operator/machine intent to change it (`GEOMETRY.FRAME_INTENT`); spelling "FrameBox" imitates PDF box keys | human task | intent mistaken for the frame; platform term read as a standard box | C (concepts) / A (materialization) |
| K-29 | slug | vendor "slug area" usage | lab "page-number slugs" | Booklet lab | vendor term as platform term | C |
| K-30 | layout box basis (legacy) | TrimBox → ArtBox → CropBox → MediaBox | `core.normalize_boxes` TrimBox → BleedBox → MediaBox | `01 C-04` | legacy term still active | C (registered `LEGACY`) |
| K-31 | action | operator UI action | D-05 filesystem action; product "Action" (Jobs) | button language doc, D-05 | | C |
| K-32 | command | operation request (`*Command` classes) | File Factory transition commands | PG transform, `transitions.py` | | C |
| K-33 | receipt | PFM verification receipt | File Factory review-context receipt | | | C |
| K-34 | bleed | BleedBox | bleed region; bleed amount | standards, VAB | | C |
| K-35 | CTM | PDF graphics-state CTM (`PDF.CTM`) | CIP4 PlacedObject CTM attribute (`GEOMETRY.PLACEMENT_TRANSFORM`); generic affine maths | ISO 32000, CIP4 Layout ICS | placement maths mistaken for content-stream maths | C (always qualify) |
| K-36 | Layout (CIP4) vs layout box | CIP4 Layout resource (`PRODUCTION.IMPOSITION_LAYOUT`) | `GEOMETRY.LAYOUT_BOX` / layout space | CIP4 Layout ICS | imposition layout confused with page layout basis | C ("layout" extended) |
| K-37 | ContentObject / content object | CIP4 ContentObject = one placement (`PRODUCTION.PLACED_CONTENT`) | source-level production object (`PRODUCTION.PRODUCTION_OBJECT`) | CIP4 Layout ICS | placement instance mistaken for the product | C |
| K-38 | TrimSize / TrimCTM vs TrimBox | placement-level finished-trim rectangle of a ContentObject | PDF page TrimBox; platform Framebox | CIP4 examples | three "trim" rectangles at different levels | **S** |
| K-39 | ClipBox vs CropBox vs clip region | CIP4 ClipBox (placement clip) | PDF CropBox; `GEOMETRY.CLIP_REGION` | CIP4, PJTF, ISO 32000 | clip semantics conflated | C |

`COLLISIONS_IDENTIFIED = 39` (34 + 5 from Standards Mapping Pass 01). Of
these, 35 are canonicalizable now, 2 need an architectural decision (K-02,
K-22) and 2 need standard review (K-16, K-38). The
materialization part of K-28 also needs a decision. Standard review is also
flagged inside several entries rather than as a collision status (§16).

---

## 6. Canonical namespace model

The candidate list was simplified:

- `OUTPUT` was dropped (Save As is a `UI` action producing an `ARTIFACT`).
- `GIT` was folded into `GOVERNANCE`.
- `PLATFORM` (services), `ARCHITECTURE` (meta-vocabulary) and `UI` (human
  labels) were added, because the review needs to say "module X uses platform
  service Y" without overloading nouns.

| Namespace | Holds | Must never hold |
|---|---|---|
| `PDF.*` | standard PDF structures (boxes, /Rotate, OC, OutputIntent, XObject) | platform interpretations |
| `GEOMETRY.*` | platform geometry semantics derived from PDF facts | module names |
| `PLATFORM.*` | platform services/cores (structural PDF core, geometry core, render service, file management) | modules |
| `ARCHITECTURE.*` | meta-vocabulary (module, platform service, algorithm, domain model) | runtime objects |
| `MODULE.*` | operator-facing modules and labs | platform layers |
| `OPERATION.*` | operations, Operation Record, kinds, requests, results, operation classes | Jobs, UI actions |
| `ARTIFACT.*` | artifact lifecycle (source, working document, candidate, receipt, promotion, final output) | governance publication |
| `PRODUCTION.*` | print-production domain (intent, imposition, signature, creep, admissibility) | dev infrastructure |
| `TECHNICAL_OBJECT.*` | marks, service text, labels, contour lines | product content |
| `DIAGNOSTIC.*` | observation codes and severity | admissibility decisions |
| `POLICY.*` | policies and policy profiles | standard PDF objects |
| `UI.*` | human-facing interaction vocabulary | machine identities of operations |
| `GOVERNANCE.*` | Human acceptance, HumanGate, review, repository publication, milestone labels | product runtime |
| `DEVINFRA.*` | File Factory, Orchestrator Operator Workplace, Kandev, D01 | product runtime |

`NAMESPACES_DEFINED = 14`.

Machine identity format: `NAMESPACE.CONCEPT[.SUBCONCEPT]` in upper snake case.
Human labels stay short and may repeat across namespaces. Example: the label
"Page Geometry" is shown only for `MODULE.PAGE_GEOMETRY`, while the platform
concept is `PLATFORM.GEOMETRY_CORE`.

---

## 7. Canonical semantic classes

Every entry has exactly one primary class:

`STANDARD_TERM`, `PLATFORM_TERM`, `PRODUCTION_DOMAIN_TERM`, `MODULE_NAME`,
`OPERATION_KIND`, `STATE`, `DIAGNOSTIC_TERM`, `POLICY_TERM`,
`GOVERNANCE_TERM`, `DEVELOPMENT_INFRASTRUCTURE_TERM`, `LEGACY_TERM`,
`PROVISIONAL_TERM`.

`ARTIFACT_KIND` is expressed as `PLATFORM_TERM` inside `ARTIFACT.*`. A
separate artifact-kind registry is premature until the Operation Record
exists. *Class* (what kind of word) is independent from *status* (how settled
the word is).

---

## 8. PDF / structural terminology

| canonical_id | Name | Alignment | Status |
|---|---|---|---|
| `PDF.BOX.MEDIA` / `CROP` / `BLEED` / `TRIM` / `ART` | MediaBox … ArtBox | `STANDARD_ALIGNED` (wording to confirm against ISO 32000-2) | CANONICAL_V1 |
| `PDF.BOX.EFFECTIVE_VALUE` | effective page box value (raw / inherited / effective) | needs ISO default rules | NEEDS_STANDARD_REVIEW |
| `PDF.PAGE_ROTATE` | page `/Rotate` | standard | CANONICAL_V1 |
| `PDF.USER_UNIT`, `PDF.MEDIABOX_ORIGIN` | | standard / standard + platform specialization | CANONICAL_V1 |
| `PDF.OPTIONAL_CONTENT`, `…_GROUP` (OCG), `…_MEMBERSHIP` (OCMD) | | standard | CANONICAL_V1 |
| `PDF.PROCESSING_STEPS` | ISO 19593-1 processing steps | standard identified, text not reviewed | NEEDS_STANDARD_REVIEW |
| `PDF.OUTPUT_INTENT`, `PDF.ICC_PROFILE` | | standard (iccMAX not reviewed) | CANONICAL_V1 |
| `PDF.PDFX_CONFORMANCE` | PDF/X | standard family identified | NEEDS_STANDARD_REVIEW |
| `PDF.FORM_XOBJECT`, `PDF.XOBJECT_BBOX`, `PDF.PAGE` | | standard | CANONICAL_V1 |

Rules: library defaults (PyMuPDF, pikepdf) are **not** the standard. Bare
"OC" is not an abbreviation of Optional Content in canonical text (K-11).

---

## 9. Geometry terminology

This section resolves the semantic part of Decision 03's blocker. It does
not decide ownership design.

### 9.1 The eight required distinctions

| Concept | canonical_id | Class | Status | Is | Is not |
|---|---|---|---|---|---|
| **module Page Geometry** | `MODULE.PAGE_GEOMETRY` | MODULE_NAME | CANONICAL_V1 | the existing production transform module (page size, crop-or-pad, scaling, output boxes) | the platform geometry layer; the value object |
| **Platform Geometry Core** | `PLATFORM.GEOMETRY_CORE` | PLATFORM_TERM | CANONICAL_V1 | platform-owned owner of generic geometry semantics: layout box policy result, Framebox, coordinate spaces, absolute ↔ working-frame transforms, orientation semantics, working geometry descriptors, geometry diagnostics, normalization semantics | "Page Geometry"; `PLATFORM.STRUCTURAL_PDF_CORE` (raw PDF structure, bounded structural mutation) |
| **PDF TrimBox** | `PDF.BOX.TRIM` | STANDARD_TERM | CANONICAL_V1 | standard PDF fact: finished-page boundary | the layout box (only its first candidate); the Framebox |
| **layout_box** | `GEOMETRY.LAYOUT_BOX` | PLATFORM_TERM | CANONICAL_V1 | source-derived canonical layout basis chosen by TrimBox → ArtBox → CropBox → MediaBox | TrimBox; Framebox; frame intent |
| **Framebox** | `GEOMETRY.FRAMEBOX` | PLATFORM_TERM | CANONICAL_V1 | platform-owned, internal, rectangular working / reference frame of the production object | a PDF box; the layout box; frame intent; a clip region; a production contour |
| **frame intent** | `GEOMETRY.FRAME_INTENT` | PLATFORM_TERM | CANONICAL_V1 | explicit operator or machine-proposed intent to establish or modify the Framebox | the Framebox itself |
| **operation-specific construction geometry** | `GEOMETRY.CLIP_REGION` | PLATFORM_TERM | CANONICAL_V1 | construction / clipping geometry used by a particular algorithm (e.g. Step & Repeat clip, Vector AutoBleed mirror clips) | a product frame; CropBox; Framebox |
| **future contour-capable physical-object geometry** | `GEOMETRY.PRODUCTION_CONTOUR` | PLATFORM_TERM | PROVISIONAL | non-rectangular outline of the finished object | Framebox; layout box; a drawn finishing line (`TECHNICAL_OBJECT.FINISHING_CONTOUR`) |

A Framebox may **coincide geometrically** with a PDF box, the layout box, a
clip region or the bounding rectangle of a contour in a given case. It is
never **semantically identical** to any of them.

### 9.2 Relationships

```text
PDF STRUCTURAL FACTS                      (PLATFORM.STRUCTURAL_PDF_CORE)
  PDF.BOX.{MEDIA,CROP,BLEED,TRIM,ART} + effective values + /Rotate + UserUnit + MediaBox origin
        │
        ▼  POLICY.LAYOUT_BOX_PRIORITY   (TrimBox → ArtBox → CropBox → MediaBox)
GEOMETRY.LAYOUT_BOX                       source-derived canonical layout basis
        │
        ▼  platform interpretation / normalization   (PLATFORM.GEOMETRY_CORE)
GEOMETRY.FRAMEBOX                         platform working frame (initially derived from the layout box)
        ▲
        │ establishes / modifies (platform-approved semantics only)
OPERATION.KIND.DEFINE_FRAMEBOX (provisional)
        ▲
        │ consumes
GEOMETRY.FRAME_INTENT                     operator or machine-proposed intent

GEOMETRY.FRAMEBOX ──► POLICY.FRAME_MATERIALIZATION ──► PDF page boxes / other explicit representation
                      (NOT_DECIDED)

GEOMETRY.LAYOUT_SPACE       : [0,0,w,h] GUI-facing space anchored on the layout box; whether it
                              follows the Framebox after an explicit frame operation is NOT_DECIDED
GEOMETRY.PLACEMENT_OBJECT_EXTENT : W_obj = layout.width, H_obj = layout.height (product law)
GEOMETRY.GAP                : distance between neighbouring layout boxes (product law)
GEOMETRY.CLIP_REGION        : construction / clipping geometry of one algorithm; never a frame,
                              never CropBox, never exported as product geometry (key for VAB)
GEOMETRY.PRODUCTION_CONTOUR : future physical-object outline; in contour/nesting workflows it
                              defines the product shape while the Framebox remains the rectangular
                              reference / bounding / placement frame; for rectangular workflows the
                              Framebox may suffice. Framebox is NOT made obsolete by contours.
GEOMETRY.BLEED_REGION       : product domain; relates to PDF.BOX.BLEED and PRODUCTION.BLEED_AMOUNT
GEOMETRY.CONTENT_BOUNDS     : analysis result (provisional); ≠ ArtBox, ≠ XObject BBox
GEOMETRY.LEGACY_LAYOUT_ZEROING (core.normalize_boxes) : LEGACY drift, not policy
```

Hard rule: **downstream modules must not choose between multiple hidden
frame sources.** They consume one canonical platform working frame and
geometry result (`GEOMETRY.PAGE_GEOMETRY_DESCRIPTOR`, code name
`PageGeometry`, which carries both the layout box and the Framebox). Frame
intent changes the Framebox only through the platform-approved operation path.

Ownership law: **no module owns generic PDF / geometry semantics.** Modules
consume `PLATFORM.GEOMETRY_CORE` and `PLATFORM.STRUCTURAL_PDF_CORE` services
and own only their operation-specific semantics (e.g. their clip regions).

### 9.3 Safe to canonize now

layout box, layout box priority, layout space and coordinate spaces (engine-neutral
contract), PDF boxes, Framebox, frame intent, clip region, bleed region,
placement object extent, gap, module Page Geometry, Platform Geometry Core.

### 9.4 Provisional or open

- Name of `GEOMETRY.PAGE_GEOMETRY_DESCRIPTOR`. The code class `PageGeometry`
  stays; the canonical name avoids the module collision.
- The spelling **FrameBox is deprecated** (it imitates PDF page-box keys);
  the canonical name is *Framebox*.
- `POLICY.FRAME_MATERIALIZATION` = NOT_DECIDED.
- Whether `GEOMETRY.LAYOUT_SPACE` follows the Framebox once they diverge =
  NOT_DECIDED (Decision 03 design).
- Content bounds, page orientation, production contour (architecture not
  finalized).

---

## 10. Artifact lifecycle terminology

`ARTIFACT.SOURCE_PDF` → `ARTIFACT.CANDIDATE` → `OPERATION.VERIFICATION` →
`ARTIFACT.VERIFICATION_RECEIPT` → `ARTIFACT.GENERATED_RESULT_COMMIT` →
`ARTIFACT.MANAGED_STAGING` → `ARTIFACT.PROMOTION` → `ARTIFACT.ADMISSION`
(candidate becomes current) → `ARTIFACT.CURRENT_POINTER` /
`ARTIFACT.WORKING_DOCUMENT` → `UI.SAVE_AS` → `ARTIFACT.FINAL_OUTPUT`.

`ARTIFACT.PREVIEW_RESULT` is canonical for the inspection artifact. Whether
*Generated Result* is the same concept as *candidate* is
`NEEDS_HUMAN_DECISION` (K-22).

Disambiguations (from `04 §13`, refined):

```text
GOVERNANCE.HUMAN_ACCEPTANCE   ≠ ARTIFACT.ADMISSION ≠ PRODUCTION.ADMISSIBILITY_OUTCOME
GOVERNANCE.REPOSITORY_PUBLICATION (alias GIT.PUBLICATION) ≠ ARTIFACT.PROMOTION ≠ UI.SAVE_AS (alias OUTPUT.SAVE_AS)
GOVERNANCE.REPOSITORY_COMMIT  ≠ ARTIFACT.GENERATED_RESULT_COMMIT
```

`04` proposed `PRODUCTION.ADMISSIBILITY`; it is registered as
`PRODUCTION.ADMISSIBILITY_OUTCOME` with alias "admissibility".
`OUTPUT.SAVE_AS` and `GIT.PUBLICATION` are kept as aliases of `UI.SAVE_AS`
and `GOVERNANCE.REPOSITORY_PUBLICATION`.

---

## 11. Operations / actions / commands terminology

| canonical_id | Meaning |
|---|---|
| `OPERATION.OPERATION` | bounded production transformation/analysis over explicit artifacts |
| `OPERATION.OPERATION_RECORD` | minimal runtime execution fact (`04 §3–4`) |
| `OPERATION.OPERATION_KIND` | registered kind + version |
| `OPERATION.REQUEST` / `OPERATION.RESULT` | typed input / outcome (module `*Command` classes are requests) |
| `OPERATION.VERIFICATION` | post-operation byte/structure check (alias *postflight*) |
| `OPERATION.PROVENANCE` | execution identity, timestamps, environment |
| `OPERATION.GENERATED_RESULT_PROFILE` | per-kind writer/verification/manifest declaration (provisional; expected to fold into the kind registry) |
| `OPERATION.CLASS.{REPAIR, TRANSFORM, SANITIZE, NORMALIZE}` | operation classes (provisional) separating "repair imperfect input" from "change the product" |
| `OPERATION.KIND.MANUAL_TRIM`, `…PAGE_GEOMETRY_TRANSFORM`, `…ROTATION_NORMALIZATION` | canonical kinds |
| `OPERATION.KIND.DEFINE_FRAMEBOX`, `…MIRROR_BLEED` | provisional kinds |
| `UI.ACTION` | human-facing interaction that may request an operation |
| `ARTIFACT.FILESYSTEM_ACTION` | D-05 takeover unit |

The generated-result profile id `PAGE_GEOMETRY` maps to
`OPERATION.KIND.PAGE_GEOMETRY_TRANSFORM`, not to a module or a platform layer.

---

## 12. Production-module terminology

Modules (`MODULE.*`) own **only** their domain-specific semantics. Canonical
sentence pattern, now expressible without overloaded nouns:

> `MODULE.VECTOR_AUTOBLEED` performs `OPERATION.KIND.MIRROR_BLEED`, uses
> `PLATFORM.GEOMETRY_CORE` semantics (`GEOMETRY.LAYOUT_BOX`,
> `GEOMETRY.BLEED_REGION`) and `PLATFORM.STRUCTURAL_PDF_CORE` services, and
> owns only its bleed-specific `ARCHITECTURE.ALGORITHM` (mirror construction).

Registered modules: Preflight, Manual Trim, Page Geometry, Size & Crop
(relation pending), Step & Repeat, Create Booklet (provisional), Booklet
Folding Lab, Vector AutoBleed, N-up with Background (provisional), Cut Stack
(provisional). Imposition *strategies* (`PRODUCTION.N_UP_IMPOSITION`) are
distinct from the *modules* that offer them.

Production-domain terms: production intent (aligned conceptually with JDF/XJDF
*Intent*; needs standard review), production job (provisional; bare "Job"
must be qualified), finished size, finished page, bleed amount, margin,
trimming, imposition, signature (folded section), folding scheme
(provisional), creep, creep compensation (alias *shingling*), lap shift
(provisional), sheet orientation, physical qualification required
(provisional), admissibility outcome, operator-accepted deviation, salvage
mode (provisional).

---

## 13. Technical-object terminology

| canonical_id | Name | Status | Note |
|---|---|---|---|
| `TECHNICAL_OBJECT.TECHNICAL_OBJECT` | technical object | CANONICAL_V1 | exact PDF representation NOT_DECIDED (OCG / ISO 19593 strong candidates) |
| `…CUT_MARK` | cut mark (umbrella of cutting marks) | CANONICAL_V1 | matches the accepted cut-mark profile registry |
| `…TRIM_MARK` | trim mark (alias *product trim mark*) | NEEDS_STANDARD_REVIEW | TRIM_MARK / CROP_MARK relationship needs standards/domain review (possibly Human decision). "crop mark" is **not** deprecated: it is established professional usage, and the CropBox collision alone is not a reason to deprecate it |
| `…CHUNK_BOUNDARY_MARK` | chunk-boundary corner mark | CANONICAL_V1 | registry family |
| `…FOLD_MARK`, `…REGISTRATION_MARK` | | CANONICAL_V1 | established domain; JDF mentions fold and register marks |
| `…COLLATING_MARK` | collating mark (staircase) | CANONICAL_V1 | standard alignment unverified |
| `…FOLD_CROSSHAIR`, `…SERVICE_TEXT`, `…TECHNICAL_NUMBERING`, `…CONTOUR_REGISTRATION_MARK` | | PROVISIONAL | lab-originated |
| `…TECHNICAL_JOB_SIGNATURE` | technical job signature | CANONICAL_V1 | **not** a folded signature |
| `…FINISHING_CONTOUR` | finishing contour line | NEEDS_STANDARD_REVIEW | drawn line ≠ `GEOMETRY.PRODUCTION_CONTOUR` |
| `…CUT_MARK_PROFILE` | cut-mark profile | CANONICAL_V1 | ≠ ICC profile |

---

## 14. Governance vs product-runtime terminology

Rule: **governance and dev-infrastructure words never silently become
product-runtime words.** Product code and Operation Records use only
`ARTIFACT.*`, `OPERATION.*`, `PRODUCTION.*`, `POLICY.*`, `DIAGNOSTIC.*`,
`UI.*`, `GEOMETRY.*`, `PDF.*` and `TECHNICAL_OBJECT.*`.

| Word | Governance | Product runtime | Dev infrastructure |
|---|---|---|---|
| acceptance | `GOVERNANCE.HUMAN_ACCEPTANCE` | `ARTIFACT.ADMISSION`, `PRODUCTION.OPERATOR_ACCEPTED_DEVIATION` | — |
| admission | — | `ARTIFACT.ADMISSION` | `DEVINFRA.REVIEW_ADMISSION` |
| admissibility | — | `PRODUCTION.ADMISSIBILITY_OUTCOME` | — |
| publication | `GOVERNANCE.REPOSITORY_PUBLICATION` | (none; use promotion / Save As) | — |
| promotion | `GOVERNANCE.LAB_PROMOTION` | `ARTIFACT.PROMOTION` | — |
| commit | `GOVERNANCE.REPOSITORY_COMMIT` | `ARTIFACT.GENERATED_RESULT_COMMIT` | receipt commit (within `DEVINFRA.REVIEW_CONTEXT_RECEIPT`) |
| Job | — | `PRODUCTION.JOB` (provisional) | `DEVINFRA.FILE_FACTORY_JOB` |
| operation | — | `OPERATION.OPERATION` | `DEVINFRA.DURABLE_OPERATION` |
| action | — | `UI.ACTION`, `ARTIFACT.FILESYSTEM_ACTION` | — |
| review | `GOVERNANCE.INDEPENDENT_REVIEW` | `OPERATION.VERIFICATION` | REVIEW job kind |
| authority | Human authority (HumanGate) | none in product runtime V1 | `DEVINFRA.AUTHORITY_UNIT` |
| evidence | `GOVERNANCE.EVIDENCE_PACKAGE` | `OPERATION.PROVENANCE` | `DEVINFRA.EVIDENCE_KIND` |
| candidate | `GOVERNANCE.CANDIDATE_RECORD` | `ARTIFACT.CANDIDATE` | Kandev successor candidate |

Milestone labels (`OC-n`, `D-0n`, `Gate`, `Stage`) are `GOVERNANCE`
identifiers and are always written with their prefix: `DECISION D-01`,
`OC-6D1`, `PDFIUM_GATE_D.D2`, `OPERATOR_WORKPLACE_STAGE_5`,
`PAGE_GEOMETRY_STAGE_8`.

---

## 15. Development-infrastructure terminology

`DEVINFRA.*` holds: File Factory, File Factory job, WorkUnit, Controller,
authority unit, review admission, review-context receipt, incident, evidence
kind, durable operation, transition command, Orchestrator Operator Workplace,
Kandev chassis, D01 kernel mediation (`LEGACY`).

"Operator Workplace" is reserved for `DEVINFRA.ORCHESTRATOR_OPERATOR_WORKPLACE`
and must always be written with *Orchestrator*. The prepress application is
`UI.PRODUCT_WORKBENCH` (provisional name; aliases *Preflight Shell*,
*product GUI*).

---

## 16. Standards-alignment register

Sources are recorded in the registry `sources` section. **No ISO clause
numbers are asserted.** Where a clause number appears, it is a third-party
citation, marked as such.

| Concept | Alignment | Basis | Limitation |
|---|---|---|---|
| Media/Crop/Bleed/Trim/ArtBox | STANDARD_ALIGNED | ISO 32000 page boundaries; definitions consistent across several independent PDF library references (setasign, GemBox) | normative text not accessed; default/inheritance rules NEEDS_STANDARD_REVIEW |
| Optional Content, OCG, OCMD | STANDARD_ALIGNED | ISO 32000 optional content | normative text not accessed |
| Processing steps | NEEDS_STANDARD_REVIEW | ISO 19593-1:2018 (title and OCG-based approach verified via PDF Association / ISO catalogue; groups such as Structural, Dimensions) | group semantics and key names not verified; relation to PDF 2.0 not verified |
| PDF/X | NEEDS_STANDARD_REVIEW | ISO 15930 family; secondary sources: MediaBox + TrimBox or ArtBox, BleedBox when bled, OutputIntent | normative text not accessed |
| OutputIntent / ICC profile | STANDARD_ALIGNED | PDF OutputIntent with destination ICC profile (Adobe, PDFlib) | iccMAX (ICC.2) not reviewed |
| Production intent, finished page, Layout/Signature, marks | NEEDS_STANDARD_REVIEW | CIP4 JDF/XJDF: intent vs production; XJDF LayoutIntent / ProductionIntent; JDF Layout SignatureName partition; MarkObject, RegisterMark | element semantics (CutMark, creep, fold catalog) not verified |
| creep, shingling, signature (folded), trim/crop marks, bleed | ESTABLISHED_DOMAIN_TERM | industry explanatory sources | not standards |
| lap shift, collating mark, contour registration mark, finishing contour | NEEDS_STANDARD_REVIEW | lab / domain usage | relation to "lip/overfold", JDF marks, ISO 19593 unverified |
| slug | vendor/application usage | — | not treated as standard |
| layout box, layout space, Framebox, frame intent, clip region, admissibility, Operation Record | IMPOZITORIUM_EXTENSION | derived from standard PDF boxes / accepted decisions | explicitly not standard terms |

Registry totals: STANDARD_ALIGNED 14, STANDARD_TERM_WITH_PLATFORM_SPECIALIZATION
5, ESTABLISHED_DOMAIN_TERM 19, NEEDS_STANDARD_REVIEW 20,
IMPOZITORIUM_EXTENSION 111.

---

## Standards Mapping — Geometry and Imposition Pass 01

**Sources and evidence strength.**

- **ISO 19593-1.** Reference edition per Human/Coordinator: **ISO
  19593-1:2026 (Edition 2)**, superseding 2018. What I could observe
  independently, from search summaries only: ISO's 2018 page says it will be
  replaced by ISO/PRF 19593-1; Edition 2 passed the DIS/FDIS stages; BSI
  lists BS ISO 19593-1 as published 2026-03-05 as an identical adoption. The
  ISO publication record itself could not be fetched (egress policy).
- **CIP4 JDF/XJDF.** JDF 1.4 *Layout Creator to Imposition ICS*, the CIP4
  Pagination Catalog and the *XJDF for Developers* presentation, all via
  search summaries. The XJDF 2.2 normative text was **not** accessed.
- **ISO 32000.** Normative text not accessed.

No normative wording or clause numbers are asserted. "SAME" below means
concept-level equivalence on the available evidence. Entries keep
`NEEDS_STANDARD_REVIEW` alignment wherever normative confirmation is
outstanding.

| Concept | IMPOZITORIUM_ID | ISO 32000 | ISO 19593-1 | JDF / XJDF | Domain | Relationship | Action |
|---|---|---|---|---|---|---|---|
| Framebox / working frame | `GEOMETRY.FRAMEBOX` | derived from page boxes; ≠ any box | — | ≠ TrimSize / TrimCTM (placement projection); ≠ FinishedDimensions (intent) | — | PLATFORM_EXTENSION | KEEP |
| layout_box | `GEOMETRY.LAYOUT_BOX` | derived from Trim/Art/Crop/MediaBox | — | none (≠ CIP4 Layout) | — | PLATFORM_EXTENSION | KEEP |
| finished size | `PRODUCTION.FINISHED_SIZE` | TrimBox = finished page dimensions | — | XJDF LayoutIntent FinishedDimensions (shape) | established | CLOSE_BUT_NOT_SAME | KEEP (relationship noted) |
| finished page | `PRODUCTION.FINISHED_PAGE` | ≠ PDF page | — | JDF finished page vs reader page | — | NEEDS_STANDARD_REVIEW | KEEP_PROVISIONAL (status NSR) |
| production object | `PRODUCTION.PRODUCTION_OBJECT` (new) | — | — | ≠ ContentObject (placement-level) | — | PLATFORM_EXTENSION | KEEP_PROVISIONAL |
| content object (placed) | `PRODUCTION.PLACED_CONTENT` (new) | — | — | ContentObject | — | SAME (concept) | MAP_TO_STANDARD_TERM |
| placed instance / placed object | `PRODUCTION.PLACED_OBJECT` (new) | — | — | PlacedObject (abstract: ContentObject or MarkObject) | — | SAME (concept) | MAP_TO_STANDARD_TERM; *PlacedInstance* deprecated → PLACED_CONTENT |
| placement transform / CTM | `GEOMETRY.PLACEMENT_TRANSFORM` (new) | ≠ graphics-state CTM | — | PlacedObject CTM | — | SPECIALIZATION (platform name, CIP4 representation) | ADD_STANDARD_ALIAS ("CIP4 CTM") |
| document transform | `GEOMETRY.DOCUMENT_TRANSFORM` (new) | — | — | none | — | PLATFORM_EXTENSION | KEEP |
| PDF CTM | `PDF.CTM` (new) | graphics-state CTM | — | — | — | SAME | MAP_TO_STANDARD_TERM |
| sheet | `PRODUCTION.SHEET` (new) | — | — | Sheet / SheetName partition | press sheet | SAME | MAP_TO_STANDARD_TERM |
| surface | `PRODUCTION.SURFACE` (new) | — | — | Side partition / Surface; SurfaceContentsBox | sheet side | SAME (concept) | MAP_TO_STANDARD_TERM |
| layout / sheet composition | `PRODUCTION.IMPOSITION_LAYOUT` (new) | — | — | Layout resource | imposition layout | SAME (concept) | MAP_TO_STANDARD_TERM; *SheetComposition* deprecated |
| sheet geometry | `GEOMETRY.SPACE.IMPOSED_SHEET` + `PRODUCTION.SHEET` | — | — | surface coordinates | — | covered | not introduced |
| clip region | `GEOMETRY.CLIP_REGION` | ≠ CropBox; clipping path is a PDF mechanism | — | ClipBox is a placement-level specialization (typically from TrimBox / BleedBox per PJTF) | — | SUPERSET | KEEP (relation noted, no alias) |
| ClipBox | → `GEOMETRY.CLIP_REGION` (note) | — | — | ContentObject ClipBox | — | SPECIALIZATION | no new ID |
| TrimSize / TrimCTM | → `PRODUCTION.PLACED_CONTENT` (note) | relates to TrimBox | — | ContentObject attributes | — | NEEDS_STANDARD_REVIEW | no new ID |
| production contour | `GEOMETRY.PRODUCTION_CONTOUR` | — | processing-step objects can *realize* it | cutting data not verified | die line | PLATFORM_EXTENSION | KEEP_PROVISIONAL |
| finishing contour | `TECHNICAL_OBJECT.FINISHING_CONTOUR` | — | Structural processing-step objects (e.g. Cutting, Creasing, Perforating; Ed. 2 list unverified) | — | die line | CLOSE_BUT_NOT_SAME | KEEP (NSR) |
| processing-step contour | → `PDF.PROCESSING_STEPS` (realization) | optional content | processing step | — | — | NEEDS_STANDARD_REVIEW | no new ID |
| technical object | `TECHNICAL_OBJECT.TECHNICAL_OBJECT` | — | processing-step objects = one realization | MarkObject = placement realization | marks, slugs, labels | SUPERSET | KEEP |
| mark object | `PRODUCTION.PLACED_MARK` (new) | — | — | MarkObject | — | SAME (concept) | MAP_TO_STANDARD_TERM |
| cut mark | `TECHNICAL_OBJECT.CUT_MARK` | — | — | "cut, fold, or register marks" (generic); CutMark element not confirmed | established | NEEDS_STANDARD_REVIEW | KEEP (alignment → NSR) |
| trim / crop mark | `TECHNICAL_OBJECT.TRIM_MARK` | — | — | not found | vendors mostly say "crop marks" | NEEDS_STANDARD_REVIEW | KEEP (NSR) |
| fold mark | `TECHNICAL_OBJECT.FOLD_MARK` | — | Folding processing step (different: finishing data, not a mark) | mentioned | established | SAME (domain) | KEEP |
| registration mark | `TECHNICAL_OBJECT.REGISTRATION_MARK` | — | — | RegisterMark (in MarkObject) | established | SAME | KEEP (alias RegisterMark exists) |
| signature | `PRODUCTION.SIGNATURE` | — | — | SignatureName partition; signature cells (Pagination Catalog) | folded section | CLOSE_BUT_NOT_SAME | KEEP (NSR) |
| imposition | `PRODUCTION.IMPOSITION` | — | — | placing pages and marks onto sheet surfaces | established | SAME | KEEP |
| bleed | `PRODUCTION.BLEED_AMOUNT` / `GEOMETRY.BLEED_REGION` / `PDF.BOX.BLEED` | BleedBox | — | StrippingParams per-edge bleed (reported) | established | CLOSE_BUT_NOT_SAME | KEEP |

**Special questions.**

- **PlacedInstance.** Not introduced. One placement of unchanged content is
  CIP4 **ContentObject** (`PRODUCTION.PLACED_CONTENT`). The umbrella of all
  placements, content and marks, is CIP4 **PlacedObject**
  (`PRODUCTION.PLACED_OBJECT`). *PlacedInstance* is kept only as a deprecated
  alias resolving to `PRODUCTION.PLACED_CONTENT`.
- **ContentObject vs production object.** Not the same concept. ContentObject
  is placement-level: one instance on one surface, with CTM, ClipBox, TrimCTM,
  TrimSize and Ord. The production object is source-level: Framebox, bleed
  semantics, optional contour and artifact identity. A distinct
  `PRODUCTION.PRODUCTION_OBJECT` (PROVISIONAL) is justified; a placed content
  is an *instance of* it.
- **Layout / Sheet / Surface.** Reuse the CIP4 concepts: `PRODUCTION.SHEET`,
  `PRODUCTION.SURFACE` (Side; SurfaceContentsBox noted) and
  `PRODUCTION.IMPOSITION_LAYOUT` (Layout). *SheetComposition* and
  *SheetGeometry* are **not** introduced. The only platform extension kept is
  the coordinate space `GEOMETRY.SPACE.IMPOSED_SHEET`.
- **Placement transform.** `GEOMETRY.PLACEMENT_TRANSFORM` changes only where
  an unchanged object is placed, and is represented in CIP4 by the
  PlacedObject **CTM**. `GEOMETRY.DOCUMENT_TRANSFORM` changes the canonical
  working artifact and has no CIP4 counterpart. The PDF graphics-state CTM
  (`PDF.CTM`) is a third, distinct concept. Generic affine maths stays
  engine-neutral and is not called "CTM".
- **Technical objects.** `TECHNICAL_OBJECT.TECHNICAL_OBJECT` remains the
  Impozitorium umbrella (a SUPERSET). JDF MarkObject (`PRODUCTION.PLACED_MARK`)
  is its *placement* realization; ISO 19593 processing-step objects are a
  *PDF* realization for finishing data. Neither is equivalent to the umbrella.
- **ProductionContour.** Retained as a PROVISIONAL platform abstraction for
  the physical-object outline. ISO 19593 processing-step objects (Structural
  group, e.g. Cutting) can *realize* it in PDF, but that is a representation,
  not the concept. No rename.
- **Framebox.** Remains an IMPOZITORIUM_EXTENSION; no equivalent industry
  term was demonstrated. Relations:
  - Framebox ↔ TrimBox: may be *derived from* it via the layout box; not
    equivalent.
  - Framebox ↔ finished size: *related* (platform working rectangle vs
    intended product size).
  - Framebox ↔ XJDF FinishedDimensions: *related*; not equivalent (intent
    level, shape value).
  - Framebox ↔ TrimSize / TrimCTM: *related*; a placed content's trim
    rectangle is a placement-level projection of a rectangular finished frame.

## 17. Canonical Registry V1 summary

```text
FILE                     = semantic_registry_v1.yaml
ENTRIES                  = 169
CANONICAL_V1             = 122
PROVISIONAL              = 32
NEEDS_STANDARD_REVIEW    = 7
NEEDS_HUMAN_DECISION     = 3
LEGACY                   = 5
DEPRECATED (entries)     = 0   (deprecation is expressed as deprecated_aliases: 6)
AMBIGUOUS_TERMS          = 31  (bare words that must be qualified; never resolvable)
NAMESPACES               = 14
SOURCES                  = 41
```

Entries per namespace: PDF 20, GEOMETRY 22, PRODUCTION 27, OPERATION 17,
DEVINFRA 14, TECHNICAL_OBJECT 14, ARTIFACT 13, GOVERNANCE 11, MODULE 10,
ARCHITECTURE 5, PLATFORM 5, DIAGNOSTIC 4, POLICY 4, UI 3.

Entry fields: `canonical_id, canonical_name, semantic_class, definition,
domain, source_basis, standard_alignment, aliases, deprecated_aliases,
not_equivalent_to, relationships, owner, status, notes?`.

---

## 18. Provisional / unresolved terms

**NEEDS_HUMAN_DECISION (3):**

| Entry | Question |
|---|---|
| `POLICY.FRAME_MATERIALIZATION` | how the Framebox is materialized into PDF page boxes or another explicit representation |
| `MODULE.SIZE_AND_CROP` | UI label of `MODULE.PAGE_GEOMETRY`, or a separate module |
| `ARTIFACT.GENERATED_RESULT` | same concept as candidate, or a distinct lifecycle stage |

**Label decisions recorded inside entries:** trim mark / crop mark
relationship (NEEDS_STANDARD_REVIEW); product name for `UI.PRODUCT_WORKBENCH`; canonical name of
`GEOMETRY.PAGE_GEOMETRY_DESCRIPTOR`; whether Define Framebox is also a module
surface; Create Booklet / Booklet Folding product-surface relationship.

**NEEDS_STANDARD_REVIEW (7):** effective page box value, PDF/X conformance,
processing steps, finished page, production intent, finishing contour line,
trim mark.
Standard-review flags also sit on several CANONICAL_V1 entries (e.g. folded
signature, collating mark) where the concept is settled but alignment is not.

**PROVISIONAL (32):** among others, operation classes, diagnostic severity,
known/unknown bad, salvage mode, production job, lap shift, folding scheme,
technical numbering, service text, structural PDF core, render service,
production contour, content bounds, production object.

---

## 19. Deprecated / legacy vocabulary

**LEGACY entries (5):** `GEOMETRY.LEGACY_LAYOUT_ZEROING` (`core.normalize_boxes`),
`GEOMETRY.TARGET_CANVAS` (module-local), `PRODUCTION.STEP_AND_REPEAT_LAYOUT`,
`GOVERNANCE.OC_WORKSTREAM` (OC-n labels), `DEVINFRA.D01_KERNEL_MEDIATION`.

**Deprecated aliases (4):** *FrameBox* → Framebox;
*Normalize-to-Zero* → layout space; *Page Geometry engine* → module Page
Geometry; *acceptance (artifact)* → artifact admission; *PlacedInstance* →
placed content (CIP4 ContentObject); *SheetComposition* → imposition layout
(CIP4 Layout). (*crop mark* is no longer deprecated; see §13.)

**Must-qualify words (31, registry `ambiguous_terms`):** OC, Operator
Workplace, Page Geometry, acceptance, action, admission, bleed, bounding box,
candidate, canvas, command, commit, content object, crop, CTM, D1/D01/D-01/D2,
evidence, frame, Job,
layout, normalize, operation, profile, promotion, publication, receipt,
review, rotation, signature, slug, trim.

---

## 20. Rules for adding future terminology

Semantic governance only; no implementation authorization.

```text
R1  NO NEW CANONICAL TERM WITHOUT REGISTRY CHECK
    (search canonical_name, aliases, deprecated_aliases, ambiguous_terms)
R2  NO NEW OPERATION KIND WITHOUT REGISTRY ENTRY
R3  NO NEW ARTIFACT KIND WITHOUT REGISTRY ENTRY
R4  NO NEW SIGNIFICANT STATE WITHOUT REGISTRY ENTRY
R5  NO DUPLICATE CANONICAL IDENTITY
    (one concept, one canonical_id; unique name per namespace)
R6  NO SILENT SEMANTIC REPURPOSING
    (changing a definition = new registry revision with Human acceptance)
R7  STANDARD FIRST: check applicable standard and domain usage before
    registering an IMPOZITORIUM_EXTENSION; never claim standard alignment
    without a recorded source
R8  MODULE NAMES NEVER NAME PLATFORM LAYERS (and vice versa)
R9  NO AMBIGUOUS BARE WORD AS AN ALIAS; add it to ambiguous_terms instead
R10 GOVERNANCE / DEVINFRA TERMS DO NOT ENTER PRODUCT RUNTIME VOCABULARY
R11 MILESTONE LABELS (OC-n, D-0n, Gate, Stage) ALWAYS CARRY THEIR PREFIX
R12 UI LABELS MAY BE SHORT; MACHINE IDS MUST BE NAMESPACED
R13 NO MODULE OWNS GENERIC PDF / GEOMETRY SEMANTICS
    (modules consume PLATFORM.GEOMETRY_CORE and PLATFORM.STRUCTURAL_PDF_CORE)
R14 PROFESSIONAL CORRECTNESS OVER NAMESPACE TIDINESS
    (do not deprecate an established professional term only to avoid a
    name collision; disambiguate by namespace instead)
```

Lightweight process: proposing agent adds a `PROVISIONAL` entry; an
independent review checks R1–R14; Human acceptance moves it to
`CANONICAL_V1`. Labs may use local terms freely but must map them at
promotion time.

---

## 21. Architecture blockers resolved / still open

```text
MODULE_PAGE_GEOMETRY_DISAMBIGUATED = YES
    MODULE.PAGE_GEOMETRY  ≠  PLATFORM.GEOMETRY_CORE  ≠  GEOMETRY.PAGE_GEOMETRY_DESCRIPTOR
    ≠  OPERATION.KIND.PAGE_GEOMETRY_TRANSFORM

PLATFORM_GEOMETRY_CORE     = PLATFORM.GEOMETRY_CORE "Platform Geometry Core" (CANONICAL_V1)
PDF_TRIMBOX                = PDF.BOX.TRIM (CANONICAL_V1, STANDARD_ALIGNED)
LAYOUT_BOX                 = GEOMETRY.LAYOUT_BOX (CANONICAL_V1)
FRAMEBOX                   = GEOMETRY.FRAMEBOX (CANONICAL_V1; rectangular platform working frame)
FRAME_INTENT               = GEOMETRY.FRAME_INTENT (CANONICAL_V1)
CLIP_REGION                = GEOMETRY.CLIP_REGION (CANONICAL_V1)
FUTURE_CONTOUR_GEOMETRY    = GEOMETRY.PRODUCTION_CONTOUR (PROVISIONAL)
FRAME_MATERIALIZATION      = NOT_DECIDED

DECISION_03_SEMANTIC_BLOCKER = RESOLVED
```

All eight required concepts have distinct, non-overlapping canonical
identities in both this document and the registry. Decision 03 can therefore
be written without overloaded terms. Still open, but not blocking the
semantic statement of Decision 03:

1. `POLICY.FRAME_MATERIALIZATION`;
2. whether GUI layout space follows the Framebox once it diverges from the
   layout box;
3. `MODULE.SIZE_AND_CROP` relation;
4. standards review of processing steps / PDF/X / JDF / trim-crop mark terms
   before technical objects or production intent are designed.

Also noted for the Coordinator: `04 §14` and `04 §20` use "Page Geometry"
for the geometry semantic authority. Under this baseline that phrase should
read `PLATFORM.GEOMETRY_CORE`. `04` itself is not modified.

```text
SOURCE_FILES_MODIFIED = NONE
REVIEW_MIRROR_MUTATION = NONE
IMPLEMENTATION_AUTHORIZATION = NONE
```
