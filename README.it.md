<h1 align="center">Giancarlo Cicellyn Comneno</h1>

<p align="center">
  <a href="./README.md">English</a> · <strong>Italiano</strong>
</p>

<p align="center">
  <strong>Sviluppatore software backend e tooling · Python · Linux · Automazione · Open Source</strong>
</p>

<p align="center">
  <img alt="Backend — Tooling · Python — Sistemi e API · Linux — Automazione · Open Source — Engineering" src="./assets/profile-badges.svg">
</p>

<p align="center">
  Trasformo problemi operativi ricorrenti in strumenti affidabili, flussi espliciti e software open source riutilizzabile.
</p>

<h3 align="center">Engineering assistito dall'AI</h3>

<p align="center">
  L'AI fa parte dei miei strumenti di lavoro. La uso per accelerare ricerca, implementazione, test, review e documentazione, mantenendo responsabilità umana, comprensione tecnica, verifica ed evidenze al centro di ogni contributo pubblicato.
</p>

<p align="center">
  <img alt="Visitatori del profilo" src="https://komarev.com/ghpvc/?username=gcomneno&label=%F0%9F%91%80&nbsp;&color=0B1F3A&style=flat-square">
</p>

## <code>01 · PROGETTI SELEZIONATI</code>

Questi progetti rappresentano meglio il mio lavoro attuale tra progettazione backend, automazione affidabile, strumenti per sviluppatori e flussi software riproducibili.

<p align="center">
  <strong>Demo live in evidenza — Atelier-Kit</strong><br>
  Prova direttamente nel browser la demo pubblica di Atelier-Kit.
</p>

<p align="center">
  <a href="https://atelier-kit-public-demo.vercel.app/">
    <img alt="Demo live di Atelier-Kit" src="https://img.shields.io/badge/LIVE%20DEMO-Apri%20nel%20browser-0B1F3A?style=for-the-badge&logo=vercel&logoColor=white">
  </a>
  &nbsp;
  <a href="https://github.com/gcomneno/atelier-kit">
    <img alt="Codice sorgente Atelier-Kit" src="https://img.shields.io/badge/SOURCE%20CODE-GITHUB-24292F?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>

