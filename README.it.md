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

- **2026-09-19** · `lotto-digit-coverage-dynamics` · **Documentazione:** [add Zenodo DOI metadata](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/7c2eded9d271484ad3a50afd8d27b43e7dc4bd0e)
- **2026-09-19** · `cat-couch-guardian` · **Documentazione:** [update M0.6 packaging and provenance](https://github.com/gcomneno/cat-couch-guardian/commit/d9ffbe1a818a80633aad78a8b50ceb45547c1880)
- **2026-09-19** · `lotto-digit-coverage-dynamics` · **Release:** [v1.2.0 — Reproducible archive tooling and semantic read queries](https://github.com/gcomneno/lotto-digit-coverage-dynamics/releases/tag/v1.2.0)
- **2026-09-19** · `cat-couch-guardian` · **Funzionalità:** [add simulated deterrent request boundary](https://github.com/gcomneno/cat-couch-guardian/commit/2050fea045b3a0e390ee7111c401781f16889035)

<details>
<summary>Altri aggiornamenti recenti e significativi</summary>

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
- **2026-09-17** · `petra` · **Sviluppo:** [research: add bounded PETRA automorphism probe](https://github.com/gcomneno/petra/commit/de22d6f6abfa38c63e3009135cbb5632c46788e9)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA automorphisms and symmetry](https://github.com/gcomneno/petra/commit/222a1b08e6404904abb7dd2a4f10a1bbcf10c8b3)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA rewrite presentations (#288)](https://github.com/gcomneno/petra/commit/b31d344c2f66386ff4f70ce540da7bfc24897789)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA rewrite presentations](https://github.com/gcomneno/petra/commit/97b0e1193d5218efbe79b9097df2a12a1e053624)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA congruences and quotients (#286)](https://github.com/gcomneno/petra/commit/027544713c44a2822acb8cfdecc090e73c47c565)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA congruences and quotients](https://github.com/gcomneno/petra/commit/b47ba15ff0ce794fc2b9ea2ef8181bfa183af8fc)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA grading and edit-graph geometry (#284)](https://github.com/gcomneno/petra/commit/18f74077cfd2ec2ee36198287904ee315e25693e)
- **2026-09-17** · `petra` · **Sviluppo:** [research: expose non-unique common-reduct witness](https://github.com/gcomneno/petra/commit/8b29fa55fef48310f40e6025fc255c0ca710d677)
- **2026-09-17** · `petra` · **Sviluppo:** [research: prove non-unique maximum common reducts](https://github.com/gcomneno/petra/commit/450b5a6cbf4981e1d5b44ac3eeaaef0fa0d78fad)
- **2026-09-17** · `petra` · **Sviluppo:** [research: add bounded PETRA edit-geometry probe](https://github.com/gcomneno/petra/commit/9bac0ea232fed01848701cfbd6315fff1f2467c2)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize PETRA grading and edit geometry](https://github.com/gcomneno/petra/commit/87183c7458d540c67b6e6499fd26a32c651cf502)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize AIP-5 interpretation theory (#282)](https://github.com/gcomneno/petra/commit/fccc9116bb98814c1597afb11e9cf48ef67a179c)
- **2026-09-17** · `petra` · **Sviluppo:** [research: tighten AIP-5 interpretation foundations](https://github.com/gcomneno/petra/commit/df3103a91954ad2e324d47d562f471b4e4489248)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize AIP-5 interpretation theory](https://github.com/gcomneno/petra/commit/3572f761b570e0788800a7fd946c45a945b88842)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize and probe AIP-4 minimal algebra (#280)](https://github.com/gcomneno/petra/commit/00d266bbc24d92276fa9ae85341e534dcbb5f357)
- **2026-09-17** · `petra` · **Sviluppo:** [research: align AIP-4 with explicit root axiom](https://github.com/gcomneno/petra/commit/6ee8b0f3c652d7841ed7f8cb4f34bebd2895812a)
- **2026-09-17** · `petra` · **Sviluppo:** [research: make root-parent axiom explicit](https://github.com/gcomneno/petra/commit/2239539ee5949699607afbed3e1ba424ed66da33)
- **2026-09-17** · `petra` · **Sviluppo:** [research: add AIP-4 minimal algebra probe](https://github.com/gcomneno/petra/commit/ad1c6eaaa891a759163454c9c654677cdd713e6f)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize AIP-4 minimal algebra](https://github.com/gcomneno/petra/commit/d4dadcf25c9613a4c265151b60dbf801910a8ae0)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize canonical PETRA carrier theory (#278)](https://github.com/gcomneno/petra/commit/74c397388cd5c30b05509c821b93c7040c160c63)
- **2026-09-17** · `petra` · **Sviluppo:** [research: tighten canonical carrier foundations](https://github.com/gcomneno/petra/commit/d72730096903332dd093901caa9411566c693682)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize canonical PETRA carrier](https://github.com/gcomneno/petra/commit/8220da283ab53420262e073ebb83f3eb7df1e0db)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize abstract carrier foundational answers (#275)](https://github.com/gcomneno/petra/commit/ac2c4187e8d280878711d8fec2a7a3c23a1ef007)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize abstract carrier foundational answers](https://github.com/gcomneno/petra/commit/668bea1bbf172bcbc21655953b23257fcb1ad211)
- **2026-09-17** · `petra` · **Sviluppo:** [research: analyze Terminal as empty composition (#273)](https://github.com/gcomneno/petra/commit/efa883dfec07ad5e1fe748426b61a190b433a5fc)
- **2026-09-17** · `petra` · **Sviluppo:** [research: probe Terminal as empty composition](https://github.com/gcomneno/petra/commit/4969fb7a25fa7c44b001415bb32bf98f59bb8484)
- **2026-09-17** · `petra` · **Sviluppo:** [research: analyze Terminal versus empty composition](https://github.com/gcomneno/petra/commit/07eaccec469ff4f566daee03f947bf3218b733c3)
- **2026-09-17** · `petra` · **Sviluppo:** [research: reassess AIP-2 primitive relation ontology (#269)](https://github.com/gcomneno/petra/commit/4c174646ed7afc2e81f8aff36cee8e5d88277ab1)
- **2026-09-17** · `petra` · **Sviluppo:** [research: reassess AIP-2 primitive relation ontology](https://github.com/gcomneno/petra/commit/6040b5179be66bf4a3e521e7d0b07fc26235458d)
- **2026-09-17** · `petra` · **Sviluppo:** [research: probe AIP-1 Set vs Multiset composition (#267)](https://github.com/gcomneno/petra/commit/ca5322a056946a84fb387dfa73e26f7149b9e34b)
- **2026-09-17** · `petra` · **Documentazione:** [record AIP-1 set vs multiset prototype](https://github.com/gcomneno/petra/commit/f736a6a7995e23aea1be43d4e93d2cf538e65ccd)
- **2026-09-17** · `petra` · **Sviluppo:** [research: add AIP-1 set vs multiset probe](https://github.com/gcomneno/petra/commit/2c0fe22271f07fffcad1daac701bf67856585c04)
- **2026-09-17** · `petra` · **Sviluppo:** [research: analyze AIP-1 multiplicity ontology (#265)](https://github.com/gcomneno/petra/commit/caca013c8b85345e639bf11cdabf1808e20df6ad)
- **2026-09-17** · `petra` · **Sviluppo:** [research: analyze AIP-1 multiplicity ontology](https://github.com/gcomneno/petra/commit/4718cd85ccc9666fc787c6e6f5625a9a7576053f)
- **2026-09-17** · `petra` · **Sviluppo:** [research: validate AIP-2 recursive containment (#262)](https://github.com/gcomneno/petra/commit/3544a4e849d45a843865468b32f948b3832d5843)
- **2026-09-17** · `petra` · **Documentazione:** [describe AIP-2 recursive containment prototype](https://github.com/gcomneno/petra/commit/4e0c122660ddfec39be4a9da753fafe7398fbc42)
- **2026-09-17** · `petra` · **Sviluppo:** [research: add AIP-2 recursive containment probe](https://github.com/gcomneno/petra/commit/9fac017bd85bb992024f02f1f5f9020f572c67ef)
- **2026-09-17** · `petra` · **Sviluppo:** [research: add AIP-2 wrapper-erasure probe](https://github.com/gcomneno/petra/commit/1d0beebe5eae9e59edb042165ef7ddcfee70cab6)
- **2026-09-17** · `petra` · **Sviluppo:** [research: audit AIP-2 level derivability (#258)](https://github.com/gcomneno/petra/commit/999fe865cf81703b40e77fa8cb300a2b1d6cd1ec)
- **2026-09-17** · `petra` · **Sviluppo:** [research: prototype AIP-3 order-independent quotient (#255)](https://github.com/gcomneno/petra/commit/58e177a9e110e78336f001ee33b7d985744a1801)
- **2026-09-17** · `petra` · **Sviluppo:** [research: formalize AIP-3 quotient invariance](https://github.com/gcomneno/petra/commit/24abb5a56d3ab361e86164075feeb5cc9711f997)
- **2026-09-17** · `petra` · **Sviluppo:** [research: add AIP-3 order-independent quotient probe](https://github.com/gcomneno/petra/commit/b17c24c5218b817edbc0d99b61ad416d383e7846)
- **2026-09-17** · `petra` · **Sviluppo:** [research: analyze AIP-3 order semantics (#253)](https://github.com/gcomneno/petra/commit/04bd54fde7bc64547871c5025688a3f6a48dc669)
- **2026-09-17** · `petra` · **Sviluppo:** [research: define PETRA abstract paradigm (#245)](https://github.com/gcomneno/petra/commit/7c3304a77d34e1630315ad0405c577f67a2e562b)
- **2026-09-17** · `petra` · **Documentazione:** [add PETRA research source register](https://github.com/gcomneno/petra/commit/91bbf2fd81160bd63448d766a75eca2ff0c8d76c)
- **2026-09-17** · `petra` · **Documentazione:** [establish PETRA related-work survey (#241)](https://github.com/gcomneno/petra/commit/a60f3dd7a4bfc9f7f6acb325d3fbc2c6730c04cc)
- **2026-09-17** · `petra` · **Documentazione:** [align release metadata with PETRA v2.0.0 (#239)](https://github.com/gcomneno/petra/commit/69e20b78ab7779f8bb8ec444de84ea7722771ba9)
- **2026-09-17** · `petra` · **Sviluppo:** [STATUS: Phase 10 complete, v2.0.0 shipped, research front updated](https://github.com/gcomneno/petra/commit/595fb2d293bc97a918587705fa4cacdc9f556b60)
- **2026-09-17** · `petra` · **Sviluppo:** [docs/research: update README with open-problems and new notes](https://github.com/gcomneno/petra/commit/140dcafb99735d27f148732d5d78b9b275098942)
- **2026-09-17** · `petra` · **Correzione:** [use $'...' so colors render inside heredoc](https://github.com/gcomneno/petra/commit/c88e1faf01242a3acffa825fb6c5573e4381ebc3)
- **2026-09-17** · `petra` · **Release:** [PETRA v2.0.0 — Prime Exponent Tower Recursive Algebra](https://github.com/gcomneno/petra/releases/tag/v2.0.0)
- **2026-09-17** · `petra` · **Documentazione:** [annotate Zenodo version DOI for v2.0.0](https://github.com/gcomneno/petra/commit/3fda09188dd5c4e7b7ab456fdc713963c00bc6c8)
- **2026-09-16** · `petra` · **Sviluppo:** [T18/P21 closed: ruff and mypy clean on resolver](https://github.com/gcomneno/petra/commit/c36d49791621c3b7236082f8e8f59f98eba8cd55)
- **2026-09-16** · `petra` · **Sviluppo:** [revert: remove RUF001/RUF002 from root config (belongs to resolver)](https://github.com/gcomneno/petra/commit/7bfb94e00e847ac89f0fa0d914012db0653572ee)
- **2026-09-16** · `petra` · **Sviluppo:** [T18: py.typed for petra, mypy fixes; T17 statement correction](https://github.com/gcomneno/petra/commit/42fa7e2154e17cab6e789aacca406639daffbf80)

_Sono mostrati i 100 aggiornamenti significativi più recenti; 1809 aggiornamenti precedenti sono stati omessi._

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
