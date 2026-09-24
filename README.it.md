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

- **2026-09-24** · `petra` · **Sviluppo:** [research: close Phase 6 external mathematical validation (#312)](https://github.com/gcomneno/petra/commit/4a65d073501b7e6e6aa0980bce88766be387bccf)
- **2026-09-24** · `petra` · **Sviluppo:** [research: record Phase 6 closure audit](https://github.com/gcomneno/petra/commit/34d47411ba5f0f8bdc1fb7c28ea47e2fbea29082)
- **2026-09-24** · `petra` · **Sviluppo:** [research: freeze Phase 6 validation matrix](https://github.com/gcomneno/petra/commit/40238b441b8b2dfe09ce03ba0b08aa1519510c5c)
- **2026-09-24** · `petra` · **Sviluppo:** [research: validate exact PETRA leaf-edit metric formula (#310)](https://github.com/gcomneno/petra/commit/dc6181ee210abb6c3faab8fe980077afde62e628)

<details>
<summary>Altri aggiornamenti recenti e significativi</summary>

- **2026-09-24** · `petra` · **Sviluppo:** [research: resolve final metric validation rows](https://github.com/gcomneno/petra/commit/95799ebe81a0e5f0fb5564a784630894197e3a70)
- **2026-09-24** · `petra` · **Sviluppo:** [research: classify exact PETRA edit metric results](https://github.com/gcomneno/petra/commit/9c6afbb684c5b60e1f69591285716f1257fac150)
- **2026-09-24** · `petra` · **Sviluppo:** [research: register edit-distance common-structure framework](https://github.com/gcomneno/petra/commit/820b86420cbeb0b928b1cfb7bacdd281b87d043f)
- **2026-09-24** · `petra` · **Sviluppo:** [research: refute rooted lower-neighbour set reconstruction (#308)](https://github.com/gcomneno/petra/commit/d7573c4c4f00b9ed2106cdd4b8186ae052af5017)
- **2026-09-24** · `petra` · **Sviluppo:** [research: record minimal rooted reconstruction counterexample](https://github.com/gcomneno/petra/commit/ca8a31245e34da8400c153feb8001ecfe8a99b54)
- **2026-09-24** · `petra` · **Sviluppo:** [research: register rooted one-leaf deck source](https://github.com/gcomneno/petra/commit/7dc08558be5341af74c68d8e2f9825202e77ba10)
- **2026-09-24** · `petra` · **Sviluppo:** [research: validate global PETRA edit-graph automorphism questions (#306)](https://github.com/gcomneno/petra/commit/cc0a0dd03380502b75f0d3804fa5b4b78f1a6699)
- **2026-09-24** · `petra` · **Sviluppo:** [research: resolve one-step target orbit converses](https://github.com/gcomneno/petra/commit/7c49124d2083cf21e27aeb1b1220accecf92160f)
- **2026-09-24** · `petra` · **Sviluppo:** [research: classify global edit-graph validation results](https://github.com/gcomneno/petra/commit/f9931e35563c1ad9e42df8ecf0b9993e17749dcf)
- **2026-09-24** · `petra` · **Sviluppo:** [research: register tree reconstruction and pseudosimilarity sources](https://github.com/gcomneno/petra/commit/4d6fae96b6c7a581fca8e976e91af7b1812a5e25)
- **2026-09-24** · `petra` · **Sviluppo:** [research: audit PETRA witnessed edits against residual-system axioms (#304)](https://github.com/gcomneno/petra/commit/4d1d7100da1fa36e2616f0c2fd3dca36285d3663)
- **2026-09-24** · `petra` · **Sviluppo:** [research: audit witnessed edits against residual-system axioms](https://github.com/gcomneno/petra/commit/8b9c8b681a1cea4af75d9400f169f4b39a5eb7b9)
- **2026-09-24** · `petra` · **Sviluppo:** [research: align residual comparison with axiom audit](https://github.com/gcomneno/petra/commit/65ca1bf808e0078b29ead87d979b3323434e68f3)
- **2026-09-24** · `petra` · **Sviluppo:** [research: resolve PETRA residual-system membership audit](https://github.com/gcomneno/petra/commit/11e5e48432159efb8afbfc45f85fa0dfcd0a53be)
- **2026-09-24** · `petra` · **Sviluppo:** [research: record residual-system audit axioms](https://github.com/gcomneno/petra/commit/9eebb2d11584ff78c20967faa5aa9b21428ab00b)
- **2026-09-24** · `petra` · **Sviluppo:** [research: compare PETRA state-dependent edit residuals with residual theory (#302)](https://github.com/gcomneno/petra/commit/7bbca260bafa6e914532b972ddc3664652802867)
- **2026-09-24** · `petra` · **Sviluppo:** [research: advance residual validation next step](https://github.com/gcomneno/petra/commit/73df852db02cb6d2b0642970b0b307aa2c53077e)
- **2026-09-24** · `petra` · **Sviluppo:** [research: compare PETRA with residual rewriting theory](https://github.com/gcomneno/petra/commit/a42ae31a43cbb872dd9b52abbf1b87651d36a0b6)
- **2026-09-24** · `petra` · **Sviluppo:** [research: extend path comparison with residual theory](https://github.com/gcomneno/petra/commit/4b6a9befd8d9db95dfbf2853de3386aa9c0a3115)
- **2026-09-24** · `petra` · **Sviluppo:** [research: sharpen state-dependent residual classification](https://github.com/gcomneno/petra/commit/c010814a3b5edafc2eae22265bf033332b78d9b1)
- **2026-09-24** · `petra` · **Sviluppo:** [research: register residual-theory sources](https://github.com/gcomneno/petra/commit/9f3c2ad260a5294779dcad2170e7c58473298b82)
- **2026-09-24** · `petra` · **Sviluppo:** [research: validate PETRA witnessed paths against free categories, groupoids, and traces (#300)](https://github.com/gcomneno/petra/commit/f13c78b2ea8fcba147790325934ba3ae833b2572)
- **2026-09-24** · `petra` · **Sviluppo:** [research: correct trace-theory source attribution](https://github.com/gcomneno/petra/commit/db17d0fad24391dffefd4e97760fd08513aeaf7a)
- **2026-09-24** · `petra` · **Sviluppo:** [research: compare witnessed paths with categories groupoids and traces](https://github.com/gcomneno/petra/commit/96c1a5ee3183392fd855e109edced28e238fa597)
- **2026-09-24** · `petra` · **Sviluppo:** [research: resolve free-category and groupoid validation rows](https://github.com/gcomneno/petra/commit/d00ce816c4e697aff167d7248913981d22370c31)
- **2026-09-24** · `petra` · **Sviluppo:** [research: register free-path and trace-theory sources](https://github.com/gcomneno/petra/commit/a03bdcb4acf3b855330c1a5e2b00759ccc080d19)
- **2026-09-24** · `petra` · **Sviluppo:** [research: validate PETRA initial algebra and quotient semantics (#298)](https://github.com/gcomneno/petra/commit/982b49372180b2b74b65ed4b06f80503276202cb)
- **2026-09-24** · `petra` · **Sviluppo:** [research: remove resolved algebra item from open candidates](https://github.com/gcomneno/petra/commit/97dc8d8aca37513ed7c4addbe642ab6577b1e8b3)
- **2026-09-24** · `petra` · **Sviluppo:** [research: align superseded algebra validation note](https://github.com/gcomneno/petra/commit/68658af32c632e9e4e495c534829cb25b1346071)
- **2026-09-24** · `petra` · **Sviluppo:** [research: compare PETRA algebraic semantics with standard theory](https://github.com/gcomneno/petra/commit/a826b7eb3ca182adfe5d85a48d7132d38076b0ad)
- **2026-09-24** · `petra` · **Sviluppo:** [research: resolve algebraic semantics validation rows](https://github.com/gcomneno/petra/commit/6740ea92b9483909c1ed0570beec15bbc58b18f0)
- **2026-09-24** · `petra` · **Sviluppo:** [research: register bag-functor and universal-algebra sources](https://github.com/gcomneno/petra/commit/678f84d2f49f75d908d1f695cb9b2812c546decf)
- **2026-09-24** · `petra` · **Sviluppo:** [research: validate PETRA leaf-edit metric against 1-degree tree edit distance (#296)](https://github.com/gcomneno/petra/commit/05cd4e74e81f2cdc70e15e71ac19f0bea4f07df6)
- **2026-09-24** · `petra` · **Sviluppo:** [research: clarify unrestricted TED boundary](https://github.com/gcomneno/petra/commit/f51cfa512d9010c9bd4942bd572b8bb27dffb51e)
- **2026-09-24** · `petra` · **Sviluppo:** [research: distinguish PETRA leaf edits from unrestricted TED](https://github.com/gcomneno/petra/commit/27d79cc8911ac9a709c7834ea34f8a2b153c4fb6)
- **2026-09-24** · `petra` · **Sviluppo:** [research: compare PETRA metric with 1-degree tree edits](https://github.com/gcomneno/petra/commit/24734516d19a7c3d613c278ff15d3e0a7ea8c37e)
- **2026-09-24** · `petra` · **Sviluppo:** [research: refine leaf-edit validation status](https://github.com/gcomneno/petra/commit/65b6a4e2e825ec4a1b2e7653ba8bf70dc19e8022)
- **2026-09-24** · `petra` · **Sviluppo:** [research: register Selkow leaf-edit prior art](https://github.com/gcomneno/petra/commit/0c49d30883322a449e99cbca6cacd5b38920e948)
- **2026-09-24** · `petra` · **Sviluppo:** [research: begin Phase 6 external mathematical validation (#294)](https://github.com/gcomneno/petra/commit/5d678187cccd27eef4e732a06fd2de10a1398eb3)
- **2026-09-23** · `lele-manager` · **Funzionalità:** [add assistant-ready context export (#258)](https://github.com/gcomneno/lele-manager/commit/ee1a000c759f94d2dea1d84b52b5ee78703f8033)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [finalize Italian M0.7 verified maturity](https://github.com/gcomneno/cat-couch-guardian/commit/254cea53e0fbf32ac43fc81c13888fcdb308138e)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [finalize M0.7 verified maturity](https://github.com/gcomneno/cat-couch-guardian/commit/92cf575744338ad7dc1371b6dbabdaa56fc303b5)
- **2026-09-23** · `cat-couch-guardian` · **Documentazione:** [align Italian exercises with M0.7 contract](https://github.com/gcomneno/cat-couch-guardian/commit/ffcb37fcb62ef7a416bd8d47c03c6b72c659e210)
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

_Sono mostrati i 100 aggiornamenti significativi più recenti; 1832 aggiornamenti precedenti sono stati omessi._

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
