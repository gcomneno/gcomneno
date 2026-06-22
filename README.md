<a id="top"></a>

<h1 align="center">👋 Giancarlo Cicellyn Comneno 👋</h1>

<p align="center">
  Backend Software Developer · C · PHP/Laravel · Python · Linux · CLI tooling · OSS
</p>

<p align="center">
  CLI, API, tooling, laboratori tecnici e progetti con test automatici, documentazione, versioning e workflow riproducibili.
</p>

<p align="center">
  <a href="#selected-work">
    <img alt="Selected Work" src="https://img.shields.io/badge/Selected%20Work-Backend%20%2F%20Python%20%2F%20Linux-blue?style=for-the-badge">
  </a>
  <a href="#flagship">
    <img alt="Research Flagship" src="https://img.shields.io/badge/Research-PET-gold?style=for-the-badge">
  </a>
  <a href="#oss">
    <img alt="Open Source" src="https://img.shields.io/badge/OSS-Contributions-black?style=for-the-badge&logo=github">
  </a>
  <a href="#visitors">
    <img alt="Visite profilo" src="https://komarev.com/ghpvc/?username=gcomneno&label=%F0%9F%91%80&style=for-the-badge">
  </a>  
</p>

---

<h2 align="center">Giadaware Remote Lab · Backend tools, CLI and reproducible experiments</h2>

<p align="center">
Lavoro su strumenti software, CLI, API e laboratori tecnici
con attenzione a chiarezza, automazione, test e documentazione.<br><br>
<em>Obiettivo pratico: rendere visibile non solo cosa costruisco, ma anche come ragiono mentre lo costruisco.</em>
</p>

---

<a id="updates"></a>
## 🗞️ Ultimi aggiornamenti

