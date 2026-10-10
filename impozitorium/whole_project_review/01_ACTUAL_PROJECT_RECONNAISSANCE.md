# 01 — Actual Project Reconnaissance

```text
TASK_ID =
    IMPOZITORIUM_WHOLE_PROJECT_REVIEW_
    ACTUAL_PROJECT_RECONNAISSANCE_01

ROLE =
    INDEPENDENT_WHOLE_PROJECT_ARCHITECTURE_REVIEWER

PHASE =
    FACTUAL_RECONNAISSANCE_BEFORE_JUDGMENT

DOCUMENT_CLASS =
    REVIEW_EVIDENCE_AND_ANALYSIS
    NOT_CANONICAL_PROJECT_TRUTH
    NO_RECOMMENDATIONS

REVIEW_SOURCE =
    Raymond-1968/Imposition_app-review-mirror  (read-only)

CANONICAL_REPOSITORY_ACCESSED =
    NO
```

This document reconstructs what the review mirror shows to exist. It does
not propose a redesign, a target architecture, a technology change, or a
roadmap change. Statements are labelled with an evidence class:

| Label | Meaning |
|---|---|
| `CODE` | observed in source code at the cited branch/path |
| `TEST` | a test file exists at the cited path (tests were **not executed** in this pass) |
| `CONTRACT` | stated in a document that itself records Human acceptance |
| `DESIGN` | stated in a design / policy / roadmap document without implementation |
| `HIST` | historical evidence (older snapshot, recovery branch, superseded record) |
| `LAB` | sandbox / laboratory evidence |
| `INFERENCE` | reviewer inference from the evidence above |
| `NOT_PROVEN` | the repository does not establish it |

Branch short names used throughout:

| Short name | Branch | Tip |
|---|---|---|
| **OW-line** | `derived/agent-hierarchy-policy-accepted-01` (descendant of `docs/operator-workplace-stage5-design-basis-01`) | `ac97bc9` |
| **EN-line** | `docs/oc6d2-b4-human-acceptance-01` (descendant of `engine-neutral-pdf-migration`) | `20c4879` |
| **OC-line** | `derived/oc1-oc5-accepted-publication-01` | `975d3f5` |

---

## Revision note — Bounded Correction 01

```text
CORRECTION_SCOPE =
    operator-runtime epistemic wording            (§21 item 3)
    geometry-path classification                  (§5, §6, C-04)
    freshest H2B Vector AutoBleed evidence        (§15.2)
    remote-publication evidence classification    (§3.4, C-23 removed, M-02)
    mirror-basis proof                            (§1.2, M-05 removed)

ARCHITECTURAL_RECOMMENDATIONS_ADDED =
    NONE

PROJECT_REDESIGN =
    NONE
```

---

## 1. Review basis and mirror identity

### 1.1 Access preflight

```text
REVIEW_MIRROR_ACCESS = PASS
    (attached read-only; cloned; push URL disabled locally;
     no ref, branch, tag, PR or issue created in the mirror)

REVIEW_OUTPUT_ACCESS = PASS
    (Raymond-1968/claude-cloud-sandbox, write scope
     impozitorium/whole_project_review/**)

CANONICAL Raymond-1968/Imposition_app = NOT ACCESSED
```

### 1.2 Mirror ref accounting

Observed with `git ls-remote` against the mirror on 2026-10-10:

```text
HEAD_COUNT = 19
TAG_COUNT  = 1  (legacy-pymupdf-pyqt6-prototype-freeze -> 714ce73, annotated a715c19)
NAMES_MATCH_EXPECTED_LIST = YES (all 19 heads, 1 tag)
TOTAL_REACHABLE_COMMITS = 1607
DEFAULT_BRANCH (origin/HEAD) = main
```

Mirror basis is established by two separate evidence sources:

```text
INDEPENDENT_REVIEWER_DIRECT_CANONICAL_VERIFICATION =
    NOT_PERFORMED
    (canonical repository deliberately not accessed)

REVIEWER_OBSERVATION_OF_MIRROR =
    19 heads + 1 tag; names match the expected list exactly

COORDINATOR_PROVIDED_MIRROR_BUILD_EVIDENCE =
    SOURCE_HEAD_COUNT = 19
    TARGET_HEAD_COUNT = 19
    SOURCE_TAG_COUNT = 1
    TARGET_TAG_COUNT = 1
    SOURCE_REMOTE_STABLE_DURING_ACQUISITION = YES
    UNAUTHORIZED_REF_COUNT = 0
    HEAD_REF_ACCOUNTING = EXACT
    TAG_REF_ACCOUNTING = EXACT
    SOURCE_TO_TARGET_SHA_MISMATCH = NONE
    SOURCE_SNAPSHOT_SHA256 =
        cb8fcbed1758207ae7874176f0452a6bb793576ee0e106f41ca9fa6aca94e1e8
    TARGET_SNAPSHOT_SHA256 =
        cb8fcbed1758207ae7874176f0452a6bb793576ee0e106f41ca9fa6aca94e1e8
    MIRROR_MANIFEST_SHA256 =
        6ca37592127a1da4663ba459684353904960dbab8e874307c52d845167da7140

MIRROR_BUILD_EVIDENCE =
    EXACT SOURCE/TARGET REF ACCOUNTING PROVEN

MIRROR_BASIS =
    PROVEN_BY_PRE_REVIEW_BUILD_EVIDENCE
```

The build evidence was supplied by the Human/Coordinator as part of the
review basis; the manifest file itself is not inside the mirror and the
canonical repository was not accessed to reconfirm it.

### 1.3 Method

- Full history fetched for all 19 heads; detached local worktrees were used
  for the OW-line and EN-line tips.
- Governance read first: `AGENTS.md`, `doc/agent_briefing.md`,
  `doc/documentation_index.md`, `doc/current_state.md` on both main lines.
- Then targeted reading of decision records, contracts, acceptance records,
  lab boundary documents, and source modules.
- Tests were counted and located but **not executed** (the runtime is
  Windows/PyQt6/PyMuPDF/pikepdf/pypdfium2 and no execution authority was
  part of this pass). Every "accepted" or "qualified" statement below is
  therefore taken from repository records, not re-run.
- No external research was performed.

---

## 2. Live branch topology

### 2.1 Branch table

"vs main" = commits ahead of `main` (`main` is ahead of none of them).

| Branch | Tip | Date | Ahead of main | Observed role |
|---|---|---|---|---|
| `main` | `b699a70` | 2026-04-28 | 0 | default branch; early prototype; stale `HIST` |
| `claude-cloud-sandbox` | `b699a70` | 2026-04-28 | 0 | identical to `main` |
| `createbooklet-outer-bleed-reconciliation` | `f7a80c2` | 2026-07-20 | 948 | historical fix point; ancestor of every later line |
| `page-geometry-non-proportional-writer-fix` | `bcc1e44` | 2026-07-20 | 949 | historical fix point; **last common ancestor of OW-line and EN-line** |
| `manual-trim-tool-checkpoint` | `c7ea34d` | 2026-09-08 | 1085 | platform working line (historical name); ancestor of OW-line |
| `docs/operator-workplace-stage5-design-basis-01` | `db95756` | 2026-10-07 | 1293 | File Factory / Operator Workplace development line; base of all four newest branches |
| `derived/agent-hierarchy-policy-accepted-01` | `ac97bc9` | 2026-10-09 | 1295 | accepted derived publication (policy docs) on top of `db95756` |
| `harvest/workstation-docs-h1-01` | `cb5bd89` | 2026-10-08 | 1295 | accepted documentation harvest on top of `db95756` |
| `sandbox/booklet-folding-lab` | `c4021c8` | 2026-10-08 | 1295 | living lab lineage on top of `db95756` |
| `sandbox/vector-autobleed-lab` | `c8c65c5` | 2026-10-09 | 1295 | living lab lineage on top of `db95756` |
| `derived/oc1-oc5-accepted-publication-01` | `975d3f5` | 2026-10-07 | 1089 | accepted derived publication (Optional Content OC-1…OC-5 code + records); forks from `0685907` (2026-09-07) on the `manual-trim-tool-checkpoint` lineage |
| `engine-neutral-pdf-migration` | `3e22b05` | 2026-10-04 | 1159 | engine migration line (Course D, OC-6, Platform File Management) |
| `docs/oc6d2-b4-human-acceptance-01` | `20c4879` | 2026-10-04 | 1182 | EN-line tip: successor file/artifact lifecycle phases 1–6 on top of `engine-neutral-pdf-migration` |
| `pdfium-gate-c-conformance-correction-03` | `f8f1e5c` | 2026-08-14 | 1134 | PDFium preview Gate C correction; forks from EN-line at `466da2c`; not merged anywhere except into `stage8-…` |
| `stage8-combined-process-test-harness-correction-02` | `7d472bd` | 2026-08-15 | 1137 | Stage 8 harness correction on top of Gate C correction 03; not merged |
| `transfer/create-booklet-backend-2026-09-30` | `5c15756` | 2026-09-30 | 952 | single transfer commit (creep clipping fix + technical numbering) on top of `9c33510` (2026-07-21) |
| `recovery/raster-quantization-candidate-20260804` | `88b8e61` | 2026-08-07 | 1132 | `UNREVIEWED_RECOVERY_CANDIDATE` (commit message) |
| `recovery/main-preview-prototype-residue-20260807` | `1c2e27e` | 2026-08-07 | 953 | `HISTORICAL_UNREVIEWED_RECOVERY_RESIDUE`, `HUMAN_ACCEPTANCE: NOT_GRANTED` |
| `recovery/preaudit-high-value-untracked-snapshot-20260807` | `ab1639e` | 2026-08-07 | 954 | `RECOVERY_SNAPSHOT_ONLY`, `HUMAN_ACCEPTANCE: NOT_GRANTED` |

Tag `legacy-pymupdf-pyqt6-prototype-freeze` → `714ce73` (2026-07-18,
"Checkpoint legacy PDF migration workspace plan"), an ancestor of every
non-`main` line. `HIST`.

