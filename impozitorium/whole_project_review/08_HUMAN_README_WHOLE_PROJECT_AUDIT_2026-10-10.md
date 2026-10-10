# Impozitorium — краткий итог whole-project audit
**Дата:** 10.10.2026

## 1. Общий вывод

Проект не заблудился и не требует переписывания с нуля. За последние месяцы построен сильный фундамент: безопасная работа с PDF, разделение движков, управление рабочими файлами, evidence/HumanGate-процесс, отдельные production-labs и большой задел под агентную разработку.

Главная проблема сейчас не в отсутствии архитектуры, а в том, что полезные части проекта разошлись по нескольким линиям и местами начали говорить разными терминами. Поэтому задача — не «начать заново», а аккуратно свести ownership, терминологию и принятые наработки в одну понятную систему.

## 2. Что уже хорошо

### PDF / structural layer
Направление признано правильным:

- **PDFium** — рендер и preview.
- **pikepdf/qpdf** — структурное чтение/изменение PDF.
- **PyMuPDF** — legacy/transitional слой, который постепенно должен уйти из production-runtime.

Уже есть реальные headless writers, preservation-проверки, Page Geometry-наработки, Optional Content work и File Management lifecycle. Это не только дизайн — значительная часть уже реализована и принята.

### Работа с файлами и артефактами
Platform File Management — одна из наиболее зрелых частей product substrate:

- Source PDF не мутируется;
- есть Candidate / verification / staging / promotion / Current Pointer;
- есть SQLite persistence и recovery;
- same-volume lifecycle уже квалифицирован.

Главный недостающий шаг — связать это с реальным GUI/Save As путём.

### Governance
HumanGate, независимый review, STOP на неопределённости, evidence и bounded authority работают как полезная дисциплина. Их не нужно отменять, но для песочниц и малорисковых изменений режим должен быть легче.

## 3. Где реально находится продукт

### EN-line — product substrate
Это сейчас наиболее логичная база будущего продукта:

- engine migration;
- pikepdf writers;
- PDFium backend;
- Platform File Management;
- OC-6;
- новая geometry work.

**Решение:** именно EN-line принимается как архитектурная product line of record.

### OW-line — development infrastructure + отдельные product deltas
Здесь живут:

- File Factory;
- Orchestrator Operator Workplace;
- Stage 2C / Kandev;
- agent governance;
- часть PDFium GUI work;
- некоторые полезные product-наработки.

OW не выбрасывается, но File Factory и её domain-модель не должны становиться зависимостью production runtime.

Полезные product deltas из OW позже переносятся выборочно.

### OC-line
OC-1…OC-5 сохранены как отдельная принятая линия Optional Content. Их семантика должна быть позже сознательно сведена в product substrate.

## 4. Production-модули и sandboxes

### Уже полезные / зрелые по смыслу
**Manual Trim**  
Реальный рабочий модуль, но GUI всё ещё сидит на legacy PyMuPDF path. Новый pikepdf backend уже существует отдельно.

**Step & Repeat**  
Есть рабочая legacy-реализация и более чистый planner в sandbox. Семантику placement/gap/orientation стоит сохранить, но сам legacy engine позже лучше пересобрать поверх нового core.

**Vector AutoBleed Lab**  
Очень сильная песочница. Зафиксировано:

- 169 accepted tests;
- векторный mirror bleed;
- 0.75 pt seam correction;
- raster fallback;
- rotation normalization;
- sanitation/preservation rules;
- synthetic fixtures.

Главное: сохранять **семантику и тестовый oracle**, а не переносить PyMuPDF-код как есть.

**Booklet Folding Lab**  
Содержит ценные производственные знания:

- signature pagination;
- creep/lap;
- folding geometry;
- collating/fold marks;
- physical qualification flags.

Лаборатория остаётся лабораторией, но её семантика должна лечь в будущий booklet/signature domain.

### Пока в основном design / early state
- N-up;
- Cut Stack;
- полный Job layer;
- Agentic Layer;
- внешний API.

## 5. File Factory — где мы находимся

File Factory продвинулся далеко по внутренней инженерии:

- persistence;
- authority units;
- review admission;
- incidents;
- restart/recovery semantics;
- evidence discipline;
- STOP behavior;
- Controller/WorkUnit/Job machinery.

Но ключевой переход ещё впереди: из «хорошо спроектированной системы управления состоянием» в **реальный multi-agent engineering cycle**, который экономит время и деньги.

Мы приняли отдельный критерий готовности:

### Minimum Useful Excavator (L2)
File Factory считается достаточно готовым, когда он реально умеет:

1. запускать несколько агентов;
2. вести 2–4 параллельных WorkUnit;
3. изолировать workspaces;
4. держать authority boundaries;
5. автоматически собирать evidence;
6. маршрутизировать независимый review;
7. корректно обрабатывать failure/STOP;
8. переживать restart/recovery;
9. давать короткий HumanGate summary;
10. маршрутизировать дорогие и дешёвые модели;
11. показывать базовую стоимость работы;
12. провести настоящий Impozitorium pilot;
13. доказать **measurable leverage** — заметно меньше человеческой координации, frontier-cost и/или wall-clock time.

То есть File Factory не нужно доводить до polished коммерческого продукта. Нужны двигатель, рычаги и реальная производительность.

**Execution priority:** File Factory остаётся нашим главным активным потоком до достижения L2.

