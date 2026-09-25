<h1 align="center">Giancarlo Cicellyn Comneno</h1>

<p align="center">
  <strong>English</strong> · <a href="./README.it.md">Italiano</a>
</p>

<p align="center">
  <strong>Backend &amp; Tooling Software Developer · Python · Linux · Automation · Open Source</strong>
</p>

<p align="center">
  <img alt="Backend — Tooling · Python — Systems and APIs · Linux — Automation · Open Source — Engineering" src="./assets/profile-badges.svg">
</p>

<p align="center">
  I turn recurring operational problems into reliable tools, explicit workflows and reusable open-source software.
</p>

<h3 align="center">AI-assisted engineering</h3>

<p align="center">
  AI is part of my engineering toolkit. I use it to accelerate research, implementation, testing, review and documentation, while keeping human responsibility, technical understanding, verification and evidence at the center of every published contribution.
</p>

<p align="center">
  <img alt="Profile visitors" src="https://komarev.com/ghpvc/?username=gcomneno&label=%F0%9F%91%80&nbsp;&color=0B1F3A&style=flat-square">
</p>

## <code>01 · SELECTED PROJECTS</code>

These projects best represent my current work across backend design, reliable automation, developer tooling and reproducible software workflows.

<p align="center">
  <strong>Featured live demo — Atelier-Kit</strong><br>
  Explore the public Atelier-Kit demo directly in your browser.
</p>

<p align="center">
  <a href="https://atelier-kit-public-demo.vercel.app/">
    <img alt="Atelier-Kit live demo" src="https://img.shields.io/badge/LIVE%20DEMO-Open%20in%20browser-0B1F3A?style=for-the-badge&logo=vercel&logoColor=white">
  </a>
  &nbsp;
  <a href="https://github.com/gcomneno/atelier-kit">
    <img alt="Atelier-Kit source code" src="https://img.shields.io/badge/SOURCE%20CODE-GITHUB-24292F?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>

