# 03 — File Factory Minimum Useful Excavator Criteria

```text
DOCUMENT_CLASS =
    ARCHITECTURAL_DECISION_SUPPORT
    + EXECUTION_READINESS_CRITERIA

STATUS =
    HUMAN_ACCEPTED_DIRECTION
    NOT_IMPLEMENTATION_AUTHORIZATION

RELATIONSHIP_TO_REVIEW =
    ADDENDUM_TO
    01_ACTUAL_PROJECT_RECONNAISSANCE.md
    02_SEMANTIC_AND_ARCHITECTURAL_ALIGNMENT_REVIEW.md
```

## 1. Purpose

File Factory is not required to become a polished, market-ready product before it is useful.

Its immediate purpose is to become a **working multi-agent development accelerator** for Impozitorium: a tool that materially reduces human coordination load, frontier-model cost, and/or elapsed engineering time while preserving bounded authority, evidence, review, and HumanGate control.

The target is therefore not:

```text
COMMERCIAL_PRODUCT_READY
```

The target is:

```text
MINIMUM_USEFUL_EXCAVATOR
```

The governing metaphor is explicit:

```text
ENGINE
HYDRAULICS
CONTROLS
BUCKET

not

SHOWROOM FINISH
```

A minimal UX is acceptable. Backend/API effectiveness is the primary value.

---

## 2. Architectural relationship to Impozitorium

The whole-project review establishes two separate concerns:

```text
IMPOZITORIUM PRODUCT SUBSTRATE
    = EN-line architectural basis

FILE FACTORY
    = DEVELOPMENT-INFRASTRUCTURE DOMAIN
```

This distinction remains valid.

However, execution priority is clarified:

```text
FILE_FACTORY_STATUS =
    ACTIVE_PRIMARY_DEVELOPMENT_STREAM

PURPOSE =
    BUILD THE MULTI-AGENT DEVELOPMENT ACCELERATOR
    REQUIRED FOR SUSTAINABLE IMPOZITORIUM CONSTRUCTION

PRODUCT_RUNTIME_DEPENDENCY_ON_FILE_FACTORY =
    FORBIDDEN

PRODUCT_MAY_REUSE_FROM_FILE_FACTORY =
    PATTERNS
    EXPLICITLY_ADOPTED CONTRACTS
    PROVEN GOVERNANCE IDEAS

RETURN_TO_MAJOR_PRODUCT_IMPLEMENTATION =
    AFTER FILE_FACTORY REACHES
    MINIMUM_USEFUL_EXCAVATOR
```

This is not a contradiction.

The product architecture determines **where Impozitorium is going**.
File Factory is the machinery intended to make getting there economically and temporally feasible.

---

## 3. Why the criterion exists

Sequential frontier-model development does not scale economically for the expected size of Impozitorium.

The project now contains:

- structural PDF migration;
- multiple engine boundaries;
- preservation requirements;
- File Management / artifact lifecycle;
- production modules;
- laboratories;
- independent review;
- evidence;
- branch reconciliation;
- future Jobs and Agentic Layer.

Using frontier models for every mechanical subtask wastes both money and human attention.

The intended labor hierarchy is therefore:

```text
FRONTIER MODEL
    architecture
    ambiguity resolution
    difficult reasoning
    decomposition
    integration review
    critical review

SECOND-TIER / LOWER-COST MODELS
    bounded implementation
    repetitive refactoring
    test writing
    evidence collection
    repository inspection
    routine documentation
    mechanical verification

FILE FACTORY
    decomposition support
    dispatch
    workspace isolation
    orchestration
    evidence capture
    review routing
    failure handling
    recovery
    HumanGate preparation
```

The objective is not to replace strong models with weak ones.

The objective is to stop paying strong-model cost for work that does not require strong-model cognition.

---

## 4. Readiness ladder

### L0 — Orchestration Prototype

The system can:

- accept one bounded task;
- send it to one executor;
- collect a result;
- record basic evidence.

This proves the concept only.

### L1 — Controlled Multi-Agent Execution

The system can:

