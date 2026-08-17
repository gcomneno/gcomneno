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

<p align="center">
  <img alt="Visitatori del profilo" src="https://komarev.com/ghpvc/?username=gcomneno&label=%F0%9F%91%80&nbsp;&color=0B1F3A&style=flat-square">
</p>

## <code>01 · PROGETTI SELEZIONATI</code>

Questi progetti rappresentano meglio il mio lavoro attuale tra progettazione backend, automazione affidabile, strumenti per sviluppatori e flussi software riproducibili.

| Progetto | Release ufficiale | Cosa fa | Cosa dimostra |
| --- | --- | --- | --- |
| [LeLe Manager](https://github.com/gcomneno/lele-manager) | [v1.11.1](https://github.com/gcomneno/lele-manager/releases/tag/v1.11.1) | Raccoglie, cerca e riutilizza lesson learned testuali tramite flussi Markdown, CLI, GUI e API | Dati local-first, persistenza JSONL, confini API, progettazione backend e distribuzione desktop pacchettizzata |
| [Smart File Organizer](https://github.com/gcomneno/smart-file-organizer) | [v0.5.0](https://github.com/gcomneno/smart-file-organizer/releases/tag/v0.5.0) | Analizza i file, mostra in anteprima un piano di organizzazione e li sposta solo su richiesta esplicita | Automazione deterministica dei file, dry-run espliciti, decisioni spiegabili e operazioni recuperabili |
| [GiadaWare Reference Engine](https://github.com/gcomneno/reference-engine) | — | Estrae, valida, traccia la provenienza e rende interrogabili informazioni da documenti personali di riferimento | Estrazione deterministica, validazione, provenienza, interrogazione e confini persistenti del repository |
| [GYTE](https://github.com/gcomneno/gyte) | [v1.3.1](https://github.com/gcomneno/gyte/releases/tag/v1.3.1) | Estrae da YouTube trascrizioni, audio e video e supporta reflow, traduzione e trascrizione locale dei contenuti | Progettazione CLI guidata da manifest, pipeline di estrazione multimediale e strumenti operativi riproducibili |
| [GiadaWare UI Components](https://github.com/gcomneno/giadaware-ui-components) | [v0.1.0](https://github.com/gcomneno/giadaware-ui-components/releases/tag/v0.1.0) | Fornisce primitive UI Svelte riutilizzabili per applicazioni GiadaWare tramite entry point base, visitor e studio isolati | Architettura di package Svelte, artefatti immutabili pacchettizzati, entry point isolati e contratti SSR/hydration e accessibilità |
| [Atelier-Kit](https://github.com/gcomneno/atelier-kit) | [v0.4.3](https://github.com/gcomneno/atelier-kit/releases/tag/v0.4.3) | Fornisce un kit vetrina configurabile con superfici di authoring Studio locali, desktop e hosted a perimetro esplicito, catalogo content-driven e strumenti di pubblicazione | Architettura di prodotto SvelteKit, confini di autorità espliciti tra local/hosted/demo, mutazioni repository atomiche, distribuzione desktop e adozione downstream di Giada UI |
| [Ubuntu System Tools](https://github.com/gcomneno/ubuntu-system-tools) | [v0.3.0](https://github.com/gcomneno/ubuntu-system-tools/releases/tag/v0.3.0) | Utilità Linux per diagnostica, manutenzione controllata, trascrizione offline e analisi degli avvisi kernel | Tooling di sistema safety-first, diagnostica read-only, flussi espliciti su opt-in e packaging Linux riproducibile |

<details>
<summary>Altri progetti operativi</summary>

| Progetto | Segnale tecnico |
| --- | --- |
| [LeLe Quizzer](https://github.com/gcomneno/lele-quizzer) | Generazione deterministica di quiz, UX da terminale e riuso della conoscenza |
| [GYTE Study Tools](https://github.com/gcomneno/gyte-study-tools) | Pipeline di contenuti riavviabili, validazione deterministica, confini privato/pubblico e handoff espliciti verso servizi esterni |
| [Semantic Mail Archivist](https://github.com/gcomneno/semantic-mail-archivist) | Audit Gmail privacy-first e repair dry-run, confini provider, confidence spiegabile e journal delle mutazioni crash-aware |

</details>

<details>
<summary>Esperienza e GiadaWare</summary>

**GiadaWare™** è il mio laboratorio personale per trasformare gli attriti ricorrenti in appunti, strumenti e progetti pubblici.

La mia esperienza professionale precedente include PHP e Laravel; il lavoro pubblico attuale è concentrato su Python, Linux, automazione e ingegneria open source. Disponibile per ruoli da remoto e opportunità professionali.

> Ogni problema risolto una volta merita di diventare conoscenza. Se quella conoscenza è riutilizzabile, merita di diventare uno strumento. Se lo strumento è utile anche ad altri, merita di diventare open source.

</details>

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

<details>
<summary>Pull request upstream selezionate e integrate</summary>

- [#545 — refactor: extract document lifecycle](https://github.com/yoctoproject/vscode-bitbake/pull/545)
- [#544 — refactor: extract Toaster lifecycle](https://github.com/yoctoproject/vscode-bitbake/pull/544)
- [#543 — Extract reusable cancellable file search utility](https://github.com/yoctoproject/vscode-bitbake/pull/543)
- [#541 — npm: minor version updates](https://github.com/yoctoproject/vscode-bitbake/pull/541)
- [#538 — Fix unbounded recipe-local file discovery](https://github.com/yoctoproject/vscode-bitbake/pull/538)
- [#535 — test: create integration workspace with bitbake-setup](https://github.com/yoctoproject/vscode-bitbake/pull/535)
- [#533 — refactor: simplify BitBake config picker flow](https://github.com/yoctoproject/vscode-bitbake/pull/533)
- [#532 — fix: update status bar after picking config by name](https://github.com/yoctoproject/vscode-bitbake/pull/532)
- [#527 — docs: fetch Yocto 6.0 documentation resources](https://github.com/yoctoproject/vscode-bitbake/pull/527)
- [#526 — fix: keep parse-on-save scans quiet on config errors](https://github.com/yoctoproject/vscode-bitbake/pull/526)
- [#524 — test: fetch split Yocto 6.0 repositories](https://github.com/yoctoproject/vscode-bitbake/pull/524)
- [#521 — fix(ui): hide toaster commands in eSDK mode](https://github.com/yoctoproject/vscode-bitbake/pull/521)

</details>

<details>
<summary>Contributi precedenti — ecosistema Canonical Craft</summary>

- [canonical/craft-application](https://github.com/canonical/craft-application) → [gcomneno/craft-application](https://github.com/gcomneno/craft-application)
- [canonical/craft-cli](https://github.com/canonical/craft-cli) → [gcomneno/craft-cli](https://github.com/gcomneno/craft-cli)
- [canonical/craft-parts](https://github.com/canonical/craft-parts) → [gcomneno/craft-parts](https://github.com/gcomneno/craft-parts)
- [canonical/craft-providers](https://github.com/canonical/craft-providers) → [gcomneno/craft-providers](https://github.com/gcomneno/craft-providers)
- [canonical/rockcraft](https://github.com/canonical/rockcraft) → [gcomneno/rockcraft](https://github.com/gcomneno/rockcraft)
- [canonical/snapcraft](https://github.com/canonical/snapcraft) → [gcomneno/snapcraft](https://github.com/gcomneno/snapcraft)

</details>

<details>
<summary>Altri fork upstream pubblici</summary>

- [canonical/testflinger](https://github.com/canonical/testflinger) → [gcomneno/testflinger](https://github.com/gcomneno/testflinger)

</details>

## <code>03 · RICERCA SELEZIONATA</code>

Questi repository usano esperimenti software riproducibili per studiare strutture di sequenze, comportamento statistico e calcolo deterministico.

| Area | Progetto | Focus tecnico |
| --- | --- | --- |
| Analisi di sequenze operative | [System Log Dynamics](https://github.com/gcomneno/system-log-dynamics) | Normalizzazione privacy-safe dei journal Linux, classificazione deterministica, manifest riproducibili e confronto temporale |
| Riconoscimento di sequenze | [OEIS Probe](https://github.com/gcomneno/oeis-probe) | Consultazione OEIS offline, ricerca normalizzata e cache SQLite |
| Analisi di sequenze | [Digit Probe](https://github.com/gcomneno/digit-probe) | Casualità, comprimibilità, autocorrelazione, n-grammi e pattern di tipo Schur |
| Modellazione stocastica a stati finiti | [Lotto Digit Coverage Dynamics](https://github.com/gcomneno/lotto-digit-coverage-dynamics) | Modelli di Markov assorbenti esatti, verifica esaustiva del kernel, analisi dei segnali storici, contratti applicativi versionati e GUI di ricerca locale riproducibile |

<details>
<summary>Altri progetti di ricerca e sperimentali</summary>

| Area | Progetto | Focus tecnico |
| --- | --- | --- |
| Partizionamento deterministico | [Turbo-Bucketizer](https://github.com/gcomneno/turbo-bucketizer) | Partizionamento IPv4 ad alta entropia e allocazione deterministica |
| Analisi modulare | [Midas](https://github.com/gcomneno/midas) | Impronte modulari deterministiche e confronto strutturale |
| Ricerca strutturale | [Integer Structural Search](https://github.com/gcomneno/integer-structural-search) | Ricerca limitata su rappresentazioni intere e vincoli |
| Compressione linguistica | [Huffman Compressor](https://github.com/gcomneno/huffman-compressor) | Pre-elaborazione del testo italiano e codifica Huffman a strati |
| Firme modulari | [Prime Tower Clocks](https://github.com/gcomneno/prime-tower-clocks) | Orologi primi, teorema cinese del resto e firme modulari |
| Compressione di serie temporali | [Lasagna v2](https://github.com/gcomneno/lasagna-v2) | Compressione lossless sperimentale per serie temporali univariate |
| Codec sperimentale | [Crystal Codec GCC v1](https://github.com/gcomneno/crystal-codec-gcc-v1) | Prototipo di codec p-adico basato su cristalli e prismi |

</details>

## <code>04 · IMPARARE IN PUBBLICO</code>

Trasformo lo studio attivo in percorsi documentati e riproducibili, senza presentare i repository didattici come esperienza di produzione.

| Area | Repository | Focus attuale |
| --- | --- | --- |
| Linux embedded | [Mini laboratorio Yocto/QEMU](https://github.com/gcomneno/yocto-qemu-mini-lab) | Build riproducibili di immagini, layer e recipe personalizzati, flussi BitBake e validazione del boot con QEMU |
| Sviluppo software | [Corso Kleis di sviluppo software](https://github.com/gcomneno/kleis-corso-sviluppo-software) | Esercizi progressivi in C#/.NET, HTML e SQL, con PHP previsto dal corso |
| Sistemi distribuiti | [Studio dei sistemi distribuiti](https://github.com/gcomneno/distributed-systems-study) | Algoritmi, modelli di guasto, coordinamento ed esercizi orientati ai colloqui |
| System design | [Studio del system design](https://github.com/gcomneno/system-design-study) | Appunti di architettura, quiz e lezioni orientate ai colloqui |
| Fisica | [Studio della fisica](https://github.com/gcomneno/physics-study) | Lezioni originali e fact-checkate; prima lezione: [Does Light ACTUALLY Move?](https://github.com/gcomneno/physics-study/blob/main/lessons/does-light-actually-move/lesson-learned.md), dalle eclissi di Io alle prove della velocità finita della luce |

<details>
<summary>Laboratori precedenti o di supporto</summary>

- [Laboratorio OOP in C](https://github.com/gcomneno/oop-in-c-lab) — layout degli oggetti, dispatch virtuale manuale, identità di tipo a runtime e downcast controllato
- [Laboratorio JavaScript](https://github.com/gcomneno/js-lab-didattico) — pipeline middleware e pattern riutilizzabili in JavaScript e TypeScript, con test eseguibili
- [BoardLab](https://github.com/gcomneno/boardlab) — architettura generica per motori di gioco ed esperimenti riproducibili di ricerca e IA, ancora in incubazione iniziale
- [Laboratorio Laravel storico](https://github.com/gcomneno/web) — studio precedente del backend web e relativa documentazione

</details>

## <code>05 · ULTIMI AGGIORNAMENTI</code>
<!-- updates:start -->

- **2026-08-15** · `atelier-kit` · **Correzione:** [propagate sharp dependency (#298)](https://github.com/gcomneno/atelier-kit/commit/c8599a4c016d376e7d21de921bfe6a7081964ee2)
- **2026-08-15** · `lele-manager` · **Funzionalità:** [add per-LeLe revision history and rollback (#237)](https://github.com/gcomneno/lele-manager/commit/b23eaa9266c18b50a6f1a40ea53872e5abb68a07)
- **2026-08-15** · `atelier-kit` · **Funzionalità:** [add optional Vercel Web Analytics (#296)](https://github.com/gcomneno/atelier-kit/commit/0ca74a873e1609f98a995b2c2ce9474fc50d46e6)
- **2026-08-15** · `lele-manager` · **Funzionalità:** [brand LeLe Manager as Your Managed Second Brain (#236)](https://github.com/gcomneno/lele-manager/commit/4272371360043e8176bb8d08331420a6865de67c)

<details>
<summary>Altri aggiornamenti recenti e significativi</summary>

- **2026-08-15** · `lele-manager` · **Correzione:** [refine original monkey cameo timing (#235)](https://github.com/gcomneno/lele-manager/commit/f9cb3a7238440d227316ab079d43674850fa5f20)
- **2026-08-15** · `atelier-kit` · **Funzionalità:** [migrate Hero image authoring to controlled boundary (#295)](https://github.com/gcomneno/atelier-kit/commit/abcbf1b4af2c155c3544d1b18dbf3d91ff77a54f)
- **2026-08-15** · `atelier-kit` · **Sviluppo:** [noop](https://github.com/gcomneno/atelier-kit/commit/8a661cd14da1ad4451bdf8ae7edb9bfc9a34416f)
- **2026-08-15** · `atelier-kit` · **Funzionalità:** [add controlled image-upload authoring boundary (#293)](https://github.com/gcomneno/atelier-kit/commit/b43a09b4ba418b8eeb59c2a9451b4fdc2bf3cac5)
- **2026-08-15** · `lele-manager` · **Funzionalità:** [add explicit lesson lifecycle and supersession semantics (#234)](https://github.com/gcomneno/lele-manager/commit/b54229be80a2e9677feecad46119445cb2312545)
- **2026-08-15** · `giadaware-ui-components` · **Release:** [Giada UI 0.1.0](https://github.com/gcomneno/giadaware-ui-components/releases/tag/v0.1.0)
- **2026-08-15** · `giadaware-ui-components` · **Documentazione:** [define release and versioning policy (#65)](https://github.com/gcomneno/giadaware-ui-components/commit/3d8d3bbf995bda6c4b6a4aa38d9ffc681cefa50a)
- **2026-08-15** · `giadaware-ui-components` · **Documentazione:** [establish bilingual public documentation contract (#63)](https://github.com/gcomneno/giadaware-ui-components/commit/2ef23bb65466032502a71b275cdad49e0933c491)
- **2026-08-15** · `lele-manager` · **Correzione:** [serialize Danger Zone destructive commits against Vault activation (#233)](https://github.com/gcomneno/lele-manager/commit/f24c25a1b35d76802781bfefa0fb3b575e913f31)
- **2026-08-15** · `giadaware-ui-components` · **Funzionalità:** [add editable list drag handles (#61)](https://github.com/gcomneno/giadaware-ui-components/commit/ce00ea338fd70091dfe2719e5fd6d5fa1e3f5abe)
- **2026-08-15** · `giadaware-ui-components` · **Funzionalità:** [add async operation progress (#60)](https://github.com/gcomneno/giadaware-ui-components/commit/43e58d50928ed040c52184beb1e61efc55a0a4c7)
- **2026-08-15** · `giadaware-ui-components` · **Funzionalità:** [add reorder position context (#59)](https://github.com/gcomneno/giadaware-ui-components/commit/f14422a0216aec6d32c139b29bd2c3961e07e4eb)
- **2026-08-15** · `giadaware-ui-components` · **Funzionalità:** [announce reorder outcomes accessibly (#58)](https://github.com/gcomneno/giadaware-ui-components/commit/08cd9e0734f95d27aa995d9c7647b2a0724ef188)
- **2026-08-15** · `giadaware-ui-components` · **Funzionalità:** [add composable StatusNotice (#57)](https://github.com/gcomneno/giadaware-ui-components/commit/1578655b453a9dc66f9e2123f2991b1254a35c10)
- **2026-08-15** · `giadaware-ui-components` · **Funzionalità:** [add field description and error primitives (#56)](https://github.com/gcomneno/giadaware-ui-components/commit/762d6677a3ce98aeb893b0e06e57108359a9e907)
- **2026-08-14** · `concorso-inps-assistente-informatico` · **Novità:** [prepare INPS study repository readiness](https://github.com/gcomneno/concorso-inps-assistente-informatico/commit/074e8ed1245d9158e531d1ad847f726e03219b01)
- **2026-08-14** · `atelier-kit` · **Documentazione:** [correct current release](https://github.com/gcomneno/atelier-kit/commit/75dad938c936ed662323e13a723e721a4ca5a218)
- **2026-08-14** · `boardlab` · **Funzionalità:** [prepare canonical Session 01 learning path](https://github.com/gcomneno/boardlab/commit/12e853899590e5ba07e1f5cb333bc4b3fc20ae05)
- **2026-08-14** · `lele-manager` · **Funzionalità:** [add per-vault destructive danger zone workflows (#231)](https://github.com/gcomneno/lele-manager/commit/b685ce1af507a430721348587a812a6c95be7c86)
- **2026-08-14** · `lele-manager` · **Funzionalità:** [add safe vault merge and transfer workflows (#230)](https://github.com/gcomneno/lele-manager/commit/4587399180a4ce6af42630500d580463420667e7)
- **2026-08-14** · `giadaware-ui-components` · **Funzionalità:** [add accessible SocialLink (#55)](https://github.com/gcomneno/giadaware-ui-components/commit/80aa64e91c5241d96bcd6936715c78903b89e21c)
- **2026-08-14** · `semantic-mail-archivist` · **Funzionalità:** [add crash-aware mutation journal (#40)](https://github.com/gcomneno/semantic-mail-archivist/commit/edf2dade4a548c8819265ef4f8fca810740263e2)
- **2026-08-14** · `giadaware-ui-components` · **Funzionalità:** [add accessible IconButton (#54)](https://github.com/gcomneno/giadaware-ui-components/commit/e8cb149c30f63fa81a8cccb5b9b6bb7d87e5dd8d)
- **2026-08-14** · `ubuntu-system-tools` · **Funzionalità:** [add safety-first ClamAV weekly health tools (#46)](https://github.com/gcomneno/ubuntu-system-tools/commit/0858174c85a867adafc8525f21786a2ce38ca7fd)
- **2026-08-14** · `giadaware-ui-components` · **Funzionalità:** [add Button content regions (#53)](https://github.com/gcomneno/giadaware-ui-components/commit/427bf4c20df7836d90d75510a03e9585d39e5392)
- **2026-08-14** · `lotto-digit-coverage-dynamics` · **Correzione:** [compact wheel digit chips (#50)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/7fb7066615579a3e6d890f59a13a6913a3bb16c6)
- **2026-08-14** · `lotto-digit-coverage-dynamics` · **Correzione:** [give consensus full-width layout (#49)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/09e91f4252fb50d969c116a1d60536bfe73af7cf)
- **2026-08-14** · `lotto-digit-coverage-dynamics` · **Correzione:** [align consensus semantics with CLI (#46)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/558072b21314daff1cf3e38e0a4e4f41e96d512b)
- **2026-08-14** · `lotto-digit-coverage-dynamics` · **Funzionalità:** [add global limit and aggregate totals (#42)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/16383cf58f36f50c71b47bcf192a62dca72c35d3)
- **2026-08-14** · `lotto-digit-coverage-dynamics` · **Correzione:** [exclude reference draw from grouped counts (#41)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/11e90b0daf8b3d4e036254a0fbdd1b4db10b93e7)
- **2026-08-14** · `lotto-digit-coverage-dynamics` · **Refactoring:** [centralize consensus rendering (#40)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/a6a230b1c7f35d0915900c7990aec117acf40ead)
- **2026-08-14** · `lotto-digit-coverage-dynamics` · **Refactoring:** [clarify consensus labels (#39)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/298b4faa48733857f7dca5110ab03a3570bdb6cf)
- **2026-08-13** · `giadaware-ui-components` · **Funzionalità:** [add optional Panel footer (#52)](https://github.com/gcomneno/giadaware-ui-components/commit/520463e48095f9e17941b974d855a2e56086ec43)
- **2026-08-13** · `semantic-mail-archivist` · **Funzionalità:** [connect Gmail repair dry-run (#39)](https://github.com/gcomneno/semantic-mail-archivist/commit/6f6a23c6fd7513f1c2b02d7aff0d978d0836c91b)
- **2026-08-13** · `giadaware-ui-components` · **Funzionalità:** [add consumer-owned actions to ImageLightbox (#51)](https://github.com/gcomneno/giadaware-ui-components/commit/d50150a1f568d321a44d143f3052034c56188fd1)
- **2026-08-13** · `semantic-mail-archivist` · **Funzionalità:** [wire Gmail read-only mailbox audit (#38)](https://github.com/gcomneno/semantic-mail-archivist/commit/af41909b40be2aecd78f1415a2864eff89c5ad64)
- **2026-08-13** · `semantic-mail-archivist` · **Funzionalità:** [add local CLI application shell (#37)](https://github.com/gcomneno/semantic-mail-archivist/commit/63d97e7244b7855d39801f34d6e3bb122260c384)
- **2026-08-13** · `giadaware-ui-components` · **Funzionalità:** [add progressive dropzone interaction to ImageAttachmentControl (#50)](https://github.com/gcomneno/giadaware-ui-components/commit/69cb67a533de90205cdf58894ddb92c09dafc2a7)
- **2026-08-13** · `atelier-kit` · **Funzionalità:** [support atomic multi-file repository mutations (#291)](https://github.com/gcomneno/atelier-kit/commit/8edf3155ed98795cd97f16c6ed71fe1a1e498ed4)
- **2026-08-13** · `semantic-mail-archivist` · **Funzionalità:** [add Gmail read-only mailbox ingestion (#36)](https://github.com/gcomneno/semantic-mail-archivist/commit/1981639457617fe2293253c2a8ec9857863983c6)
- **2026-08-13** · `semantic-mail-archivist` · **Funzionalità:** [add local Gmail authentication (#35)](https://github.com/gcomneno/semantic-mail-archivist/commit/3be0d27f83fb8067186e0f54c864e617da6d3ce2)
- **2026-08-13** · `semantic-mail-archivist` · **Funzionalità:** [define provider adapter contract (#34)](https://github.com/gcomneno/semantic-mail-archivist/commit/a9f2a0c36983fee8c865f1a262c6adc246d31a38)
- **2026-08-12** · `atelier-kit` · **Refactoring:** [consume GIADA semantic palette contract](https://github.com/gcomneno/atelier-kit/commit/0bd9e1b088f227521cdf831d548dde72364ceec6)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [consume canonical GIADA theme tokens](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/0fe92fd60aa6f23fc67989a9f6afe0e54ec90db4)
- **2026-08-12** · `giadaware-ui-components` · **Funzionalità:** [add shared semantic palette tokens](https://github.com/gcomneno/giadaware-ui-components/commit/224c449f62c01cb063b45a66dcc1cabc46acb296)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [add auditable mailbox change log (#22)](https://github.com/gcomneno/semantic-mail-archivist/commit/d17f6a8b5c638fe0b2203fa8fe501635adfa17d5)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [keep missing digits on two rows (#37)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/6679a1ff1acf19675d1b0aa68d2b54f5eaa19dfb)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [improve digit-set readability and contrast (#36)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/fac81bbeebac554acf3489f34d8cc9124cf864bc)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Sviluppo:** [demo: reset social links](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/80afac2112e81e040783f4144ad4bcde4b40fbe0)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Sviluppo:** [demo: update social links](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/a485a554558834ba6fb9d7da835bcf4b88053360)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [wait for complete pywebview API readiness (#35)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/86b1bc75558fff2c4581c83c9f1482aa4460b27c)
- **2026-08-12** · `distributed-systems-study` · **Documentazione:** [prepare distributed systems foundations study path (#4)](https://github.com/gcomneno/distributed-systems-study/commit/f1107c2ba599d139fec0879b9a59e57d6d15e814)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [align native controls with application theme (#34)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/cb53452fe24f9e8c0c8f3619dcfdda300dc9ddb4)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [add complete mailbox audit report (#21)](https://github.com/gcomneno/semantic-mail-archivist/commit/e4e1018708ef03f73b57673483ef845eecd2dfcf)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [harden first desktop road-test experience](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/a954d3340edf4f0dad1cd9d2efa6ab8d483e5a28)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [preserve default database through pywebview serialization](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/af9c57c9b37d3e7b6ab55f16004311e2f1104c94)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Sviluppo:** [probe](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/0e1986ffdfdce5229b9d9f17bcc76ab0479d9686)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Sviluppo:** [tmp](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/e207b114c5a89f4ce94901da43a38dae041c2697)
- **2026-08-12** · `semantic-mail-archivist` · **Correzione:** [tighten generic notification obsolescence cue](https://github.com/gcomneno/semantic-mail-archivist/commit/119d5adb9f2977f68b83309b3674b783316113d5)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [handshake pywebview bridge before loading reports](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/e45535d5941908e0e54a20097f3e07c808c625f2)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [add optional operational state layer (#19)](https://github.com/gcomneno/semantic-mail-archivist/commit/f8746d2ca6f69169f801b732048d7e5eaf9cdc25)
- **2026-08-12** · `atelier-kit` · **Funzionalità:** [wire bounded public social experience (#288)](https://github.com/gcomneno/atelier-kit/commit/18b9bd65e80c7aecf33aef8ce3930f803eb10db1)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Funzionalità:** [wire bounded public social experience (#288)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/18b9bd65e80c7aecf33aef8ce3930f803eb10db1)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [repair road-test reactivity and research navigation (#30)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/a50e98ec019384362d3a1df1c29e01cc44193e18)
- **2026-08-12** · `software-architecture-study` · **Documentazione:** [prepare software architecture foundations study path](https://github.com/gcomneno/software-architecture-study/commit/750e815782a4932fa7100d6af7e533b9ee09cb52)
- **2026-08-12** · `semantic-mail-archivist` · **Correzione:** [validate protected document ownership](https://github.com/gcomneno/semantic-mail-archivist/commit/a6db5b48ad5bfada26f7843e2c52ef3dbb5e48fb)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [detect obsolete low-value messages safely (#17)](https://github.com/gcomneno/semantic-mail-archivist/commit/94602084453cf3d4832f8d99dcb7322cb4c21f0c)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Funzionalità:** [complete local research interface (#29)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/c20d266f43928efe132b3b58c4000aa609cc1cc7)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Funzionalità:** [add same-wheel occurrence explorer (#28)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/d6f62ea24e8ecebbb28980f6efa3259495d3e997)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Funzionalità:** [establish GIADA UI desktop foundation (#27)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/9d401669a06ccbc8b447d70e3fc6cd05b4618829)
- **2026-08-12** · `system-design-study` · **Documentazione:** [complete API design study session](https://github.com/gcomneno/system-design-study/commit/db2694f37d845d547be3e364c2ebca89095ebeaf)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [complete historical research migration (#26)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/dc0b5a19fe4aeb801bc0c03ac376ee4dc5aaa690)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [migrate historical signal reports (#25)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/c44daca80c7622d95ff4c8c7dcb87ce4879d3176)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [migrate historical Markov reports (#24)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/0e4521286b00feb647e120e05acad81421488d79)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [dispatch migrated application commands directly (#23)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/c270307388c0c78f830647b4bbe14c4d0d6270f1)
- **2026-08-12** · `atelier-kit` · **Funzionalità:** [isolate sandbox social authoring (#287)](https://github.com/gcomneno/atelier-kit/commit/d46155274278eeaf443d6fd6eb4c3bd7d6e50657)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Funzionalità:** [isolate sandbox social authoring (#287)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/d46155274278eeaf443d6fd6eb4c3bd7d6e50657)
- **2026-08-12** · `system-design-study` · **Documentazione:** [integrate private study SOT workflow](https://github.com/gcomneno/system-design-study/commit/16a412710fb82e3821b59520f67403bfa1a2031f)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [add stable versioned application contracts (#22)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/3915fc42c9c00006b3870006e6501ac04df96d14)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [separate occurrence groups from terminal rendering (#21)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/bb42fb578d316f326392798ba7103fd7151b5137)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [expose structured current application report (#20)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/c0a0247372a0a64dc88bb6cbd29e1e70bc2c648c)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [isolate draw repository contract from SQLite (#19)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/a7998c541ad333e63954818ad4d805ab8ef7c4f9)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [introduce protected semantic categories (#16)](https://github.com/gcomneno/semantic-mail-archivist/commit/e4e6b2d6cae2b431efe9a7f4f6237ded993d5a2f)
- **2026-08-12** · `atelier-kit` · **Funzionalità:** [enforce bounded mutation integrity (#286)](https://github.com/gcomneno/atelier-kit/commit/d793bbc9fd11f31c50d74dbe38741afe5e4331b3)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Funzionalità:** [enforce bounded mutation integrity (#286)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/d793bbc9fd11f31c50d74dbe38741afe5e4331b3)
- **2026-08-12** · `atelier-kit` · **Funzionalità:** [add isolated guest session authority (#285)](https://github.com/gcomneno/atelier-kit/commit/1c434e533c9bb63a9a9a503cb517302f5cab3bf4)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Funzionalità:** [add isolated guest session authority (#285)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/1c434e533c9bb63a9a9a503cb517302f5cab3bf4)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Sviluppo:** [Introduce explicit architecture package boundaries (#18)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/ef329e7f73de3211afdbf3e5f54e91d3d20d280d)
- **2026-08-12** · `giadaware-ui-components` · **Funzionalità:** [add accessible ImageLightbox (#46)](https://github.com/gcomneno/giadaware-ui-components/commit/998e358c3562e32a039bbd8770909dc47f82ef04)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [detect significant documents (#15)](https://github.com/gcomneno/semantic-mail-archivist/commit/093f839f3b50f200754484914b099167d35bd6a3)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Sviluppo:** [Add grouped occurrence totals to the Lotto viewer (#8)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/20fd321a8748fa007430196a4104b01c297db196)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Sviluppo:** [Replace TUTTE with consensus and add twin-number analysis (#7)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/d5d4360c3a773ca67a00fb56790d1b5875a14a36)
- **2026-08-12** · `atelier-kit` · **Funzionalità:** [establish isolated public demo runtime (#284)](https://github.com/gcomneno/atelier-kit/commit/ffc798e238d30af5e7ac1beca788ddeac7a23bd3)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Funzionalità:** [establish isolated public demo runtime (#284)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/ffc798e238d30af5e7ac1beca788ddeac7a23bd3)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [add dry-run repair reports](https://github.com/gcomneno/semantic-mail-archivist/commit/c57d069374cc99418ff878d55af0e4785313a98d)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [infer labels with explainable confidence](https://github.com/gcomneno/semantic-mail-archivist/commit/bd15fc64b9ced4fd479b9cf68fb425b4f0a27125)

_Sono mostrati i 100 aggiornamenti significativi più recenti; 999 aggiornamenti precedenti sono stati omessi._

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
