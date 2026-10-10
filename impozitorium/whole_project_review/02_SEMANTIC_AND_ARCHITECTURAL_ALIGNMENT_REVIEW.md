# 02 — Semantic and Architectural Alignment Review

```text
TASK_ID =
    IMPOZITORIUM_WHOLE_PROJECT_REVIEW_
    SEMANTIC_AND_ARCHITECTURAL_ALIGNMENT_REVIEW_01

ROLE =
    INDEPENDENT_PRODUCT_AND_ARCHITECTURE_REVIEWER

FACTUAL_BASELINE =
    impozitorium/whole_project_review/01_ACTUAL_PROJECT_RECONNAISSANCE.md
    (Bounded Correction 01, PR #3, commit df59fb9)

REVIEW_SOURCE =
    Raymond-1968/Imposition_app-review-mirror (read-only)

CANONICAL_REPOSITORY_ACCESSED =
    NO

DOCUMENT_CLASS =
    ARCHITECTURE_RECOMMENDATIONS
    NO_IMPLEMENTATION_AUTHORIZATION
    NOT_CANONICAL_PROJECT_TRUTH
```

References such as `01 §8` or `C-04` point to the factual baseline. A few
additional facts were checked in the mirror for this pass; they are cited
inline with branch and path.

## Revision note — Bounded Correction 01

```text
CORRECTION_SCOPE =
    Define Framebox canonicalization wording                 (§7, §21 D3)
    structural substrate vs Page Geometry ownership          (§1, §6, §7, §20)
    booklet/signature convergence wording                    (§9, §19, §20)
    technical-object PDF representation wording              (§6, §15)

NEW_ARCHITECTURAL_DOMAINS_ADDED =
    NONE

NEW_IMPLEMENTATION_AUTHORIZATION =
    NONE
```

Short names follow `01`: **OW-line** (`derived/agent-hierarchy-policy-accepted-01`
lineage), **EN-line** (`docs/oc6d2-b4-human-acceptance-01` lineage),
**OC-line** (`derived/oc1-oc5-accepted-publication-01`).

---

## 1. Executive verdict

```text
OVERALL_ARCHITECTURAL_ALIGNMENT = MIXED
INFRASTRUCTURE_BALANCE          = MIXED
CANDIDATE_DEPENDENCY_ORDER      = ACCEPT_WITH_REORDERING
```

**The product laws are right, and the platform substrate is moving in the
right direction.** Source safety, separating Working Document / Preview Result
/ Save As, the layout-box law, pt-vs-pixel separation, and the engine decisions
D-01…D-08 match a fast-turnaround digital-print workbench. The EN-line has
made those laws real in headless code: pikepdf writers, a PDFium render
boundary, and a verified, crash-safe artifact lifecycle.

**Product capability that an operator can touch has not moved at the same
pace.** As observed in the repository, the operator-facing implementation is
still the legacy PyMuPDF shell with one mounted capability (`01 §21`). None of
the new substrate is bound to the GUI, and no production module has been
rebuilt on it.

**Three structural problems now limit progress more than any single missing
feature:**

1. **No product operation seam.** Each capability invents its own request,
   result, manifest and verification shape. There are already two different
   manifest representations for two capabilities (§11).
2. **No declared product line.** Two long-lived lines carry different code
   at the same module paths (`01 C-06`, `C-26`), and Optional Content code
   lives on a third (§5).
3. **The development-infrastructure track is pulling attention away from the
   product.** The File Factory is careful, well-tested engineering, but by its
   own charter it has no product leverage. It is still growing (Waves 01–03,
   Kandev qualification, a kernel driver), while its stated purpose,
   agent-executed engineering work, remains `NOT_AUTHORIZED` (§4).

The candidate product sequence (File Management → structural PDF → Define
Framebox / Page Geometry → modules → Operations → Jobs → Agent) is
substantially correct. Three changes are needed:

- Move a **minimal Operation Record** with an **admissibility outcome** ahead
  of the production modules.
- Develop the **structural PDF substrate and the Page Geometry layer in the
  same broad phase**, as adjacent owners with a strict contract (not one
  combined domain). Make Define Framebox the first new operator-facing
  operation on Page Geometry.
- Require one **end-to-end vertical slice through the GUI** before porting
  modules broadly.

---

## 2. Product intent vs actual architecture

| Product requirement | Architectural support today | Alignment |
|---|---|---|
| Source PDF sacred | contract + code (legacy guards; EN `SOURCE_IMMUTABILITY: ACCEPTED`) | **Strong** |
| Working Document / Preview Result / Save As distinct | legacy GUI implements it; EN lifecycle implements candidate → verify → commit → promote → Current Pointer headless | **Strong in design, split in code** |
| Imperfect customer PDFs (Canva, Word, mobile, AI) | diagnostics severity model (`doc/platform_diagnostics_architecture.md`: INFO / WARNING / BLOCKER / ERROR); rotation gate; VAB sanitation (lab); PDF risk probe (lab) | **Moderate**: many observers, few repairs on the platform |
| No time to send files back → repair in-house | repairs exist mostly in labs (VAB bleed/sanitation, rotation normalization) or legacy code (quick bleed) | **Weak** |
| Deterministic and explainable | strong evidence culture; EN writers carry writer IDs, verification profiles and receipts | **Strong** where implemented |
| Fast | no product evidence of throughput design; the heavy evidence culture applies to platform changes, not runtime | **Not proven** (watch) |
| Operator-controlled, including knowing compromises | design exists (`doc/platform_command_api_manifesto.md` §13–15: warnings vs blockers, *known bad vs unknown bad*, Emergency / Salvage mode with logged risk acceptance); **no implemented record** | **Designed, not built** |
| Production-economic usefulness (Step & Repeat, booklet, N-up, cut stack, bleed) | legacy Step & Repeat window; booklet in sandbox and lab; N-up/Cut Stack design-only; VAB lab | **Weak** on platform, **strong** in lab semantics |
| GUI / batch / agent over the same core | Operation Registry is design-only; no shared invocation layer (`01 §14`) | **Not yet** |

