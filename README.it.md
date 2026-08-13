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
| [LeLe Manager](https://github.com/gcomneno/lele-manager) | [v1.11.0](https://github.com/gcomneno/lele-manager/releases/tag/v1.11.0) | Raccoglie, cerca e riutilizza lesson learned testuali tramite flussi Markdown, CLI, GUI e API | Dati local-first, persistenza JSONL, confini API, progettazione backend e distribuzione desktop pacchettizzata |
| [Smart File Organizer](https://github.com/gcomneno/smart-file-organizer) | [v0.5.0](https://github.com/gcomneno/smart-file-organizer/releases/tag/v0.5.0) | Analizza i file, mostra in anteprima un piano di organizzazione e li sposta solo su richiesta esplicita | Automazione deterministica dei file, dry-run espliciti, decisioni spiegabili e operazioni recuperabili |
| [GiadaWare Reference Engine](https://github.com/gcomneno/reference-engine) | — | Estrae, valida, traccia la provenienza e rende interrogabili informazioni da documenti personali di riferimento | Estrazione deterministica, validazione, provenienza, interrogazione e confini persistenti del repository |
| [GYTE](https://github.com/gcomneno/gyte) | [v1.3.1](https://github.com/gcomneno/gyte/releases/tag/v1.3.1) | Estrae da YouTube trascrizioni, audio e video e supporta reflow, traduzione e trascrizione locale dei contenuti | Progettazione CLI guidata da manifest, pipeline di estrazione multimediale e strumenti operativi riproducibili |
| [GiadaWare UI Components](https://github.com/gcomneno/giadaware-ui-components) | — | Fornisce primitive UI Svelte riutilizzabili per applicazioni GiadaWare tramite entry point base, visitor e studio isolati | Architettura di package Svelte, artefatti immutabili pacchettizzati, entry point isolati e contratti SSR/hydration e accessibilità |
| [Atelier-Kit](https://github.com/gcomneno/atelier-kit) | [v0.4.3](https://github.com/gcomneno/atelier-kit/releases/tag/v0.4.3) | Fornisce un kit vetrina configurabile con authoring locale via Studio, catalogo content-driven e strumenti di pubblicazione | Architettura di prodotto SvelteKit, authoring local-first, distribuzione desktop e adozione downstream reale di componenti Giada UI riutilizzabili |
| [Ubuntu System Tools](https://github.com/gcomneno/ubuntu-system-tools) | [v0.3.0](https://github.com/gcomneno/ubuntu-system-tools/releases/tag/v0.3.0) | Utilità Linux per diagnostica, manutenzione controllata, trascrizione offline e analisi degli avvisi kernel | Tooling di sistema safety-first, diagnostica read-only, flussi espliciti su opt-in e packaging Linux riproducibile |

<details>
<summary>Altri progetti operativi</summary>

| Progetto | Segnale tecnico |
| --- | --- |
| [LeLe Quizzer](https://github.com/gcomneno/lele-quizzer) | Generazione deterministica di quiz, UX da terminale e riuso della conoscenza |
| [GYTE Study Tools](https://github.com/gcomneno/gyte-study-tools) | Pipeline di contenuti riavviabili, validazione deterministica, confini privato/pubblico e handoff espliciti verso servizi esterni |

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

<details>
<summary>Pull request upstream selezionate e integrate</summary>

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
| Modellazione stocastica a stati finiti | [Lotto Digit Coverage Dynamics](https://github.com/gcomneno/lotto-digit-coverage-dynamics) | Modelli di Markov assorbenti esatti, verifica esaustiva del kernel e confronto storico |

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

- **2026-08-12** · `atelier-kit` · **Refactoring:** [consume GIADA semantic palette contract](https://github.com/gcomneno/atelier-kit/commit/7360e7a91d7028ee0a830cb36f6f281f05dd6836)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [consume canonical GIADA theme tokens](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/84d734ff76a6540b4fd200cf7e5f5a216cfb3cb7)
- **2026-08-12** · `giadaware-ui-components` · **Funzionalità:** [add shared semantic palette tokens](https://github.com/gcomneno/giadaware-ui-components/commit/26f9e2068696ecfa215b75b2628cfce2736c164b)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [add auditable mailbox change log (#22)](https://github.com/gcomneno/semantic-mail-archivist/commit/d8fdbaf51c4d25e490fa75ad05a7ceb10ffaa658)

<details>
<summary>Altri aggiornamenti recenti e significativi</summary>

- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [keep missing digits on two rows (#37)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/bac5b21eecfa72d66442dcd9a8a633f546a9030c)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [improve digit-set readability and contrast (#36)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/4fb432c6b9761cc612a8619d2d8551a41635f728)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Sviluppo:** [demo: reset social links](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/d8b3e4273cd9e6667043510856af601038c2b9a9)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Sviluppo:** [demo: update social links](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/95a82920f3a291bf1daf3bb2c25d9373b3172120)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [wait for complete pywebview API readiness (#35)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/746cd294b921b751f6fa75ef9ab84a4e08c86c2a)
- **2026-08-12** · `distributed-systems-study` · **Documentazione:** [prepare distributed systems foundations study path (#4)](https://github.com/gcomneno/distributed-systems-study/commit/ad4eec9cc25879a111236875c6f603e70734aa69)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [align native controls with application theme (#34)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/d95dded95e0ec204c653fa2bcc6705f89470d520)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [add complete mailbox audit report (#21)](https://github.com/gcomneno/semantic-mail-archivist/commit/e89d771901d6a66165babd12e5cfb7b63696aaa7)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [harden first desktop road-test experience](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/18e5ef5694d005b9d0d56a35416de3d0b05b7fa8)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [preserve default database through pywebview serialization](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/14df410cf20a3ed36233e1a09240cda67badd662)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Sviluppo:** [probe](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/ab5345e95de3ec809529f45c67c93d1d423f2dd2)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Sviluppo:** [tmp](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/ab3ad66c89e9e5a5c2c79e35df08916b0e34aae8)
- **2026-08-12** · `semantic-mail-archivist` · **Correzione:** [tighten generic notification obsolescence cue](https://github.com/gcomneno/semantic-mail-archivist/commit/439a65121039b357a6fdde47af4aff6e77b39522)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [handshake pywebview bridge before loading reports](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/79e359e77d63841be24000a93bf37a9e5fcbab7c)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [add optional operational state layer (#19)](https://github.com/gcomneno/semantic-mail-archivist/commit/c3fab155dab0acbfdcd28bb49e84ea305fa3bbbc)
- **2026-08-12** · `atelier-kit` · **Funzionalità:** [wire bounded public social experience (#288)](https://github.com/gcomneno/atelier-kit/commit/a3390f5b4451240a2c2b674db9b120192d6c641b)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Funzionalità:** [wire bounded public social experience (#288)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/a3390f5b4451240a2c2b674db9b120192d6c641b)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Correzione:** [repair road-test reactivity and research navigation (#30)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/df87b219e706c111b21994019d2c2c5b24cf0fe0)
- **2026-08-12** · `software-architecture-study` · **Documentazione:** [prepare software architecture foundations study path](https://github.com/gcomneno/software-architecture-study/commit/5662238f65f88e7aab675bd2aa8b5e7d0f53b343)
- **2026-08-12** · `semantic-mail-archivist` · **Correzione:** [validate protected document ownership](https://github.com/gcomneno/semantic-mail-archivist/commit/36423437d48522725f5d48e05667a72899485919)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [detect obsolete low-value messages safely (#17)](https://github.com/gcomneno/semantic-mail-archivist/commit/967b2d8a751bc6040452a91bc3d88e87acf3c0e6)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Funzionalità:** [complete local research interface (#29)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/6542a4656d0beb81c7fb3110e825647356a12851)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Funzionalità:** [add same-wheel occurrence explorer (#28)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/722a78a3597241ccfdf3233387964346d26cdff2)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Funzionalità:** [establish GIADA UI desktop foundation (#27)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/2003e22b91c1bd1cc586dd9b806d71cff17e89fe)
- **2026-08-12** · `system-design-study` · **Documentazione:** [complete API design study session](https://github.com/gcomneno/system-design-study/commit/d90b1ca398b44c80fcc8e229b4a587897e2e98d3)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [complete historical research migration (#26)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/8d37fdf45f25bfeb2618e2a40cd625d249c949bc)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [migrate historical signal reports (#25)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/db45d3d9af74965aa140a910d146911867a624aa)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [migrate historical Markov reports (#24)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/85f2a202b167d5e444011af1d45f79a11ddd65a5)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [dispatch migrated application commands directly (#23)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/ce2cf020779588a9dc19786cb2a1411b935026ed)
- **2026-08-12** · `atelier-kit` · **Funzionalità:** [isolate sandbox social authoring (#287)](https://github.com/gcomneno/atelier-kit/commit/7c714b5f13b352c92a560ad8933b715fa929e6d9)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Funzionalità:** [isolate sandbox social authoring (#287)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/7c714b5f13b352c92a560ad8933b715fa929e6d9)
- **2026-08-12** · `system-design-study` · **Documentazione:** [integrate private study SOT workflow](https://github.com/gcomneno/system-design-study/commit/978feb9dfe43477880277b99d695aea5e663857b)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [add stable versioned application contracts (#22)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/935c18f9651710dd19b3647072f6db5051729338)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [separate occurrence groups from terminal rendering (#21)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/b0e35181390b8c74ecdd94e472538f88e3b14ec9)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [expose structured current application report (#20)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/1ffae09eb2ef2c78c6156320c65e596f5ccfd8dc)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Refactoring:** [isolate draw repository contract from SQLite (#19)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/be860752a517f0965cdf4aeaf810c27b3b4b4990)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [introduce protected semantic categories (#16)](https://github.com/gcomneno/semantic-mail-archivist/commit/88464b2ad7660d2c182a6295ec3a5607a227676a)
- **2026-08-12** · `atelier-kit` · **Funzionalità:** [enforce bounded mutation integrity (#286)](https://github.com/gcomneno/atelier-kit/commit/387740529cb81d3ac2a9825104c51812b9f96838)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Funzionalità:** [enforce bounded mutation integrity (#286)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/387740529cb81d3ac2a9825104c51812b9f96838)
- **2026-08-12** · `atelier-kit` · **Funzionalità:** [add isolated guest session authority (#285)](https://github.com/gcomneno/atelier-kit/commit/46d2e5044bc6ccad2cd5b37de6d411bf7d897eff)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Funzionalità:** [add isolated guest session authority (#285)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/46d2e5044bc6ccad2cd5b37de6d411bf7d897eff)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Sviluppo:** [Introduce explicit architecture package boundaries (#18)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/091ca177210c29e215ddb86782c6ed96a81a83f2)
- **2026-08-12** · `giadaware-ui-components` · **Funzionalità:** [add accessible ImageLightbox (#46)](https://github.com/gcomneno/giadaware-ui-components/commit/8faf67e3c28c5bc33ad8a522236ecda25ec613d6)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [detect significant documents (#15)](https://github.com/gcomneno/semantic-mail-archivist/commit/d78ee7cd9ed19d2c48ad5f4f2a2ebe6e18fbe9e6)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Sviluppo:** [Add grouped occurrence totals to the Lotto viewer (#8)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/5f3be5fef608a2065f39f64f649e8b3c7108067c)
- **2026-08-12** · `lotto-digit-coverage-dynamics` · **Sviluppo:** [Replace TUTTE with consensus and add twin-number analysis (#7)](https://github.com/gcomneno/lotto-digit-coverage-dynamics/commit/54337d9e11846e94108b8f26e5e48fb75eda223f)
- **2026-08-12** · `atelier-kit` · **Funzionalità:** [establish isolated public demo runtime (#284)](https://github.com/gcomneno/atelier-kit/commit/2f1be53ce5eeb4e11803398955de14c9e49050b3)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Funzionalità:** [establish isolated public demo runtime (#284)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/2f1be53ce5eeb4e11803398955de14c9e49050b3)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [add dry-run repair reports](https://github.com/gcomneno/semantic-mail-archivist/commit/4e040998ce6200d07fb34bfe5a487467472a08a5)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [infer labels with explainable confidence](https://github.com/gcomneno/semantic-mail-archivist/commit/e33b3cd2e19ac84f6507ae98ab81fb925122c399)
- **2026-08-12** · `semantic-mail-archivist` · **Funzionalità:** [detect message-level label gaps (#12)](https://github.com/gcomneno/semantic-mail-archivist/commit/7647b4bb985fa303bda0b7fac2c4d6157b962e73)
- **2026-08-12** · `atelier-kit` · **Funzionalità:** [harden public demo deployment boundary (#282)](https://github.com/gcomneno/atelier-kit/commit/f36fdd55f865292044133a017abac5eef48b47a5)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Funzionalità:** [harden public demo deployment boundary (#282)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/f36fdd55f865292044133a017abac5eef48b47a5)
- **2026-08-12** · `semantic-mail-archivist` · **Documentazione:** [define classification and safety model (#11)](https://github.com/gcomneno/semantic-mail-archivist/commit/5b850441494a747de1d7aece38ea2ca058b1f82c)
- **2026-08-12** · `semantic-mail-archivist` · **Documentazione:** [link roadmap to founding issues](https://github.com/gcomneno/semantic-mail-archivist/commit/fb71d9f894ec561c468fe60114e4cc7698023a04)
- **2026-08-12** · `semantic-mail-archivist` · **Documentazione:** [add project charter](https://github.com/gcomneno/semantic-mail-archivist/commit/b4ac07fd0f7ed0eb843b7a3717ef8e104ca63d07)
- **2026-08-12** · `semantic-mail-archivist` · **Documentazione:** [initialize project documentation directory](https://github.com/gcomneno/semantic-mail-archivist/commit/8cb3982b0943eab4f3b1078197594cc0379c717b)
- **2026-08-12** · `semantic-mail-archivist` · **Documentazione:** [establish project vision and MVP](https://github.com/gcomneno/semantic-mail-archivist/commit/c975e7fbfb1b34a452726dddaf68e9729be69307)
- **2026-08-12** · `semantic-mail-archivist` · **Sviluppo:** [Initial commit](https://github.com/gcomneno/semantic-mail-archivist/commit/e6520c0c24641cbf8933e3183ec894e4dae86f72)
- **2026-08-12** · `gyte-study-tools` · **Documentazione:** [adopt bilingual documentation convention (#10) (#13)](https://github.com/gcomneno/gyte-study-tools/commit/da985b9f0d27eb77cf04fa617f9569558252435f)
- **2026-08-12** · `gyte-study-tools` · **Sviluppo:** [Align source lesson handoff with LeLe Manager (#9)](https://github.com/gcomneno/gyte-study-tools/commit/88d924f3faa54abb0babe82296cef76bc67403e5)
- **2026-08-12** · `giadaware-ui-components` · **Correzione:** [make RelationshipGraph labels consumer-owned and improve keyboard navigation (#45)](https://github.com/gcomneno/giadaware-ui-components/commit/24b0318159d7f5481f80b7c66e1709c8e98e7b0e)
- **2026-08-12** · `gyte-study-tools` · **Sviluppo:** [Preserve lexical words across transcript reflow (#6)](https://github.com/gcomneno/gyte-study-tools/commit/9a5ba932e45d6d4af9a72c419762975e4f94a604)
- **2026-08-12** · `atelier-kit` · **Correzione:** [preserve focal area and localize navigation (#278)](https://github.com/gcomneno/atelier-kit/commit/04909d71d62bf97d347e16ddf11c767622f77a88)
- **2026-08-12** · `atelier-kit-demo-sandbox` · **Correzione:** [preserve focal area and localize navigation (#278)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/04909d71d62bf97d347e16ddf11c767622f77a88)
- **2026-08-12** · `gyte-study-tools` · **Sviluppo:** [Fix extraction from article-scoped content containers (#4)](https://github.com/gcomneno/gyte-study-tools/commit/226ddbda0efca0c92e7d1b58a4816f4e34571685)
- **2026-08-11** · `lele-manager` · **Correzione:** [harden vault snapshot restore boundaries](https://github.com/gcomneno/lele-manager/commit/6de01844a5dcff039c0d0feae9d3663e0758ee1d)
- **2026-08-11** · `lele-manager` · **Funzionalità:** [add vault snapshot and restore workflows](https://github.com/gcomneno/lele-manager/commit/0cd38b6b82ae4ea30f255546b8b13dc47992ea01)
- **2026-08-11** · `lele-manager` · **Correzione:** [enforce active-vault snapshot coherence](https://github.com/gcomneno/lele-manager/commit/8996a6528df5f6f70941af30db16d0dcf84620b8)
- **2026-08-11** · `lele-manager` · **Correzione:** [harden multi-vault runtime boundaries](https://github.com/gcomneno/lele-manager/commit/d082a78a04bfd9a362f2a1da5504c9ffa3e14f85)
- **2026-08-11** · `lele-manager` · **Funzionalità:** [add multi-vault registry and active-vault management](https://github.com/gcomneno/lele-manager/commit/592c8177a5015f471e91afddf3a7da71c9b174c4)
- **2026-08-10** · `lele-manager` · **Correzione:** [harden duplicate resolution workflows](https://github.com/gcomneno/lele-manager/commit/83daefb3f2b77d3dd8046febb09124ac8eaf92f0)
- **2026-08-10** · `lele-manager` · **Funzionalità:** [add explicit duplicate resolution](https://github.com/gcomneno/lele-manager/commit/c12217338979a86c39b61d3ff318d175217d8abf)
- **2026-08-10** · `atelier-kit` · **Funzionalità:** [deploy and validate the first real private Hosted Studio (#276)](https://github.com/gcomneno/atelier-kit/commit/784bca31be717e159f7ad34ed8aea24dbf2d6921)
- **2026-08-10** · `atelier-kit-demo-sandbox` · **Funzionalità:** [deploy and validate the first real private Hosted Studio (#276)](https://github.com/gcomneno/atelier-kit-demo-sandbox/commit/784bca31be717e159f7ad34ed8aea24dbf2d6921)
- **2026-08-10** · `lele-manager` · **Funzionalità:** [add safe Browse bulk deletion](https://github.com/gcomneno/lele-manager/commit/3476e4c717bbd89ccde033c1ac4b57930ce0ec48)
- **2026-08-10** · `lele-manager` · **Funzionalità:** [add canonical single-lesson actions](https://github.com/gcomneno/lele-manager/commit/73f7fb48d92b03ee518f64212ff901ce46d7bb9d)
- **2026-08-10** · `system-log-dynamics` · **Sviluppo:** [Add structured systemd lifecycle semantic facets v2 (#40)](https://github.com/gcomneno/system-log-dynamics/commit/5df2b7b1bbf963c03c40895864a759d9beb02c94)
- **2026-08-10** · `lele-manager` · **Sviluppo:** [ux: simplify metadata authoring](https://github.com/gcomneno/lele-manager/commit/8a6b619f9ac19d45fb4b37a46d65dd7589f9cea3)
- **2026-08-10** · `lele-manager` · **Correzione:** [preserve responsive shell navigation contracts](https://github.com/gcomneno/lele-manager/commit/3f68e2362a44c5076a7c075abd24266727b7d9bd)
- **2026-08-10** · `lele-manager` · **Sviluppo:** [ux: redesign global application header](https://github.com/gcomneno/lele-manager/commit/ab6af6e1245f704a7052008fa222020a058e8a78)
- **2026-08-10** · `system-log-dynamics` · **Sviluppo:** [Expose semantic evidence v1 through the CLI (#38)](https://github.com/gcomneno/system-log-dynamics/commit/a93a038788186c754ad52e289473dde2774457a4)
- **2026-08-10** · `system-log-dynamics` · **Sviluppo:** [Preserve descriptive event semantics for downstream IDS consumers (#36)](https://github.com/gcomneno/system-log-dynamics/commit/8fbaf8f03d6e0e1911c1ca3009b1d2445af10e38)
- **2026-08-10** · `lele-manager` · **Sviluppo:** [ux: make sidebar groups collapsible](https://github.com/gcomneno/lele-manager/commit/fc041d6ce0f8743ed1584a504931f220db7f3b8b)
- **2026-08-10** · `lele-manager` · **Sviluppo:** [ux: differentiate sidebar icons](https://github.com/gcomneno/lele-manager/commit/348b56aed4e5c83dadff7e73a14e4019fc3eca3f)
- **2026-08-10** · `lele-manager` · **Sviluppo:** [ux: turn Settings into Diagnostics workflow](https://github.com/gcomneno/lele-manager/commit/5c2e74b2c6bb522b39282b1b80c232e8c5b82424)
- **2026-08-10** · `system-log-dynamics` · **Correzione:** [distinguish observed boot transitions (#34)](https://github.com/gcomneno/system-log-dynamics/commit/e01e943286c23b4fb6a4dd4218fbaa9cbe428ae5)
- **2026-08-10** · `lele-manager` · **Correzione:** [serialize desktop launcher paths correctly](https://github.com/gcomneno/lele-manager/commit/292aa534207e8ef34cb6410f221b41d28197669c)
- **2026-08-10** · `lele-manager` · **Funzionalità:** [install Linux desktop integration](https://github.com/gcomneno/lele-manager/commit/6e90b369bce196d0898ae92a58bfbb012e76b065)
- **2026-08-10** · `system-log-dynamics` · **Documentazione:** [define downstream IDS trust boundary (#32)](https://github.com/gcomneno/system-log-dynamics/commit/01587ee34b8fa2687de604d79d70b2114258d898)
- **2026-08-10** · `lele-manager` · **Correzione:** [isolate Linux install payload from user data](https://github.com/gcomneno/lele-manager/commit/8dc411e90325ed768ee3311d5b05e50923ad2956)
- **2026-08-10** · `system-log-dynamics` · **Funzionalità:** [export versioned evidence bundles (#31)](https://github.com/gcomneno/system-log-dynamics/commit/1718750adb0c937bb06d42e85d9cc075477c73fa)
- **2026-08-10** · `lele-manager` · **Funzionalità:** [add stable Linux install contract](https://github.com/gcomneno/lele-manager/commit/af309a147b8f089f057ff298e4cff66df1b96847)
- **2026-08-09** · `lele-manager` · **Correzione:** [reuse running launcher instance](https://github.com/gcomneno/lele-manager/commit/2e730e1af2df736eafd6021a49d3fc8a1f45c577)
- **2026-08-09** · `lele-manager` · **Sviluppo:** [ux: move similarity tuning to advanced options](https://github.com/gcomneno/lele-manager/commit/31c14be4d05273601d8f3490bafda4aa5e14cd1c)
- **2026-08-09** · `lele-manager` · **Correzione:** [lower mascot tongue by 3px](https://github.com/gcomneno/lele-manager/commit/a2554539c285928ce428eb47c5651a5df86ff812)

_Sono mostrati i 100 aggiornamenti significativi più recenti; 957 aggiornamenti precedenti sono stati omessi._

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