- manage multiple executors;
- isolate workspaces;
- maintain authority boundaries;
- track state;
- stop safely;
- route review;
- return results to HumanGate.

This proves that the engine runs.

### L2 — Minimum Useful Excavator

The system can take a **real bounded Impozitorium engineering package** and move it through a multi-agent implementation/review cycle with materially less human coordination and/or frontier cost than the current sequential workflow.

This is the target gate for resuming major Impozitorium product implementation.

### L3 — Mature Development Factory

Optional later maturity may include:

- polished GUI;
- richer dashboards;
- advanced scheduling;
- sophisticated automatic routing;
- detailed cost optimization;
- multi-user operation;
- broader provider support;
- higher automation.

L3 is **not required** before File Factory is used as the primary development tool.

---

## 5. Minimum Useful Excavator gate

```text
FILE_FACTORY_MINIMUM_USEFUL_EXCAVATOR_GATE
```

### A. Multi-agent execution

File Factory must be able to execute multiple bounded WorkUnits through actual agents, not merely represent them in a data model.

```text
PASS requires:
    real executor invocation
    bounded authority
    observable completion state
```

### B. Parallel WorkUnits

At least 2–4 independent WorkUnits must execute concurrently.

```text
PASS requires:
    no workspace collision
    no output confusion
    no shared-state corruption
    no manual serial launching by Human
```

### C. Workspace isolation

Every WorkUnit must have explicit:

- repository / basis;
- isolated workspace;
- read scope;
- write scope;
- authority;
- expected outputs.

Accidental cross-task mutation is a gate failure.

### D. Authority boundaries

The runtime must enforce or reliably preserve:

- one-shot / bounded authority;
- no unauthorized scope expansion;
- no implicit HumanGate bypass;
- STOP on unknown authority state.

### E. Automatic evidence collection

For each WorkUnit, File Factory should collect at minimum:

```text
executor identity
basis identity
changed files
commit / artifact identity where applicable
test result
terminal outcome
warnings
blockers
```

Human reconstruction of basic task history must not be required.

### F. Independent review routing

For work requiring independent verification:

```text
implementation
→ independent reviewer
→ verdict
→ bounded correction loop if needed
→ HumanGate
```

The implementer must not silently become its own independent reviewer.

### G. Failure / STOP semantics

The system must correctly classify and preserve at least:

```text
agent timeout
agent failure
invalid output
test failure
scope violation
stale basis
partial completion
unknown side effect
```

L2 does not require autonomous repair of all failures.

It requires that failure is not misreported as success.

### H. Restart / recovery

After File Factory or host restart, the system must be able to determine:

```text
what was running
what completed
what was accepted
what is uncertain
what is safe to replay
what must not be replayed automatically
```

Loss of orchestration truth after restart is not acceptable for L2.

### I. HumanGate summary

HumanGate must be concise.

The Human should receive:

```text
what was requested
what was done
what was verified
what failed or remained uncertain
what changed
what decision is required
```

If HumanGate routinely requires rereading raw logs and reconstructing agent history, leverage has not been achieved.

### J. Multi-model routing

File Factory must demonstrate at least two executor classes under one orchestration model:

```text
HIGH-CAPABILITY / HIGH-COST

and

LOWER-COST / COMMODITY
```

The same WorkUnit abstraction should not require provider-specific redesign.

The minimum gate does not require a large provider marketplace.

### K. Basic cost visibility

At WorkUnit or Job level, capture where available:

```text
model / provider
runtime
token or request usage
approximate cost
retry count
```

A sophisticated billing engine is unnecessary.

The purpose is to make engineering-cost routing measurable.

### L. Real Impozitorium pilot

The acceptance test must use a **real bounded Impozitorium engineering task**, not only File Factory self-tests.

The pilot should exercise approximately:

```text
planning / decomposition
→ 2–4 parallel worker tasks
→ implementation
→ tests
→ evidence
→ independent review
→ correction if necessary
→ HumanGate
```

The exact product slice is to be selected later.

### M. Measurable leverage

This is the governing acceptance criterion.