### 2.2 Shape

```text
main (b699a70, 2026-04-28)
 └─ … legacy freeze tag 714ce73 (2026-07-18)
     └─ f7a80c2 createbooklet-outer-bleed-reconciliation
         └─ bcc1e44 page-geometry-non-proportional-writer-fix   <-- last common ancestor
             ├─ OW lineage ─ manual-trim-tool-checkpoint (c7ea34d)
             │                └─ docs/operator-workplace-stage5-design-basis-01 (db95756)
             │                     ├─ derived/agent-hierarchy-policy-accepted-01
             │                     ├─ harvest/workstation-docs-h1-01
             │                     ├─ sandbox/booklet-folding-lab
             │                     └─ sandbox/vector-autobleed-lab
             │           (0685907 on this lineage) └─ derived/oc1-oc5-accepted-publication-01
             ├─ EN lineage ─ engine-neutral-pdf-migration (3e22b05)
             │                └─ docs/oc6d2-b4-human-acceptance-01 (20c4879)
             │          (466da2c) └─ pdfium-gate-c-conformance-correction-03 └─ stage8-…-02
             ├─ 9c33510 └─ transfer/create-booklet-backend-2026-09-30
             └─ recovery/* (three branches)
```

Facts (`CODE` / git):

- **No branch has been merged into `main` since 2026-04-28.** `main`
  contains 86 files; the line tips contain 1,300–2,324 files.
- OW-line and EN-line share **no commits after 2026-07-20**:
  346 commits are OW-only (2026-07-21 … 2026-10-09) and 233 are EN-only.
- Subject distribution of the divergent commits (commit-message grep):
  "File Factory" 44 / "Kandev" 56 / "Gate D" 25 are OW-only;
  "Stage 8" 25 / "Gate C" 12 / "Page Geometry" 11 / "OC-6" 8 / "Course D" 2
  are EN-only (`INFERENCE` from message text).
- The Agent Hierarchy Policy records
  `PERMANENT REPOSITORY / BRANCH / WORKTREE TOPOLOGY: NOT_DECIDED`
  (`CONTRACT`, OW-line `doc/agent_orchestration/IMPOZITORIUM_AGENT_HIERARCHY_POLICY_ACCEPTED_DERIVED_01.md` §8, §12, §15).
  No document in the mirror nominates a single canonical integration branch.

---

## 3. Documentation authority map

### 3.1 Shared entry documents

`AGENTS.md` and `doc/agent_briefing.md` are byte-identical on OW-line and
EN-line. `AGENTS.md` declares: read `AGENTS.md` and
`doc/documentation_index.md`; "current code is the source of truth when old
docs describe abandoned ideas"; PyMuPDF default rendering; persistent shell;
crop marks belong to imposition/export modules.

### 3.2 The two main lines route authority differently

| Item | OW-line | EN-line |
|---|---|---|
| `doc/documentation_index.md` | 3,973 lines; begins with File Factory Astra/Wave-01/02/03 status; "Core Rule" routes first-time orientation to `agent_briefing.md` **and `current_state.md`** | 1,487 lines; begins with "Current Course D / Engine Migration Routing"; routes to `course_d_final_closure_and_reconciliation_2026_07_29.md` and D-08; states `current_state.md` and `project_review_for_codex.md` **are historical snapshots, not current authority** |
| `doc/current_state.md` | 5,393 lines; extended in place as the File Factory current-state ledger | 490 lines; prefixed with `HISTORICAL_SNAPSHOT_NOT_CURRENT_AUTHORITY` (reconciled 2026-07-29); body = 2026-06-14 snapshot |
| Declared source priority | Blueprint 08 §1: repository state > Human-accepted records > registered audits > plans/evidence > routing docs > parent blueprint > task | Index: Human acceptance + D-01…D-08 > accepted contracts > dated roadmap + index overlay > implementation/evidence records > working plans > historical snapshots |
| Agent Hierarchy Policy | present (derived publication) | absent |

### 3.3 Authority documents per area (as routed by the repository)

| Area | Authoritative source(s) observed | Class |
|---|---|---|
| Project governance / roles | OW-line `doc/agent_orchestration/IMPOZITORIUM_AGENT_HIERARCHY_POLICY_ACCEPTED_DERIVED_01.md` + publication acceptance record | `CONTRACT` |
| Engine ownership (render / structural / PyMuPDF sunset / filesystem) | EN-line `doc/engine_migration_decision_d01…d08_2026_07_29.md`, `doc/course_d_final_closure_and_reconciliation_2026_07_29.md` | `CONTRACT` |
| Optional Content | OC-line `doc/pdf_optional_content_audits/*OC_1…OC_5*` (evidence/review/acceptance triplets); EN-line `doc/pdf_optional_content_audits/…OC_6_MIGRATION_CONFORMANCE_PREREQUISITE_ROADMAP_ADDENDUM_01.md` and `doc/IMPOZITORIUM_OC_6*` | `CONTRACT` |
| File Management lifecycle | EN-line `doc/IMPOZITORIUM_FILE_MANAGEMENT_POST_AUDIT_ROADMAP_01.md`, OC-6B*/6C/6D* records, successor phase 1–6 records | `CONTRACT` |
| File Factory | OW-line `doc/agent_orchestration/IMPOZITORIUM_FILE_FACTORY_CURRENT_PROJECT_BLUEPRINT_0x.md` (Blueprint 07 accepted; Blueprint 08 file header says `AUTHORED_CANDIDATE_PENDING_INDEPENDENT_REVIEW`, a separate acceptance record exists), Backend Construction Roadmap 02, Astra audit + Wave records | `CONTRACT` |
| Orchestrator Operator Workplace | OW-line `doc/agent_orchestration/IMPOZITORIUM_ORCHESTRATOR_OPERATOR_WORKPLACE_CONTRACT_01.md` (`HUMAN_ACCEPTANCE: NOT_GRANTED` in its own header), Stage 0–5 documents | `DESIGN` / mixed |
| Geometry | `doc/page_geometry_contract.md` (`Status: Draft`, v0.1); `doc/impositorium_engine_neutral_geometry_coordinate_space_diagnostic_boundary_contract.md` (routed as normative contract); `doc/box_policy_standard.md` | `DESIGN` / `CONTRACT` |
| Product direction (Operation Registry, Jobs, Agent) | `doc/application_stack_and_operation_registry_policy.md` (`Platform Direction / Documentation Only`), `doc/platform_command_api_manifesto.md` | `DESIGN` |
| Labs | `sandbox/<lab>/…_LAB_BOUNDARY.md` on each lab branch + H2A/H2B harvest acceptance records | `CONTRACT` (boundary) / `LAB` (content) |
| Prior whole-repo audit | OW-line `doc/impositorium_full_read_only_reconstruction_audit_2026-07-17.md` (on `manual-trim-tool-checkpoint`, 2026-07-17) | `HIST` |

### 3.4 Observations on the routing documents

- Both indexes combine a routing table with an append-only historical ledger
  (`INFERENCE`; also stated by the 2026-07-17 audit, `HIST`).
- Repository evidence gap (not an architectural finding): some acceptance
  records state that remote publication was not authorized at that
  acceptance-publication stage (Agent Hierarchy derived publication
  acceptance, H1 harvest acceptance), and the corresponding branches exist on
  the remote copied by the mirror. The later Human authorization that
  permitted the remote push is not materialized in this repository snapshot.
  No governance violation is inferred (see §20, M-02).

---

## 4. Actual architectural domains

