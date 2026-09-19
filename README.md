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

- **2026-09-19** · `giadaware-ai` · **Release:** [GiadaWare AI v0.0.1](https://github.com/gcomneno/giadaware-ai/releases/tag/v0.0.1)
- **2026-09-19** · `lele-manager` · **Feature:** [add semantic Lesson Learned extraction (#255)](https://github.com/gcomneno/lele-manager/commit/faf88c59e75dccf132c0e17677b359ae42ea820d)
- **2026-09-19** · `giadaware-ai` · **Feature:** [support Ollama thinking control](https://github.com/gcomneno/giadaware-ai/commit/36a1bb751ec3851d3ceb0a38abe052747984ce5e)
- **2026-09-19** · `giadaware-ai` · **Docs:** [record GPT-6 Astra runtime verification](https://github.com/gcomneno/giadaware-ai/commit/7081dd4c2e00db2907da6e4f0569ff80dd68df58)

<details>
<summary>More recent meaningful updates</summary>

- **2026-09-18** · `digit-probe` · **Docs:** [record Zenodo DOI for v1.0.0 (#32)](https://github.com/gcomneno/digit-probe/commit/b632e18d05d24a9050dc87e2411ed8b47efbdf07)
- **2026-09-18** · `digit-probe` · **Docs:** [add Zenodo citation metadata (#31)](https://github.com/gcomneno/digit-probe/commit/dc1d2f399170804c3e66fc4eb86af6360c7d38ba)
- **2026-09-18** · `smart-file-organizer` · **Release:** [v0.6.0](https://github.com/gcomneno/smart-file-organizer/releases/tag/v0.6.0)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Docs:** [add v0.5.0 download and quick start CTA (#53)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/1c19b4413b29ee3ddc0d62df85b1b096e90da268)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Release:** [GYTE AI Learning Pipeline v0.5.0 Technical Preview](https://github.com/gcomneno/gyte-ai-learning-pipeline/releases/tag/v0.5.0)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Feature:** [prepare downloadable technical preview (#52)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/010e681ef03fadda97a9bff2a94c4c1210e6524c)
- **2026-09-18** · `digit-probe` · **Release:** [Digit Probe v1.0.0](https://github.com/gcomneno/digit-probe/releases/tag/v1.0.0)
- **2026-09-18** · `smart-file-organizer` · **Docs:** [align README with verifiable recovery state (#106)](https://github.com/gcomneno/smart-file-organizer/commit/19376637a6abe79a9fd56d0c0a145cadfdf73120)
- **2026-09-18** · `digit-probe` · **Docs:** [define consumer-safe analysis contract (#22) (#25)](https://github.com/gcomneno/digit-probe/commit/8239fc4198b5526552ee40f22cff9446d9650f56)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Docs:** [complete manual social-source triage PoV (#50)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/fc54e981b9478ba44f24bb1d86af9609d5acc727)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Docs:** [complete Source-to-Skill human/agent PoV (#49)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/5ca6e842c6bcf861ebc8a33faa01d21725684724)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Docs:** [adopt canonical English localization boundary (#48)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/2f89a7ecd4bd379a33eaa44ac17da51614d98f34)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Feature:** [automate approved repository handoff up to PR creation (#47)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/00ca1c5502ee087d15ee099bb47757e9890488a6)
- **2026-09-18** · `giadaware-ai` · **Docs:** [add repository agent governance](https://github.com/gcomneno/giadaware-ai/commit/ae7387f74e7423513409e80c8e193121ffda6040)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA structural statistics and Lipschitz observables (#292)](https://github.com/gcomneno/petra/commit/12ca1ae1a982e82e125879cf71de8778d0147ac3)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA automorphisms and symmetry (#290)](https://github.com/gcomneno/petra/commit/34957ac2603dafb961f62e83671c34d3f943a2c0)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA rewrite presentations (#288)](https://github.com/gcomneno/petra/commit/b31d344c2f66386ff4f70ce540da7bfc24897789)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA congruences and quotients (#286)](https://github.com/gcomneno/petra/commit/027544713c44a2822acb8cfdecc090e73c47c565)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA grading and edit-graph geometry (#284)](https://github.com/gcomneno/petra/commit/18f74077cfd2ec2ee36198287904ee315e25693e)
- **2026-09-17** · `petra` · **Development:** [research: formalize AIP-5 interpretation theory (#282)](https://github.com/gcomneno/petra/commit/fccc9116bb98814c1597afb11e9cf48ef67a179c)
- **2026-09-17** · `petra` · **Development:** [research: formalize and probe AIP-4 minimal algebra (#280)](https://github.com/gcomneno/petra/commit/00d266bbc24d92276fa9ae85341e534dcbb5f357)
- **2026-09-17** · `petra` · **Development:** [research: formalize canonical PETRA carrier theory (#278)](https://github.com/gcomneno/petra/commit/74c397388cd5c30b05509c821b93c7040c160c63)
- **2026-09-17** · `petra` · **Development:** [research: formalize abstract carrier foundational answers (#275)](https://github.com/gcomneno/petra/commit/ac2c4187e8d280878711d8fec2a7a3c23a1ef007)
- **2026-09-17** · `petra` · **Development:** [research: analyze Terminal as empty composition (#273)](https://github.com/gcomneno/petra/commit/efa883dfec07ad5e1fe748426b61a190b433a5fc)
- **2026-09-17** · `petra` · **Development:** [research: reassess AIP-2 primitive relation ontology (#269)](https://github.com/gcomneno/petra/commit/4c174646ed7afc2e81f8aff36cee8e5d88277ab1)
- **2026-09-17** · `petra` · **Development:** [research: probe AIP-1 Set vs Multiset composition (#267)](https://github.com/gcomneno/petra/commit/ca5322a056946a84fb387dfa73e26f7149b9e34b)
- **2026-09-17** · `petra` · **Development:** [research: analyze AIP-1 multiplicity ontology (#265)](https://github.com/gcomneno/petra/commit/caca013c8b85345e639bf11cdabf1808e20df6ad)
- **2026-09-17** · `petra` · **Development:** [research: validate AIP-2 recursive containment (#262)](https://github.com/gcomneno/petra/commit/3544a4e849d45a843865468b32f948b3832d5843)
- **2026-09-17** · `petra` · **Development:** [research: audit AIP-2 level derivability (#258)](https://github.com/gcomneno/petra/commit/999fe865cf81703b40e77fa8cb300a2b1d6cd1ec)
- **2026-09-17** · `petra` · **Development:** [research: prototype AIP-3 order-independent quotient (#255)](https://github.com/gcomneno/petra/commit/58e177a9e110e78336f001ee33b7d985744a1801)
- **2026-09-17** · `petra` · **Development:** [research: analyze AIP-3 order semantics (#253)](https://github.com/gcomneno/petra/commit/04bd54fde7bc64547871c5025688a3f6a48dc669)
- **2026-09-17** · `petra` · **Development:** [research: define PETRA abstract paradigm (#245)](https://github.com/gcomneno/petra/commit/7c3304a77d34e1630315ad0405c577f67a2e562b)
- **2026-09-17** · `petra` · **Docs:** [establish PETRA related-work survey (#241)](https://github.com/gcomneno/petra/commit/a60f3dd7a4bfc9f7f6acb325d3fbc2c6730c04cc)
- **2026-09-17** · `petra` · **Docs:** [align release metadata with PETRA v2.0.0 (#239)](https://github.com/gcomneno/petra/commit/69e20b78ab7779f8bb8ec444de84ea7722771ba9)
- **2026-09-17** · `petra` · **Development:** [STATUS: Phase 10 complete, v2.0.0 shipped, research front updated](https://github.com/gcomneno/petra/commit/595fb2d293bc97a918587705fa4cacdc9f556b60)
- **2026-09-17** · `petra` · **Development:** [docs/research: update README with open-problems and new notes](https://github.com/gcomneno/petra/commit/140dcafb99735d27f148732d5d78b9b275098942)
- **2026-09-17** · `petra` · **Fix:** [use $'...' so colors render inside heredoc](https://github.com/gcomneno/petra/commit/c88e1faf01242a3acffa825fb6c5573e4381ebc3)
- **2026-09-17** · `petra` · **Release:** [PETRA v2.0.0 — Prime Exponent Tower Recursive Algebra](https://github.com/gcomneno/petra/releases/tag/v2.0.0)
- **2026-09-17** · `petra` · **Docs:** [annotate Zenodo version DOI for v2.0.0](https://github.com/gcomneno/petra/commit/3fda09188dd5c4e7b7ab456fdc713963c00bc6c8)
- **2026-09-16** · `petra` · **Development:** [T18/P21 closed: ruff and mypy clean on resolver](https://github.com/gcomneno/petra/commit/c36d49791621c3b7236082f8e8f59f98eba8cd55)
- **2026-09-16** · `petra` · **Development:** [revert: remove RUF001/RUF002 from root config (belongs to resolver)](https://github.com/gcomneno/petra/commit/7bfb94e00e847ac89f0fa0d914012db0653572ee)
- **2026-09-16** · `petra` · **Development:** [T18: py.typed for petra, mypy fixes; T17 statement correction](https://github.com/gcomneno/petra/commit/42fa7e2154e17cab6e789aacca406639daffbf80)
- **2026-09-16** · `petra` · **Development:** [resolver: fix remaining ruff errors (SIM108, SIM110, RUF005, RUF059, B905)](https://github.com/gcomneno/petra/commit/54d88fa6e4f942f26873145587994ea515b9d01a)
- **2026-09-16** · `petra` · **Development:** [resolver: ignore RUF001/RUF002 for × separator](https://github.com/gcomneno/petra/commit/2f6b4cf6516955cbc8c189ad19ce232a64d4d774)
- **2026-09-16** · `petra` · **Development:** [T17/P20 closed: fix id() cache bug in resolver search](https://github.com/gcomneno/petra/commit/cc9b5d8ae6db7350d42c98d53afd8f8b49cee83a)
- **2026-09-16** · `petra` · **Development:** [T19: fifth data point at 10^8, SumPk2 ~ c/sqrt(log log N) excluded](https://github.com/gcomneno/petra/commit/b8d2c4bf2c621956b07597cc351670080e287576)
- **2026-09-16** · `petra` · **Development:** [P16/P17/P18 closed: T13 covered by P8, T14 and T15 out of scope](https://github.com/gcomneno/petra/commit/efbb1baba4d36564e02c41d14d5fa4a79e29a7d4)
- **2026-09-16** · `petra` · **Development:** [P15/T12 closed: sparse sampling out of scope](https://github.com/gcomneno/petra/commit/62c041961000738c8356149ad9ad29b58da04e7c)
- **2026-09-16** · `petra` · **Development:** [P14/T11 closed: Beatty and non-obvious families out of scope](https://github.com/gcomneno/petra/commit/dd4ff9a9be502bdcd2ad36f0d84c61ac2082809d)
- **2026-09-16** · `petra` · **Development:** [P13/T10 closed: fingerprint catalogue out of scope](https://github.com/gcomneno/petra/commit/8c0f7895d88fe7ee3dd9fdab0f1653bf24ac851c)
- **2026-09-16** · `petra` · **Development:** [T09 closed: covered by P3 (no bounded context)](https://github.com/gcomneno/petra/commit/7eccaac1ff0d9a66f8eba6b86551646c3137320d)
- **2026-09-16** · `petra` · **Development:** [P12/T08 closed: 3n-1 is reduction-dominant, sign of k irrelevant](https://github.com/gcomneno/petra/commit/c876759ab868543dc748cb0b8af3dff6386ba966)
- **2026-09-16** · `petra` · **Development:** [P11/T07 closed: finer metrics change the fingerprint classification](https://github.com/gcomneno/petra/commit/730dce7518d6aee694e188c486d635a105943fdf)
- **2026-09-16** · `petra` · **Development:** [P10 closed: structural elision tracking is out of scope](https://github.com/gcomneno/petra/commit/3a86e11e8fcf97e35931205007ef8eb4ec2b365a)
- **2026-09-16** · `petra` · **Development:** [P9 closed: arithmetic layer out of scope, shape-first principle](https://github.com/gcomneno/petra/commit/b206294ccd94b76696994140da91bc0023622fb7)
- **2026-09-16** · `petra` · **Development:** [P8 closed: meet/join overlap too coarse to cluster](https://github.com/gcomneno/petra/commit/9a2405f1052d3cc1104d1b840c68932ce389347d)
- **2026-09-16** · `petra` · **Development:** [P7 closed: fingerprint depends only on exponent multiset](https://github.com/gcomneno/petra/commit/cf1ef4289f1f9e2af94a62c64da0a7134f6757fb)
- **2026-09-16** · `petra` · **Development:** [P6 partial: shift and double admit F_T on bounded sample](https://github.com/gcomneno/petra/commit/a632c1c42a9d23dc1df69ae29995f2025dfd59ad)
- **2026-09-16** · `petra` · **Development:** [P5 closed: struct gains inner-container hook, destruct invertible with inner=True](https://github.com/gcomneno/petra/commit/b514c3eee40b0b14c096501cb15856f15d06179f)
- **2026-09-16** · `petra` · **Development:** [P5 open: extend struct with inner-container hook](https://github.com/gcomneno/petra/commit/0e610096cff2a49f69df67aae50920489a8358f9)
- **2026-09-16** · `petra` · **Development:** [T01 closed: struct/destruct on shape(k^n) explored, one struct limit found](https://github.com/gcomneno/petra/commit/1e656bda46445cc03aa29a27ea49333f08505d46)
- **2026-09-16** · `petra` · **Development:** [P4 closed: shape multiplicity is large and concentrated](https://github.com/gcomneno/petra/commit/bce0dda24875f823403fb2ffa261438a6774c9e8)
- **2026-09-16** · `petra` · **Development:** [P3 closed: no bounded context for deterministic succession](https://github.com/gcomneno/petra/commit/ac55b2971d20f3581cb7434a053156390d8d33f1)
- **2026-09-16** · `petra` · **Development:** [P2 closed: counterexample is the result, follow-up out of scope](https://github.com/gcomneno/petra/commit/516345ef5fcd40d709bc1af0c5810de580870337)
- **2026-09-16** · `petra` · **Development:** [P2 first result: all 3n+k maps are reduction-dominant, not only Collatz](https://github.com/gcomneno/petra/commit/aee0906ee96e2f227c771948ba702cad81c4ff6a)
- **2026-09-16** · `petra` · **Development:** [P1 closed: no hard family separation under strict gap test](https://github.com/gcomneno/petra/commit/a24d07e7a2cc9ac71211146b75574248c117ef6c)
- **2026-09-16** · `petra` · **Development:** [remove PET-METICA line: docs, reports, and references](https://github.com/gcomneno/petra/commit/aba12e9bc8636ac789008d372798c122b76e3f0e)
- **2026-09-16** · `petra` · **Development:** [remove PET-METICA line: docs and reports](https://github.com/gcomneno/petra/commit/741a19459b80d8dbc6aded86da5d66685c650cf6)
- **2026-09-16** · `petra` · **Development:** [research: add open-problems.md as active front, archive open-threads.md](https://github.com/gcomneno/petra/commit/d21f12405b928d2024334fd5b70208df74e7adf1)
- **2026-09-16** · `petra` · **Development:** [T07: recursive metric, no natural clusters on small shapes](https://github.com/gcomneno/petra/commit/a9ae8add85dfa483cd306c006862103aeea62346)
- **2026-09-16** · `petra` · **Development:** [destruct: add father-detach cases, return (piece, rest, kind)](https://github.com/gcomneno/petra/commit/932416f53d095c62a04fac10d38fbe98c7dfd2e5)
- **2026-09-16** · `petra` · **Development:** [research(T16): decompose stab = rho * SumPk2; sharpen T19](https://github.com/gcomneno/petra/commit/3adf62749f43c3f1d89277b03df7a36ac617d1b7)
- **2026-09-16** · `petra` · **Development:** [research(T16): reduce fingerprint to arithmetic g(n); open T19 on stab asymptotics](https://github.com/gcomneno/petra/commit/d0f4e9849cb7560012fe6f83b6c546c3a2906731)
- **2026-09-16** · `petra` · **Development:** [research(T01): chain count via hook length formula, verified on 299 targets](https://github.com/gcomneno/petra/commit/c9a618f6b1dd38cc4d920dac9ba3790810505015)
- **2026-09-16** · `petra` · **Development:** [research(T01): chain is not canonical, only one traversal among many](https://github.com/gcomneno/petra/commit/931bba7838451a0e9d81e020dcf84d7b57e622a5)
- **2026-09-16** · `petra` · **Development:** [research(T18): open thread on resolver lint and type debt](https://github.com/gcomneno/petra/commit/c4bb30ab4f0c87ac4534b826d3867a8dc657392f)
- **2026-09-16** · `petra` · **Development:** [research(T17): reformulate thread from asymmetry to flakiness](https://github.com/gcomneno/petra/commit/605f354ecd8efb3a51c79a887cc87df06716e29f)
- **2026-09-16** · `petra` · **Development:** [research(T01): step count and comparison with BFS](https://github.com/gcomneno/petra/commit/e851c11b5b30219df7c9b406ead4ccb7737ef8c5)
- **2026-09-16** · `petra` · **Feature:** [struct max_nodes limit; destruct without terminal flag](https://github.com/gcomneno/petra/commit/1ffd0d63134ccee14f4e5799d9db500ea953b656)
- **2026-09-16** · `petra` · **Development:** [research(T01): document scaling and limits of reconstruction](https://github.com/gcomneno/petra/commit/ddad298a09d5839dd96b7cc2f5da601a05d72e12)
- **2026-09-16** · `petra` · **Development:** [research(T01): add summary of the T01 line](https://github.com/gcomneno/petra/commit/1fab6c7d80bc148726d18ae5f527c3655b19c0c8)
- **2026-09-16** · `petra` · **Development:** [research(T01): recursive reconstruction note and thread update](https://github.com/gcomneno/petra/commit/3c7213b8119b5abd65c547c200841a69bf2fee27)
- **2026-09-16** · `petra` · **Feature:** [rebuild_shape accepts --pieces minimal|all](https://github.com/gcomneno/petra/commit/f433c17351c069b70f1f8fe33d3d6c2fee067bd2)
- **2026-09-16** · `petra` · **Development:** [research(T01): recursive single-chain reconstruction, height-first](https://github.com/gcomneno/petra/commit/b2d13092d1ff75e9674f239c87bef12183b62a87)
- **2026-09-16** · `petra` · **Fix:** [struct with leaf piece adds a father, not identity](https://github.com/gcomneno/petra/commit/50a767bd827dade8c8fc37db6a597d953d5d35e9)
- **2026-09-16** · `petra` · **Fix:** [mother notation uses parentheses for containers](https://github.com/gcomneno/petra/commit/6af4530db62010edb04f34caefb269ad711c82a4)
- **2026-09-16** · `petra` · **Development:** [research(T01): add BFS reconstruction of a shape using struct](https://github.com/gcomneno/petra/commit/c70cd5bdccf86d614d810ad0ee371e3e4f6101e5)
- **2026-09-16** · `petra` · **Feature:** [struct handles all attachment hooks](https://github.com/gcomneno/petra/commit/ef1e2a503f32dc51023a82e213693bd99eb0a82e)
- **2026-09-15** · `petra` · **Development:** [research: add form-strada-value boundary note (T01/T16)](https://github.com/gcomneno/petra/commit/9ca84ec4a64fb9b7aab21ea9e3b26d8193809d3c)
- **2026-09-15** · `petra` · **Development:** [research(T17): open thread on distance asymmetry](https://github.com/gcomneno/petra/commit/3a0ead389560a31c49ccfbd57e87f164d6c52880)
- **2026-09-15** · `petra` · **Feature:** [add mother notation for shapes](https://github.com/gcomneno/petra/commit/201a36c0ee42e5f20cb434529487b69b191a3789)
- **2026-09-15** · `petra` · **Feature:** [struct/destruct with mother hook and depth ordering](https://github.com/gcomneno/petra/commit/6438a5eb36a43bc75fd69da97a9e73e07d7a9c43)
- **2026-09-15** · `petra` · **Refactor:** [rename compose/decompose to struct/destruct](https://github.com/gcomneno/petra/commit/f675b00ff91ceb86a0df8461b66658f49b935f91)
- **2026-09-15** · `petra` · **Feature:** [add compose and decompose (one-level)](https://github.com/gcomneno/petra/commit/d5471132e8ae00b4574aa607e0a92953e199dadb)
- **2026-09-15** · `petra` · **Development:** [research(T16): add fingerprint convergence measurement tool](https://github.com/gcomneno/petra/commit/9af46e47949effbdef2d09b063a45ff7067399a4)
- **2026-09-15** · `petra` · **Development:** [research(T16): open thread on convergence of cumulative fingerprint](https://github.com/gcomneno/petra/commit/8f286182ea2fcc1a60b30a34be592d610de0d1a9)

_Showing the 100 most recent meaningful updates; 1814 older update(s) omitted._

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
