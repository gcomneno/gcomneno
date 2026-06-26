# Giancarlo Cicellyn Comneno

Backend Software Developer · PHP/Laravel · Python · Linux · CLI tooling · Open Source

> Problems become knowledge. Knowledge becomes tools. Tools become open source.

Non colleziono repository. Colleziono problemi risolti.

Ogni progetto qui nasce da un attrito reale: qualcosa che ho dovuto capire, ripetere, automatizzare, spiegare o rendere più affidabile. Quando un problema torna più di una volta, lo trasformo in conoscenza. Quando quella conoscenza diventa riutilizzabile, provo a trasformarla in uno strumento. Quando lo strumento può essere utile anche ad altri, lo pubblico.

**GiadaWare** è il nome del mio laboratorio personale: il posto dove problemi ricorrenti diventano appunti, strumenti e progetti pubblici.

---

## Latest Updates

<!-- updates:start -->

- **2026-06-26** · Recuperate e documentate lezioni su responsive design, Flexbox, CSS Grid e media query.
- **2026-06-20** · Avviati `python-fast-track` e `pygit-lab`.
- **2026-06-19** · Pubblicato `oop-in-c-lab`, laboratorio didattico su OOP modellata in C.

<!-- updates:end -->

---

## The Problem Collection

Una selezione di problemi reali trasformati in strumenti, laboratori o progetti open source.

### 1. Come non perdere le lesson learned?

**Problema:** Le conoscenze operative si disperdono facilmente tra chat, file, appunti, repo e memoria personale.

**Strumento:** LeLe Manager: una knowledge base locale in JSONL, interrogabile da CLI e API, pensata per rendere ricercabili le lesson learned.

**Metodo:** CLI, REST API, backend deterministici, test automatici, configurazione esplicita e confini chiari tra dati pubblici e dati locali.