Domains derived from code and records (not from the task's candidate list).
"Line" = where the code lives.

| # | Domain | Main location | Line(s) | Code size signal |
|---|---|---|---|---|
| D1 | Preflight diagnostics & report | `preflight/core.py`, `report*.py`, `ocg_diagnostics.py`, `platform_diagnostics.py` | all | `CODE` |
| D2 | Persistent GUI shell (PyQt6) | `preflight_gui/` (`window.py`, `preview.py`, `rulers.py`) launched by `main.py` / `run_preflight.py` | all (3 variants) | `CODE` |
| D3 | Page geometry model | `preflight/page_geometry.py` (PyMuPDF), `preflight/engine_neutral_geometry.py` (pure Python) | all (EN and OW versions differ) | `CODE` |
| D4 | Page Geometry transform ("Size & Crop") | `preflight/page_geometry_transform.py`; EN adds `page_geometry_integrated_route.py`, `page_geometry_output_writer.py` (pikepdf) | all / EN | `CODE` |
| D5 | Manual Trim | `preflight_gui/modules/manual_trim/tool.py`, `preflight/manual_trim_*.py`; EN adds `manual_trim_output_writer.py` (pikepdf), `manual_trim_generated_result_adapter.py` | all / EN | `CODE` |
| D6 | Rotation compatibility gate & normalizer | `preflight/rotation_compatibility_gate.py`, `rotation_normalizer.py`; lab copy in VAB | all / LAB | `CODE` |
| D7 | Optional Content (OCG/OCMD) | OC-line `preflight/optional_content*.py`; EN-line OC preservation inside `manual_trim_output_writer.py` | OC / EN | `CODE` |
| D8 | Rendering / preview | PyMuPDF in GUI; PDFium: OW `pdfium_backend.py` + `preflight_gui/pdfium_worker.py`; EN `renderer.py` + `renderer_pdfium.py`; Gate C on its own branch | all, divergent | `CODE` |
| D9 | Structural PDF writing | PyMuPDF (legacy export, Step & Repeat) / pikepdf (EN writers) | all / EN | `CODE` |
| D10 | Working Document / Preview Result / Candidate / Acceptance | `preflight/preview_result.py`, `working_document_candidate.py`, `working_document_acceptance*.py`; GUI save-as path | all | `CODE` |
| D11 | Platform File Management | `preflight/platform_file_management_*.py` (9 modules OW, 17 EN) | all / EN extended | `CODE` |
| D12 | Shared headless registries | `preflight/cut_mark_profile_registry.py`, `signature_profile_registry.py`, `technical_font_bundle_registry.py`, PreCollate/catalog docs | all | `CODE` |
| D13 | Step & Repeat | `step_repeat/` (legacy PyMuPDF engine + GUI window via `snr.py`); `sandbox/step_repeat_seed/` | all | `CODE` / `LAB` |
| D14 | Create Booklet | `sandbox/booklet_pipeline_lab/` + 32–33 `doc/create_booklet_*.md` | all / transfer | `LAB` / `DESIGN` |
| D15 | Booklet Folding / signature imposition | `sandbox/booklet_folding_lab/` | lab branch only | `LAB` |
| D16 | Vector AutoBleed | `sandbox/vector_autobleed_lab/` | lab branch only | `LAB` |
| D17 | Future placement modules (N-up with Background, Cut Stack, Numbering/Text Overlay) | `doc/future_placement_modules_foundation.md` (`Status: Draft`) | all | `DESIGN` |
| D18 | Product Operation Registry / Jobs / Agent / commercial shell | `doc/application_stack_and_operation_registry_policy.md`, `doc/platform_command_api_manifesto.md` | all | `DESIGN` |
| D19 | File Factory (development orchestration backend) | `operator_workplace/` (canonical_core, durable_core, controller_runtime, l3, l4, l5, l7, l9a) ≈14.1k Python lines | OW | `CODE` |
| D20 | Stage 2C reviewer / Kandev runtime | `stage2c/runtime/`, `tools/qualification/kandev_v0_95_0/` | OW | `CODE` |
| D21 | Windows D01 kernel minifilter source | `operator_workplace/windows_d01_source/` (C, `fltKernel.h`) | OW | `CODE` |
| D22 | Agent governance / HumanGate / publication | Agent Hierarchy Policy, acceptance/review record conventions | OW (policy) / all (practice) | `CONTRACT` |
| D23 | Normalizer | `normalizer/` (6 files) | all | `CODE` (briefing: "not a mature active pipeline") |
| D24 | Other research / sandboxes | 60 `sandbox/` directories (24 `*_fixture_lab`), `pdf_risk_probe`, `finishing_contour_imposition_lab`, `weekend_share_scout`, `icon_asset_lab`, `research/page_geometry_phase1`, `tools/laboratories/pdfium_phase_a` | all | `LAB` |

`ARCHITECTURAL_DOMAINS_IDENTIFIED = 24`

**"Define Framebox"**: zero occurrences of `framebox`, `frame box` or
`define frame` in any of the 19 branches. `NOT_PROVEN` (see M-01). The
2026-07-17 audit uses the product name "Size & Crop over Page Geometry"
(`HIST`).

---

## 5. Ownership map

| Domain / question | Primary owner (observed) | Secondary / transitional | Status | Evidence |
|---|---|---|---|---|
| Geometry semantics (value model) | EN `preflight/engine_neutral_geometry.py` (schema `engine-neutral-geometry-v1`, pure Python, no backend) | OW has a different version of the same file; `preflight/page_geometry.py` (PyMuPDF-based PageGeometry with layout priority) | `REAL_BUT_TRANSITIONAL`; **AMBIGUOUS across lines** | `CODE`; EN index row "Engine-Neutral Geometry Core Implementation" |
| GUI-facing box semantics | `preflight/core.py::normalize_boxes` (TrimBox→BleedBox→MediaBox basis, Corel shift heuristic) | `page_geometry.py` (TrimBox→ArtBox→CropBox→MediaBox) | `REAL_BUT_TRANSITIONAL` — `page_geometry.py` carries the accepted/intended policy; legacy `core.normalize_boxes` path not yet displaced (legacy implementation drift, C-04) | `CODE` EN `preflight/core.py:176-225`, `preflight/page_geometry.py:60-70` |
| Rendering | PyMuPDF in GUI (`preflight_gui/window.py` `get_pixmap`) | PDFium: OW opt-in `--preview-engine pdfium_d2`; EN backend-only provider `preflight/renderer.py` → `renderer_pdfium.py` | `REAL_BUT_TRANSITIONAL` | `CODE`; D-01 `CONTRACT` |
| PDF structural mutation | PyMuPDF (legacy Manual Trim export, Step & Repeat, GUI Save As) | pikepdf/qpdf (EN `manual_trim_output_writer.py`, `page_geometry_output_writer.py`, PFM verifier/promotion) | `REAL_BUT_TRANSITIONAL` | `CODE`; D-02 `CONTRACT` |
| File identity / artifact lifecycle (product) | Platform File Management (`preflight/platform_file_management_*`) | legacy shell (`preflight_gui/window.py` working document / preview result / save-as / cleanup) holds temporary authority | `TRANSITIONAL_DUAL_OWNERSHIP` (declared) | D-04, D-05 `CONTRACT`; `CODE` |
| Provenance / receipts (product) | EN PFM verification receipt, successor finalization | — | `PARTIALLY_IMPLEMENTED` (not wired to GUI) | `CODE`, `TEST` |
| Persistence (product) | SQLite inside `preflight/platform_file_management_*` (schema v4; successor schema v5 recorded in phase 6) | — | `REAL_AND_IMPLEMENTED` headless; not GUI-wired | `CODE` |
| Persistence (File Factory) | `operator_workplace/durable_core/store.py` (SQLite: `durable_meta`, `canonical_state`, `durable_operations`) | — | `REAL_AND_IMPLEMENTED` (dev infrastructure) | `CODE` |
| Operation state (product) | none in code | Operation Registry described as future | `DESIGN_INTENT` | `DESIGN` |
| Operation / Job state (File Factory) | `operator_workplace/canonical_core` (`JobKind` = IMPLEMENTATION / REVIEW / CORRECTION / RECONCILIATION; WorkUnit; AuthorityUnit; Incident) | — | `REAL_AND_IMPLEMENTED` (dev infrastructure) | `CODE` `operator_workplace/canonical_core/types.py` |
| Review / admission state | File Factory P0 review-context admission (`canonical_core/review_context_*`) | Human records in `doc/` for everything else | `REAL_AND_IMPLEMENTED` (File Factory) / document practice (project) | `CODE`, `CONTRACT` |
| Recovery / restart | File Factory `durable_core/recovery.py`, `controller_runtime/restart_classifier.py`; EN PFM successor recovery coordinator | — | `REAL_AND_IMPLEMENTED` (two separate subsystems) | `CODE` |
| GUI layout semantics | `preflight_gui/` shell (three variants: OW, EN, OC) | module panels (`modules/manual_trim`, `modules/shell_cleanup`) | `REAL_AND_IMPLEMENTED`, **BRANCH-DIVERGENT** | `CODE` |
| Technical marks today | legacy `step_repeat/backend/engine.py::_draw_cutmarks`; Booklet Folding Lab; booklet_pipeline_lab technical numbering (transfer branch) | `preflight/cut_mark_profile_registry.py` (headless, consumed only by `sandbox/step_repeat_seed`) | **AMBIGUOUS** (four owners) | `CODE`, `LAB` |
| Technical marks later | not decided | Booklet lab boundary: "Any platform-wide technical-layer model … requires a separate platform review" | `DESIGN_INTENT` | `CONTRACT` (lab boundary) |
| Governance / HumanGate | Human Owner (Agent Hierarchy Policy) | File Factory encodes `HumanDecision` enum | `ACCEPTED_CONTRACT` + partial code in File Factory | `CONTRACT`, `CODE` |

`OWNERSHIP_AMBIGUITIES = 4` (rows marked AMBIGUOUS: geometry value model
across lines, GUI shell variants, technical marks today, plus the
product/File-Factory "Job" ownership split in §13). Layout-box selection is
classified as transitional legacy drift, not as an ownership ambiguity
(Bounded Correction 01).

---

## 6. Geometry policy and implementation map

| Topic | Accepted platform law | Current implementation | Migration target | Lab |
|---|---|---|---|---|
| Layout-box selection | `TrimBox -> ArtBox -> CropBox -> MediaBox` ("future policy" in `agent_briefing.md`; engine-neutral contract "preserves the existing layout priority") | newer `page_geometry.py` implements it; the legacy **`core.normalize_boxes` (report/GUI) path still uses TrimBox → BleedBox → MediaBox** and a Corel-specific CropBox shift (legacy implementation drift; not displaced yet) | engine-neutral `PageGeometry` with explicit box provenance | VAB copies the platform box documents unchanged |
| Absolute vs relative | contract separates backend-absolute and GUI-relative geometry (`page_geometry_contract.md`, Draft) | `core.normalize_boxes` returns GUI-relative rects (TrimBox origin = 0) and does not expose absolute rects; `page_geometry.py` exposes both | engine-neutral spaces: `PDF_NATIVE_PAGE_SPACE`, `PAGE_MEDIA_SPACE`, `PAGE_LAYOUT_SPACE`, `IMPOSED_SHEET_SPACE`, raster/widget/device pixel | — |
| GUI representation | points in core, mm in GUI (`AGENTS.md`) | as stated (`CODE`) | engine-neutral contract: top-left, x-right/y-down unrotated platform spaces, raw bottom-left PDF evidence retained | labs: points in backend, mm in GUI |
| Normalize-to-Zero | "original note describes a normalize-to-zero internal model `Point_Internal = Point_PDF - MediaBox.Origin`" (`doc/pdf_preflight_readme_3.md`) | `core.normalize_boxes` explicitly does **not** subtract MediaBox origin (comment) and zeroes on the layout basis instead | EN acceptance: `NEGATIVE_MEDIABOX_ORIGIN: ACCEPTED` for the pikepdf Manual Trim writer | VAB fixture `stage6_negative_origin_rotate_90.pdf` |
| Rotation | `AGENTS.md`: preview rotation-aware, must not be ignored; contract: rotation visible to backend | `rotation_compatibility_gate.py`, `rotation_normalizer.py` (PyMuPDF) | EN index: `ROTATION_NORMALIZATION_SANDBOX_REFERENCE = REGISTERED`, `PLATFORM_ADOPTION = NOT_OPENED` | VAB `rotation_normalization.py` (RN01–RN06 closed in sandbox) |
| MediaBox origin | as above | PyMuPDF rects keep raw origin | pikepdf writer: raw box presence semantics accepted | — |
| Step & Repeat object geometry | `doc/step_and_repeat_math.md` (effective size `W_obj + 2b`) | legacy engine: "imposition strictly from TrimBox", clip = TrimBox, bleed added on sheet | `ImpositionSheetSizeCatalog` runtime contract (documentation) | `step_repeat_seed` planner (87 tests per its README) |
| Gap semantics | math note: gaps `s_X`, `s_Y` between objects | legacy engine: `hgap`/`vgap` between TrimBox tiles; `cols = (sheet_w - 2*edge + hgap) // (pw + hgap)` | PHASE_12S "gap/margin policy clarification" in seed sandbox | Booklet lab: crop gap 2 mm + length 5 mm; derived central gap (design notes) |

Distinction summary:

```text
ACCEPTED PLATFORM LAW     = layout priority (as stated), pt/mm separation,
                            GUI geometry != PDF-write geometry
CURRENT IMPLEMENTATION    = TRANSITIONAL_DUAL_GEOMETRY_PATH:
                            page_geometry.py implements the accepted policy;
                            legacy core.normalize_boxes still implements older
                            behavior (LEGACY_IMPLEMENTATION_DRIFT);
                            PyMuPDF rects as GUI geometry
MIGRATION TARGET          = engine-neutral value model (implemented on EN,
                            not yet consumed by GUI)
LAB EXPERIMENT            = rotation normalization (VAB), signature geometry
                            (Booklet Folding)
```

---

## 7. PDF engine responsibility map

### 7.1 Declared dependencies

- `requirements.txt` (OW and EN identical): `PyQt6`, `PyMuPDF`,
  `pypdfium2==5.12.1`. **pikepdf is not in `requirements.txt` on any line.**
- EN only: `requirements-page-geometry-design-b-cp310.lock.txt`
  (`pikepdf==10.10.0`, `PyMuPDF==1.26.7` "preserved oracle"),
  `requirements-pdfium-production-cp310.lock.txt` (pypdfium2 5.12.1,
  PDFium build 7947, `HUMAN_ACCEPTED`), Stage 8 PDFium lock.
- Labs import `fitz` (PyMuPDF) and **PySide6**, not PyQt6.

### 7.2 Responsibility matrix (current code)

| Engine | READ | WRITE | STRUCTURAL MUTATION | BOX HANDLING | ROTATION | CONTENT PRESERVATION | OPTIONAL CONTENT | RENDER / PREVIEW | VALIDATION |
|---|---|---|---|---|---|---|---|---|---|
| PyMuPDF (`fitz`) | all lines: core, page_geometry, GUI | legacy Manual Trim export, Step & Repeat, GUI Save As, labs | yes (legacy) | yes (core, page_geometry) | yes (gate/normalizer) | `show_pdf_page` reuse | OC-line `optional_content*.py`; `ocg_diagnostics.py` | GUI preview default on all lines | PDFium Phase A fixtures use `pymupdf` as tooling |
| pikepdf / qpdf | EN only | EN `manual_trim_output_writer.py`, `page_geometry_output_writer.py` | EN writers (backend only) | raw box presence semantics | negative MediaBox origin accepted | `PYMUPDF_WRITER_DEPENDENCY: NONE` for D1 | `OC_PRESERVATION: ACCEPTED_FOR_D1_QUALIFIED_SCOPE` | — | EN `platform_file_management_candidate_verifier.py` |
| PDFium (pypdfium2) | OW `pdfium_backend.py`; EN `renderer_pdfium.py` | — | — | — | render-side | — | — | OW: GUI opt-in `pdfium_d2`; EN: `PRODUCTION_ACTIVATION: BACKEND_ONLY` (used by MT writer), `SILENT_PYMUPDF_FALLBACK: NONE` | Stage 8 render tests |

### 7.3 Current ownership vs migration intent

```text
CURRENT RENDER OWNER (GUI)           = PyMuPDF                       (CODE, all lines)
TARGET RENDER OWNER                  = PDFium, capability by capability   (D-01 CONTRACT)
CURRENT STRUCTURAL OWNER (GUI path)  = PyMuPDF                       (CODE)
TARGET STRUCTURAL OWNER              = pikepdf/qpdf                  (D-02 CONTRACT)
PYMUPDF END STATE                    = absent from production runtime; global and
                                       capability fallback prohibited  (D-03 CONTRACT)
EN STATUS                            = writer/renderer backends exist, NOT lifecycle-bound,
                                       NOT GUI-bound                   (EN index)
EXECUTION ROADMAP                    = CORRECTED_PROPOSED_NOT_ACCEPTED; ACTIVE_IMPLEMENTATION_STREAM = NONE
                                       (EN index header)
```

`AGENTS.md` ("Default PyMuPDF rendering") and
`application_stack_and_operation_registry_policy.md` ("Python / PyMuPDF PDF
engine") describe the pre-D-01/D-02 state (see C-05).

---

## 8. Artifact lifecycle map

| Concept | Status | Evidence |
|---|---|---|
| Source PDF (sacred, not overwritten) | `ACCEPTED_CONTRACT` + implemented in GUI save/cleanup guards; EN acceptance `SOURCE_IMMUTABILITY: ACCEPTED` | `AGENTS.md`, `agent_briefing.md`; `CODE` `preflight_gui/window.py` |
| Preview Result | `REAL_AND_IMPLEMENTED` in legacy GUI (Manual Trim creates it; cleanup of registered preview results) | `CODE` `preflight/preview_result.py`, `window.py` `_registered_preview_result_cleanup_paths` |
| Working Document | `REAL_AND_IMPLEMENTED` (legacy GUI `working_kind`, `_load_pdf_path_as_working_document`) | `CODE` |
| Candidate | `PARTIALLY_IMPLEMENTED`: `working_document_candidate.py` consumed by PFM modules and `page_geometry_integrated_route.py`; **not by the GUI** | `CODE` |
| Verification | EN `platform_file_management_candidate_verifier.py` (pikepdf) + external verification receipt | `CODE`, `TEST` |
| Acceptance (artifact) | `working_document_acceptance*.py`; OC-3 adds OC postflight gating on OC-line | `CODE` |
| Generated Result Commit / managed staging / promotion / Current Pointer | EN OC-6B1…6B4 accepted; successor phases 1–6 accepted; `QUALIFIED_SAME_VOLUME_BASELINE`; cross-volume unqualified | `CONTRACT` + `CODE` + `TEST` |
| Save As (final) | legacy GUI Save As implemented (PyMuPDF); D-04 "LEGACY_SAVE_AS_EXECUTION: TEMPORARILY_AUTHORIZED"; phase 6: "no GUI, Save As, production-routing … change" | `CODE`, `CONTRACT` |

Factual transitions:

```text
LEGACY GUI (implemented):
  Open PDF -> Working Document (source) -> Manual Trim Preview Result
  -> Working Document (preview_result) -> Save As (PyMuPDF) ; cleanup of owned temporaries

EN HEADLESS (implemented, not GUI-bound):
  candidate bytes -> candidate verifier (pikepdf) -> verification receipt
  -> Generated Result Commit (Composite Unit of Work, SQLite)
  -> managed staging -> filesystem promotion -> Current Pointer
  -> successor finalization / reader precedence
```

The OC-6 addendum names the full chain as
`… -> accepted/current Working Document -> Save As -> final-byte verification`;
the Save As and final-byte steps are **not** bound in the EN headless chain
(`CONTRACT` phase 6 row: no Save As change).

---

## 9. Production capability map

| Capability | Classification | Backend vs GUI | Evidence |
|---|---|---|---|
| Preflight / diagnostics | `PLATFORM IMPLEMENTATION` | backend + GUI report | `preflight/core.py`, `report*.py`, `preflight_gui/` |
| Manual Trim | `PLATFORM IMPLEMENTATION` (legacy PyMuPDF, GUI-mounted) + `ACCEPTED BACKEND` (EN pikepdf D1 writer, backend-only) | GUI uses legacy export only; EN writer not GUI-bound | `preflight_gui/modules/manual_trim/tool.py` imports `manual_trim_export.export_manual_trim_pdf_v0`; EN index `MANUAL_TRIM_MIGRATION_WRITER` |
| Page Geometry / Size & Crop | `PARTIAL PLATFORM CAPABILITY`: headless transform + EN integrated route + pikepdf writer; GUI panel only in `sandbox/page_geometry_panel_mockup` | backend ahead of GUI | `CODE`; EN tests `test_page_geometry_*` |
| Define Framebox | `NOT_PROVEN` | — | no occurrence |
| Create Booklet | `SANDBOX` (`booklet_pipeline_lab`) + `DESIGN ONLY` platform contracts (32–33 documentation-only docs) | no GUI panel | `doc/create_booklet_*.md` statuses ("Documentation-only", "No Implementation") |
| Step & Repeat | legacy standalone window (`step_repeat/gui`, launched via `snr.py`, **not referenced by `main.py` or `preflight_gui`**) + `SANDBOX` seed (frozen at Phase 13A) | GUI exists but outside the shell | `CODE` |
| Booklet Folding Lab | `STANDALONE LAB` (PySide6 GUI + PyMuPDF engine) | standalone | `sandbox/booklet_folding_lab/`, boundary `PLATFORM_INTEGRATION = NOT_AUTHORIZED` |
| Vector AutoBleed Lab | `STANDALONE LAB` (PySide6 + PyMuPDF; self-described v0.2.2 "certified ready for integration") | standalone | `sandbox/vector_autobleed_lab/`, boundary `PLATFORM_INTEGRATION = NOT_AUTHORIZED` |
| N-up with Background / Cut Stack / Numbering | `DESIGN ONLY` | — | `doc/future_placement_modules_foundation.md` (`Status: Draft`) |
| Optional Content preservation | `ACCEPTED BACKEND` on OC-line (legacy) and EN-line (D1 writer); not on OW-line | — | §15/§18 |
| Rotation normalization | `PLATFORM IMPLEMENTATION` (gate + normalizer) + `SANDBOX` reference (VAB RN01–RN06) | — | `CODE`, EN index |
| PDFium preview | three separate states: OW GUI opt-in; Gate C branch; EN backend-only | — | §17 |
| Shared registries (cut mark, signature profile, font bundle) | `ACCEPTED BACKEND` headless cores without production consumers | — | `CODE`; consumers only in `sandbox/` |
| Raster quantization | `HISTORICAL / UNREVIEWED` | — | `recovery/raster-quantization-candidate-20260804` |

GUI maturity and backend maturity differ for Manual Trim (GUI = legacy,
newest backend = EN pikepdf), Page Geometry (backend only), and File
Management (backend only).

---

## 10. File Management map

| Concern | Observed owner | Status |
|---|---|---|
| File identity | EN PFM schema / artifact acceptance runtime; legacy GUI uses filesystem paths | `TRANSITIONAL_DUAL_OWNERSHIP` (D-04/D-05) |
| File selection | legacy GUI (Qt file dialogs in `window.py`) | `REAL_AND_IMPLEMENTED` |
| Filesystem interaction | legacy GUI (temporary authority, D-04) + EN `platform_file_management_filesystem_promotion.py`, `managed_staging_executor.py` | `TRANSITIONAL_DUAL_OWNERSHIP`; D-05 `ONE_FILESYSTEM_ACTION_ONE_ACTIVE_EXECUTOR: REQUIRED` |
| Canonical artifact references | EN Current Pointer runtime + successor reader | `PARTIALLY_IMPLEMENTED` (same-volume qualified) |
| File lifecycle | `platform_file_management_lifecycle_runtime.py` | `REAL_AND_IMPLEMENTED` headless |
| Working copy behavior | legacy GUI preview result / temp files | `REAL_AND_IMPLEMENTED` |
| Open / Save / Save As | legacy GUI only | `REAL_AND_IMPLEMENTED` (legacy) |
| Artifact persistence | PFM SQLite (schema v4; successor v5) | `REAL_AND_IMPLEMENTED` headless |

`D-05 PLATFORM_TAKEOVER_MODE = CAPABILITY_BY_CAPABILITY`,
`TAKEOVER_UNIT = ONE_ACTION_ONE_ARTIFACT_CLASS_ONE_ROUTE`,
`DUAL_AUTHORITY = PROHIBITED` (`CONTRACT`). No GUI action has been taken
over in code (`CODE`: no `platform_file_management` import under
`preflight_gui/`, `main.py`, `run_preflight.py`).

The OW-line also contains PFM (9 modules) but not the EN additions
(candidate verifier, filesystem promotion, managed staging executor,
successor modules).

---

## 11. File Factory / Controller map

**What it is (`CONTRACT`, Blueprint 08 §2):** "an internal specialized
engineering subsystem for building, maintaining, migrating, and engineering
Impozitorium. It is not a general commercial orchestrator, … Impozitorium
production Job owner, or generalized product-agent platform." Code lives in
`operator_workplace/` on the OW-line only.

| Concern | Owner | Status |
|---|---|---|
| Controller (WorkUnit / Job / canonical state / authority / evidence lineage) | `operator_workplace/canonical_core`, `controller_runtime` | `REAL_AND_IMPLEMENTED` |
| Job / work-unit state | `canonical_core/types.py`, `transitions.py` | `REAL_AND_IMPLEMENTED` |
| Persistence (L2A) | `durable_core/store.py` (SQLite) | `REAL_AND_IMPLEMENTED` |
| Receipts | P0-I4 durable review-context receipt commit gate | `REAL_AND_IMPLEMENTED` |
| Identity / provenance | P0-I1/P0-I2 producer source package and law; P0-CR3 producer provenance | `REAL_AND_IMPLEMENTED` |
| Review admission | P0-I5 Transaction B; Wave-03 S2 runtime binding (`db95756`) | `REAL_AND_IMPLEMENTED` |
| Unknown side effects | `IncidentReason.UNKNOWN_SIDE_EFFECT`; law `UNKNOWN_SIDE_EFFECT -> STOP -> INCIDENT / RECONCILIATION` | `REAL_AND_IMPLEMENTED` |
| Restart recovery | `durable_core/recovery.py`, `controller_runtime/restart_classifier.py`; CR4-B01 retry gate | `REAL_AND_IMPLEMENTED` |
| Incident reconciliation | `ReconciliationDisposition`, L5 integration | `REAL_AND_IMPLEMENTED` |
| Worker identity / execution chassis | L7A chassis-neutral seam implemented; L7B Kandev mapping `NOT_IMPLEMENTED_NOT_AUTHORIZED`; Kandev v0.95.0 `SUCCESSOR_QUALIFICATION_CANDIDATE_ONLY` | `PARTIALLY_IMPLEMENTED` |
| Authority boundaries | `HumanGate = HUMAN_ONLY`; `KANDEV_IS_HUMANGATE = NO` | `ACCEPTED_CONTRACT` + `CODE` (`HumanDecision` enum) |

Layer status (Blueprint 08 §3, `CONTRACT`): L1, L2A, L3, L4, L5, L9A
`HUMAN_ACCEPTED_PUBLISHED_COMPLETE`; L7A accepted; L7 incomplete; L7B, L8B,
L10 not opened; `REAL_FILE_FACTORY_JOB_EXECUTION = NOT_AUTHORIZED`;
`PRODUCTION_ENABLEMENT = NONE`.

Audit state (OW `current_state.md` / index, `CONTRACT`): Astra Structural
Adversarial Audit 01 `OUTCOME_FAIL`, 17 open findings (6 Critical, 11
Major); Wave-01 and Wave-02 implemented and Human-accepted with C8 (re-audit)
pending; Wave-03 S1/S2 accepted per index and commits (see C-02).

**Accepted frontier (as recorded):** next candidate HumanGate
`WAVE_03_HUMAN_AUTHORIZATION_DECISION` in `current_state.md`, while the
index and commits record Wave-03 S1 and S2 as already accepted. The exact
current frontier is therefore `AMBIGUOUS` between the two documents.

**D01 kernel mediation:** C source of a Windows minifilter exists
(`operator_workplace/windows_d01_source/`, S03 native build + DriverEntry
self-test publication recorded). Human acceptance 2026-09-16:
`FILE_FACTORY_V0_KERNEL_D01_CRITICAL_PATH = NO` (`CONTRACT`). The driver
source remains in the tree.

**Naming:** the package is `operator_workplace`, and the governing contract
is the "Orchestrator **Operator Workplace**" — "the human-facing operating
workplace of the Impozitorium agent/code factory … does not define an
Impozitorium production agent or job runtime" (`DESIGN`). It is not the
prepress operator GUI (see C-14).

---

## 12. Governance and authority-flow map

### 12.1 Roles (Agent Hierarchy Policy, `CONTRACT`)

| Role | May | May not |
|---|---|---|
| Human Owner | define intent; accept/change policy; HumanGate; authorize publication | delegate HumanGate; infer acceptance from silence/tests |
| Coordinating Agent | coherence; prepare policies, task packages, acceptance prompts | replace human acceptance; declare readiness from reports |
| Work | gather context; prepare task packages, matrices, handoffs | treat synthesis as decision; change code; conduct HumanGate |
| Lead Codex Agent | decompose and coordinate authorized engineering; evidence package | expand scope; treat tests as acceptance; publish/merge |
| Read-only Reviewer | inspect; return pass / blocking / insufficient evidence | modify; fix-and-accept; change criteria after results |
| Implementation Agent | modify authorized files; tests; records | fix neighbours; accept own work; integrate |
| Test / Evidence Agent | run authorized procedures; verify hashes | change criteria; convert missing evidence into PASS |
| Computer Use | mechanical GUI operation, screenshots | decide correctness; touch live production; accept |

### 12.2 Six-stage separation

```text
planning -> implementation -> execution -> review -> acceptance -> publication
"No stage automatically authorizes the next."           (CONTRACT §4)
```

### 12.3 Where controls live

| Control | Form |
|---|---|
| Human acceptance, HumanGate, publication authorization | **human-only**; recorded as `*_HUMAN_ACCEPTANCE_*.md` documents (`CONTRACT`) |
| Independent review | document practice (`*_INDEPENDENT_REVIEW_*.md`, verdicts A/B/PASS); policy states isolation level "not yet universally defined" |
| Stage separation, scope limits, stop-lines | **policy-only** for project work in general (`CONTRACT`) |
| File Factory authority units, one-shot authority, stale/replay rejection, review admission, incident STOP | **implemented code** in `operator_workplace/` (`CODE`), but `REAL_FILE_FACTORY_JOB_EXECUTION = NOT_AUTHORIZED` |
| Tool/harness enforcement of agent roles | `NOT_PROVEN` (no harness configuration enforcing roles found; Agent Hierarchy §13 authorizes no orchestration code) |
| Identity of accepted artifacts | SHA-256 / commit / tree identities embedded in records (`CONTRACT`); verification of those identities was not re-run here |

Agent authority stops at: acceptance, publication, scope change,
policy/invariant change, topology change (`CONTRACT` §5, §8).

---

## 13. Jobs / Actions / Operation-contract status

| Concept | Product (prepress) | File Factory (development) |
|---|---|---|
| Jobs | `DESIGN_INTENT` / `CONCEPTUAL` — "Jobs are future linear recipes" (`application_stack_and_operation_registry_policy.md` §7) | `IMPLEMENTED` — `JobKind` IMPLEMENTATION / REVIEW / CORRECTION / RECONCILIATION; execution `NOT_AUTHORIZED` |
| Actions | `PARTIALLY_IMPLEMENTED` as legacy GUI actions (Open, Manual Trim Apply, Save As, Close/cleanup); D-05 "action-by-action takeover" defines action as takeover unit | n/a |
| Operations | `DESIGN_INTENT` — "Operation Registry is the future central execution layer" | `IMPLEMENTED` — `durable_operations` table, `controller_runtime/operation_types.py`, operation scope |
| Artifact transition records | `PARTIALLY_IMPLEMENTED` — EN PFM Generated Result Commit / successor finalization (headless) | `IMPLEMENTED` — evidence lineage, receipts |
| Typed operation contracts | `PARTIALLY_IMPLEMENTED` — typed request/result in specific backends (e.g. EN `generated_result_profiles.py` "IMPLEMENTED + AWAITING_FRESH_REVIEW + NOT_HUMAN_ACCEPTED"); no registry | `IMPLEMENTED` — typed commands/requests in `canonical_core` |
| Operation inputs/outputs | per-module only | typed |
| Verification records | EN verification receipt | review-context receipts |
| Evidence relationship | per-capability acceptance documents | `EvidenceKind` enum, L5 |
| Agentic Layer (product) | `CONCEPTUAL` — "future Agent is a controlled interpreter of user intent into formal operations" (`DESIGN`); labs mark `AGENTIC_LAYER = NOT_AUTHORIZED` | — |
| External API | `NOT_STARTED` — no HTTP/server code on any line (no fastapi/flask/aiohttp/http.server) | — |

The word "Job" therefore names an implemented development-infrastructure
concept and a design-only product concept (C-15).

---

## 14. Interaction-surface status

| Surface | Current state |
|---|---|
| GUI | PyQt6 shell (`main.py`, `run_preflight.py`); Manual Trim and read-only shell-cleanup panels mounted; OW adds `--preview-engine {legacy,pdfium_d2}` |
| CLI | no product CLI; `run_preflight.py`/`main.py` argument parsing only for the preview selector (OW); `preflight/ocg_diagnostics.py` argparse; many `scripts/debug/*` and `tools/` evidence scripts |
| Batch | no product batch surface found (`NOT_PROVEN`) |
| Agent | product: `DESIGN_INTENT`; development: File Factory + Stage 2C reviewer runtime (Kandev / "antigravity" worker adapter in `stage2c/runtime/`) |
| External API | none |

No shared product operation layer is present that GUI, CLI, batch and agent
call in common (`CODE`); the Operation Registry is `DESIGN_INTENT`.

---

## 15. Laboratory and sandbox map

### 15.1 `sandbox/booklet-folding-lab` (`c4021c8`)

| Field | Finding |
|---|---|
| Purpose | standalone lab for booklet / signature folding imposition (16p/24p signatures, saddle-stitch and perfect binding models) |
| Implemented | `imposer_a5_signatures_sra3.py` (1,030 lines, PyMuPDF), `gui_signature_imposer.py` (822 lines, **PySide6**), `prototype_16p_signature_fitz.py`, launcher `run_booklet_lab.py` |
| Tests | `tests/test_imposer_creep_semantics.py` (not executed) |
| Unique production knowledge | 3-layer split (pagination / cell geometry / physical production); 16-page pagination formula (declared `INTERNALLY_CONSISTENT`); Lap Shift limits `max_allowed_lap = (sheet_width − 2×trim_width − 2×(crop_gap+crop_length))/2`; creep moves content toward spine with fixed marks; collating staircase mark; fold crosshair; head-to-head 2×2 |
| Overlap with platform | Create Booklet (`booklet_pipeline_lab`), technical marks, signature labels, sheet size catalog |
| Boundary documents | `BOOKLET_FOLDING_LAB_BOUNDARY.md`, `LAB_RULES.md`, `ARCHITECTURE_VERDICT.md`; H2A harvest review + Human acceptance |
| Lab-local | mark placement (`CURRENT_MARK_PLACEMENT = LAB_LOCAL`); GUI; V2 binding policy / V3 tail strategy |
| Upstream concerns stated | platform technical-layer model (possible ISO 19593-aligned separation) needs separate review; `PHYSICAL_BINDERY_QUALIFICATION = REQUIRED`; `CREEP_PHYSICAL_QUALIFICATION = REQUIRED`; signature numbering as future cross-module candidate |
| Integration status | `PLATFORM_INTEGRATION = NOT_AUTHORIZED`, `CREATE_BOOKLET_MERGE = NOT_AUTHORIZED`, `JOBS_INTEGRATION = NOT_AUTHORIZED` |

### 15.2 `sandbox/vector-autobleed-lab` (`c8c65c5`)

| Field | Finding |
|---|---|
| Purpose | mirror-bleed generation around arbitrary TrimBox; box sanitation; rotation normalization; raster fallback |
| Implemented | `gui_vector_autobleed.py` (955 lines, **PySide6**), vector backend (Form XObject + eight clipped reflection CTMs, 0.75 pt inward overlap), `raster_bleed_engine.py` (600 DPI fallback), `rotation_normalization.py`, `rotation_validation.py`, OCG catalog cloning; compiled `dist/VectorAutoBleed_v0.26.exe` referenced |
| Tests | current accepted baseline (H2B fresh independent review + Human acceptance, `doc/agent_orchestration/IMPOZITORIUM_WORKSTATION_UNIQUE_ASSET_HARVEST_H2B_VECTOR_AUTOBLEED_LAB_FRESH_INDEPENDENT_REVIEW_01.md`, `…_H2B_VECTOR_AUTOBLEED_LAB_HUMAN_ACCEPTANCE_01.md`): `LAB_TEST_FILE_COUNT = 11`, `TEST_COUNT = 169`, `PASSED = 169`, `SKIP_COUNT = 0`, `FAIL_COUNT = 0`, `EDGE_INSET_PT = 0.75`, `EDGE_INSET_REPRODUCIBILITY = PROVEN`, `WORKSTATION_RUNTIME_SEMANTICS_PRESERVED = YES`, `UNEXPLAINED_SEMANTIC_DELTA = NONE` (`CONTRACT`; from accepted repository review evidence — not executed in this reconnaissance). The as-built report's "60 passed" for v0.2.2 is a `HISTORICAL LAB-LOCAL RECORD`, not the current accepted baseline |
| Unique production knowledge | negative-CTM mirror construction; seam elimination (center-first order, inset); DeviceCMYK preservation; Transparency Group / ExtGState preservation during sanitation; ArtBox translation |
| Overlap with platform | Page Geometry, rotation gate/normalizer, Optional Content, box policy; lab carries **byte-identical copies** of six platform documents (`page_geometry_contract.md`, `page_geometry_backend_contract.md`, `manual_trim_module_policy.md`, `box_policy_standard.md`, `rotation_compatibility_gate_and_normalizer.md`, `Bleed Reconstruction Policy.md`) |
| Boundary documents | `VECTOR_AUTOBLEED_LAB_BOUNDARY.md`, `AGENT.md`, H2B harvest review + Human acceptance |
| Lab-local | vector/raster bleed semantics (`CURRENT_VECTOR_AUTOBLEED_SEMANTICS = LAB_OWNED`), box/rotation/OCG/PDF-X/ICC assumptions |
| Upstream concerns stated | `STRUCTURAL_PDF_PLATFORM_OWNERSHIP = NOT_GRANTED_BY_THIS_LAB`; rotation lineage partially already published (EN rotation reference registration) |
| Integration status | `PLATFORM_INTEGRATION = NOT_AUTHORIZED`, `PAGE_GEOMETRY_INTEGRATION = NOT_AUTHORIZED`, `PRODUCTION_ENABLEMENT = NOT_AUTHORIZED` |

### 15.3 Other materially relevant sandboxes

| Sandbox | Purpose | Status |
|---|---|---|
| `sandbox/booklet_pipeline_lab` | Create Booklet backend prototype (chunk PDF, creep compensation) | `SANDBOX`; transfer branch holds a newer fix (C-09) |
| `sandbox/step_repeat_seed` | Step & Repeat planner / backend nursery | frozen at Phase 13A; README: "not a production module" |
| `sandbox/*_fixture_lab` (24) | shape fixtures for PFM, cleanup, registry, shell view model, candidate adapters | `LAB` evidence for platform contracts |
| `sandbox/pdfium_rendering_phase_a_lab`, `tools/laboratories/pdfium_phase_a` (EN) | PDFium Phase A | `ACCEPTED_WITH_EXPLICIT_LIMITATIONS` (D-01 basis) |
| `sandbox/finishing_contour_imposition_lab`, `pdf_risk_probe`, `weekend_share_scout`, `pdf_layer_research` | research | `current_state.md` §5 "Sandbox / Research" |
| `sandbox/pdf_oxide_five_box_roundtrip_lab` (OW) | five-box round trip probe | `LAB` (not evaluated) |

```text
SANDBOX != PLATFORM
LAB != PRODUCTION AUTHORITY
```

---

## 16. Technical marks / technical-layer current state

| Mark type | Where implemented | Ownership class |
|---|---|---|
| Crop / cut marks | legacy `step_repeat/backend/engine.py::_draw_cutmarks` (PyMuPDF, offset 3 mm default); Booklet Folding Lab (8 outer marks, 2 mm gap, 5 mm length); `step_repeat_seed/backend/external_cut_mark_geometry.py` | legacy platform code + lab + sandbox |
| Cut-mark profiles | `preflight/cut_mark_profile_registry.py` (families `product_trim_marks`, `chunk_boundary_corner_marks`; builtin/manual/custom) | headless platform core; consumer only `sandbox/step_repeat_seed` |
| Fold marks, folding crosshair | Booklet Folding Lab | `LAB_LOCAL` |
| Collating marks | Booklet Folding Lab (staircase, 6×3 mm, 12 mm step from GUI) | `LAB_LOCAL` |
| Service text / slugs | Booklet Folding Lab; legacy Step & Repeat `insert_textbox` | lab + legacy |
| Signature labels / job signature | `preflight/signature_profile_registry.py`, `technical_font_bundle_registry.py` (headless); H1 `doc/production_policy/create_booklet_signature_placement_policy.md` (documentation-only) | headless core + design |
| Technical page numbering | transfer branch `booklet_pipeline_lab` (`enable_technical_numbering`); Booklet Folding Lab external page numbering | lab / transfer-only |
| Plotter / cutter marks | finishing contour lab (research) | `LAB` |
| Diagnostic preview crop marks | prohibited by `AGENTS.md` ("Do not add crop marks to preview") | `ACCEPTED_CONTRACT` |

Platform policy: `AGENTS.md` places crop marks in imposition/export modules.
A platform-wide technical-layer separation (including any ISO 19593
alignment) is mentioned only as a future separate review in the Booklet lab
boundary → `DESIGN_INTENT`.

---

## 17. Active migration fronts

| Front | Current basis | Current accepted state | Next authorized / unauthorized frontier |
|---|---|---|---|
| Engine-neutral PDF migration (Course D) | EN-line; D-01…D-08 | Course D `CLOSED`; render/structural targets accepted; PDFium declared production dependency (backend only); Manual Trim pikepdf D1 writer accepted | `EXECUTION_ROADMAP_DRAFT = CORRECTED_PROPOSED_NOT_ACCEPTED`; `ACTIVE_IMPLEMENTATION_STREAM = NONE`; `NEXT_GATE = NOT_OPENED`; D2 full lifecycle blocked pending profile + successor acceptance (index header) |
| Optional Content | OC-line (OC-1…OC-5 legacy) + EN (OC-6A…OC-6D2) | OC-1…OC-5 accepted on legacy belt; OC-6B1–6B4, 6C, 6D1, 6D2 B4 readiness accepted | generated-result profile repair `IMPLEMENTED_CANDIDATE_PENDING_INDEPENDENT_REVIEW`; `NEXT_PROPOSED_GATE = FRESH_INDEPENDENT_PROFILE_REPAIR_REVIEW (PROPOSED_NOT_OPENED)` |
| Platform File Management successor | EN tip `20c4879` | phases 1–6 accepted; `QUALIFIED_SAME_VOLUME_BASELINE`; schema v5 | cross-volume unqualified; no GUI / Save As / production routing authorized |
| Page Geometry structural ownership | EN (`page_geometry_output_writer.py`, integrated route, Stage 7/8) **and** OW (`doc/global_migration_roadmap/candidate_01_*` pikepdf intake and Route B legal review preparation) | EN: implementation + tests exist; OW: candidate intake/provenance records | which track governs is `AMBIGUOUS` (C-13) |
| PDFium preview | OW Gate D (D2–D6 accepted per commits); Gate C correction branches; EN Stage 8 | three unmerged states | not proven |
| Rotation normalization | EN reference registration (VAB handoff v0.3.0 zip) | `SANDBOX_REFERENCE_VALIDATED` | `NEXT_ROTATION_GATE = ROTATION_NORMALIZER_PLATFORM_ADAPTATION_RECONCILIATION` (not opened) |
| File Factory evolution | OW `db95756` | L1–L5, L9A, L7A accepted; Wave-01/02 accepted (C8 pending); Wave-03 S1/S2 accepted per index | L7B/L8B/L10 not opened; global re-audit not authorized |
| Orchestrator Operator Workplace | OW Stage 0–5 docs; D01 | Stage 5 D01 S01, S02, S03 (native build + DriverEntry self-test) Human-accepted per records; D01 removed from v0 critical path | contract itself `HUMAN_ACCEPTANCE: NOT_GRANTED` |
| Production-module extraction from sandboxes | Create Booklet docs; Step & Repeat seed; labs | documentation-only boundaries; Step & Repeat seed frozen | labs `PLATFORM_INTEGRATION = NOT_AUTHORIZED` |

---

## 18. Contradiction and ambiguity register

| ID | Category | Area | Evidence A | Evidence B | Why unclear | Current authority status |
|---|---|---|---|---|---|---|
| C-01 | CONTRADICTION | authority of `current_state.md` | EN `doc/current_state.md` header `HISTORICAL_SNAPSHOT_NOT_CURRENT_AUTHORITY`; EN index Core Rule | OW index Core Rule routes orientation to `current_state.md`; OW extends it as current File Factory ledger | same path, opposite authority by branch | branch-local; no cross-line resolution |
| C-02 | DOCUMENTATION_DRIFT | File Factory frontier | OW `current_state.md`: `WAVE_03 = NOT_AUTHORIZED`, `NEXT_CANDIDATE_HUMANGATE = WAVE_03_HUMAN_AUTHORIZATION_DECISION` (last updated `a6142a4`, 2026-10-01) | OW index title "…Wave-03 S1/S2 publication"; commits `2acaf8b` (W3-S1), `db95756` (W3-S2 accepted) | ledger not updated after 2026-10-01 | index + commits newer |
| C-03 | DOCUMENTATION_DRIFT | EN lifecycle status | EN index header: `SUCCESSOR_FINAL_IMPLEMENTATION: NOT_OPENED`, `SCHEMA_IMPLEMENTATION: NOT_OPENED`, `D2_FULL_LIFECYCLE: STILL_BLOCKED` | same index row + `…PHASE_6_HUMAN_ACCEPTANCE_01.md`: phases 1–6 accepted, schema v5, `QUALIFIED_SAME_VOLUME_BASELINE` | header block not updated | acceptance record newer |
| C-04 | TRANSITIONAL_DUAL_OWNERSHIP (legacy implementation drift from accepted/current geometry policy) | layout-box basis | legacy `preflight/core.py::normalize_boxes`: TrimBox → BleedBox → MediaBox + Corel shift + GUI zeroing | newer `preflight/page_geometry.py` (`choose_layout_box`) and `agent_briefing.md`: TrimBox → ArtBox → CropBox → MediaBox | the legacy path has not yet been displaced by the newer implementation | policy-bearing direction = TrimBox → ArtBox → CropBox → MediaBox; one policy, two code paths (`TRANSITIONAL_DUAL_GEOMETRY_PATH`) |
| C-05 | CONTRADICTION | engine statement in entry docs | `AGENTS.md` "Default PyMuPDF rendering"; `application_stack_and_operation_registry_policy.md` "Python / PyMuPDF PDF engine" | D-01 PDFium target, D-02 pikepdf target, D-03 PyMuPDF absent from production | entry docs predate Course D and are shared by both lines | D-01…D-03 accepted on EN only |
| C-06 | BRANCH_DIVERGENCE | `preflight/renderer.py` | OW: `PreviewRenderCoordinator` (GUI PDFium Gate D) | EN: provider registry `create_renderer/render` used by MT writer | same module path, unrelated contents | no line chosen |
| C-07 | BRANCH_DIVERGENCE | PDFium preview | OW Gate D (D2–D6) files `pdfium_backend.py`, `pdfium_worker.py`, `preview_runtime_contract.py` | Gate C implementation only on `pdfium-gate-c-…-03` / `stage8-…-02`; EN has none of these files | three separate PDFium preview states | not proven |
| C-08 | BRANCH_DIVERGENCE | Optional Content code | OC-line `preflight/optional_content*.py`, modified `manual_trim_export.py` (blob `020fda7`) | OW and EN: no `optional_content*.py`; `manual_trim_export.py` blob `804a55a` | accepted OC-1…5 code absent from both main lines | OC-line accepted derived |
| C-09 | BRANCH_DIVERGENCE | Create Booklet backend | transfer `5c15756`: creep clipping fix + technical numbering | all other lines: older `chunk_pdf_prototype.py` | fix exists on one isolated branch | `transfer/` name only; no acceptance record in commit |
| C-10 | TRANSITIONAL_DUAL_OWNERSHIP | structural writing | PyMuPDF writers (legacy) | pikepdf writers (EN) | declared controlled transition | D-02 |
| C-11 | TRANSITIONAL_DUAL_OWNERSHIP | rendering | PyMuPDF GUI default | PDFium backend / opt-in | declared controlled transition | D-01 |
| C-12 | TRANSITIONAL_DUAL_OWNERSHIP | filesystem authority | legacy shell (D-04 temporary authority) | Platform File Management (D-05) | declared; no action taken over in GUI yet | D-04/D-05 |
| C-13 | BRANCH_DIVERGENCE | migration governance | OW `doc/global_migration_roadmap/` Candidate 01 pikepdf Page Geometry intake (2026-08-09) | EN Course D / OC-6 / Page Geometry Stage 7–8 implementation | two migration record sets on two lines | not reconciled in repository |
| C-14 | AMBIGUITY | term "Operator Workplace" | `IMPOZITORIUM_ORCHESTRATOR_OPERATOR_WORKPLACE_CONTRACT_01.md`: development agent/code-factory workplace; package `operator_workplace/` = File Factory | prepress operator shell in `AGENTS.md` / briefing ("operator") | same word, two systems | contract `HUMAN_ACCEPTANCE: NOT_GRANTED` |
| C-15 | AMBIGUITY | term "Job" | File Factory `JobKind` (implemented) | product "Jobs as linear operation chains" (design) | same word, two systems | both documented |
| C-16 | AMBIGUITY | "OC" series scope | OC-1…OC-5 = Optional Content | OC-6B0…6B4, 6D2 = transaction filesystem protocol, staging, promotion, B4 readiness | Optional Content prefix carries File Management lifecycle work | addendum explains the prerequisite chain |
| C-17 | LAB_PLATFORM_SEMANTIC_GAP | GUI toolkit | labs: PySide6 | platform: PyQt6 | GUI code not shell-compatible as is | labs not integrated |
| C-18 | LAB_PLATFORM_SEMANTIC_GAP | Booklet lab self-description | README: "Module UI panels are designed to plug directly into the Impositorium `PDFPreflightGUI`" | implemented GUI is standalone PySide6; boundary `PLATFORM_INTEGRATION = NOT_AUTHORIZED` | README intent vs as-built | boundary governs |
| C-19 | LAB_PLATFORM_SEMANTIC_GAP | VAB readiness claim | `INDEX.md`: "certified … ready for integration review and transfer into `src/`" | boundary: `PLATFORM_INTEGRATION = NOT_AUTHORIZED`; no `src/` directory exists in the repository | lab-local certification vocabulary | boundary governs |
| C-20 | LAB_PLATFORM_SEMANTIC_GAP | technical marks | four producers (§16) | no platform technical-layer policy | ownership not assigned | `DESIGN_INTENT` only |
| C-21 | LAB_PLATFORM_SEMANTIC_GAP | VAB structural writes | VAB writes boxes/bleed with PyMuPDF; OCG preservation by catalog clone | D-02 pikepdf target; platform OC acceptance chain (OC-3 postflight) | lab semantics outside platform OC/engine law | lab-owned |
| C-22 | AMBIGUITY | VectorAutoBleed version | EN index: "VectorAutoBleed v0.3.0" rotation handoff | lab branch `HISTORY.md`: `CURRENT_VERSION = 0.2.2` | possibly separate version streams; not stated | not proven |
| C-24 | HISTORICAL_RESIDUE | default branch | `main` = 2026-04-28 prototype, default branch | all accepted work on unmerged lines | default branch does not represent current work | topology `NOT_DECIDED` (policy) |
| C-25 | DOCUMENTATION_DRIFT | geometry contract status | `doc/page_geometry_contract.md` `Status: Draft`, v0.1, "future" | engine-neutral contract routed as normative; EN core implemented | older draft remains routed | engine-neutral contract newer |
| C-26 | BRANCH_DIVERGENCE | `engine_neutral_geometry.py` | OW version | EN version (diff ≈1,436 lines) | same module path, different content | not reconciled |

Counts:

```text
CONTRADICTION                = 2   (C-01, C-05)
DOCUMENTATION_DRIFT          = 3   (C-02, C-03, C-25)
BRANCH_DIVERGENCE            = 6   (C-06, C-07, C-08, C-09, C-13, C-26)
TRANSITIONAL_DUAL_OWNERSHIP  = 4   (C-04, C-10, C-11, C-12)
AMBIGUITY                    = 4   (C-14, C-15, C-16, C-22)
LAB_PLATFORM_SEMANTIC_GAP    = 5   (C-17 … C-21)
HISTORICAL_RESIDUE           = 1   (C-24)
TOTAL                        = 25

C-23 (remote publication) was removed from the register by Bounded
Correction 01 and is kept only as repository evidence gap M-02.
IDs are not renumbered.
```

---

## 19. Historical / superseded residue

```text
HISTORICAL != CURRENT
```

| Item | Why historical |
|---|---|
| `main` / `claude-cloud-sandbox` (`b699a70`) | 2026-04-28 prototype; no later merge |
| tag `legacy-pymupdf-pyqt6-prototype-freeze` | freeze checkpoint of the PyMuPDF/PyQt6 prototype (2026-07-18) |
| `createbooklet-outer-bleed-reconciliation`, `page-geometry-non-proportional-writer-fix` | fix points fully contained in later lines |
| `recovery/raster-quantization-candidate-20260804` | `UNREVIEWED_RECOVERY_CANDIDATE` |
| `recovery/main-preview-prototype-residue-20260807` | `HISTORICAL_UNREVIEWED_RECOVERY_RESIDUE`, not accepted |
| `recovery/preaudit-high-value-untracked-snapshot-20260807` | `RECOVERY_SNAPSHOT_ONLY` (analyzer, icon, layer research residue) |
| EN `doc/current_state.md`, `doc/project_review_for_codex.md` | declared historical snapshots (2026-06-14) |
| `doc/impositorium_full_read_only_reconstruction_audit_2026-07-17.md` | prior whole-repo audit; predates Course D and File Factory |
| File Factory Blueprints 01–07, Kandev v0.92.1/v0.93.0 lines, Run08/Run09 lineage, Receipt contract revision 1 | superseded by later revisions (Blueprint 08 §4; index) |
| OW/EN PyMuPDF preview path | current but declared transitional (D-01) — not residue, listed for contrast |
| `doc/New Text Document.txt`, `doc/box_policy_standard (2).md/.html`, `doc/pdf_preflight_readme{,_2,_3}.md` | duplicate/placeholder documentation files |
| `operator_workplace/windows_d01_source/` | kernel source retained after D01 removal from v0 critical path |
| VAB structural spike (`spike_mirror_xobject.py`) | "retained as historical evidence; does not prove the superseding v0.2.2 contract" (lab report) |
| Step & Repeat standalone window (`snr.py`) | not launched by `main.py`; shell no longer references it |

---

## 20. Missing context / not proven

| ID | Question | Why repository is insufficient | Source required |
|---|---|---|---|
| M-01 | What is "Define Framebox" and where does it live? | no occurrence of the term on any branch | Human Owner definition / external source |
| M-02 | Repository evidence gap: the mirror contains remotely published branches (`derived/*`, `harvest/*`, `sandbox/*` labs), while their local acceptance documents record that remote publication was not authorized at that earlier acceptance-publication stage. The later Human authorization that permitted the remote push is not materialized in this repository snapshot. No governance violation is inferred. | later Human authorization records are outside the repository | Human/Coordinator publication records |
| M-03 | Which line (OW, EN, OC, or a future one) is the intended integration trunk, and how will OW and EN reconverge? | policy says topology `NOT_DECIDED`; no merge plan found | Human decision |
| M-04 | Byte provenance of originals referenced by derived publications (`a9bb8d6…` Agent Hierarchy basis; `fa40c1cf…` OC legacy reference head) | both commits are absent from the mirror | original local repositories / canonical history |
| M-06 | Do the recorded test results still hold? | tests not executed in this pass; Windows/PyQt6/pikepdf/pypdfium2 runtime | authorized execution environment |
| M-07 | Kandev chassis actual installed version and behavior | Blueprint 08: `CURRENT_LOCAL_DESKTOP_BINARY_VERSION = NOT_PROVEN`; Kandev source is external | workstation evidence |
| M-08 | Licensing / legal basis motivating PyMuPDF exit | Route B legal review preparation exists "does not provide a legal opinion" | legal review outcome |
| M-09 | Physical correctness of booklet creep / lap / duplex | lab marks `PHYSICAL_BINDERY_QUALIFICATION = REQUIRED` | physical specimens |
| M-10 | Relationship between "Size & Crop", "Page Geometry" and any "Framebox" product naming | names used inconsistently across eras | Human product taxonomy |
| M-11 | Which build/branch operators actually use in production today | no release/deployment record found besides the freeze tag and VAB exe reference | release records |
| M-12 | External fixture corpus (A0, A1, BAD_MT) contents | only SHA-256 identities in Git; binaries intentionally not committed | fixture store |
| M-13 | Current role and deployment of the D01 kernel driver source | removed from v0 critical path; later use not stated | Human decision / Operator Workplace records |

`MISSING_CONTEXT_ITEMS = 12`

M-05 (mirror SHA equality) was resolved by coordinator-provided mirror-build
evidence (§1.2) and removed by Bounded Correction 01. IDs are not renumbered.

---

## 21. Factual current-state synthesis

1. The mirror holds 19 heads and 1 tag. The default branch `main` is an
   April 2026 prototype; every later accepted result lives on unmerged
   branches.
2. Since 2026-07-20 the project has two disjoint working lines:
   - the **OW-line** (File Factory development infrastructure, Orchestrator
     Operator Workplace, PDFium preview Gate D, Agent Hierarchy Policy,
     harvests, and the two living labs on top of it);
   - the **EN-line** (Course D engine decisions, PDFium backend renderer,
     pikepdf Manual Trim and Page Geometry writers, Platform File Management
     transaction/staging/promotion/successor lifecycle, OC-6).
   A third accepted code line (**OC-line**) carries OC-1…OC-5 Optional
   Content work on the legacy engine. These lines do not share code for the
   same modules (`renderer.py`, `engine_neutral_geometry.py`,
   `manual_trim_export.py`, `preflight_gui/window.py` differ).
3. The operator-facing implementation observed in the repository is the
   PyQt6 Preflight shell with diagnostics, rulers/overlays and one mounted
   capability, Manual Trim, on the legacy PyMuPDF rendering/writing path, with
   a legacy Working Document / Preview Result / Save As path. Step & Repeat
   exists as a legacy standalone window outside the shell.
   `REPOSITORY IMPLEMENTATION OBSERVED != DEPLOYED PRODUCTION BUILD`: which
   build operators use in production remains `NOT_PROVEN` (M-11).
4. Engine ownership is in a declared controlled transition: PDFium (render)
   and pikepdf/qpdf (structural) are accepted targets and exist as backends
   on the EN-line, but are not bound to the GUI or to Save As.
5. Platform File Management is substantial headless code with SQLite
   persistence and a same-volume-qualified lifecycle on the EN-line; the GUI
   still holds temporary filesystem authority.
6. Create Booklet, Booklet Folding, Vector AutoBleed, Step & Repeat seed and
   many fixture labs are sandbox or lab code; N-up, Cut Stack, Numbering,
   Operation Registry, product Jobs, product Agent and external API exist only
   as design documents.
7. The File Factory is implemented development infrastructure (Controller,
   Jobs of kind IMPLEMENTATION/REVIEW/CORRECTION/RECONCILIATION, durable
   SQLite core, receipts, incidents, review admission). It is documented as
   not being the production Job owner, and its real Job execution is not
   authorized.
8. Governance is an accepted Human-only HumanGate model with six-stage
   separation, recorded through acceptance/review documents. It is enforced in
   code only inside the File Factory; elsewhere it is policy and document
   practice.
9. The register holds 25 items: 2 contradictions, 3 documentation drifts,
   6 branch divergences, 4 transitional dual ownerships (3 declared engine /
   filesystem transitions plus legacy geometry drift), 4 ambiguities,
   5 lab–platform semantic gaps and 1 historical residue item. 12 questions
   cannot be settled from repository evidence. Permanent integration topology
   remains `NOT DECIDED / NOT PROVEN`.

---

```text
RECOMMENDATIONS_MADE = NONE
CANONICAL_PROJECT_MUTATION = NONE
REVIEW_MIRROR_MUTATION = NONE
```