```text
MINIMUM_USEFUL_EXCAVATOR = PASS

only if at least one of:

    HUMAN_COORDINATION_LOAD
    FRONTIER_MODEL_COST
    WALL_CLOCK DELIVERY TIME

is materially reduced

without materially degrading correctness.
```

A useful initial target is approximately:

```text
~2x lower Human coordination burden

or

~2x faster elapsed delivery

with comparable review quality and correctness
```

The exact multiplier is not a permanent product law.

The requirement is measurable, material leverage.

---

## 6. What is explicitly not required for L2

The following are not prerequisites for Minimum Useful Excavator:

```text
polished GUI
commercial installer
market-ready UX
multi-user accounts
cloud deployment
billing subsystem
plugin marketplace
beautiful dashboards
full autonomous planning
automatic architectural decisions
zero-human operation
production-grade packaging
```

A small operational control surface is sufficient if the engine, orchestration, evidence and HumanGate path work.

---

## 7. Evaluation principle

File Factory must not be judged primarily by:

- number of layers;
- number of agents;
- number of documents;
- amount of code;
- UI completeness.

It must be judged by **development leverage**.

```text
PRIMARY KPI =
    LEVERAGE

SECONDARY KPIs =
    SAFETY
    REPEATABILITY
    RECOVERABILITY
    COST VISIBILITY
    HUMAN ATTENTION SAVED
```

A technically sophisticated File Factory that consumes the same Human attention and the same frontier-model budget as the sequential workflow has not yet passed L2.

---

## 8. Relationship to current File Factory work

Existing File Factory work already provides substantial parts of the eventual gate, including evidence around:

- durable persistence;
- authority units;
- review admission;
- incidents;
- restart / recovery semantics;
- evidence discipline;
- STOP behavior.

The remaining decisive transition is from:

```text
WELL-DESIGNED ORCHESTRATION STATE MACHINE
```

to:

```text
REAL MULTI-AGENT ENGINEERING CYCLE
THAT SAVES HUMAN TIME AND/OR MONEY
```

Future File Factory roadmap decisions should therefore be evaluated against one question:

> Does this work materially move the system toward the L2 Minimum Useful Excavator gate?

If not, it may still be valuable, but it should not automatically outrank work that closes an unmet L2 criterion.

---

## 9. Human decision

```text
DECISION =
    ACCEPTED_DIRECTION

FILE_FACTORY_COMPLETION_TARGET =
    NOT "PRODUCTION READY"
    NOT "COMMERCIAL PRODUCT"

TARGET =
    MINIMUM_USEFUL_EXCAVATOR

MAJOR_IMPOZITORIUM_PRODUCT_IMPLEMENTATION =
    RESUMES AFTER L2 GATE
    unless Human explicitly decides otherwise

FILE_FACTORY_CONTINUES_AFTER L2 =
    YES
    IN PARALLEL / AS NEEDED

IMPLEMENTATION_AUTHORIZATION =
    NONE BY THIS DOCUMENT
```

---

## 10. Gate summary

```text
A. MULTI_AGENT_EXECUTION          REQUIRED
B. PARALLEL_WORK_UNITS            REQUIRED
C. WORKSPACE_ISOLATION            REQUIRED
D. AUTHORITY_BOUNDARIES           REQUIRED
E. EVIDENCE_COLLECTION            REQUIRED
F. INDEPENDENT_REVIEW_ROUTING     REQUIRED
G. FAILURE / STOP_SEMANTICS       REQUIRED
H. RESTART / RECOVERY             REQUIRED
I. HUMAN_GATE_SUMMARY             REQUIRED
J. MULTI_MODEL_ROUTING            REQUIRED
K. BASIC_COST_VISIBILITY          REQUIRED
L. REAL_IMPOZITORIUM_PILOT        REQUIRED
M. MEASURABLE_LEVERAGE            REQUIRED

L2_PASS =
    ALL REQUIRED CAPABILITIES SUFFICIENT
    + REAL PILOT PASS
    + MATERIAL LEVERAGE DEMONSTRATED
```

This gate defines when File Factory becomes a useful development machine.

It does not define when File Factory is finished.