- **2026-06-21** · ["Il Gentiluomo delle Ombre"]([https://github.com/gcomneno/club-dell-assurdo/blob/main/fiction/stories/Nero%20quotidiano/Le%20Cronache%20del%20Gentiluomo%20delle%20Ombre/01.%20Il%20Gentiluomo%20delle%20Ombre%20(Atto%20I)/Capitolo-14-finale-assurdo-reale.md](https://github.com/gcomneno/club-dell-assurdo/blob/main/fiction/stories/Nero%20quotidiano/Le%20Cronache%20del%20Gentiluomo%20delle%20Ombre/01.%20Il%20Gentiluomo%20delle%20Ombre%20(Atto%20I)/Capitolo-14.md)). Finale del primo atto riscritto. Molto meglio adesso! ❤️
- **2026-06-20** · Avviati `python-fast-track` e `pygit-lab`, due nuovi laboratori didattici su Python per sviluppatori esperti e internals di Git ricostruiti in Python.
- **2026-06-19** · Avviato [OOP-in-C Lab](https://github.com/gcomneno/oop-in-c-lab), laboratorio didattico per esplorare come modellare concetti OOP in C.
- **2026-06-12** · Pubblicato LeLe Quizzer `v0.1.0`, quiz da terminale collegato alla knowledge base locale di LeLe Manager.
- **2026-06-11** · Ripreso PET dai principi primi, chiarendo rappresentazione canonica, confini del modello e ruolo come lente strutturale sugli interi.

<p align="right"><a href="#top">↑ torna su</a></p>

---

<a id="selected-work"></a>
## 🧰 Selected work

Una selezione breve per capire rapidamente cosa so costruire, senza aprire quaranta tab e perdere la fede nell'umanità.

### LeLe Manager - Knowledge-base tooling

Lessons Learned manager e toolkit ML con CLI, REST API, test automatici e packaging.

- gestione di una knowledge base locale in JSONL
- ricerca/similarità con backend deterministici
- CLI e API pensate per workflow riproducibili
- attenzione a privacy, configurazione e confini tra dati pubblici e locali

**Repo:** https://github.com/gcomneno/lele-manager

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12-yellow?logo=python">
  &nbsp;
  <img alt="CLI" src="https://img.shields.io/badge/Interface-CLI-blue">
  &nbsp;
  <img alt="API" src="https://img.shields.io/badge/API-REST-brightgreen">
  &nbsp;
  <img alt="Tests" src="https://img.shields.io/badge/Tests-Automatici-success">
</p>

### LeLe Quizzer - Terminal quiz game

Quiz game didattico collegato alla "Knowledge Base" prodotta da LeLe Manager. Permette di ispezionare la KB, cercare lesson, generare domande deterministiche, giocare quiz interattivi, salvare i tentativi in locale e riepilogare le aree più allenate/deboli. 

Privacy-first: configurazione privata, knowledge base reale e risposte utente restano fuori dal repository:
- configurazione tramite YAML
- ricerca locale nella knowledge base
- generazione di bozze di domande
- quiz interattivo da terminale
- salvataggio locale dei tentativi
- release pubblica `v0.1.0`

**Repo:** https://github.com/gcomneno/lele-quizzer

**Release:** https://github.com/gcomneno/lele-quizzer/releases/tag/v0.1.0

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12-yellow?logo=python">
  &nbsp;
  <img alt="CLI" src="https://img.shields.io/badge/Interface-CLI-blue">
  &nbsp;
  <img alt="Quiz" src="https://img.shields.io/badge/Mode-Quiz%20Game-purple">
  &nbsp;
  <img alt="Release" src="https://img.shields.io/badge/Release-v0.1.0-success">
</p>

### Smart File Organizer - Python clean coding lab

Laboratorio Python orientato a codice pulito e sviluppo production-style.

- layout `src/`
- project management con `uv`
- lint/format con `ruff`
- test con `pytest`
- CLI con dry-run sicuro e applicazione esplicita

**Repo:** https://github.com/gcomneno/smart-file-organizer

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12-yellow?logo=python">
  &nbsp;
  <img alt="uv" src="https://img.shields.io/badge/Tooling-uv-purple">
  &nbsp;
  <img alt="pytest" src="https://img.shields.io/badge/Tests-pytest-brightgreen">
  &nbsp;
  <img alt="ruff" src="https://img.shields.io/badge/Lint%20%2F%20Format-ruff-black">
</p>

### Yocto/QEMU Mini Lab - Embedded Linux learning lab

Mini laboratorio Yocto/QEMU per build, boot, layer custom e ricette BitBake.

- build di `core-image-minimal`
- boot con QEMU
- layer custom `meta-monkey`
- ricetta `hello-monkey`
- immagine custom `monkey-image-minimal`
- release pubblica `v0.1.0`

**Repo:** https://github.com/gcomneno/yocto-qemu-mini-lab

<p>
  <img alt="Yocto" src="https://img.shields.io/badge/Yocto-Lab-blue">
  &nbsp;
  <img alt="QEMU" src="https://img.shields.io/badge/QEMU-Boot-orange">
  &nbsp;
  <img alt="BitBake" src="https://img.shields.io/badge/BitBake-Recipes-purple">
  &nbsp;
  <img alt="Embedded Linux" src="https://img.shields.io/badge/Embedded-Linux-black?logo=linux&logoColor=white">
</p>

<p align="right"><a href="#top">↑ torna su</a></p>

---

<a id="flagship"></a>
## 👑 Progetto in Evidenza

### PET - Prime Exponent Tree

**Rappresentazione canonica e ricorsiva degli interi basata su fattorizzazione in numeri primi e alberi degli esponenti.**

PET è il mio progetto-bandiera: un modello strutturale degli interi che non guarda solo il valore numerico,
ma anche la loro **forma fattoriale ricorsiva**.

- rappresentazione **canonica, invertibile e lossless**
- codifica/decodifica, validazione e **JSON canonico**
- metriche strutturali e analisi di dataset numerici
- CLI minimale e workflow riproducibili
- focus R&D tra matematica computazionale, struttura e sperimentazione

**Repo:** https://github.com/gcomneno/pet

<p>
  <img alt="Interface" src="https://img.shields.io/badge/Interface-CLI-blue">
  &nbsp;
  <img alt="Canonical" src="https://img.shields.io/badge/Representation-Canonical-brightgreen">
  &nbsp;
  <img alt="Lossless" src="https://img.shields.io/badge/Encoding-Lossless-success">
  &nbsp;
  <img alt="R&D" src="https://img.shields.io/badge/Focus-Math%20R%26D-purple">
</p>

<p align="right"><a href="#top">↑ torna su</a></p>

---

<a id="labs"></a>
## 🧪 Altri laboratori didattici

Altri percorsi di studio, esercizi guidati e laboratori pratici pensati per imparare facendo.

<details>
<summary><strong>Apri elenco completo</strong></summary>
<br>

- **C# / HTML Lab - Didattico** - `kleis-sviluppo-software-4`
  Laboratorio didattico in C# sui fondamenti della programmazione, con esempi e commenti utili per capire il linguaggio passo dopo passo.
  <br>
  Repo: https://github.com/gcomneno/kleis-sviluppo-software-4
  <p>
    <img alt="C#" src="https://img.shields.io/badge/C%23-.NET-purple?logo=dotnet">
    &nbsp;
    <img alt="HTML" src="https://img.shields.io/badge/HTML-5-orange?logo=html5&logoColor=white">
    &nbsp;
    <img alt="CSS" src="https://img.shields.io/badge/CSS-3-blue?logo=css3&logoColor=white">
    &nbsp;
    <img alt="Didattico" src="https://img.shields.io/badge/Focus-Didattico-brightgreen">
  </p>

* **Python Fast Track** - `python-fast-track`
  Percorso compatto di Python per sviluppatori già esperti: lezioni pratiche, confronti con altri linguaggi, esercizi e appunti orientati a diventare produttivi rapidamente.
  <br>
  Repo: https://github.com/gcomneno/python-fast-track
  <p>
    <img alt="Python" src="https://img.shields.io/badge/Python-Fast%20Track-yellow?logo=python">
    <img alt="Experienced Developers" src="https://img.shields.io/badge/Target-Experienced%20Developers-blue">
    <img alt="Lessons" src="https://img.shields.io/badge/Docs-Lessons-brightgreen">
    <img alt="Didattico" src="https://img.shields.io/badge/Focus-Didattico-purple">
  </p>

* **PyGit Lab** - `pygit-lab`
  Laboratorio didattico per esplorare gli internals di Git ricostruendo concetti fondamentali con Python: repository, oggetti, comandi minimi e Lesson Learned operative.
  <br>
  Repo: https://github.com/gcomneno/pygit-lab
  <p>
    <img alt="Python" src="https://img.shields.io/badge/Python-Lab-yellow?logo=python">
    <img alt="Git" src="https://img.shields.io/badge/Git-Internals-orange?logo=git&logoColor=white">
    <img alt="CLI" src="https://img.shields.io/badge/Interface-CLI-blue">
    <img alt="Didattico" src="https://img.shields.io/badge/Focus-Didattico-brightgreen">
  </p>

- **Web Lab / Laravel Lab** - `web`
  Laboratorio personale per progetti web. Il primo sottoprogetto attivo è un percorso Laravel seguito lezione per lezione, con appunti, glossario, progetto locale e Lesson Learned.
  <br>
  Repo: https://github.com/gcomneno/web
  <p>
    <img alt="Laravel" src="https://img.shields.io/badge/Laravel-Lab-red?logo=laravel&logoColor=white">
    &nbsp;
    <img alt="PHP" src="https://img.shields.io/badge/PHP-Web-blue?logo=php&logoColor=white">
    &nbsp;
    <img alt="Lesson Learned" src="https://img.shields.io/badge/Docs-Lesson%20Learned-brightgreen">
    &nbsp;
    <img alt="Focus" src="https://img.shields.io/badge/Focus-Web%20Lab-purple">
  </p>

- **JavaScript Lab - Didattico** - `js-lab-didattico`
  Laboratorio didattico in JavaScript e TypeScript sui design pattern, con esempi eseguibili, test automatici e spiegazioni.
  <br>
  Repo: https://github.com/gcomneno/js-lab-didattico
  <p>
    <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-Lab-yellow?logo=javascript&logoColor=black">
    &nbsp;
    <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-Patterns-blue?logo=typescript&logoColor=white">
    &nbsp;
    <img alt="Tests" src="https://img.shields.io/badge/Tests-Automatici-brightgreen">
    &nbsp;
    <img alt="Didattico" src="https://img.shields.io/badge/Focus-Didattico-purple">
  </p>

- **OOP-in-C Lab - Didattico** - `oop-in-c-lab`
  Laboratorio didattico in C per esplorare come modellare concetti tipici della programmazione a oggetti usando `struct`, puntatori, layout di memoria e dispatch manuale.
  <br>
  Repo: https://github.com/gcomneno/oop-in-c-lab
  <p>
    <img alt="C" src="https://img.shields.io/badge/C-Lab-blue">
    &nbsp;
    <img alt="OOP" src="https://img.shields.io/badge/OOP-Concepts-purple">
    &nbsp;
    <img alt="Memory Layout" src="https://img.shields.io/badge/Memory-Layout-orange">
    &nbsp;
    <img alt="Didattico" src="https://img.shields.io/badge/Focus-Didattico-brightgreen">
  </p>
 
- **Cyber-Security Lab** - `cyse-lab`
  Laboratorio didattico white-hat con script per recon/enumeration, scenari ripetibili e template di Lesson Learned.
  <br>
  Repo: https://github.com/gcomneno/cyse-lab
  <p>
    <img alt="Cybersecurity" src="https://img.shields.io/badge/Cybersecurity-White--hat-black">
    &nbsp;
    <img alt="Recon" src="https://img.shields.io/badge/Recon-Enumeration-blue">
    &nbsp;
    <img alt="Scripts" src="https://img.shields.io/badge/Scripts-Lab-purple">
    &nbsp;
    <img alt="Lesson Learned" src="https://img.shields.io/badge/Docs-Lesson%20Learned-brightgreen">
  </p>

</details>

<p align="right"><a href="#top">↑ torna su</a></p>

---

<a id="software"></a>
## 💖 Altri progetti tecnici

<details>
<summary><strong>Apri elenco completo</strong></summary>
<br>

- **ISS - Integer Structural Search**
  Motore di ricerca strutturale bounded su interi: strategie dichiarate, budget espliciti, output JSON stabile e guardrail contro la fattorizzazione generale mascherata.
  Repo: https://github.com/gcomneno/integer-structural-search

- **MIDAS - Modular Integer Dataset Analysis System**
  Deterministic CLI tool per analisi di dataset di interi, con focus su pattern modulari e struttura non-casuale.
  Repo: https://github.com/gcomneno/midas

- **Ubuntu System Tools**
  Tool CLI Bash per Ubuntu progettati per essere public-safe, con attenzione a automazione, manutenzione e riproducibilità.
  Repo: https://github.com/gcomneno/ubuntu-system-tools

- **GYTE - YouTube Transcript Extractor**
  Batch extractor di trascrizioni YouTube con provider abstraction, CLI leggibile e workflow riproducibili.
  Repo: https://github.com/gcomneno/gyte

</details>

<p align="right"><a href="#top">↑ torna su</a></p>

---

<a id="rnd"></a>
## 🧭 Altri progetti di ricerca

<details>
<summary><strong>Apri elenco completo</strong></summary>
<br>

- **OCF - Onion Compressor Framework** - `onion-compressor-framework`
  Framework modulare di compressione con layer pluggabili, pipeline deterministiche e quality gates automatizzati.
  Repo: https://github.com/gcomneno/onion-compressor-framework

- **Turbo-Bucketizer (C++17)** - `turbo-bucketizer-cpp`
  Deterministic IPv4 bucketizer in C++17 per classificazione ad alte prestazioni, testing e esperimenti di rete riproducibili.
  Repo: https://github.com/gcomneno/turbo-bucketizer-cpp

- **Crystal Codec (GCC v1)** - `crystal-codec-gcc-v1`
  Codec p-adico in Python con API pulita, test e SPEC matematica per esperimenti su struttura, invarianti e compressione.
  Repo: https://github.com/gcomneno/crystal-codec-gcc-v1

- **OEIS Probe** - `oeis-probe`
  Strumento CLI per fingerprinting di sequenze su OEIS: query online via API, cache SQLite e comandi rapidi per capire “a cosa somiglia” una sequenza.
  Repo: https://github.com/gcomneno/oeis-probe

- **Digit-Probe** - `digit-probe`
  Analizzatore statistico/strutturale per sequenze numeriche: chi-quadrato, runs, gaps, autocorrelazione, compressione, n-gram e confronti con modelli ideali.
  Repo: https://github.com/gcomneno/digit-probe

- **Prime Tower Clocks** - `prime-tower-clocks`
  Tool matematico/CLI per rappresentare interi grandi tramite firme modulari basate su orologi primi e CRT.
  Repo: https://github.com/gcomneno/prime-tower-clocks

- **Huffman Compressor (legacy)** - `huffman-compressor`
  Laboratorio storico di compressione “a strati”, mantenuto come base evolutiva verso framework più maturi.
  Repo: https://github.com/gcomneno/huffman-compressor

- **Lasagna v2** - `lasagna-v2`
  Codec sperimentale per serie temporali con segmentazione adattiva, predittori multipli e tagging dei pattern.
  Repo: https://github.com/gcomneno/lasagna-v2

- **GianKoLotto® - Smart Combos** - `giankolotto-smart-combos`
  Motore combinatorio Lotto-compliant con pruning aggressivo e vincoli modulari configurabili.
  Repo: https://github.com/gcomneno/giankolotto-smart-combos

- **QHSE Supply Chain Demo** - `qhse-supplychain-demo`
  Architettura backend orientata all’affidabilità: FastAPI + SQLAlchemy + Postgres + pattern Outbox, worker idempotente, RBAC e modelli ben documentati.
  Repo: https://github.com/gcomneno/qhse-supplychain-demo

</details>

<p align="right"><a href="#top">↑ torna su</a></p>

---

<a id="oss"></a>
## 🌍 Contributi Open Source

- [yoctoproject/vscode-bitbake](https://github.com/yoctoproject/vscode-bitbake) → [gcomneno/vscode-bitbake](https://github.com/gcomneno/vscode-bitbake)

<details>
<summary><strong>Apri elenco completo</strong></summary>
<br>

Fork attivi di lavoro per contributi e patch:

- [canonical/rockcraft](https://github.com/canonical/rockcraft) → [gcomneno/rockcraft](https://github.com/gcomneno/rockcraft)
- [canonical/snapcraft](https://github.com/canonical/snapcraft) → [gcomneno/snapcraft](https://github.com/gcomneno/snapcraft)
- [canonical/craft-application](https://github.com/canonical/craft-application) → [gcomneno/craft-application](https://github.com/gcomneno/craft-application)
- [canonical/craft-cli](https://github.com/canonical/craft-cli) → [gcomneno/craft-cli](https://github.com/gcomneno/craft-cli)
- [canonical/craft-parts](https://github.com/canonical/craft-parts) → [gcomneno/craft-parts](https://github.com/gcomneno/craft-parts)
- [canonical/craft-providers](https://github.com/canonical/craft-providers) → [gcomneno/craft-providers](https://github.com/gcomneno/craft-providers)
- [copier-org/copier](https://github.com/copier-org/copier) → [gcomneno/copier](https://github.com/gcomneno/copier)

</details>

<p align="right"><a href="#top">↑ torna su</a></p>

---

<a id="books"></a>
## 📚 Narrativa - Il Club dell'Assurdo

<strong>Narrativa breve e seriale tra surreale e satira.</strong>

Universo narrativo in evoluzione continua, strutturato come libreria digitale:
atti, episodi, catalogo, roadmap editoriale e manifesto poetico.

- 🎭 Surreale logico
- 🧠 Satira filosofica
- 🕰️ Memoria, identità, potere
- 📖 Serialità modulare

👉 <a href="https://github.com/gcomneno/club-dell-assurdo"><strong>Entra nel Club dell'Assurdo</strong></a>

- <a href="https://github.com/gcomneno/club-dell-assurdo/blob/main/@INIZIA_DA_QUI.md">Inizia da qui</a>
- <a href="https://github.com/gcomneno/club-dell-assurdo/blob/main/CATALOG.md">Catalogo completo</a>
- <a href="https://github.com/gcomneno/club-dell-assurdo?tab=readme-ov-file#news">News & aggiornamenti</a>

<p align="right"><a href="#top">↑ torna su</a></p>

---

<a id="music"></a>
## 🎵 Musica - The Only Fly

Composizioni originali tra elettronica minimale, atmosfera e sperimentazione.
Pattern iterativi, variazioni controllate e ricerca timbrica.

- 🎹 Elettronica minimale e struttura
- 🌌 Atmosfere cinematiche e sospese
- 🔁 Variazioni tematiche e forme iterative

<p align="center">
  👉 <a href="https://theonlyfly.bandcamp.com/"><strong>Ascolta su Bandcamp</strong></a>
</p>

<p align="center">
  <a href="https://theonlyfly.bandcamp.com/">
    <img
      alt="Segui The Only Fly su Bandcamp"
      src="https://img.shields.io/badge/Bandcamp-Segui%20The%20Only%20Fly-629aa9?style=for-the-badge&logo=bandcamp&logoColor=white">
  </a>
</p>

<p align="center">
  <em>Un laboratorio sonoro dove anche i loop hanno una dignità filosofica.</em>
</p>

<p align="right"><a href="#top">↑ torna su</a></p>

---

## 💬 Motto

> “Se funziona ed è assurdo, allora è perfettamente logico.”

<p align="center">
  <a href="https://github.com/sponsors/gcomneno">
    <img alt="Sponsor on GitHub" src="https://img.shields.io/badge/Sponsor%20on%20GitHub-💖-pink?style=for-the-badge">
  </a>
</p>

<p align="center"><em>💖 Supporta “La Scimmia Curiosa” - perché anche i bit hanno bisogno di banane 🍌</em></p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=gcomneno&show_icons=true&hide_title=true" height="140" alt="Stats">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=gcomneno&layout=compact" height="140" alt="Top Langs">
</p>

<p align="right"><a href="#top">↑ torna su</a></p>