| Progetto | Release ufficiale | Cosa fa | Cosa dimostra |
| --- | --- | --- | --- |
| [Atelier-Kit](https://github.com/gcomneno/atelier-kit) | [v0.5.1](https://github.com/gcomneno/atelier-kit/releases/tag/v0.5.1) | Fornisce un kit vetrina configurabile con authoring tramite Studio locale, Atelier Desktop e Hosted Studio privato configurato separatamente, catalogo content-driven e strumenti di pubblicazione | Architettura di prodotto SvelteKit, confini di autorità espliciti tra Visitor/local/hosted, mutazioni repository atomiche, distribuzione desktop e adozione downstream di Giada UI |
| [Smart File Organizer](https://github.com/gcomneno/smart-file-organizer) | [v0.6.0](https://github.com/gcomneno/smart-file-organizer/releases/tag/v0.6.0) | Analizza i file, mostra in anteprima un piano di organizzazione e li sposta solo su richiesta esplicita | Automazione deterministica dei file, dry-run espliciti, decisioni spiegabili, verifica del filesystem e pianificazione read-only del recupero |
| [LeLe Manager](https://github.com/gcomneno/lele-manager) | [v1.11.1](https://github.com/gcomneno/lele-manager/releases/tag/v1.11.1) | Raccoglie, cerca e riutilizza lesson learned testuali tramite flussi Markdown, CLI, GUI e API | Dati local-first, persistenza JSONL, confini API, progettazione backend e distribuzione desktop pacchettizzata |
| [GiadaWare UI Components](https://github.com/gcomneno/giadaware-ui-components) | [v0.1.0](https://github.com/gcomneno/giadaware-ui-components/releases/tag/v0.1.0) | Fornisce primitive UI Svelte riutilizzabili per applicazioni GiadaWare tramite entry point base, visitor e studio isolati | Architettura di package Svelte, artefatti immutabili pacchettizzati, entry point isolati e contratti SSR/hydration e accessibilità |
| [GYTE](https://github.com/gcomneno/gyte) | [v1.3.1](https://github.com/gcomneno/gyte/releases/tag/v1.3.1) | Estrae da YouTube trascrizioni, audio e video e supporta reflow, traduzione e trascrizione locale dei contenuti | Progettazione CLI guidata da manifest, pipeline di estrazione multimediale e strumenti operativi riproducibili |
| [Ubuntu System Tools](https://github.com/gcomneno/ubuntu-system-tools) | [v0.3.0](https://github.com/gcomneno/ubuntu-system-tools/releases/tag/v0.3.0) | Utilità Linux per diagnostica, manutenzione controllata, trascrizione offline e analisi degli avvisi kernel | Tooling di sistema safety-first, diagnostica read-only, flussi espliciti su opt-in e packaging Linux riproducibile |
| [GiadaWare AI](https://github.com/gcomneno/giadaware-ai) | [v0.0.1](https://github.com/gcomneno/giadaware-ai/releases/tag/v0.0.1) | Infrastruttura sperimentale 0.x per capacità AI read-only indipendenti dal provider, con output tipizzati e backend sostituibili | Infrastruttura AI indipendente dal provider, output tipizzati, confini di validazione deterministici e backend sostituibili |
| [GYTE AI Learning Pipeline](https://github.com/gcomneno/gyte-ai-learning-pipeline) | [v0.5.0](https://github.com/gcomneno/gyte-ai-learning-pipeline/releases/tag/v0.5.0) | Pipeline di contenuti riavviabili per acquisire, validare e trasferire materiale tra confini privati e pubblici | Validazione deterministica, workflow riavviabili, confini espliciti di privacy e handoff controllati verso servizi esterni |


### Esperienza e GiadaWare

**GiadaWare™** è il mio laboratorio personale per trasformare gli attriti ricorrenti in appunti, strumenti e progetti pubblici.

La mia esperienza professionale precedente include PHP e Laravel; il lavoro pubblico attuale è concentrato su Python, Linux, automazione e ingegneria open source. Disponibile per ruoli da remoto e opportunità professionali.

> Ogni problema risolto una volta merita di diventare conoscenza. Se quella conoscenza è riutilizzabile, merita di diventare uno strumento. Se lo strumento è utile anche ad altri, merita di diventare open source.


## <code>02 · INGEGNERIA OPEN SOURCE</code>

Contribuisco upstream partendo da problemi reali del progetto: riproduco il comportamento, delimito la modifica, aggiungo test e porto la patch attraverso il processo di review del progetto.

### Yocto Project · `vscode-bitbake`

Estensione VS Code e language tooling per lavorare con **BitBake e Yocto Project**.

Upstream: [yoctoproject/vscode-bitbake](https://github.com/yoctoproject/vscode-bitbake) · Fork: [gcomneno/vscode-bitbake](https://github.com/gcomneno/vscode-bitbake)

| Cosa ho contribuito | Cosa dimostra |
| --- | --- |
| Correzioni alla discovery dei file recipe-local, limitando le scansioni ricorsive e introducendo cancellazione, caching e caricamento lazy | Debugging su codebase esistente, performance, concorrenza/cancellazione e non-regression testing |
| Semplificazione del flusso di selezione delle configurazioni BitBake e correzione dell'aggiornamento della status bar | Refactoring conservativo, characterization test e gestione coerente dello stato UI |
| Evoluzione del workspace di integration test verso `bitbake-setup` e Yocto 6.0 | Linux/Yocto, ambienti di integrazione riproducibili e manutenzione dell'infrastruttura di test |
| Aggiornamento controllato delle dipendenze npm, riducendo le vulnerabilità senza modificare i range dichiarati | Dependency maintenance, security hygiene e validazione multilivello |
| Estrazione di una ricerca file cancellabile riutilizzabile e di lifecycle dedicati per Toaster e gestione dei documenti BitBake | Refactoring TypeScript modulare, ownership esplicita del lifecycle e characterization test che preservano il comportamento |


### Pull request upstream selezionate e integrate

Le voci seguenti sono pull request upstream verificate come integrate; i fork pubblici non vengono usati come prova di un contributo accettato.

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
<summary>Ecosistema Canonical Craft</summary>

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

## <code>03 · RICERCA SELEZIONATA</code>

Questi repository usano esperimenti software riproducibili per studiare strutture di sequenze, comportamento statistico e calcolo deterministico.

| Area | Progetto | Focus tecnico |
| --- | --- | --- |
| Algebra strutturale ricorsiva | [PETRA](https://github.com/gcomneno/petra) | Algebra canonica shape-first per strutture a torre di esponenti primi, con forme ricorsive immutabili, operatori di riscrittura strutturale, CLI mantenuta e strumenti Resolver per cammini minimi e distanza |
| Analisi di sequenze | [Digit Probe](https://github.com/gcomneno/digit-probe) | Casualità, comprimibilità, autocorrelazione, n-grammi e pattern di tipo Schur tramite un'API di analisi riutilizzabile |
| Analisi della struttura modulare | [Midas](https://github.com/gcomneno/midas) | Impronte modulari deterministiche, localizzazione delle anomalie e confronto strutturale senza claim predittivi |
| Modellazione stocastica a stati finiti | [Lotto Digit Coverage Dynamics](https://github.com/gcomneno/lotto-digit-coverage-dynamics) | Modelli di Markov assorbenti esatti, verifica esaustiva del kernel, analisi dei segnali storici, contratti applicativi versionati e GUI di ricerca locale riproducibile |
| Riconoscimento di sequenze | [OEIS Probe](https://github.com/gcomneno/oeis-probe) | Consultazione OEIS offline, ricerca normalizzata e cache SQLite |
| Partizionamento deterministico | [Turbo-Bucketizer](https://github.com/gcomneno/turbo-bucketizer) | Partizionamento IPv4 ad alta entropia e allocazione deterministica |
| Ricerca strutturale | [Integer Structural Search](https://github.com/gcomneno/integer-structural-search) | Ricerca limitata su rappresentazioni intere e vincoli |
| Compressione di serie temporali | [Lasagna v2](https://github.com/gcomneno/lasagna-v2) | Segmentazione adattiva, codifica dei residui basata su predittori ed esperimenti lossy/lossless controllati su serie temporali univariate |

## <code>04 · IMPARARE IN PUBBLICO</code>

Trasformo lo studio in percorsi documentati e riproducibili, senza presentare i repository didattici come esperienza di produzione.

| Area | Repository | Focus attuale |
| --- | --- | --- |
| Analisi applicata di sequenze | [System Log Dynamics](https://github.com/gcomneno/system-log-dynamics) | Dimostratore riproducibile di Digit-Probe basato su normalizzazione privacy-safe dei journal Linux, evidenze deterministiche e confronto temporale |
| Linux embedded | [Mini laboratorio Yocto/QEMU](https://github.com/gcomneno/yocto-qemu-mini-lab) | Build riproducibili di immagini, layer e recipe personalizzati, flussi BitBake e validazione del boot con QEMU |
| Linux embedded | [Cat Couch Guardian](https://github.com/gcomneno/cat-couch-guardian) | Slice didattica C11 virtual-first basata su eventi di movimento, integrata in un’immagine ARM64 derivata con Yocto, autostart systemd ed evidence deterministica in QEMU |
| Sviluppo software | [Corso Kleis di sviluppo software](https://github.com/gcomneno/kleis-corso-sviluppo-software) | Esercizi progressivi in C#/.NET, HTML, SQL e PHP, incluso un CRUD verificato con PDO/MySQL e interfaccia Bootstrap |
| Fisica | [Studio della fisica](https://github.com/gcomneno/physics-study) | Lezioni originali e fact-checkate; prima lezione: [Does Light ACTUALLY Move?](https://github.com/gcomneno/physics-study/blob/main/lessons/does-light-actually-move/lesson-learned.md), dalle eclissi di Io alle prove della velocità finita della luce |
| Sviluppo software | [Laboratorio OOP in C](https://github.com/gcomneno/oop-in-c-lab) | Layout degli oggetti, dispatch virtuale manuale, identità di tipo a runtime e downcast controllato |
| Sviluppo software | [Laboratorio JavaScript](https://github.com/gcomneno/js-lab-didattico) | Pipeline middleware e pattern riutilizzabili in JavaScript e TypeScript, con test eseguibili |
| Architettura di motori di gioco | [BoardLab](https://github.com/gcomneno/boardlab) | Architettura generica per motori di gioco ed esperimenti riproducibili di ricerca e IA, ancora in incubazione iniziale |

## <code>05 · ULTIMI AGGIORNAMENTI</code>
<!-- updates:start -->

- **2026-09-23** · `lele-manager` · **Funzionalità:** [add assistant-ready context export (#258)](https://github.com/gcomneno/lele-manager/commit/ee1a000c759f94d2dea1d84b52b5ee78703f8033)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [finalize Italian M0.7 verified maturity](https://github.com/gcomneno/cat-couch-guardian/commit/254cea53e0fbf32ac43fc81c13888fcdb308138e)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [finalize M0.7 verified maturity](https://github.com/gcomneno/cat-couch-guardian/commit/92cf575744338ad7dc1371b6dbabdaa56fc303b5)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [align Italian exercises with M0.7 contract](https://github.com/gcomneno/cat-couch-guardian/commit/ffcb37fcb62ef7a416bd8d47c03c6b72c659e210)

<details>
<summary>Altri aggiornamenti recenti e significativi</summary>

- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [align exercises with implemented M0.7 contract](https://github.com/gcomneno/cat-couch-guardian/commit/50522837c3d72b5f3f7008611319a78c17ec63cc)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [explain Italian M0.7 state machine architecture](https://github.com/gcomneno/cat-couch-guardian/commit/8a738ff099989ee18925f4c0696e427c6eeedffd)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [explain M0.7 state machine architecture](https://github.com/gcomneno/cat-couch-guardian/commit/cc7eb5e5d7ffb20b59794c9dafc5545cac0d1baf)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [document Italian M0.7 cooldown contract](https://github.com/gcomneno/cat-couch-guardian/commit/72076360836a9c41d2ee8ad2a568d7381329be85)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [document M0.7 cooldown contract](https://github.com/gcomneno/cat-couch-guardian/commit/59e4d661da9fbb2833561a41356265cbe5900375)
- **2026-09-23** · `cat-couch-guardian` · **Funzionalità:** [demonstrate deterministic cooldown decisions](https://github.com/gcomneno/cat-couch-guardian/commit/1051135633978b45d2b7b30530e9120613e57e54)
- **2026-09-23** · `cat-couch-guardian` · **Funzionalità:** [emit deterministic event timestamps](https://github.com/gcomneno/cat-couch-guardian/commit/2f4b6b56aada4affd83f4992503fe811233344aa)
- **2026-09-23** · `cat-couch-guardian` · **Funzionalità:** [make simulated event time explicit](https://github.com/gcomneno/cat-couch-guardian/commit/a33c380bc25f1aef385593298f26a9bf149c5930)
- **2026-09-23** · `cat-couch-guardian` · **Funzionalità:** [implement deterministic cooldown policy](https://github.com/gcomneno/cat-couch-guardian/commit/6169521e0caa488610c2b751fe68734cd316f1f9)
- **2026-09-23** · `cat-couch-guardian` · **Funzionalità:** [add explicit cooldown state](https://github.com/gcomneno/cat-couch-guardian/commit/051117395c57e19719a9fa2acaba6ada282fa925)
- **2026-09-23** · `cat-couch-guardian` · **Funzionalità:** [expose suppression evidence boundary](https://github.com/gcomneno/cat-couch-guardian/commit/ae9756aaa1d1c31dd7b3224efae4a291feda7545)
- **2026-09-23** · `cat-couch-guardian` · **Funzionalità:** [add deterministic event timestamp](https://github.com/gcomneno/cat-couch-guardian/commit/ea2947edd385b37d55075c93a52507cda628e447)
- **2026-09-23** · `cat-couch-guardian` · **Funzionalità:** [define cooldown suppression evidence](https://github.com/gcomneno/cat-couch-guardian/commit/2d49dacbe884d617a1d3f97dde3687ab0ab40374)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [add Italian engineering exercises](https://github.com/gcomneno/cat-couch-guardian/commit/112e7ce1f1b6fde7acf8beb2ce957c2c60893819)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [add Italian architecture guide](https://github.com/gcomneno/cat-couch-guardian/commit/ae274bd5852d02d54a58eb7291420525ce014b78)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [add Italian learning path](https://github.com/gcomneno/cat-couch-guardian/commit/7bb5745443ad6c0a37589891f858e1394f502df8)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [add Italian README](https://github.com/gcomneno/cat-couch-guardian/commit/073f027a9e81f6a1111ecdd7a41cdf6dc9d5ec95)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [add Italian documentation policy](https://github.com/gcomneno/cat-couch-guardian/commit/281af14a8435b14a2daf53ab47f9e07662f14380)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [define bilingual documentation policy](https://github.com/gcomneno/cat-couch-guardian/commit/90dea27e13a8e806f675adbb68b7bac8eb99e5c1)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [add bilingual language selectors](https://github.com/gcomneno/cat-couch-guardian/commit/b4d8f85b1a7f4223d60b0ba909c7eb121e540dd4)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [make README a learning entry point](https://github.com/gcomneno/cat-couch-guardian/commit/c34fb57fce30b7c8ecbafe4da8b49cfb239b71aa)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [add junior engineering exercises](https://github.com/gcomneno/cat-couch-guardian/commit/60e99d05d6682e0bd6b13bfd38fb4e28af73812c)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [explain architecture for learners](https://github.com/gcomneno/cat-couch-guardian/commit/2d0eab196de69b9799d23b56459e5a1779f7dfd1)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [add junior learning path](https://github.com/gcomneno/cat-couch-guardian/commit/c22bc0bc90af3b82149e37f68a31e619fe05b4c1)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [formalize final exam simulation (#14)](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/0538d4f42527efc0fe791e4e8ee309674f640274)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [explain ISBN as sketch-derived design choice](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/529272834cac9b0fe98d5eae2766a827713b69ae)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [tighten faithful transcription of exam part A](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/21cdaeb19251138eabbcf352c5a11a74776cd2bd)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [expose final exam simulation from root README](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/eb24ac14c3bcec5e4727a6106a6c41bebfc4e5f6)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [add final exam simulation runbook](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/10f40f9dbec12a7dfc4b65af2ae7439dc5556dcb)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [add runnable part B fixture](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/875c177e649d2e73b8d87d406446fdd56639f3f7)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [add expected SQL result](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/ecb0fadc2dd43905b3b088d3eab75f9957eed1fb)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [add final exam SQL solution](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/adb618d40ce4f88c20cc6ee9f6bbf503ae3071ea)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Funzionalità:** [add exam simulation custom CSS](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/c029deed486ef1311a31dd5f3d4d31b98a9c9379)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Funzionalità:** [add exam simulation delete action](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/40af7deb555cc39aff446889f0013cbea3e02432)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Funzionalità:** [add exam simulation create action](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/394ff13870eb57c475c3526adbb14175561e87ab)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Funzionalità:** [add exam simulation main page](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/0956ca1bfe5941bc22221e09f9977e6b8c33bd99)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Funzionalità:** [add exam simulation PDO boundary](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/975db1f0501612b8921c3ffe515b66ca2e24e9f8)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Funzionalità:** [add exam simulation seed](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/ad53e4e488404376b95e34e223477c2466770725)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Funzionalità:** [add exam simulation book schema](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/62a5884d24c2e85546514ee2b8f1ee5de617e4ee)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [add detailed final exam reference solution](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/dae9a78b606fa3ececeb8ec43649904f926b85ed)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [add final exam verification checklist](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/91811b655929d10ef51453efe82392d9d44edc7d)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [add repeatable final exam protocol](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/96436f0536e064326dbed6d704ee12948906d530)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [transcribe final exam simulation part B](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/cf6a9c4d4a8a7810ea4c9d91dd14c366d4d32c39)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [transcribe final exam simulation part A](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/86e8f45cd5e8daad750454e82d92103bd64daed8)
- **2026-09-23** · `kleis-corso-sviluppo-software` · **Documentazione:** [add final exam simulation overview](https://github.com/gcomneno/kleis-corso-sviluppo-software/commit/026eea6e29d26939ccf4cd140ddbd947aa79ed27)
- **2026-09-19** · `lotto-digit-coverage-dynamics` · **Documentazione:** [add Zenodo DOI metadata](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/7c2eded9d271484ad3a50afd8d27b43e7dc4bd0e)
- **2026-09-19** · `cat-couch-guardian` · **Documentazione:** [update M0.6 packaging and provenance](https://github.com/gcomneno/cat-couch-guardian/commit/d9ffbe1a818a80633aad78a8b50ceb45547c1880)
- **2026-09-19** · `lotto-digit-coverage-dynamics` · **Release:** [v1.2.0 — Reproducible archive tooling and semantic read queries](https://github.com/gcomneno/lotto-digit-coverage-dynamics/releases/tag/v1.2.0)
- **2026-09-19** · `cat-couch-guardian` · **Funzionalità:** [add simulated deterrent request boundary](https://github.com/gcomneno/cat-couch-guardian/commit/2050fea045b3a0e390ee7111c401781f16889035)
- **2026-09-19** · `lotto-digit-coverage-dynamics` · **Documentazione:** [prepare v1.2.0 publication metadata](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/c2dadf97e7aa3dfd6c312f034978756974303b4b)
- **2026-09-19** · `lotto-digit-coverage-dynamics` · **Funzionalità:** [integrate semantic read queries into db ask](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/6ff339782d33651f3eb9f48c92c819d0966675d6)
- **2026-09-19** · `lele-manager` · **Funzionalità:** [add task-focused Context Packs (#257)](https://github.com/gcomneno/lele-manager/commit/3a39af8491c49fef337c0ba41561709c4e151eee)
- **2026-09-19** · `lele-manager` · **Documentazione:** [define canonical product language contract (#256)](https://github.com/gcomneno/lele-manager/commit/2f1848a7a7c49b2ac8a6d5ab4d29ce543036d808)
- **2026-09-19** · `giadaware-ai` · **Release:** [GiadaWare AI v0.0.1](https://github.com/gcomneno/giadaware-ai/releases/tag/v0.0.1)
- **2026-09-19** · `lele-manager` · **Funzionalità:** [add semantic Lesson Learned extraction (#255)](https://github.com/gcomneno/lele-manager/commit/faf88c59e75dccf132c0e17677b359ae42ea820d)
- **2026-09-19** · `giadaware-ai` · **Funzionalità:** [support Ollama thinking control](https://github.com/gcomneno/giadaware-ai/commit/36a1bb751ec3851d3ceb0a38abe052747984ce5e)
- **2026-09-19** · `giadaware-ai` · **Documentazione:** [record GPT-6 Astra runtime verification](https://github.com/gcomneno/giadaware-ai/commit/7081dd4c2e00db2907da6e4f0569ff80dd68df58)
- **2026-09-18** · `digit-probe` · **Documentazione:** [record Zenodo DOI for v1.0.0 (#32)](https://github.com/gcomneno/digit-probe/commit/b632e18d05d24a9050dc87e2411ed8b47efbdf07)
- **2026-09-18** · `digit-probe` · **Documentazione:** [add Zenodo citation metadata (#31)](https://github.com/gcomneno/digit-probe/commit/dc1d2f399170804c3e66fc4eb86af6360c7d38ba)
- **2026-09-18** · `smart-file-organizer` · **Release:** [v0.6.0](https://github.com/gcomneno/smart-file-organizer/releases/tag/v0.6.0)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [add v0.5.0 download and quick start CTA (#53)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/1c19b4413b29ee3ddc0d62df85b1b096e90da268)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Release:** [GYTE AI Learning Pipeline v0.5.0 Technical Preview](https://github.com/gcomneno/gyte-ai-learning-pipeline/releases/tag/v0.5.0)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Funzionalità:** [prepare downloadable technical preview (#52)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/010e681ef03fadda97a9bff2a94c4c1210e6524c)
- **2026-09-18** · `digit-probe` · **Release:** [Digit Probe v1.0.0](https://github.com/gcomneno/digit-probe/releases/tag/v1.0.0)
- **2026-09-18** · `smart-file-organizer` · **Documentazione:** [align README with verifiable recovery state (#106)](https://github.com/gcomneno/smart-file-organizer/commit/19376637a6abe79a9fd56d0c0a145cadfdf73120)
- **2026-09-18** · `digit-probe` · **Documentazione:** [define consumer-safe analysis contract (#22) (#25)](https://github.com/gcomneno/digit-probe/commit/8239fc4198b5526552ee40f22cff9446d9650f56)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [complete manual social-source triage PoV (#50)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/fc54e981b9478ba44f24bb1d86af9609d5acc727)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [complete Source-to-Skill human/agent PoV (#49)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/5ca6e842c6bcf861ebc8a33faa01d21725684724)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [adopt canonical English localization boundary (#48)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/2f89a7ecd4bd379a33eaa44ac17da51614d98f34)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [record social triage PoV automation decision](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/22040b3553c8fb1e97103d6d5137c438b920f310)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [complete manual social-source triage PoV](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/b9696140261acc619068a2ce097aee5b57e08073)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [record Source-to-Skill PoV result](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/cacd624733a41a51601998093e414761b021a1b8)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [complete single-source Source-to-Skill PoV](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/5214a3d027beb313e1f9534294f44e812dc7f17d)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Funzionalità:** [automate approved repository handoff up to PR creation (#47)](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/00ca1c5502ee087d15ee099bb47757e9890488a6)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [mirror localization boundary in Italian README](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/a32b491c40d826e67f3ac7376362b611f383a704)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [expose canonical English localization boundary](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/2692fd3426f2f32c2300100122343a9f20e5d35b)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [align Italian documentation policy mirror](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/4803e4240058d70045836e12402b9731a20501f5)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [align documentation with canonical English policy](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/00cba5f3ec531c3d67fc652f361d3ec4633b4c53)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Documentazione:** [define canonical language and translation boundary](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/dea1ecddba814f811b078fdcdd35233871fbfe2f)
- **2026-09-18** · `gyte-ai-learning-pipeline` · **Correzione:** [bind handoff checkout to declared repository](https://github.com/gcomneno/gyte-ai-learning-pipeline/commit/fbe3a4d9e722d67a726585f485a050624c78e9e2)
- **2026-09-18** · `giadaware-ai` · **Documentazione:** [add repository agent governance](https://github.com/gcomneno/giadaware-ai/commit/ae7387f74e7423513409e80c8e193121ffda6040)
- **2026-09-17** · `petra` · **Sviluppo:** [research: tighten Phase 6 source register](https://github.com/gcomneno/petra/commit/5b6bb4e39f82d1e3123173731ac95f7befa6601e)
- **2026-09-17** · `petra` · **Sviluppo:** [research: tighten Phase 6 validation statuses](https://github.com/gcomneno/petra/commit/86ed4f2c7f84b3fa1fe67157d2046ef9ee6f86e1)
- **2026-09-17** · `petra` · **Sviluppo:** [research: add Phase 6 validation matrix](https://github.com/gcomneno/petra/commit/3bfe5532092422f1b77ccccd65f9672efd3855ac)
- **2026-09-17** · `petra` · **Sviluppo:** [research: add Phase 6 source register](https://github.com/gcomneno/petra/commit/ec555670629311bb844ff89f7d0fa52a86d68a5b)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA structural statistics and Lipschitz observables (#292)](https://github.com/gcomneno/petra/commit/12ca1ae1a982e82e125879cf71de8778d0147ac3)
- **2026-09-17** · `petra` · **Sviluppo:** [research: add structural statistics probe](https://github.com/gcomneno/petra/commit/74775285f144e8a260303524acaaac394746a722)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA structural statistics](https://github.com/gcomneno/petra/commit/cba03abd4d4a70d67f8c591e50dc382c5950b987)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA automorphisms and symmetry (#290)](https://github.com/gcomneno/petra/commit/34957ac2603dafb961f62e83671c34d3f943a2c0)
- **2026-09-17** · `petra` · **Sviluppo:** [research: strengthen automorphism probe independence](https://github.com/gcomneno/petra/commit/00b1a9473946bf915ed31ee5fb0efbb36f015cd7)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA automorphisms and symmetry](https://github.com/gcomneno/petra/commit/222a1b08e6404904abb7dd2a4f10a1bbcf10c8b3)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA rewrite presentations (#288)](https://github.com/gcomneno/petra/commit/b31d344c2f66386ff4f70ce540da7bfc24897789)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA congruences and quotients (#286)](https://github.com/gcomneno/petra/commit/027544713c44a2822acb8cfdecc090e73c47c565)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA congruences and quotients](https://github.com/gcomneno/petra/commit/b47ba15ff0ce794fc2b9ea2ef8181bfa183af8fc)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA grading and edit-graph geometry (#284)](https://github.com/gcomneno/petra/commit/18f74077cfd2ec2ee36198287904ee315e25693e)
- **2026-09-17** · `petra` · **Sviluppo:** [research: expose non-unique common-reduct witness](https://github.com/gcomneno/petra/commit/8b29fa55fef48310f40e6025fc255c0ca710d677)

_Sono mostrati i 100 aggiornamenti significativi più recenti; 1819 aggiornamenti precedenti sono stati omessi._

</details>

<!-- updates:end -->

---

<p align="center">
  <br>
  <em>Questo profilo è un laboratorio in movimento: software affidabile, decisioni esplicite, documentazione chiara e iterazione pubblica.</em>
</p>

<p align="center">
  <a href="https://github.com/sponsors/gcomneno">
    <img alt="Sostieni questo laboratorio su GitHub" src="https://img.shields.io/badge/Sostieni%20questo%20laboratorio-GitHub%20Sponsors-0B1F3A?style=flat-square&logo=githubsponsors&logoColor=white&labelColor=555555">
  </a>
</p>