## 6. Главные найденные gaps

Самые важные:

- две продуктовые линии долго расходились и содержат разные версии одних и тех же модулей;
- часть принятого Optional Content живёт отдельно;
- новый structural/backend слой почти не связан с GUI;
- отсутствует общий product **Operation Record**;
- geometry semantics исторически размазаны между core и модулями;
- technical marks создаются несколькими независимыми способами;
- терминология проекта начала конфликтовать сама с собой;
- status/ledger-документы местами отстали от фактического состояния;
- product Jobs и Agentic Layer пока в основном design;
- color-management architecture ещё не спроектирована, хотя preservation уже нужно учитывать.

## 7. Самый важный результат сегодняшней работы — семантика

Мы выяснили, что проекту нужен не просто glossary, а **Canonical Product Semantics Registry**.

Создан machine-readable `semantic_registry_v1.yaml` и human-readable baseline.

Теперь ключевые понятия разделены явно:

- `MODULE.PAGE_GEOMETRY` ≠ `PLATFORM.GEOMETRY_CORE`;
- Human Acceptance ≠ Artifact Admission ≠ Production Admissibility;
- Repository Publication ≠ Artifact Promotion ≠ Save As;
- Product Job ≠ File Factory Job;
- PDF TrimBox ≠ layout_box ≠ Framebox ≠ ClipRegion ≠ ProductionContour.

Словарь строится по правилу:

1. международный/отраслевой стандарт;
2. устоявшаяся полиграфическая терминология;
3. уже принятая терминология Impozitorium;
4. собственный термин только если аналога нет.

Мы также начали стыковку с ISO 32000-2, ISO 19593-1:2026 и CIP4 JDF/XJDF.

## 8. Принятые архитектурные решения

### Decision 01 — product line / devinfra boundary
- EN-line — product substrate base.
- File Factory / Kandev / Orchestrator — отдельная development infrastructure.
- Product runtime не зависит от File Factory runtime.
- File Factory при этом остаётся главным текущим execution stream до L2.

### Decision 02 — Operation Record + semantic registry
Нужен минимальный общий `OperationRecord`:

- inputs;
- operation kind/version;
- parameters/policy;
- diagnostics;
- admissibility;
- outputs;
- verification;
- provenance.

PFM остаётся владельцем артефактов.

Jobs и Agentic Layer строятся позже поверх этих операций.

### Decision 03 — geometry / ProductionObject / placement
- generic PDF structure принадлежит `Structural PDF Core`;
- generic geometry — `Platform Geometry Core`;
- `Page Geometry` остаётся модулем;
- `Framebox` — внутренний прямоугольный рабочий frame;
- `layout_box` — source-derived basis из TrimBox → ArtBox → CropBox → MediaBox;
- `FrameIntent` — намерение изменить Framebox;
- `Document Transform` меняет canonical working object и должен быть полностью разрешён до следующей операции;
- `Placement Transform` относится только к размещению экземпляра на листе и не требует пересборки source PDF;
- `ProductionObject` — целостная production-unit с geometry, artwork, technical content и color semantics;
- `PlacedObject` — экземпляр размещения на Layout/Sheet/Surface;
- contour nesting должен использовать тот же placement model, а не отдельную архитектуру.

## 9. Цвет — пока только правильная граница

Полный ICC/color-management design вынесен в отдельное будущее решение.

Но уже принят важный инвариант:

> геометрическая или структурная операция не имеет права молча менять color semantics.

Должны сохраняться, где применимо:

- ICCBased;
- process color meaning;
- Separation / DeviceN;
- spot-color identities;
- OutputIntent-related information.

Preview color transform и реальный output conversion — разные будущие процессы.

## 10. Краткая дорожная карта

### Сейчас
**File Factory → Minimum Useful Excavator L2.**

Не polish, а реальный multi-agent leverage.

### Параллельно
Продолжаем semantic registry и standards mapping только там, где это предотвращает будущую переделку.

### После L2
1. Зафиксировать product convergence strategy вокруг EN-line.
2. Свести нужные OW / OC / transfer deltas.
3. Закончить Platform Geometry Core + Structural PDF Core boundary.
4. Ввести минимальный Operation Record.
5. Провести первый end-to-end vertical slice: GUI → operation → structural transform → PFM → verification → PDFium preview → Working Document → Save As.
6. Переносить production capabilities: Manual Trim / Define Framebox → Step & Repeat → Vector AutoBleed → booklet/signature → N-up / Cut Stack.
7. Затем production intent + Jobs.
8. После Jobs — Agentic Layer поверх тех же операций.
9. Отдельным архитектурным блоком — Color Management / ICC.

## 11. Самое короткое резюме

Impozitorium сегодня — уже не набор скриптов и не проект «с нуля». У него есть хороший structural и lifecycle фундамент, серьёзные production-labs и сильная инженерная дисциплина.

Основная проблема — не недостаток работы, а её распределённость: несколько ветвей, legacy/new engine coexistence, разные vocabulary и ещё не сведённые platform boundaries.

Whole-project audit показал, что **переписывать проект не нужно**. Нужно:

- собрать ownership;
- удержать единый язык;
- сохранить добытую production-семантику;
- закончить multi-agent File Factory как рабочий экскаватор;
- а затем использовать его для аккуратного сведения product substrate и переноса реальных production-модулей на новую платформу.
