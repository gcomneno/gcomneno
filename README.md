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
| [Smart File Organizer](https://github.com/gcomneno/smart-file-organizer) | [v0.5.0](https://github.com/gcomneno/smart-file-organizer/releases/tag/v0.5.0) | Analyzes files, previews an organization plan and moves them only when explicitly requested | Deterministic file automation, explicit dry-run workflows, explainable decisions, filesystem verification and read-only recovery planning |
| [LeLe Manager](https://github.com/gcomneno/lele-manager) | [v1.11.1](https://github.com/gcomneno/lele-manager/releases/tag/v1.11.1) | Collects, searches and reuses textual lessons learned through Markdown, CLI, GUI and API workflows | Local-first data, JSONL persistence, API boundaries, backend design and packaged desktop delivery |
| [GiadaWare UI Components](https://github.com/gcomneno/giadaware-ui-components) | [v0.1.0](https://github.com/gcomneno/giadaware-ui-components/releases/tag/v0.1.0) | Provides reusable Svelte UI primitives for GiadaWare applications through isolated base, visitor and studio entry points | Svelte package architecture, immutable packed artifacts, isolated entry points, SSR/hydration and accessibility contracts |
| [GYTE](https://github.com/gcomneno/gyte) | [v1.3.1](https://github.com/gcomneno/gyte/releases/tag/v1.3.1) | Extracts transcripts, audio and video from YouTube and supports text reflow, translation and local transcription workflows | Manifest-driven CLI design, media extraction pipelines and reproducible operational tooling |
| [Ubuntu System Tools](https://github.com/gcomneno/ubuntu-system-tools) | [v0.3.0](https://github.com/gcomneno/ubuntu-system-tools/releases/tag/v0.3.0) | Linux utilities for diagnostics, controlled maintenance, offline transcription and kernel warning analysis | Safety-first system tooling, read-only diagnostics, explicit opt-in workflows and reproducible Linux packaging |


<details>
<summary>More operational projects</summary>

| Project | Technical signal |
| --- | --- |
| [GiadaWare AI](https://github.com/gcomneno/giadaware-ai) | Experimental 0.x infrastructure for provider-independent, read-only AI capabilities with typed outputs, deterministic validation boundaries and replaceable backends |
| [GYTE AI Learning Pipeline](https://github.com/gcomneno/gyte-ai-learning-pipeline) | Restartable content pipelines, deterministic validation, private/public boundaries and explicit external-delivery handoffs |
| [LeLe Quizzer](https://github.com/gcomneno/lele-quizzer) | Deterministic quiz generation, CLI UX and knowledge reuse |

</details>

<details>
<summary>Background and GiadaWare</summary>

**GiadaWare™** is my personal lab for turning recurring friction into notes, tools and public projects.

Earlier professional experience includes PHP and Laravel; my current public work focuses on Python, Linux, automation and open-source engineering. Open to remote roles and opportunities.

> Every problem solved once deserves to become knowledge. If that knowledge is reusable, it deserves to become a tool. If that tool is useful to others too, it deserves to become open source.

</details>

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

<details>
<summary>More research and experimental projects</summary>

| Area | Project | Technical focus |
| --- | --- | --- |
| Deterministic bucketing | [Turbo-Bucketizer](https://github.com/gcomneno/turbo-bucketizer) | High-entropy IPv4 partitioning and deterministic allocation |
| Structural search | [Integer Structural Search](https://github.com/gcomneno/integer-structural-search) | Bounded search over integer representations and constraints |
| Linguistic compression | [Huffman Compressor](https://github.com/gcomneno/huffman-compressor) | Italian text preprocessing and layered Huffman coding |
| Modular signatures | [Prime Tower Clocks](https://github.com/gcomneno/prime-tower-clocks) | Prime clocks, the Chinese Remainder Theorem and modular signatures |
| Time-series compression | [Lasagna v2](https://github.com/gcomneno/lasagna-v2) | Adaptive segmentation, predictor-based residual coding and controlled lossy/lossless experiments on univariate time series |
| Experimental codec | [Crystal Codec GCC v1](https://github.com/gcomneno/crystal-codec-gcc-v1) | p-adic crystal and prism codec prototype |

</details>

## <code>04 · LEARNING IN PUBLIC</code>

I turn study into documented, reproducible paths rather than presenting learning repositories as production experience.

| Area | Repository | Current focus |
| --- | --- | --- |
| Applied sequence analysis | [System Log Dynamics](https://github.com/gcomneno/system-log-dynamics) | Reproducible Digit-Probe demonstrator over privacy-safe Linux journal normalization, deterministic evidence and temporal comparison |
| Embedded Linux | [Yocto/QEMU Mini Lab](https://github.com/gcomneno/yocto-qemu-mini-lab) | Reproducible image builds, custom layers and recipes, BitBake workflows and QEMU boot validation |
| Embedded Linux | [Cat Couch Guardian](https://github.com/gcomneno/cat-couch-guardian) | Educational virtual-first C11 motion-event slice packaged in a Yocto-derived ARM64 image, with systemd autostart and deterministic QEMU evidence |
| Linux isolation | [Linux Container Lab](https://github.com/gcomneno/linux-container-lab) | Studied Linux container primitives through executed non-privileged experiments and partial verification; container implementation has not started |
| Distributed systems | [Distributed Systems Study](https://github.com/gcomneno/distributed-systems-study) | Session 01 is prepared around algorithms, failure models and coordination; active study is not yet marked complete |
| System design | [System Design Study](https://github.com/gcomneno/system-design-study) | Architecture notes, quizzes and interview-oriented lessons |
| Software development | [Kleis Software Development Course](https://github.com/gcomneno/kleis-corso-sviluppo-software) | Progressive exercises in C#/.NET, HTML, SQL and PHP, including a verified PDO/MySQL CRUD application with Bootstrap |
| Physics | [Physics Study](https://github.com/gcomneno/physics-study) | Original, fact-checked lessons; first lesson: [Does Light ACTUALLY Move?](https://github.com/gcomneno/physics-study/blob/main/lessons/does-light-actually-move/lesson-learned.md), from Io eclipse timing to evidence for the finite speed of light |

<details>
<summary>Earlier or supporting learning labs</summary>

- [OOP in C Lab](https://github.com/gcomneno/oop-in-c-lab) — object layout, manual virtual dispatch, runtime type identity and checked downcasting
- [JavaScript Lab](https://github.com/gcomneno/js-lab-didattico) — JavaScript and TypeScript middleware pipelines and reusable design patterns, with executable tests
- [BoardLab](https://github.com/gcomneno/boardlab) — generic game-engine architecture and reproducible search/AI experiments in early incubation
- [Historical Laravel Lab](https://github.com/gcomneno/web) — earlier backend web study and documentation

</details>

## <code>05 · LATEST UPDATES</code>
<!-- updates:start -->

- **2026-09-17** · `petra` · **Development:** [research: tighten Phase 6 source register](https://github.com/gcomneno/petra/commit/5b6bb4e39f82d1e3123173731ac95f7befa6601e)
- **2026-09-17** · `petra` · **Development:** [research: tighten Phase 6 validation statuses](https://github.com/gcomneno/petra/commit/86ed4f2c7f84b3fa1fe67157d2046ef9ee6f86e1)
- **2026-09-17** · `petra` · **Development:** [research: add Phase 6 validation matrix](https://github.com/gcomneno/petra/commit/3bfe5532092422f1b77ccccd65f9672efd3855ac)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA structural statistics and Lipschitz observables (#292)](https://github.com/gcomneno/petra/commit/12ca1ae1a982e82e125879cf71de8778d0147ac3)

<details>
<summary>More recent meaningful updates</summary>

- **2026-09-17** · `petra` · **Development:** [research: add structural statistics probe](https://github.com/gcomneno/petra/commit/74775285f144e8a260303524acaaac394746a722)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA automorphisms and symmetry (#290)](https://github.com/gcomneno/petra/commit/34957ac2603dafb961f62e83671c34d3f943a2c0)
- **2026-09-17** · `petra` · **Development:** [research: add bounded PETRA automorphism probe](https://github.com/gcomneno/petra/commit/de22d6f6abfa38c63e3009135cbb5632c46788e9)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA rewrite presentations (#288)](https://github.com/gcomneno/petra/commit/b31d344c2f66386ff4f70ce540da7bfc24897789)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA rewrite presentations](https://github.com/gcomneno/petra/commit/97b0e1193d5218efbe79b9097df2a12a1e053624)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA congruences and quotients (#286)](https://github.com/gcomneno/petra/commit/027544713c44a2822acb8cfdecc090e73c47c565)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA congruences and quotients](https://github.com/gcomneno/petra/commit/b47ba15ff0ce794fc2b9ea2ef8181bfa183af8fc)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA grading and edit-graph geometry (#284)](https://github.com/gcomneno/petra/commit/18f74077cfd2ec2ee36198287904ee315e25693e)
- **2026-09-17** · `petra` · **Development:** [research: expose non-unique common-reduct witness](https://github.com/gcomneno/petra/commit/8b29fa55fef48310f40e6025fc255c0ca710d677)
- **2026-09-17** · `petra` · **Development:** [research: prove non-unique maximum common reducts](https://github.com/gcomneno/petra/commit/450b5a6cbf4981e1d5b44ac3eeaaef0fa0d78fad)
- **2026-09-17** · `petra` · **Development:** [research: add bounded PETRA edit-geometry probe](https://github.com/gcomneno/petra/commit/9bac0ea232fed01848701cfbd6315fff1f2467c2)
- **2026-09-17** · `petra` · **Development:** [research: formalize PETRA grading and edit geometry](https://github.com/gcomneno/petra/commit/87183c7458d540c67b6e6499fd26a32c651cf502)
- **2026-09-17** · `petra` · **Development:** [research: formalize AIP-5 interpretation theory (#282)](https://github.com/gcomneno/petra/commit/fccc9116bb98814c1597afb11e9cf48ef67a179c)
- **2026-09-17** · `petra` · **Development:** [research: tighten AIP-5 interpretation foundations](https://github.com/gcomneno/petra/commit/df3103a91954ad2e324d47d562f471b4e4489248)
- **2026-09-17** · `petra` · **Development:** [research: formalize AIP-5 interpretation theory](https://github.com/gcomneno/petra/commit/3572f761b570e0788800a7fd946c45a945b88842)
- **2026-09-17** · `petra` · **Development:** [research: formalize and probe AIP-4 minimal algebra (#280)](https://github.com/gcomneno/petra/commit/00d266bbc24d92276fa9ae85341e534dcbb5f357)
- **2026-09-17** · `petra` · **Development:** [research: align AIP-4 with explicit root axiom](https://github.com/gcomneno/petra/commit/6ee8b0f3c652d7841ed7f8cb4f34bebd2895812a)
- **2026-09-17** · `petra` · **Development:** [research: make root-parent axiom explicit](https://github.com/gcomneno/petra/commit/2239539ee5949699607afbed3e1ba424ed66da33)
- **2026-09-17** · `petra` · **Development:** [research: add AIP-4 minimal algebra probe](https://github.com/gcomneno/petra/commit/ad1c6eaaa891a759163454c9c654677cdd713e6f)
- **2026-09-17** · `petra` · **Development:** [research: formalize AIP-4 minimal algebra](https://github.com/gcomneno/petra/commit/d4dadcf25c9613a4c265151b60dbf801910a8ae0)
- **2026-09-17** · `petra` · **Development:** [research: formalize canonical PETRA carrier theory (#278)](https://github.com/gcomneno/petra/commit/74c397388cd5c30b05509c821b93c7040c160c63)
- **2026-09-17** · `petra` · **Development:** [research: tighten canonical carrier foundations](https://github.com/gcomneno/petra/commit/d72730096903332dd093901caa9411566c693682)
- **2026-09-17** · `petra` · **Development:** [research: formalize canonical PETRA carrier](https://github.com/gcomneno/petra/commit/8220da283ab53420262e073ebb83f3eb7df1e0db)
- **2026-09-17** · `petra` · **Development:** [research: formalize abstract carrier foundational answers (#275)](https://github.com/gcomneno/petra/commit/ac2c4187e8d280878711d8fec2a7a3c23a1ef007)
- **2026-09-17** · `petra` · **Development:** [research: formalize abstract carrier foundational answers](https://github.com/gcomneno/petra/commit/668bea1bbf172bcbc21655953b23257fcb1ad211)
- **2026-09-17** · `petra` · **Development:** [research: analyze Terminal as empty composition (#273)](https://github.com/gcomneno/petra/commit/efa883dfec07ad5e1fe748426b61a190b433a5fc)
- **2026-09-17** · `petra` · **Development:** [research: probe Terminal as empty composition](https://github.com/gcomneno/petra/commit/4969fb7a25fa7c44b001415bb32bf98f59bb8484)
- **2026-09-17** · `petra` · **Development:** [research: analyze Terminal versus empty composition](https://github.com/gcomneno/petra/commit/07eaccec469ff4f566daee03f947bf3218b733c3)
- **2026-09-17** · `petra` · **Development:** [research: reassess AIP-2 primitive relation ontology (#269)](https://github.com/gcomneno/petra/commit/4c174646ed7afc2e81f8aff36cee8e5d88277ab1)
- **2026-09-17** · `petra` · **Development:** [research: reassess AIP-2 primitive relation ontology](https://github.com/gcomneno/petra/commit/6040b5179be66bf4a3e521e7d0b07fc26235458d)
- **2026-09-17** · `petra` · **Development:** [research: probe AIP-1 Set vs Multiset composition (#267)](https://github.com/gcomneno/petra/commit/ca5322a056946a84fb387dfa73e26f7149b9e34b)
- **2026-09-17** · `petra` · **Docs:** [record AIP-1 set vs multiset prototype](https://github.com/gcomneno/petra/commit/f736a6a7995e23aea1be43d4e93d2cf538e65ccd)
- **2026-09-17** · `petra` · **Development:** [research: add AIP-1 set vs multiset probe](https://github.com/gcomneno/petra/commit/2c0fe22271f07fffcad1daac701bf67856585c04)
- **2026-09-17** · `petra` · **Development:** [research: analyze AIP-1 multiplicity ontology (#265)](https://github.com/gcomneno/petra/commit/caca013c8b85345e639bf11cdabf1808e20df6ad)
- **2026-09-17** · `petra` · **Development:** [research: analyze AIP-1 multiplicity ontology](https://github.com/gcomneno/petra/commit/4718cd85ccc9666fc787c6e6f5625a9a7576053f)
- **2026-09-17** · `petra` · **Development:** [research: validate AIP-2 recursive containment (#262)](https://github.com/gcomneno/petra/commit/3544a4e849d45a843865468b32f948b3832d5843)
- **2026-09-17** · `petra` · **Fix:** [make AIP-2 wrapper erasure assertion semantic](https://github.com/gcomneno/petra/commit/c3f4498135c382b763a2387dab3dfc018d908182)
- **2026-09-17** · `petra` · **Docs:** [describe AIP-2 recursive containment prototype](https://github.com/gcomneno/petra/commit/4e0c122660ddfec39be4a9da753fafe7398fbc42)
- **2026-09-17** · `petra` · **Development:** [research: add AIP-2 recursive containment probe](https://github.com/gcomneno/petra/commit/9fac017bd85bb992024f02f1f5f9020f572c67ef)
- **2026-09-17** · `petra` · **Development:** [research: add AIP-2 wrapper-erasure probe](https://github.com/gcomneno/petra/commit/1d0beebe5eae9e59edb042165ef7ddcfee70cab6)
- **2026-09-17** · `petra` · **Development:** [research: audit AIP-2 relation ontology](https://github.com/gcomneno/petra/commit/5d0154d73bad78043716c77ed54082913d9ef2fe)
- **2026-09-17** · `petra` · **Development:** [research: audit AIP-2 level derivability (#258)](https://github.com/gcomneno/petra/commit/999fe865cf81703b40e77fa8cb300a2b1d6cd1ec)
- **2026-09-17** · `petra` · **Development:** [research: audit AIP-2 level derivability](https://github.com/gcomneno/petra/commit/e7d1e4d91a9e64c71bb560ba6b639e1cf8c4c6b5)
- **2026-09-17** · `petra` · **Development:** [research: prototype AIP-3 order-independent quotient (#255)](https://github.com/gcomneno/petra/commit/58e177a9e110e78336f001ee33b7d985744a1801)
- **2026-09-17** · `petra` · **Development:** [research: formalize AIP-3 quotient invariance](https://github.com/gcomneno/petra/commit/24abb5a56d3ab361e86164075feeb5cc9711f997)
- **2026-09-17** · `petra` · **Docs:** [record AIP-3 order-independent prototype](https://github.com/gcomneno/petra/commit/b4ca28e936ae34b0966ad4c24a242b881ffadbb7)
- **2026-09-17** · `petra` · **Development:** [research: analyze AIP-3 order semantics (#253)](https://github.com/gcomneno/petra/commit/04bd54fde7bc64547871c5025688a3f6a48dc669)
- **2026-09-17** · `petra` · **Development:** [research: analyze AIP-3 order semantics](https://github.com/gcomneno/petra/commit/6add6275c466293e44ffcd3b957ede0aa34c692d)
- **2026-09-17** · `petra` · **Development:** [research: audit PETRA model against abstract paradigm](https://github.com/gcomneno/petra/commit/723b656301937df64f2c36b38d27d622d2bfd8b9)
- **2026-09-17** · `petra` · **Development:** [research: define PETRA abstract paradigm (#245)](https://github.com/gcomneno/petra/commit/7c3304a77d34e1630315ad0405c577f67a2e562b)
- **2026-09-17** · `petra` · **Development:** [research: define PETRA abstract paradigm](https://github.com/gcomneno/petra/commit/ca66a14c034b8102d9e6f4d3f08dc9fa749e04cc)
- **2026-09-17** · `petra` · **Docs:** [link PETRA research source register](https://github.com/gcomneno/petra/commit/1fc32d9cf8d457a833d9559461a4e6ea7053342e)
- **2026-09-17** · `petra` · **Docs:** [add PETRA research source register](https://github.com/gcomneno/petra/commit/91bbf2fd81160bd63448d766a75eca2ff0c8d76c)
- **2026-09-17** · `petra` · **Docs:** [establish PETRA related-work survey (#241)](https://github.com/gcomneno/petra/commit/a60f3dd7a4bfc9f7f6acb325d3fbc2c6730c04cc)
- **2026-09-17** · `petra` · **Docs:** [link maintained related-work survey](https://github.com/gcomneno/petra/commit/133762e3a85dae199840673ca69c282cd652f6ab)
- **2026-09-17** · `petra` · **Docs:** [establish PETRA related-work survey](https://github.com/gcomneno/petra/commit/d69e18289312a48755885fde76ac0506ffcecde0)
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

_Showing the 100 most recent meaningful updates; 1975 older update(s) omitted._

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