**Repo:** [gcomneno/lele-manager](https://github.com/gcomneno/lele-manager)

### 2. Come trasformare una knowledge base in allenamento?

**Problema:** Archiviare conoscenza non basta: bisogna richiamarla, verificarla e usarla.

**Strumento:** LeLe Quizzer: un quiz da terminale collegato alla knowledge base locale di LeLe Manager.

**Metodo:** Quiz interattivo, domande deterministiche, tentativi salvati localmente, riepilogo delle aree allenate/deboli e approccio privacy-first.

**Repo:** [gcomneno/lele-quizzer](https://github.com/gcomneno/lele-quizzer)

### 3. Come automatizzare file senza creare disastri?

**Problema:** Gli script che spostano file possono diventare pericolosi se non mostrano chiaramente cosa stanno per fare.

**Strumento:** Smart File Organizer: una CLI Python che organizza file con piano, dry-run e applicazione esplicita.

**Metodo:** Layout `src/`, `uv`, `ruff`, `pytest`, comandi chiari e attenzione alla sicurezza operativa.

**Repo:** [gcomneno/smart-file-organizer](https://github.com/gcomneno/smart-file-organizer)

### 4. Come capire Git oltre i comandi copiati?

**Problema:** Git viene spesso usato come sequenza di incantesimi terminale, senza capire il modello sotto.

**Strumento:** PyGit Lab: laboratorio didattico per ricostruire concetti fondamentali di Git in Python.

**Metodo:** Oggetti, repository, comandi minimi, esperimenti riproducibili e lesson learned operative.

**Repo:** [gcomneno/pygit-lab](https://github.com/gcomneno/pygit-lab)

### 5. Come capire davvero cosa c’è sotto l’OOP?

**Problema:** L’Object-Oriented Programming rischia di sembrare magia se non si guarda cosa succede sotto astrazioni, metodi e dispatch.

**Strumento:** OOP-in-C Lab: laboratorio in C che modella concetti OOP con `struct`, puntatori, vtable e layout di memoria.

**Metodo:** Esempi piccoli, output osservabile, confronto tra astrazione e memoria reale.

**Repo:** [gcomneno/oop-in-c-lab](https://github.com/gcomneno/oop-in-c-lab)

---

## Working Method

Il mio metodo di lavoro è semplice:

1. parto da un problema reale o ricorrente;
2. lo documento come conoscenza riutilizzabile;
3. cerco il modello minimo che lo rende comprensibile;
4. costruisco uno strumento piccolo e verificabile;
5. aggiungo test, documentazione e workflow riproducibile;
6. pubblico il progetto quando può essere utile anche fuori dal mio contesto.

Non mi interessa solo “fare un repo”. Mi interessa lasciare dietro un percorso leggibile: problema, ragionamento, soluzione, limiti, prossimi passi.

---

## Flagship Research: PET

PET, Prime Exponent Tree, è il punto in cui lo stesso metodo entra nella matematica computazionale.

**Problema:** Gli interi possono essere osservati non solo come valori, ma come strutture ricorsive generate dalla fattorizzazione.

**Strumento:** PET rappresenta gli interi come alberi canonici degli esponenti primi.

**Metodo:** Rappresentazione canonica, codifica/decodifica lossless, JSON canonico, CLI minimale, metriche strutturali e dataset analizzabili.

**Repo:** [gcomneno/pet](https://github.com/gcomneno/pet)

---

## Learning in Public

Uso i laboratori pubblici per trasformare studio, appunti e prove tecniche in percorsi riproducibili.

* [Python Fast Track](https://github.com/gcomneno/python-fast-track): Python per sviluppatori già esperti.
* [Web / Laravel Lab](https://github.com/gcomneno/web): percorso pratico su Laravel e sviluppo backend web.
* [PyGit Lab](https://github.com/gcomneno/pygit-lab): internals di Git ricostruiti in Python.
* [OOP-in-C Lab](https://github.com/gcomneno/oop-in-c-lab): concetti OOP ricostruiti in C.
* [Yocto/QEMU Mini Lab](https://github.com/gcomneno/yocto-qemu-mini-lab): embedded Linux, build, boot e BitBake.
* [C# / HTML Lab](https://github.com/gcomneno/kleis-sviluppo-software-4): fondamenti di programmazione e web.
* [JavaScript Lab](https://github.com/gcomneno/js-lab-didattico): pattern, TypeScript e test.
* [Cyber-Security Lab](https://github.com/gcomneno/cyse-lab): laboratorio white-hat con recon, script e lesson learned.

---

## Open Source Path

Il mio percorso open source è ancora in costruzione, ma segue la stessa logica: partire da problemi concreti, leggere il contesto tecnico, proporre modifiche piccole e verificabili.

Contributo principale in corso:

* [yoctoproject/vscode-bitbake](https://github.com/yoctoproject/vscode-bitbake) → [gcomneno/vscode-bitbake](https://github.com/gcomneno/vscode-bitbake)

Fork attivi di lavoro:

* [canonical/rockcraft](https://github.com/canonical/rockcraft) → [gcomneno/rockcraft](https://github.com/gcomneno/rockcraft)
* [canonical/snapcraft](https://github.com/canonical/snapcraft) → [gcomneno/snapcraft](https://github.com/gcomneno/snapcraft)
* [canonical/craft-application](https://github.com/canonical/craft-application) → [gcomneno/craft-application](https://github.com/gcomneno/craft-application)
* [canonical/craft-cli](https://github.com/canonical/craft-cli) → [gcomneno/craft-cli](https://github.com/gcomneno/craft-cli)
* [canonical/craft-parts](https://github.com/canonical/craft-parts) → [gcomneno/craft-parts](https://github.com/gcomneno/craft-parts)
* [canonical/craft-providers](https://github.com/canonical/craft-providers) → [gcomneno/craft-providers](https://github.com/gcomneno/craft-providers)
* [copier-org/copier](https://github.com/copier-org/copier) → [gcomneno/copier](https://github.com/gcomneno/copier)

---

Questo profilo è un laboratorio in movimento: problemi reali, strumenti piccoli, documentazione chiara e iterazioni pubbliche.