| Project | Official release | What it does | What it demonstrates |
| --- | --- | --- | --- |
| [Atelier-Kit](https://github.com/gcomneno/atelier-kit) | [v0.5.1](https://github.com/gcomneno/atelier-kit/releases/tag/v0.5.1) | Provides a configurable showcase kit with local Studio, Atelier Desktop and separately configured private Hosted Studio authoring, content-driven catalog workflows and deployment tooling | SvelteKit product architecture, explicit Visitor/local/hosted authority boundaries, atomic repository mutations, desktop delivery and downstream Giada UI adoption |
| [Smart File Organizer](https://github.com/gcomneno/smart-file-organizer) | [v0.6.0](https://github.com/gcomneno/smart-file-organizer/releases/tag/v0.6.0) | Analyzes files, previews an organization plan and moves them only when explicitly requested | Deterministic file automation, explicit dry-run workflows, explainable decisions, filesystem verification and read-only recovery planning |
| [LeLe Manager](https://github.com/gcomneno/lele-manager) | [v1.11.1](https://github.com/gcomneno/lele-manager/releases/tag/v1.11.1) | Collects, searches and reuses textual lessons learned through Markdown, CLI, GUI and API workflows | Local-first data, JSONL persistence, API boundaries, backend design and packaged desktop delivery |
| [GiadaWare UI Components](https://github.com/gcomneno/giadaware-ui-components) | [v0.1.0](https://github.com/gcomneno/giadaware-ui-components/releases/tag/v0.1.0) | Provides reusable Svelte UI primitives for GiadaWare applications through isolated base, visitor and studio entry points | Svelte package architecture, immutable packed artifacts, isolated entry points, SSR/hydration and accessibility contracts |
| [GYTE](https://github.com/gcomneno/gyte) | [v1.3.1](https://github.com/gcomneno/gyte/releases/tag/v1.3.1) | Extracts transcripts, audio and video from YouTube and supports text reflow, translation and local transcription workflows | Manifest-driven CLI design, media extraction pipelines and reproducible operational tooling |
| [Ubuntu System Tools](https://github.com/gcomneno/ubuntu-system-tools) | [v0.3.0](https://github.com/gcomneno/ubuntu-system-tools/releases/tag/v0.3.0) | Linux utilities for diagnostics, controlled maintenance, offline transcription and kernel warning analysis | Safety-first system tooling, read-only diagnostics, explicit opt-in workflows and reproducible Linux packaging |
| [GiadaWare AI](https://github.com/gcomneno/giadaware-ai) | [v0.0.1](https://github.com/gcomneno/giadaware-ai/releases/tag/v0.0.1) | Experimental 0.x infrastructure for provider-independent, read-only AI capabilities with typed outputs and replaceable backends | Provider-independent AI infrastructure, typed outputs, deterministic validation boundaries and replaceable backends |
| [GYTE AI Learning Pipeline](https://github.com/gcomneno/gyte-ai-learning-pipeline) | [v0.5.0](https://github.com/gcomneno/gyte-ai-learning-pipeline/releases/tag/v0.5.0) | Restartable content pipelines for acquiring, validating and handing off learning material across private and public boundaries | Deterministic validation, restartable workflows, explicit privacy boundaries and controlled external delivery |


### Background and GiadaWare

**GiadaWare™** is my personal lab for turning recurring friction into notes, tools and public projects.

Earlier professional experience includes PHP and Laravel; my current public work focuses on Python, Linux, automation and open-source engineering. Open to remote roles and opportunities.

> Every problem solved once deserves to become knowledge. If that knowledge is reusable, it deserves to become a tool. If that tool is useful to others too, it deserves to become open source.


## <code>02 · OPEN SOURCE ENGINEERING</code>

I contribute upstream by starting from real project problems: reproduce the behavior, bound the change, add tests and carry the patch through the project's review process.

### Yocto Project · `vscode-bitbake`

VS Code extension and language tooling for working with **BitBake and Yocto Project**.

Upstream: [yoctoproject/vscode-bitbake](https://github.com/yoctoproject/vscode-bitbake) · Fork: [gcomneno/vscode-bitbake](https://github.com/gcomneno/vscode-bitbake)

| What I contributed | What it demonstrates |
| --- | --- |
| Fixed recipe-local file discovery by bounding recursive scans and adding cancellation, caching and lazy loading | Debugging in an existing codebase, performance, concurrency/cancellation and non-regression testing |
| Simplified the BitBake configuration-selection flow and corrected status-bar updates | Conservative refactoring, characterization tests and coherent UI state management |
| Evolved the integration-test workspace toward `bitbake-setup` and Yocto 6.0 | Linux/Yocto, reproducible integration environments and test-infrastructure maintenance |
| Updated npm dependencies in a controlled way, reducing vulnerabilities without changing declared ranges | Dependency maintenance, security hygiene and layered validation |
| Extracted reusable cancellable file-search and lifecycle boundaries for Toaster and BitBake document handling | Modular TypeScript refactoring, explicit lifecycle ownership and behavior-preserving characterization tests |


### Selected merged upstream pull requests

The entries below are upstream pull requests verified as merged; public forks are not used as evidence of accepted contribution.

<details>
<summary>Yocto Project — <code>vscode-bitbake</code></summary>

- [#546 — refactor: extract Devtool commands](https://github.com/yoctoproject/vscode-bitbake/pull/546)
- [#538 — Fix unbounded recipe-local file discovery](https://github.com/yoctoproject/vscode-bitbake/pull/538)
- [#543 — Extract reusable cancellable file search utility](https://github.com/yoctoproject/vscode-bitbake/pull/543)
- [#545 — refactor: extract document lifecycle](https://github.com/yoctoproject/vscode-bitbake/pull/545)
- [#544 — refactor: extract Toaster lifecycle](https://github.com/yoctoproject/vscode-bitbake/pull/544)
- [#513 — test: finish integration run on success](https://github.com/yoctoproject/vscode-bitbake/pull/513)
- [#518 — fix(scanner): prefer non-skipped recipe entries](https://github.com/yoctoproject/vscode-bitbake/pull/518)
- [#510 — Preserve sane BitBake state for restored scan cache](https://github.com/yoctoproject/vscode-bitbake/pull/510)
- [#533 — refactor: simplify BitBake config picker flow](https://github.com/yoctoproject/vscode-bitbake/pull/533)
- [#532 — fix: update status bar after picking config by name](https://github.com/yoctoproject/vscode-bitbake/pull/532)
- [#535 — test: create integration workspace with bitbake-setup](https://github.com/yoctoproject/vscode-bitbake/pull/535)
- [#524 — test: fetch split Yocto 6.0 repositories](https://github.com/yoctoproject/vscode-bitbake/pull/524)
- [#526 — fix: keep parse-on-save scans quiet on config errors](https://github.com/yoctoproject/vscode-bitbake/pull/526)

</details>

<details>
<summary>Canonical Craft ecosystem</summary>

- [craft-parts#1523 — fix(executor): preserve special files during build copy](https://github.com/canonical/craft-parts/pull/1523)
- [craft-parts#1485 — fix(deb): avoid python-apt for installed package checks](https://github.com/canonical/craft-parts/pull/1485)
- [craft-parts#1600 — fix(git): checkout commit before updating submodules](https://github.com/canonical/craft-parts/pull/1600)
- [craft-parts#1598 — feat(organize): support build pseudo-partition source](https://github.com/canonical/craft-parts/pull/1598)
- [craft-parts#1562 — fix(organize): reject sources outside install dir](https://github.com/canonical/craft-parts/pull/1562)
- [craft-parts#1533 — fix(sources): handle streaming request errors](https://github.com/canonical/craft-parts/pull/1533)
- [craft-application#1068 — fix(application): preserve non-success dispatcher return codes](https://github.com/canonical/craft-application/pull/1068)
- [craft-providers#966 — chore(types): enable explicit re-export checking](https://github.com/canonical/craft-providers/pull/966)
- [craft-cli#444 — fix(messages): reset terminal style after open_stream](https://github.com/canonical/craft-cli/pull/444)
- [snapcraft#6216 — fix(init): allow long directory names](https://github.com/canonical/snapcraft/pull/6216)
- [craft-cli#425 — fix(utils): correct humanize_list formatting for two-item lists](https://github.com/canonical/craft-cli/pull/425)
- [rockcraft#1148 — docs: update LXD/Docker incompatibility handling](https://github.com/canonical/rockcraft/pull/1148)

</details>

<details>
<summary>Canonical Operator Framework</summary>

- [operator#2454 — fix: treat remote unit zero as explicit](https://github.com/canonical/operator/pull/2454)

</details>

## <code>03 · SELECTED RESEARCH</code>

These repositories use reproducible software experiments to investigate sequence structure, statistical behavior and deterministic computation.

| Area | Project | Technical focus |
| --- | --- | --- |
| Recursive structural algebra | [PETRA](https://github.com/gcomneno/petra) | Canonical shape-first algebra for prime-exponent tower structures, with immutable recursive forms, structural rewrite operators, a maintained CLI and Resolver shortest-path/distance tooling |
| Sequence analysis | [Digit Probe](https://github.com/gcomneno/digit-probe) | Randomness, compressibility, autocorrelation, n-grams and Schur-like patterns through a reusable analysis API |
| Modular structure analysis | [Midas](https://github.com/gcomneno/midas) | Deterministic modular fingerprints, anomaly localization and structural comparison without predictive claims |
| Finite-state stochastic modeling | [Lotto Digit Coverage Dynamics](https://github.com/gcomneno/lotto-digit-coverage-dynamics) | Exact absorbing Markov models, exhaustive kernel verification, historical signal analysis, versioned application contracts and a local reproducible research GUI |
| Sequence recognition | [OEIS Probe](https://github.com/gcomneno/oeis-probe) | Offline OEIS lookup, normalized search and SQLite caching |
| Deterministic bucketing | [Turbo-Bucketizer](https://github.com/gcomneno/turbo-bucketizer) | High-entropy IPv4 partitioning and deterministic allocation |
| Structural search | [Integer Structural Search](https://github.com/gcomneno/integer-structural-search) | Bounded search over integer representations and constraints |
| Time-series compression | [Lasagna v2](https://github.com/gcomneno/lasagna-v2) | Adaptive segmentation, predictor-based residual coding and controlled lossy/lossless experiments on univariate time series |

## <code>04 · LEARNING IN PUBLIC</code>

I turn study into documented, reproducible paths rather than presenting learning repositories as production experience.

| Area | Repository | Current focus |
| --- | --- | --- |
| Applied sequence analysis | [System Log Dynamics](https://github.com/gcomneno/system-log-dynamics) | Reproducible Digit-Probe demonstrator over privacy-safe Linux journal normalization, deterministic evidence and temporal comparison |
| Embedded Linux | [Yocto/QEMU Mini Lab](https://github.com/gcomneno/yocto-qemu-mini-lab) | Reproducible image builds, custom layers and recipes, BitBake workflows and QEMU boot validation |
| Embedded Linux | [Cat Couch Guardian](https://github.com/gcomneno/cat-couch-guardian) | Educational virtual-first C11 motion-event slice packaged in a Yocto-derived ARM64 image, with systemd autostart and deterministic QEMU evidence |
| Software development | [Kleis Software Development Course](https://github.com/gcomneno/kleis-corso-sviluppo-software) | Progressive exercises in C#/.NET, HTML, SQL and PHP, including a verified PDO/MySQL CRUD application with Bootstrap |
| Physics | [Physics Study](https://github.com/gcomneno/physics-study) | Original, fact-checked lessons; first lesson: [Does Light ACTUALLY Move?](https://github.com/gcomneno/physics-study/blob/main/lessons/does-light-actually-move/lesson-learned.md), from Io eclipse timing to evidence for the finite speed of light |
| Software development | [OOP in C Lab](https://github.com/gcomneno/oop-in-c-lab) | Object layout, manual virtual dispatch, runtime type identity and checked downcasting |
| Software development | [JavaScript Lab](https://github.com/gcomneno/js-lab-didattico) | JavaScript and TypeScript middleware pipelines and reusable design patterns, with executable tests |
| Game-engine architecture | [BoardLab](https://github.com/gcomneno/boardlab) | Generic game-engine architecture and reproducible search/AI experiments in early incubation |

## <code>05 · LATEST UPDATES</code>
<!-- updates:start -->

- **2026-09-24** · `petra` · **Development:** [research: close Phase 6 external mathematical validation (#312)](https://github.com/gcomneno/petra/commit/4a65d073501b7e6e6aa0980bce88766be387bccf)
- **2026-09-24** · `petra` · **Development:** [research: record Phase 6 closure audit](https://github.com/gcomneno/petra/commit/34d47411ba5f0f8bdc1fb7c28ea47e2fbea29082)
- **2026-09-24** · `petra` · **Development:** [research: close Phase 6 source register](https://github.com/gcomneno/petra/commit/4a220f31cce20e299a52b5801f5445aff46109c8)
- **2026-09-24** · `petra` · **Development:** [research: freeze Phase 6 validation matrix](https://github.com/gcomneno/petra/commit/40238b441b8b2dfe09ce03ba0b08aa1519510c5c)

<details>
<summary>More recent meaningful updates</summary>

- **2026-09-24** · `petra` · **Development:** [research: validate exact PETRA leaf-edit metric formula (#310)](https://github.com/gcomneno/petra/commit/dc6181ee210abb6c3faab8fe980077afde62e628)
- **2026-09-24** · `petra` · **Development:** [research: resolve final metric validation rows](https://github.com/gcomneno/petra/commit/95799ebe81a0e5f0fb5564a784630894197e3a70)
- **2026-09-24** · `petra` · **Development:** [research: classify exact PETRA edit metric results](https://github.com/gcomneno/petra/commit/9c6afbb684c5b60e1f69591285716f1257fac150)
- **2026-09-24** · `petra` · **Development:** [research: register edit-distance common-structure framework](https://github.com/gcomneno/petra/commit/820b86420cbeb0b928b1cfb7bacdd281b87d043f)
- **2026-09-24** · `petra` · **Development:** [research: refute rooted lower-neighbour set reconstruction (#308)](https://github.com/gcomneno/petra/commit/d7573c4c4f00b9ed2106cdd4b8186ae052af5017)
- **2026-09-24** · `petra` · **Development:** [research: record minimal rooted reconstruction counterexample](https://github.com/gcomneno/petra/commit/ca8a31245e34da8400c153feb8001ecfe8a99b54)
- **2026-09-24** · `petra` · **Development:** [research: refute lower-neighbour set reconstruction](https://github.com/gcomneno/petra/commit/bb294651cef10b67be9858afdf2532ba7fec39eb)
- **2026-09-24** · `petra` · **Development:** [research: register rooted one-leaf deck source](https://github.com/gcomneno/petra/commit/7dc08558be5341af74c68d8e2f9825202e77ba10)
- **2026-09-24** · `petra` · **Development:** [research: validate global PETRA edit-graph automorphism questions (#306)](https://github.com/gcomneno/petra/commit/cc0a0dd03380502b75f0d3804fa5b4b78f1a6699)
- **2026-09-24** · `petra` · **Development:** [research: compare global edit graph with reconstruction literature](https://github.com/gcomneno/petra/commit/63794839cbcfbf08c11b6610927601bbc0c61eba)
- **2026-09-24** · `petra` · **Development:** [research: resolve one-step target orbit converses](https://github.com/gcomneno/petra/commit/7c49124d2083cf21e27aeb1b1220accecf92160f)
- **2026-09-24** · `petra` · **Development:** [research: classify global edit-graph validation results](https://github.com/gcomneno/petra/commit/f9931e35563c1ad9e42df8ecf0b9993e17749dcf)
- **2026-09-24** · `petra` · **Development:** [research: register tree reconstruction and pseudosimilarity sources](https://github.com/gcomneno/petra/commit/4d6fae96b6c7a581fca8e976e91af7b1812a5e25)
- **2026-09-24** · `petra` · **Development:** [research: audit PETRA witnessed edits against residual-system axioms (#304)](https://github.com/gcomneno/petra/commit/4d1d7100da1fa36e2616f0c2fd3dca36285d3663)
- **2026-09-24** · `petra` · **Development:** [research: audit witnessed edits against residual-system axioms](https://github.com/gcomneno/petra/commit/8b9c8b681a1cea4af75d9400f169f4b39a5eb7b9)
- **2026-09-24** · `petra` · **Development:** [research: align residual comparison with axiom audit](https://github.com/gcomneno/petra/commit/65ca1bf808e0078b29ead87d979b3323434e68f3)
- **2026-09-24** · `petra` · **Development:** [research: resolve PETRA residual-system membership audit](https://github.com/gcomneno/petra/commit/11e5e48432159efb8afbfc45f85fa0dfcd0a53be)
- **2026-09-24** · `petra` · **Development:** [research: record residual-system audit axioms](https://github.com/gcomneno/petra/commit/9eebb2d11584ff78c20967faa5aa9b21428ab00b)
- **2026-09-24** · `petra` · **Development:** [research: compare PETRA state-dependent edit residuals with residual theory (#302)](https://github.com/gcomneno/petra/commit/7bbca260bafa6e914532b972ddc3664652802867)
- **2026-09-24** · `petra` · **Development:** [research: advance residual validation next step](https://github.com/gcomneno/petra/commit/73df852db02cb6d2b0642970b0b307aa2c53077e)
- **2026-09-24** · `petra` · **Development:** [research: compare PETRA with residual rewriting theory](https://github.com/gcomneno/petra/commit/a42ae31a43cbb872dd9b52abbf1b87651d36a0b6)
- **2026-09-24** · `petra` · **Development:** [research: extend path comparison with residual theory](https://github.com/gcomneno/petra/commit/4b6a9befd8d9db95dfbf2853de3386aa9c0a3115)
- **2026-09-24** · `petra` · **Development:** [research: sharpen state-dependent residual classification](https://github.com/gcomneno/petra/commit/c010814a3b5edafc2eae22265bf033332b78d9b1)
- **2026-09-24** · `petra` · **Development:** [research: register residual-theory sources](https://github.com/gcomneno/petra/commit/9f3c2ad260a5294779dcad2170e7c58473298b82)
- **2026-09-24** · `petra` · **Development:** [research: validate PETRA witnessed paths against free categories, groupoids, and traces (#300)](https://github.com/gcomneno/petra/commit/f13c78b2ea8fcba147790325934ba3ae833b2572)
- **2026-09-24** · `petra` · **Development:** [research: correct trace-theory source attribution](https://github.com/gcomneno/petra/commit/db17d0fad24391dffefd4e97760fd08513aeaf7a)
- **2026-09-24** · `petra` · **Development:** [research: compare witnessed paths with categories groupoids and traces](https://github.com/gcomneno/petra/commit/96c1a5ee3183392fd855e109edced28e238fa597)
- **2026-09-24** · `petra` · **Development:** [research: resolve free-category and groupoid validation rows](https://github.com/gcomneno/petra/commit/d00ce816c4e697aff167d7248913981d22370c31)
- **2026-09-24** · `petra` · **Development:** [research: register free-path and trace-theory sources](https://github.com/gcomneno/petra/commit/a03bdcb4acf3b855330c1a5e2b00759ccc080d19)
- **2026-09-24** · `petra` · **Development:** [research: validate PETRA initial algebra and quotient semantics (#298)](https://github.com/gcomneno/petra/commit/982b49372180b2b74b65ed4b06f80503276202cb)
- **2026-09-24** · `petra` · **Development:** [research: remove resolved algebra item from open candidates](https://github.com/gcomneno/petra/commit/97dc8d8aca37513ed7c4addbe642ab6577b1e8b3)
- **2026-09-24** · `petra` · **Development:** [research: align superseded algebra validation note](https://github.com/gcomneno/petra/commit/68658af32c632e9e4e495c534829cb25b1346071)
- **2026-09-24** · `petra` · **Development:** [research: compare PETRA algebraic semantics with standard theory](https://github.com/gcomneno/petra/commit/a826b7eb3ca182adfe5d85a48d7132d38076b0ad)
- **2026-09-24** · `petra` · **Development:** [research: resolve algebraic semantics validation rows](https://github.com/gcomneno/petra/commit/6740ea92b9483909c1ed0570beec15bbc58b18f0)
- **2026-09-24** · `petra` · **Development:** [research: register bag-functor and universal-algebra sources](https://github.com/gcomneno/petra/commit/678f84d2f49f75d908d1f695cb9b2812c546decf)
- **2026-09-24** · `petra` · **Development:** [research: validate PETRA leaf-edit metric against 1-degree tree edit distance (#296)](https://github.com/gcomneno/petra/commit/05cd4e74e81f2cdc70e15e71ac19f0bea4f07df6)
- **2026-09-24** · `petra` · **Development:** [research: clarify unrestricted TED boundary](https://github.com/gcomneno/petra/commit/f51cfa512d9010c9bd4942bd572b8bb27dffb51e)
- **2026-09-24** · `petra` · **Development:** [research: distinguish PETRA leaf edits from unrestricted TED](https://github.com/gcomneno/petra/commit/27d79cc8911ac9a709c7834ea34f8a2b153c4fb6)
- **2026-09-24** · `petra` · **Development:** [research: compare PETRA metric with 1-degree tree edits](https://github.com/gcomneno/petra/commit/24734516d19a7c3d613c278ff15d3e0a7ea8c37e)
- **2026-09-24** · `petra` · **Development:** [research: refine leaf-edit validation status](https://github.com/gcomneno/petra/commit/65b6a4e2e825ec4a1b2e7653ba8bf70dc19e8022)
- **2026-09-24** · `petra` · **Development:** [research: register Selkow leaf-edit prior art](https://github.com/gcomneno/petra/commit/0c49d30883322a449e99cbca6cacd5b38920e948)
- **2026-09-24** · `petra` · **Development:** [research: begin Phase 6 external mathematical validation (#294)](https://github.com/gcomneno/petra/commit/5d678187cccd27eef4e732a06fd2de10a1398eb3)
- **2026-09-23** · `lele-manager` · **Feature:** [add assistant-ready context export (#258)](https://github.com/gcomneno/lele-manager/commit/ee1a000c759f94d2dea1d84b52b5ee78703f8033)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [finalize Italian M0.7 verified maturity](https://github.com/gcomneno/cat-couch-guardian/commit/254cea53e0fbf32ac43fc81c13888fcdb308138e)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [finalize M0.7 verified maturity](https://github.com/gcomneno/cat-couch-guardian/commit/92cf575744338ad7dc1371b6dbabdaa56fc303b5)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [align Italian exercises with M0.7 contract](https://github.com/gcomneno/cat-couch-guardian/commit/ffcb37fcb62ef7a416bd8d47c03c6b72c659e210)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [align exercises with implemented M0.7 contract](https://github.com/gcomneno/cat-couch-guardian/commit/50522837c3d72b5f3f7008611319a78c17ec63cc)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [explain Italian M0.7 state machine architecture](https://github.com/gcomneno/cat-couch-guardian/commit/8a738ff099989ee18925f4c0696e427c6eeedffd)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [explain M0.7 state machine architecture](https://github.com/gcomneno/cat-couch-guardian/commit/cc7eb5e5d7ffb20b59794c9dafc5545cac0d1baf)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [document Italian M0.7 cooldown contract](https://github.com/gcomneno/cat-couch-guardian/commit/72076360836a9c41d2ee8ad2a568d7381329be85)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [document M0.7 cooldown contract](https://github.com/gcomneno/cat-couch-guardian/commit/59e4d661da9fbb2833561a41356265cbe5900375)
- **2026-09-23** · `cat-couch-guardian` · **Feature:** [demonstrate deterministic cooldown decisions](https://github.com/gcomneno/cat-couch-guardian/commit/1051135633978b45d2b7b30530e9120613e57e54)
- **2026-09-23** · `cat-couch-guardian` · **Feature:** [emit deterministic event timestamps](https://github.com/gcomneno/cat-couch-guardian/commit/2f4b6b56aada4affd83f4992503fe811233344aa)
- **2026-09-23** · `cat-couch-guardian` · **Feature:** [make simulated event time explicit](https://github.com/gcomneno/cat-couch-guardian/commit/a33c380bc25f1aef385593298f26a9bf149c5930)
- **2026-09-23** · `cat-couch-guardian` · **Feature:** [implement deterministic cooldown policy](https://github.com/gcomneno/cat-couch-guardian/commit/6169521e0caa488610c2b751fe68734cd316f1f9)
- **2026-09-23** · `cat-couch-guardian` · **Feature:** [add explicit cooldown state](https://github.com/gcomneno/cat-couch-guardian/commit/051117395c57e19719a9fa2acaba6ada282fa925)
- **2026-09-23** · `cat-couch-guardian` · **Feature:** [expose suppression evidence boundary](https://github.com/gcomneno/cat-couch-guardian/commit/ae9756aaa1d1c31dd7b3224efae4a291feda7545)
- **2026-09-23** · `cat-couch-guardian` · **Feature:** [add deterministic event timestamp](https://github.com/gcomneno/cat-couch-guardian/commit/ea2947edd385b37d55075c93a52507cda628e447)
- **2026-09-23** · `cat-couch-guardian` · **Feature:** [define cooldown suppression evidence](https://github.com/gcomneno/cat-couch-guardian/commit/2d49dacbe884d617a1d3f97dde3687ab0ab40374)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [add Italian engineering exercises](https://github.com/gcomneno/cat-couch-guardian/commit/112e7ce1f1b6fde7acf8beb2ce957c2c60893819)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [add Italian architecture guide](https://github.com/gcomneno/cat-couch-guardian/commit/ae274bd5852d02d54a58eb7291420525ce014b78)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [add Italian learning path](https://github.com/gcomneno/cat-couch-guardian/commit/7bb5745443ad6c0a37589891f858e1394f502df8)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [add Italian README](https://github.com/gcomneno/cat-couch-guardian/commit/073f027a9e81f6a1111ecdd7a41cdf6dc9d5ec95)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [add Italian documentation policy](https://github.com/gcomneno/cat-couch-guardian/commit/281af14a8435b14a2daf53ab47f9e07662f14380)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [define bilingual documentation policy](https://github.com/gcomneno/cat-couch-guardian/commit/90dea27e13a8e806f675adbb68b7bac8eb99e5c1)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [add bilingual language selectors](https://github.com/gcomneno/cat-couch-guardian/commit/b4d8f85b1a7f4223d60b0ba909c7eb121e540dd4)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [make README a learning entry point](https://github.com/gcomneno/cat-couch-guardian/commit/c34fb57fce30b7c8ecbafe4da8b49cfb239b71aa)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [add junior engineering exercises](https://github.com/gcomneno/cat-couch-guardian/commit/60e99d05d6682e0bd6b13bfd38fb4e28af73812c)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [explain architecture for learners](https://github.com/gcomneno/cat-couch-guardian/commit/2d0eab196de69b9799d23b56459e5a1779f7dfd1)
- **2026-09-23** · `cat-couch-guardian` · **Docs:** [add junior learning path](https://github.com/gcomneno/cat-couch-guardian/commit/c22bc0bc90af3b82149e37f68a31e619fe05b4c1)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [formalize final exam simulation (#14)](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/0538d4f42527efc0fe791e4e8ee309674f640274)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [explain ISBN as sketch-derived design choice](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/529272834cac9b0fe98d5eae2766a827713b69ae)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [tighten faithful transcription of exam part A](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/21cdaeb19251138eabbcf352c5a11a74776cd2bd)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [expose final exam simulation from root README](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/eb24ac14c3bcec5e4727a6106a6c41bebfc4e5f6)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [add final exam simulation runbook](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/10f40f9dbec12a7dfc4b65af2ae7439dc5556dcb)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [add runnable part B fixture](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/875c177e649d2e73b8d87d406446fdd56639f3f7)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [add expected SQL result](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/ecb0fadc2dd43905b3b088d3eab75f9957eed1fb)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [add final exam SQL solution](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/adb618d40ce4f88c20cc6ee9f6bbf503ae3071ea)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Feature:** [add exam simulation custom CSS](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/c029deed486ef1311a31dd5f3d4d31b98a9c9379)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Feature:** [add exam simulation delete action](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/40af7deb555cc39aff446889f0013cbea3e02432)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Feature:** [add exam simulation create action](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/394ff13870eb57c475c3526adbb14175561e87ab)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Feature:** [add exam simulation main page](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/0956ca1bfe5941bc22221e09f9977e6b8c33bd99)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Feature:** [add exam simulation PDO boundary](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/975db1f0501612b8921c3ffe515b66ca2e24e9f8)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Feature:** [add exam simulation seed](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/ad53e4e488404376b95e34e223477c2466770725)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Feature:** [add exam simulation book schema](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/62a5884d24c2e85546514ee2b8f1ee5de617e4ee)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [add detailed final exam reference solution](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/dae9a78b606fa3ececeb8ec43649904f926b85ed)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [add final exam verification checklist](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/91811b655929d10ef51453efe82392d9d44edc7d)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [add repeatable final exam protocol](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/96436f0536e064326dbed6d704ee12948906d530)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [transcribe final exam simulation part B](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/cf6a9c4d4a8a7810ea4c9d91dd14c366d4d32c39)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [transcribe final exam simulation part A](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/86e8f45cd5e8daad750454e82d92103bd64daed8)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Docs:** [add final exam simulation overview](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/026eea6e29d26939ccf4cd140ddbd947aa79ed27)
- **2026-09-19** · `lotto-digit-coverage-dynamics` · **Docs:** [add Zenodo DOI metadata](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/7c2eded9d271484ad3a50afd8d27b43e7dc4bd0e)
- **2026-09-19** · `cat-couch-guardian` · **Docs:** [update M0.6 packaging and provenance](https://github.com/gcomneno/cat-couch-guardian/commit/d9ffbe1a818a80633aad78a8b50ceb45547c1880)
- **2026-09-19** · `lotto-digit-coverage-dynamics` · **Release:** [v1.2.0 — Reproducible archive tooling and semantic read queries](https://github.com/gcomneno/lotto-digit-coverage-dynamics/releases/tag/v1.2.0)
- **2026-09-19** · `cat-couch-guardian` · **Feature:** [add simulated deterrent request boundary](https://github.com/gcomneno/cat-couch-guardian/commit/2050fea045b3a0e390ee7111c401781f16889035)
- **2026-09-19** · `lotto-digit-coverage-dynamics` · **Docs:** [prepare v1.2.0 publication metadata](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/c2dadf97e7aa3dfd6c312f034978756974303b4b)

_Showing the 100 most recent meaningful updates; 1830 older update(s) omitted._

</details>

<!-- updates:end -->

---

<p align="center">
  <br>
  <em>This profile is a moving lab: reliable software, explicit decisions, clear documentation and public iteration.</em>
</p>

<p align="center">
  <a href="https://github.com/sponsors/gcomneno">
    <img alt="Sponsor this lab on GitHub" src="https://img.shields.io/badge/Sponsor%20this%20lab-GitHub%20Sponsors-0B1F3A?style=flat-square&logo=githubsponsors&logoColor=white&labelColor=555555">
  </a>
</p>