The product thinking already in the repository, in the Command API
manifesto, `booklet_exception_handling_vision.md` ("automate the rule,
visualize the exception, let the human specify production reality") and the
lab boundaries, matches the stated intent closely. What lags is the
**implementation of that thinking in product runtime**.

---

## 3. What is already architecturally strong

1. **Engine ownership decisions D-01…D-08** (EN-line). One renderer per
   capability, one final structural writer per artifact, PyMuPDF to exit,
   capability-by-capability migration with no silent fallback. This is a
   clean and testable migration law.
2. **Platform File Management lifecycle** (EN-line). Candidate verification
   → receipt → Composite Unit of Work → managed staging → promotion → Current
   Pointer, qualified for same-volume use, with a crash matrix. This is the
   correct backbone for "never damage the source, never lose the result".
3. **Engine-neutral geometry value model** (`preflight/engine_neutral_geometry.py`,
   EN). Explicit coordinate spaces, units, box provenance, affine law and
   stable diagnostic IDs. This is the right foundation for Page Geometry.
4. **Explicit admissibility thinking** (Command API manifesto, diagnostics
   severity, compatibility-gate classifications `supported` /
   `supported_with_warning` / `requires_normalization` / `blocked_for_this_module`).
   The concept the product needs is already articulated (§18).
5. **HumanGate and evidence discipline.** The Agent Hierarchy Policy
   separates stages, forbids self-acceptance, and states proportionality (§10).
6. **Lab semantics grounded in physical production.** Booklet Folding records
   pagination formulas, lap/creep sign rules and physical-qualification flags.
   Vector AutoBleed has a proven mirror-bleed construction with 169 accepted
   tests (`01 §15.2`). This is production knowledge that is hard to
   rediscover.

---

## 4. Infrastructure-to-product balance

| Area | Verdict | Reason |
|---|---|---|
| EN-line PFM lifecycle + engine migration | **A — healthy foundation investment** (some B) | directly carries product laws (source safety, verified output); every future module needs it |
| EN-line representation proliferation (schema v4 → successor v5, receipt v1/v2, profile representations `PAGE_GEOMETRY_LEGACY_SIDECAR_V1` vs `GENERATED_RESULT_CANDIDATE_MANIFEST_V2`) | **B — temporarily heavy but rational** | migration needs exact replay; watch that versions retire |
| File Factory core (L1–L5, L9A, L7A) | **B/C** | well-built, but by charter "not … Impozitorium production Job owner"; real execution `NOT_AUTHORIZED`; its own audit is `OUTCOME_FAIL` with 17 open findings being remediated wave by wave |
| File Factory expansion (Kandev L7B qualification across v0.92.1 / v0.93.0 / v0.95.0, C-LIVE recorder, D01 kernel minifilter, Operator Workplace Stage 5) | **D — risk that orchestration becomes the project** | high effort and high governance ceremony for a capability that has never run a real Job and whose external chassis is volatile (Blueprint 08 §4 records three Kandev version roles) |

**Overall: MIXED.** The product-substrate investment is sound. The
development-infrastructure investment has passed the point of diminishing
returns for the current product stage. It is not wrong; it is ahead of need.
Its leverage arrives only when an agent actually performs engineering work,
and it does not yet.

---

## 5. OW-line / EN-line architectural split

**Is the split still useful?** Conceptually yes; physically no.

- **Healthy specialization:** development infrastructure (File Factory,
  Orchestrator Operator Workplace, Stage 2C, D01) is a different product with
  different runtime, risk and audience. It deserves its own boundary.
- **Integration debt:** the two lines diverged at the *product* level too.
  The same module paths have different contents (`preflight/renderer.py`,
  `preflight/engine_neutral_geometry.py`, `preflight_gui/window.py`;
  `01 C-06`, `C-26`). PDFium preview exists in three unmerged states
  (`01 C-07`). OC-1…OC-5 is on neither main line (`01 C-08`). The Create
  Booklet creep fix is on an isolated branch (`01 C-09`). Every week of
  divergence makes convergence more manual.

**What would be lost if one line were naïvely declared the winner:**

| If the winner were… | Lost |
|---|---|
| EN-line | Gate D GUI PDFium integration (`pdfium_backend.py`, `pdfium_worker.py`, `PreviewRenderCoordinator`); Agent Hierarchy Policy; H1 harvest documents; lab lineages; File Factory and its accepted records; OW `global_migration_roadmap` provenance work |
| OW-line | pikepdf writers; PDFium production dependency declaration; D-01…D-08; PFM verifier/staging/promotion/successor; OC-6; Page Geometry Stage 7/8; engine-neutral geometry v1 as implemented on EN |
| either | OC-1…OC-5 legacy code and acceptance chain (OC-line); transfer-branch booklet fix |

**What must converge (product substrate):** geometry value model, renderer
boundary (EN provider model + OW GUI worker/coordinator), structural
writers, PFM, Optional Content semantics, the GUI shell, and routing
documentation for product areas.

**What must remain separate:** File Factory / Operator Workplace / Stage 2C /
D01 (development infrastructure); living labs; recovery archives.

**Assessment.** The product substrate on the EN-line is the more complete
and more product-relevant base. Product-relevant OW deltas (Gate D GUI
integration, governance policy documents) are additive to it. No Git
strategy is proposed here (see Decision 1).

---

## 6. PDF engine and structural ownership assessment

**Is PDFium = render, pikepdf/qpdf = structure, PyMuPDF = transitional
architecturally sound?** Yes. It separates concerns that differ in risk:
rendering mistakes are visible and reversible, while structural mistakes
silently damage production bytes. The EN evidence (`PYMUPDF_WRITER_DEPENDENCY:
NONE` for D1, `SILENT_PYMUPDF_FALLBACK: NONE`) shows that the law is
enforceable.

**Does code support it?** On EN backends, yes. In the GUI and legacy modules,
not yet: preview, Save As, Manual Trim export, Step & Repeat, `core.normalize_boxes`
and both labs use PyMuPDF (`01 §7`). This is the declared transition
(`01 C-10/C-11`), and acceptable while the transition is capability-by-capability.

**Leaks across engine boundaries.**
- `fitz.Rect` is the GUI geometry type (`preflight_gui/preview.py`). GUI
  geometry is engine-typed. This blocks PDFium preview from being
  geometry-neutral.
- The Gate D GUI path (OW) and the EN renderer provider are two different
  render boundaries with one module name (`01 C-06`).
- Labs write structure through PyMuPDF content-stream rewriting (VAB),
  which is outside D-02 (`01 C-21`).
- `pikepdf` is absent from `requirements.txt` and lives only in an isolated
  lock file. The structural engine is not yet a declared product dependency
  in the way PDFium is (EN index: PDFium production declaration accepted).

**Is structural preservation first-class?** In the EN writers, yes:
raw-box-presence semantics, negative MediaBox origin, OC preservation and
source immutability are accepted properties. Elsewhere, preservation is
handled patch by patch: OC-2 fixed Manual Trim box-only export, VAB clones
`/OCProperties`, and rotation is a separate gate.

**Coherence.** Optional Content, boxes, rotation and geometry are currently
**isolated workstreams joined by documents**, not one substrate. Each
writer re-proves preservation for its own scope.

**Minimum coherent structural layer the product needs** (one owner,
pikepdf-based, engine-neutral types at its boundary):

```text
STRUCTURAL PDF SUBSTRATE
  open(source, read-only)  -> immutable document handle + content identity (hash)
  read page facts          -> PageBoxes (raw + inherited + effective), /Rotate, UserUnit,
                              OC catalog, OutputIntent presence        (engine-neutral types)
  apply bounded mutations  -> box set/clear, rotate/normalize, place page as Form XObject,
                              add technical objects with structurally separable
                              identity/grouping (exact PDF representation not decided)
  preservation contract    -> what each mutation guarantees to keep (OC, ICC/OutputIntent,
                              transparency groups, annotations policy, metadata)
  write candidate          -> bytes + writer identity
  verify candidate         -> structural postflight (boxes, OC, page count, invariants)
```

Every production operation builds on these six verbs. Preservation is then
proven once per mutation kind, not once per module.

---

## 7. Page Geometry / Define Framebox assessment

**Page Geometry is becoming the correct owner, but it has not displaced the
legacy path.** `preflight/page_geometry.py` implements the layout-box law;
`engine_neutral_geometry.py` provides the value model; EN Page Geometry
Stage 7/8 carries transform → pikepdf write → PDFium render. The GUI and
report still take geometry from `core.normalize_boxes` (`01 C-04`), which
uses an older rule and a Corel-specific heuristic.

**Recommended ownership split.**

```text
STRUCTURAL PDF SUBSTRATE != PAGE GEOMETRY
```

They are adjacent layers with a strict contract, not one combined ownership
domain:

```text
STRUCTURAL PDF SUBSTRATE OWNS          (factual PDF structure + safe structural mutation)
    raw / inherited / effective PDF boxes
    MediaBox origin
    /Rotate
    UserUnit
    structural object preservation
    structural mutation
    write candidate
    structural verification

PAGE GEOMETRY OWNS                     (production interpretation of structural page facts)
    layout_box selection
    layout size
    orientation semantics
    absolute <-> layout-relative transforms
    GUI-facing geometry
    page-frame semantics
    geometry warnings
```

Operations such as Define Framebox, Manual Trim and Page Geometry Transform
use Page Geometry semantics and request bounded structural mutation through
the structural PDF substrate.

| Concern | Owner |
|---|---|
| box discovery (raw, inherited, effective), UserUnit, /Rotate, MediaBox origin | **structural substrate** (read facts) |
| layout_box selection (TrimBox → ArtBox → CropBox → MediaBox), absolute ↔ layout-relative transforms, page orientation, page size | **Page Geometry layer** (single geometry authority; engine-neutral) |
| GUI-relative geometry `[0, 0, w, h]`, rulers, overlays | **GUI**, *consuming* PageGeometry, never computing it |
| warnings / validation codes (e.g. `ARTBOX_FALLBACK_USED`, `ROTATION_GEOMETRY_INCONSISTENT`) | **Page Geometry layer** emits; **admissibility policy** classifies |
| box mutation, frame definition, structural write-back | **operations** (Define Framebox, Manual Trim, Page Geometry transform) via the substrate |
| production thresholds (bleed ≥ 2 mm etc.) | **product policy** (profiles), not geometry code |
| Corel / producer-specific heuristics | **diagnostics / repair operations**, explicit and named, not inside normalization |

**Define Framebox is a genuine missing seam.** For imperfect customer PDFs,
the first decision a technologist makes is often "what is the finished
object on this page?" The repository today can *select* a layout box by
priority and *transform* geometry, but it cannot record an **operator-assigned
frame** as intent. That intent is distinct from the boxes the file happens
to carry.

- `DEFINE_FRAMEBOX` = explicit operator production intent about the intended
  page/frame geometry. Architecturally it is a **Page Geometry operation**.
  It may result in structural box mutation, a recorded frame intent, or
  another explicit canonical representation.
  `FINAL_FRAME_MATERIALIZATION_POLICY = NOT_DECIDED`.
- Define Framebox establishes explicit operator intent. How that intent is
  materialized into canonical page geometry must be explicit and
  structurally recorded.
- **Define Framebox must not create a parallel hidden layout-box precedence
  chain.** The accepted law (TrimBox → ArtBox → CropBox → MediaBox) remains.
  The platform still exposes **one canonical `layout_box` result**:
  downstream operations consume one canonical PageGeometry result and never
  choose between an implicit operator frame and the standard hierarchy.
- It is the **ideal first new operation** on the new stack: small, central,
  operator-interactive, and immediately useful to every module downstream
  (Step & Repeat `W_obj = layout.width` depends on it).

---

## 8. Artifact lifecycle / File Management assessment

- **KEEP_AND_COMPLETE.** The EN lifecycle is the right backbone.
- **Main gap:** it is not bound to the GUI or to Save As (`01 §8`). The
  OC-6 addendum names `… -> accepted/current Working Document -> Save As ->
  final-byte verification`, and those last steps are not implemented.
  Until one action is taken over end to end (D-05 "action-by-action"),
  the legacy shell remains the real filesystem owner.
- **Complexity watch:** schema v4 → successor v5, two receipt representations
  and two manifest representations in a short time. Representation versions
  need a retirement rule, or replay support becomes permanent weight.
- **Cross-volume** remains unqualified. This is acceptable to defer for a
  workstation product if documented as a deployment constraint (managed
  workspace on the same volume).
- **Vocabulary:** "acceptance" means both Human governance acceptance and
  artifact acceptance (`working_document_acceptance.py`), and "publication"
  means both Git publication and file promotion. Distinct terms are needed in
  product code (§18).

---

## 9. Production capability assessment

| Capability | Classification | Semantics worth preserving | Implementation worth preserving | Urgency |
|---|---|---|---|---|
| Preflight / diagnostics | KEEP AS PLATFORM CORE (KEEP_AND_COMPLETE) | severity model, compatibility classifications, stable codes | report/GUI pieces; geometry input to be switched to PageGeometry | NEXT |
| Manual Trim | KEEP AS PLATFORM CORE (KEEP_AND_COMPLETE) | v0 rules, quick bleed, OC-2 box-only preservation | EN pikepdf D1 writer + generated-result adapter; legacy GUI panel interactions | **NOW** (first vertical slice) |
| Define Framebox | MISSING → new Page Geometry operation | — | — | NEXT |
| Page Geometry / Size & Crop | KEEP AS PLATFORM CORE (CHANGE_OWNERSHIP to single geometry layer) | transform command model (`PageGeometryTransformCommand`, scopes, target canvas, scaling) | EN integrated route + pikepdf writer | NOW |
| Step & Repeat | REIMPLEMENT AGAINST NEW CORE | seed planner policies (P1 placement invariants, gap/margin, orientation, source traceability), sheet-size catalog contract, cut-mark profile registry | seed planner (pure); **not** legacy `step_repeat/backend/engine.py` (uses TrimBox only, not layout box, and draws its own marks) | NEXT |
| Vector AutoBleed | REIMPLEMENT FROM PRESERVED SEMANTICS (lab stays a lab meanwhile) | mirror-bleed construction, 0.75 pt inset, center-first order, sanitation that preserves transparency/ExtGState/DeviceCMYK, OCG preservation, raster fallback as explicit emergency | 169-test suite and fixtures **as oracle**; PyMuPDF content-stream rewriting not preserved as platform code (D-02) | NEXT — high value for imperfect customer PDFs |
| Create Booklet | CONVERGE with Booklet Folding on a shared booklet/signature semantic domain, then REIMPLEMENT (product surface relationship not yet decided) | artifact roles, creep compensation, chunking, technical numbering (transfer fix), exception vision | booklet_pipeline_lab backend as reference only | LATER |
| Booklet Folding / signature planning | KEEP AS SEPARATE LAB FOR NOW → converge semantics into the shared booklet/signature domain | 3-layer split (pagination / cell geometry / physical production), 16p formula, lap/creep rules, physical-qualification flags | engine as reference; PySide6 GUI not reused | LATER |
| N-up | DEFER; MERGE WITH placement core shared with Step & Repeat | "N-up with Background", sequence-into-cells | none yet | LATER |
| Cut Stack | DEFER; on the same placement core, distinct ordering strategy | "postpress-driven, not generic N-up", reversed output | none yet | LATER |
| Technical numbering / marks | MISSING common representation (§15) | all lab mark semantics | registries (cut mark, signature, font bundle) | NEXT |
| Rotation normalization | CONVERGE platform gate/normalizer with VAB RN01–RN06 reference | RN contract | VAB handoff as oracle | LATER |

---

## 10. Labs: what semantics deserve preservation

**Booklet Folding Lab**
- three-layer separation: pagination / cell geometry / physical production
  (the best articulated decomposition of imposition in the repository);
- 16-page signature pagination and rotation table (declared internally
  consistent for its scope);
- Lap Shift physical limit formula; creep direction derived from the physical
  slot, not page parity; marks stationary under creep;
- mark vocabulary (outer crop, fold, crosshair, collating staircase, slugs);
- explicit `PHYSICAL_BINDERY_QUALIFICATION = REQUIRED`. This flag deserves to
  become a platform concept ("unproven physically" ≠ "wrong").

**Vector AutoBleed Lab**
- mirror-bleed via one shared Form XObject and eight clipped reflection CTMs;
  seam elimination by 0.75 pt inset and center-first order;
- sanitation rules that **preserve** transparency groups, ExtGState and
  DeviceCMYK. This is exactly the "repair imperfect PDFs without damage"
  requirement;
- raster fallback as an explicit, labelled emergency path (an early instance
  of operator-admissible deviation);
- rotation normalization contract (RN01–RN06);
- the accepted 169-test baseline as a semantic oracle for reimplementation.

**booklet_pipeline_lab / transfer branch:** creep clipping correctness and
technical page numbering (`01 C-09`).

**step_repeat_seed:** planner policies (gap = distance between neighboring
layout boxes is consistent with the product law), 87-test planner baseline.

**Governance for labs:** keep the current model. Labs evolve freely with
regular remote backup, and strong review happens only at *promotion points*
(§16).

---

## 11. Missing Operation / Action seam assessment

**Is the seam missing?** Yes. Evidence:

- `preflight/generated_result_profiles.py` (EN) is a registry of exactly two
  operation outputs, `PAGE_GEOMETRY` and `MANUAL_TRIM`, each with a writer ID,
  a verification profile and a **different manifest representation**
  (`PAGE_GEOMETRY_LEGACY_SIDECAR_V1` vs `GENERATED_RESULT_CANDIDATE_MANIFEST_V2`).
  This is the seam being invented locally per capability.
- `page_geometry_integrated_route.py` has its own request/success/failure
  types, artifact ledger, sidecar and rollback. Manual Trim has a different
  adapter. A third module would add a third shape.
- The Command API manifesto (Draft) already describes command input, command
  result, validation result and warnings/blockers, but nothing implements it.

**Does File Management already provide part of it?** Yes, the **back half**:
artifact identity, verification receipt, commit, staging, promotion and
current pointer. What PFM does not represent is the **front half**: which
operation, which version, which parameters and policy, which inputs, which
diagnostics, which operator decisions.

**Does File Factory provide reusable concepts?** As **patterns, not code**:
idempotent operation IDs, request digest, replay classification, receipts,
`UNKNOWN_SIDE_EFFECT → STOP → incident`. Its domain objects (WorkUnit,
AuthorityUnit, JobKind IMPLEMENTATION / REVIEW / CORRECTION / RECONCILIATION,
review admission, HumanGate decisions) model **engineering governance**. They
are inappropriate for product jobs, and the product runtime must not depend on
the `operator_workplace` package.

**Would an Operation contract reduce duplication?** Yes:

- one invocation shape for GUI, batch and agent;
- one place for diagnostics and admissibility decisions;
- one lineage record that Jobs can later chain;
- PFM commits *operation results* instead of module-specific manifests.

**Would it become bureaucracy?** Only if it is designed as a framework. Keep it
as a **record + registry**, not an engine:

```text
OperationRecord (minimal, product runtime)
  operation_id, operation_kind + version
  input artifact refs (content identity)
  parameters + policy profile ref
  engine/writer identity
  diagnostics[] (stable codes, severity)
  admissibility decision (auto-pass | warned | operator-accepted deviation | blocked)
      + who/why for operator acceptance
  output artifact refs (candidate -> PFM)
  verification result
  provenance (timestamps, environment identity)
```

The Generated Result Profile registry becomes the **operation kind
registry**. PFM stays the artifact authority.

---

## 12. Jobs architecture assessment

- **FULL JOB SYSTEM** (ordered multi-operation workflow, recipes, resumable
  state, Job Trace, rollback/re-entry): **DEFER** (LATER).
- **MINIMAL OPERATION / ARTIFACT LINEAGE** (each operation records inputs →
  outputs, and outputs can be inputs): **NEXT**, as part of §11.

Once every operation writes an OperationRecord over PFM artifacts, a Job is
little more than *an ordered list of OperationRecords plus intent*. Lineage
is the prerequisite; the Job engine is not.

One concept is missing from both: **production intent / product
specification** (finished size, binding, stock and grain, quantity, sides,
finishing). Today it is scattered across Step & Repeat layout dicts, the
sheet-size catalog contract, booklet parameters and Define Framebox's future
frame. A Job is "production intent + operations". Without an intent object,
Jobs will degrade into scripts. Recognize it as a model **before** Jobs
(LATER, but before F).

---

## 13. Agentic Layer readiness assessment

**Current architecture does not yet lead there naturally.** The prerequisites
are missing in product runtime:

1. explicit operations with typed inputs/outputs (§11);
2. admissibility decisions that distinguish automatic, warned and
   operator-accepted results;
3. artifact lineage (PFM + OperationRecord);
4. a non-GUI invocation path for the same operations (CLI/batch) as the
   proving ground before any agent.

**Assessment of existing agent work:**

| Item | Judgment |
|---|---|
| Agent Hierarchy Policy (roles, stage separation, no self-acceptance) | **useful prerequisite**: the same HumanGate logic applies when an agent proposes production actions |
| File Factory authority units, one-shot authority, replay/stale rejection, incident on unknown side effect | **partially reusable as patterns** for "agent may propose, operator authorizes" |
| File Factory domain model, Kandev chassis, Stage 2C reviewer runtime, Orchestrator Operator Workplace | **too development-centric**: orthogonal to product agents |

Principle to keep: the agent gets **no capability the operator lacks** and
calls the same operations. Production execution stays operator-authorized.

---

## 14. GUI / operator-workplace assessment

First, separate the terms. "Operator Workplace" in the repository means the
**development** Orchestrator Operator Workplace (`01 C-14`). The prepress
GUI needs its own unambiguous name. Renaming the development package or
contract avoids lasting confusion in code, documents and agent context.

| Question | Recommendation |
|---|---|
| Should GUI own filesystem behavior? | **No** (D-04 already marks it temporary). GUI chooses paths and confirms actions; PFM executes. |
| Should GUI own PDF mutation? | **No.** GUI invokes operations. |
| Should GUI own geometry decisions? | **No.** GUI renders PageGeometry; it may *propose* geometry (drag a frame), but an operation validates and records it. |
| Should GUI merely invoke operations? | **Mostly**, but not "thin at all costs". |

**What must stay interactive and operator-specific:** preview, zoom and
rulers, measurement, temporary overlay tools, direct manipulation of frames
and crops with live feedback, before/after comparison, and **the moment of
risk acceptance** (the operator seeing the exception and deciding). Fast
iterative preview may use a lightweight preview path, but **committing** goes
through the operation and PFM.

The OW-line Gate D work (`PreviewRenderCoordinator`, background PDFium
worker, request supersession) is valuable GUI architecture for responsive
preview, and should converge onto the EN render provider rather than be lost.

---

## 15. Technical layers / marks assessment

Current state: four independent producers (`01 §16`, `C-20`).

**Verdict: MIXED. Common representation + operation-specific policy.**

- **Platform concern (common):** a *technical object* model:
  kind (cut / crop / fold / collate / registration / service text /
  signature label / numbering / plotter contour), geometry in imposed-sheet
  space, intent (finishing instruction vs information), placement constraint
  class (must be outside finished object / may intrude into bleed / free),
  rendering resources (from the existing font-bundle and signature registries),
  semantic identity, and **structural-layer membership / grouping metadata**.
- Technical objects should support explicit, structurally separable
  identity/grouping. OCG-based realization is a strong candidate because it
  provides named, identifiable, toggleable PDF content, but the exact platform
  representation remains subject to later technical-layer policy and
  standards review. `EXACT_PDF_REPRESENTATION = NOT_DECIDED`.
- **Operation-specific (policy):** *which* marks a module emits and *where*
  (booklet fold marks, step-and-repeat cut marks, cut-stack sequence marks).
- **Admissibility:** the example in the brief (a mark that cannot sit fully
  outside the product) is a constraint-class violation that admissibility
  can classify as *operator-admissible deviation*, rather than a hard failure.

The existing headless registries (cut-mark profile, signature profile,
technical font bundle, sheet-size catalog) are the right ingredients. They
lack the shared object they are meant to feed.

Placing technical objects in their own structural layer from the start keeps
the architecture compatible with future production-layer conventions in
modern PDF workflows, without designing them now.

---

## 16. Governance-cost assessment

**Where the discipline creates real safety:**
- structural PDF bytes, writers and preservation;
- artifact lifecycle and filesystem promotion;
- engine selection and dependency intake;
- accepted architecture and policy changes;
- promotion of lab semantics into the platform.

**Where it is heavier than the risk:**
- **File Factory internal iterations.** Wave sub-slices each carry evidence,
  independent review, Human acceptance and local publication records, plus
  identity reconciliations of review metadata (e.g. W2-S4 "review-identity
  issue reconciled as a proven metadata-label mismatch"). Effort goes into
  proving the process about the process.
- **Status documents as ledgers.** OW `current_state.md` is 5,393 lines and
  drifted from its own index within a week (`01 C-02`). The EN index header
  drifted from its own rows (`01 C-03`). Agents and humans pay this cost on
  every task.
- **Documentation-only gates** for low-risk shape fixtures (dozens of
  `*_fixture_lab` checkpoints).

**Recommendation (respecting HumanGate):** make the policy's existing
proportionality clause (§10) operational with explicit tiers:

| Tier | Scope | Required |
|---|---|---|
| L (lab) | living labs, spikes | remote backup; no per-change review; review at promotion |
| R (routine) | bounded implementation on accepted contracts, low-risk docs | one independent review; Human acceptance can batch several items |
| P (platform-critical) | structural bytes, lifecycle, engine/dependency, policy | full current discipline |

In addition: **one present-tense status page per product area**, kept short
and regenerated, separate from the append-only ledger.

---

## 17. Architectural debt and duplication

| Item | Temporary and acceptable | Becoming debt |
|---|---|---|
| PyMuPDF vs pikepdf writers | ✔ declared transition (D-02) | if no GUI capability migrates within the next phase |
| PyMuPDF vs PDFium render | ✔ declared (D-01) | two PDFium GUI/backend boundaries (OW Gate D vs EN provider) are debt **now** |
| legacy shell vs PFM filesystem | ✔ declared (D-04/D-05) | while no single action has been taken over end to end |
| `core.normalize_boxes` vs PageGeometry | ✔ transitional drift (`01 C-04`) | GUI/report still on legacy rule; Corel heuristic hidden in normalization |
| OW vs EN same-path modules | ✘ | **debt now**; grows with every commit |
| OC-1…OC-5 on its own line | ✘ | **debt now** (accepted semantics on neither main line) |
| per-capability manifests/profiles | ✘ | **debt next** (third module triples it) |
| marks drawn by four producers | ✘ | debt as soon as a second module is promoted |
| lab copies of platform documents | ✔ for standalone lab coherence | if copies drift from the platform originals |
| PySide6 (labs) vs PyQt6 (platform) | ✔ lab-local | irrelevant if labs are reimplemented, not transplanted |
| status ledgers vs routing | ✘ | **debt now** (`01 C-01..C-03`) |
| "Operator Workplace", "Job", "acceptance", "publication", "OC" overloaded | ✘ | **debt now** for humans and agents |

---

## 18. Missing architecture

1. **Operation / Action Record + operation kind registry** (§11). NOW.
2. **Admissibility model**: `hard prohibition | warning | operator-admissible
   deviation | automatic repair | policy-controlled tolerance | human override`.
   The manifesto's *known bad vs unknown bad* and salvage mode already define
   the semantics. What is missing is the **record** (decision, actor, reason,
   policy profile) inside the OperationRecord, and **policy profiles** that
   hold tolerances instead of code constants (e.g. bleed threshold 2.0 mm).
   NEXT.
3. **Define Framebox / frame assignment** as recorded operator intent (§7).
   NEXT.
4. **Technical object representation** (§15). NEXT.
5. **GUI ↔ operation ↔ PFM binding**: one end-to-end vertical slice (§20).
   NOW.
6. **Production intent / product specification model** (§12). LATER, before
   Jobs.
7. **Pipeline vocabulary.** The repository uses all seven concepts, but they
   are not one model:

   | Stage | Present pieces | Gap |
   |---|---|---|
   | OBSERVE | preflight core, OC inspection, box discovery | geometry from legacy path |
   | DIAGNOSE | diagnostics severity, compatibility gate (design) | per-module classification not implemented |
   | REPAIR | rotation normalizer, quick bleed, VAB sanitation (lab) | no platform repair family |
   | TRANSFORM | Page Geometry transform, Manual Trim writer | per-module shapes |
   | VERIFY | PFM candidate verifier, OC postflight | verification profiles per module |
   | ADMIT | working-document acceptance, OC-3 gating | **operator risk acceptance missing** |
   | PUBLISH | promotion, Current Pointer, Save As | Save As not bound to PFM |

   Recommend fixing these seven as the **product pipeline vocabulary**, with
   product terms distinct from governance terms ("admit" ≠ Human acceptance;
   "publish/promote" ≠ Git publication).
8. **Shared production fixture corpus** of real-world imperfect PDFs
   (Canva, Word, mobile, AI-generated) as the regression oracle for engine
   migration and repairs. Pieces exist: the external A0/A1/BAD_MT corpus, PDF
   risk probe, anomaly inventory, VAB fixtures. NEXT.

---

## 19. KEEP / CHANGE / DEFER / REMOVE-MERGE / MISSING matrix

| # | Area | Classification | Urgency |
|---|---|---|---|
| 1 | Agent Hierarchy Policy / HumanGate | KEEP | WATCH |
| 2 | Engine decisions D-01…D-08 | KEEP | NOW |
| 3 | Engine-neutral geometry value model | KEEP_AND_COMPLETE | NOW |
| 4 | Page Geometry as single geometry owner | CHANGE_OWNERSHIP | NOW |
| 5 | `core.normalize_boxes` as geometry authority (incl. Corel heuristic) | REMOVE_OR_MERGE (into PageGeometry + named repair) | NEXT |
| 6 | Define Framebox | MISSING | NEXT |
| 7 | Platform File Management lifecycle | KEEP_AND_COMPLETE (bind one GUI action + Save As) | NOW |
| 8 | Legacy GUI filesystem authority (D-04) | REMOVE_OR_MERGE (action by action) | NEXT |
| 9 | pikepdf/qpdf structural writers → structural substrate | KEEP_AND_COMPLETE | NOW |
| 10 | PDFium render boundary (EN provider + OW Gate D GUI) | CONVERGE | NEXT |
| 11 | Optional Content (OC-1…5 + EN writer preservation) | CONVERGE | NEXT |
| 12 | Rotation normalization (platform + VAB RN reference) | CONVERGE | LATER |
| 13 | Operation / Action Record | MISSING | NOW |
| 14 | Generated Result Profile registry → operation kind registry | KEEP_AND_COMPLETE | NOW |
| 15 | Admissibility record + policy profiles | MISSING | NEXT |
| 16 | Preflight / diagnostics severity model | KEEP_AND_COMPLETE | NEXT |
| 17 | Manual Trim | KEEP_AND_COMPLETE (first vertical slice) | NOW |
| 18 | Step & Repeat | REIMPLEMENT_FROM_PRESERVED_SEMANTICS | NEXT |
| 19 | Vector AutoBleed | REIMPLEMENT_FROM_PRESERVED_SEMANTICS (lab continues) | NEXT |
| 20 | Create Booklet + Booklet Folding | CONVERGE (share one booklet/signature semantic domain; final module / operation / UI boundary not decided; `PRODUCT_SURFACE_RELATIONSHIP = NOT_YET_DECIDED`) | LATER |
| 21 | N-up / Cut Stack | DEFER (shared placement core) | LATER |
| 22 | Technical object representation | MISSING | NEXT |
| 23 | Cut-mark / signature / font-bundle / sheet-size registries | KEEP | LATER |
| 24 | File Factory core (L1–L5, L9A, L7A) | KEEP_BUT_SIMPLIFY (freeze scope) | NOW |
| 25 | File Factory expansion (L7B/Kandev, L8B, L10, further waves) | DEFER | NOW |
| 26 | `operator_workplace` package / Orchestrator naming / D01 source | CHANGE_OWNERSHIP (dev-infra boundary, distinct name) | NEXT |
| 27 | OW / EN product-line split | CONVERGE | NOW |
| 28 | Full product Job system | DEFER | LATER |
| 29 | Agentic Layer | DEFER | LATER |
| 30 | External API / cloud / licensing shell | DEFER | LATER |
| 31 | Documentation topology (ledger vs present-tense status) | KEEP_BUT_SIMPLIFY | NEXT |
| 32 | Production intent / product specification model | MISSING | LATER |
| 33 | Production fixture corpus (imperfect real-world PDFs) | KEEP_AND_COMPLETE | NEXT |
| 34 | Legacy Step & Repeat window; `normalizer/` direction | REMOVE_OR_MERGE (after reimplementation) | LATER |
| 35 | Recovery / historical branches | KEEP (archive, no action) | WATCH |
| 36 | Governance proportionality tiers | KEEP_BUT_SIMPLIFY | NEXT |

```text
KEEP family        = 14  (KEEP 4, KEEP_AND_COMPLETE 7, KEEP_BUT_SIMPLIFY 3)
CHANGE family      = 9   (CHANGE_OWNERSHIP 2, CONVERGE 5, REIMPLEMENT_FROM_PRESERVED_SEMANTICS 2)
DEFER              = 5
REMOVE_OR_MERGE    = 3
MISSING            = 5
TOTAL              = 36
```

`PROMOTE_FROM_LAB` is deliberately unused. No lab implementation is
recommended for direct transplant; lab *semantics* are promoted through
reimplementation.

---

## 20. Proposed dependency order

**Candidate order evaluation: `ACCEPT_WITH_REORDERING`.**

```text
0. DECIDE the product line of record and the dev-infrastructure boundary   (decision, not code)

A. File Management / artifact lifecycle            — largely done; complete ONE GUI action + Save As
B. Structural PDF substrate (+ Optional Content / rotation / preservation converged)
   and, in the same broad phase, the adjacent Page Geometry layer (moved up from C)
   — two owners with a strict contract, not one domain
E-min. Minimal Operation Record + admissibility outcome + operation kind registry  (moved up from E)
C. Define Framebox — first new operation built on B + E-min
   + Manual Trim re-bound through GUI → operation → PFM  (vertical slice)
T. Technical object representation (minimal)        (inserted before mark-emitting modules)
D. Production operations, reimplemented on B + E-min + T:
     Step & Repeat → Vector AutoBleed → booklet/signature domain (Create Booklet + Booklet Folding
     converged; surface relationship not decided) → N-up → Cut Stack
I. Production intent model                           (inserted before Jobs)
F. Jobs (ordered OperationRecords + intent)
G. Agentic Layer (same operations, operator-authorized)
```

**Reasons for each change:**

- **0 first:** porting modules onto a substrate that exists in two divergent
  versions multiplies convergence cost (§5).
- **Page Geometry alongside B:** Page Geometry interprets structural page
  facts (boxes, rotation, origin) that the substrate owns, so the two layers
  and their contract are best settled together. They remain separate owners
  (§7). Define Framebox is an *operation* on Page Geometry. Deferring Page
  Geometry to after the substrate preserves the legacy geometry path longer.
- **E-min before C and D:** without it, each module invents its own
  request/manifest/verification shape. This is already visible with two
  modules (§11). A *minimal* record is cheap; retrofitting it to five modules
  is not. The full Operation Registry and Jobs stay late.
- **Vertical slice with C:** proves GUI ↔ operation ↔ PFM ↔ Save As once
  before scaling. Until then, no new substrate reaches the operator.
- **T before D:** Step & Repeat, booklet, N-up and Cut Stack all emit marks.
  Without a shared representation, each will hard-code its own.
- **Step & Repeat first in D:** simplest geometry, a mature planner, and an
  accepted catalog contract. **VAB second:** highest value for imperfect
  customer PDFs, with a proven test oracle. **Booklet** after the two
  booklet lines converge on a shared semantic domain.
- **I before F:** a Job without production intent is a script.

---

## 21. Recommended next 3 architectural decisions

```text
NEXT_ARCHITECTURAL_DECISION_1 =
    PRODUCT LINE OF RECORD AND DEV-INFRASTRUCTURE BOUNDARY
```
Decide which lineage is the basis for **product substrate** work (this
review's assessment favors the EN-line as the base). Decide which OW / OC /
transfer deltas must converge into it: Gate D GUI render work, OC-1…5
semantics, the booklet creep fix, governance documents. Declare File Factory,
Orchestrator Operator Workplace, Stage 2C and D01 a **separate
development-infrastructure boundary** with its own name, with no product
runtime dependency on it, and with its expansion frozen until the product
vertical slice exists. *This unblocks every later step and commits to no Git
strategy.*

```text
NEXT_ARCHITECTURAL_DECISION_2 =
    ADOPT A MINIMAL PRODUCT OPERATION RECORD WITH AN ADMISSIBILITY OUTCOME
```
Define one product-runtime contract for "an operation was applied to
artifacts". It covers kind/version, inputs, parameters and policy profile,
engine/writer identity, diagnostics, an admissibility decision (auto / warned
/ operator-accepted deviation / blocked, with actor and reason), outputs into
PFM, verification and provenance. It generalizes the Generated Result
Profile registry, uses the Command API manifesto's known-bad / unknown-bad
semantics, and explicitly does **not** reuse File Factory domain objects.
*This prevents per-module duplication and is the base for batch, Jobs and
the agent.*

```text
NEXT_ARCHITECTURAL_DECISION_3 =
    PAGE GEOMETRY IS THE SINGLE GEOMETRY AUTHORITY; DEFINE FRAMEBOX IS ITS FIRST OPERATION
```
Declare the engine-neutral PageGeometry layer the only producer of
layout-box and relative geometry for GUI, report and operations. Retire
`core.normalize_boxes` as an authority, and move producer-specific heuristics
into named repair diagnostics. Recognize Define Framebox (explicit operator
frame intent, materialized into the one canonical PageGeometry result through
an explicit, structurally recorded mechanism; final materialization policy not
decided; no hidden parallel layout-box precedence) as the first new operation
built on the new stack, delivered with the Manual Trim re-binding
as the end-to-end vertical slice. *This aligns the product's most frequent
operator decision with the architecture.*

---

## 22. What should explicitly NOT be done yet

- Do not build the full Job system, recipes or Job Trace engine.
- Do not start the product Agentic Layer, external API, cloud/licensing shell
  or commercial packaging.
- Do not open further File Factory expansion (L7B Kandev qualification,
  L8B, L10, new waves beyond those already authorized, D01 kernel work) before
  the product vertical slice.
- Do not transplant lab code (PySide6 GUIs, PyMuPDF content-stream writers)
  into the platform; reimplement from preserved semantics with the lab test
  suites as oracles.
- Do not port N-up or Cut Stack before the placement core and technical
  object model exist.
- Do not design an ISO 19593 / PDF 2.0 production-layer implementation; only
  keep technical objects in a separable structural layer.
- Do not qualify cross-volume promotion unless a deployment need appears.
- Do not delete accepted work, recovery branches or historical records to
  tidy topology.
- Do not perform branch surgery before Decision 1 is made.
- Do not rewrite the legacy GUI wholesale; migrate it capability by
  capability through the vertical slice pattern.

---

```text
RECOMMENDATIONS_MADE = YES (ARCHITECTURE_ONLY, NO IMPLEMENTATION AUTHORIZATION)
CANONICAL_REPOSITORY_ACCESSED = NO
REVIEW_MIRROR_MUTATION = NONE
FACTUAL_BASELINE_MUTATED = NO
```
