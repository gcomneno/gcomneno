from __future__ import annotations

from pathlib import Path

PATHS = {"en": Path("README.md"), "it": Path("README.it.md")}

REPLACEMENTS = {
    "en": [
        (
            "| [Atelier-Kit](https://github.com/gcomneno/atelier-kit) | [v0.4.3](https://github.com/gcomneno/atelier-kit/releases/tag/v0.4.3) | Provides a configurable showcase kit with local Studio authoring, content-driven catalog workflows and deployment tooling | SvelteKit product architecture, local-first authoring, desktop delivery and real downstream adoption of reusable Giada UI components |",
            "| [Atelier-Kit](https://github.com/gcomneno/atelier-kit) | [v0.4.3](https://github.com/gcomneno/atelier-kit/releases/tag/v0.4.3) | Provides a configurable showcase kit with local, desktop and bounded hosted Studio authoring, content-driven catalog workflows and deployment tooling | SvelteKit product architecture, explicit local/hosted/demo authority boundaries, atomic repository mutations, desktop delivery and downstream Giada UI adoption |",
        ),
        (
            "| [GYTE Study Tools](https://github.com/gcomneno/gyte-study-tools) | Restartable content pipelines, deterministic validation, private/public boundaries and explicit external-delivery handoffs |",
            "| [GYTE Study Tools](https://github.com/gcomneno/gyte-study-tools) | Restartable content pipelines, deterministic validation, private/public boundaries and explicit external-delivery handoffs |\n| [Semantic Mail Archivist](https://github.com/gcomneno/semantic-mail-archivist) | Privacy-first Gmail audit and repair dry-runs, provider boundaries, explainable confidence and crash-aware mutation journaling |",
        ),
        (
            "| Updated npm dependencies in a controlled way, reducing vulnerabilities without changing declared ranges | Dependency maintenance, security hygiene and layered validation |",
            "| Updated npm dependencies in a controlled way, reducing vulnerabilities without changing declared ranges | Dependency maintenance, security hygiene and layered validation |\n| Extracted reusable cancellable file-search and lifecycle boundaries for Toaster and BitBake document handling | Modular TypeScript refactoring, explicit lifecycle ownership and behavior-preserving characterization tests |",
        ),
        (
            "- [#541 — npm: minor version updates](https://github.com/yoctoproject/vscode-bitbake/pull/541)",
            "- [#545 — refactor: extract document lifecycle](https://github.com/yoctoproject/vscode-bitbake/pull/545)\n- [#544 — refactor: extract Toaster lifecycle](https://github.com/yoctoproject/vscode-bitbake/pull/544)\n- [#543 — Extract reusable cancellable file search utility](https://github.com/yoctoproject/vscode-bitbake/pull/543)\n- [#541 — npm: minor version updates](https://github.com/yoctoproject/vscode-bitbake/pull/541)",
        ),
        (
            "| Finite-state stochastic modeling | [Lotto Digit Coverage Dynamics](https://github.com/gcomneno/lotto-digit-coverage-dynamics) | Exact absorbing Markov models, exhaustive kernel verification and historical comparison |",
            "| Finite-state stochastic modeling | [Lotto Digit Coverage Dynamics](https://github.com/gcomneno/lotto-digit-coverage-dynamics) | Exact absorbing Markov models, exhaustive kernel verification, historical signal analysis, versioned application contracts and a local reproducible research GUI |",
        ),
    ],
    "it": [
        (
            "| [Atelier-Kit](https://github.com/gcomneno/atelier-kit) | [v0.4.3](https://github.com/gcomneno/atelier-kit/releases/tag/v0.4.3) | Fornisce un kit vetrina configurabile con authoring locale via Studio, catalogo content-driven e strumenti di pubblicazione | Architettura di prodotto SvelteKit, authoring local-first, distribuzione desktop e adozione downstream reale di componenti Giada UI riutilizzabili |",
            "| [Atelier-Kit](https://github.com/gcomneno/atelier-kit) | [v0.4.3](https://github.com/gcomneno/atelier-kit/releases/tag/v0.4.3) | Fornisce un kit vetrina configurabile con superfici di authoring Studio locali, desktop e hosted a perimetro esplicito, catalogo content-driven e strumenti di pubblicazione | Architettura di prodotto SvelteKit, confini di autorità espliciti tra local/hosted/demo, mutazioni repository atomiche, distribuzione desktop e adozione downstream di Giada UI |",
        ),
        (
            "| [GYTE Study Tools](https://github.com/gcomneno/gyte-study-tools) | Pipeline di contenuti riavviabili, validazione deterministica, confini privato/pubblico e handoff espliciti verso servizi esterni |",
            "| [GYTE Study Tools](https://github.com/gcomneno/gyte-study-tools) | Pipeline di contenuti riavviabili, validazione deterministica, confini privato/pubblico e handoff espliciti verso servizi esterni |\n| [Semantic Mail Archivist](https://github.com/gcomneno/semantic-mail-archivist) | Audit Gmail privacy-first e repair dry-run, confini provider, confidence spiegabile e journal delle mutazioni crash-aware |",
        ),
        (
            "| Aggiornamento controllato delle dipendenze npm, riducendo le vulnerabilità senza modificare i range dichiarati | Dependency maintenance, security hygiene e validazione multilivello |",
            "| Aggiornamento controllato delle dipendenze npm, riducendo le vulnerabilità senza modificare i range dichiarati | Dependency maintenance, security hygiene e validazione multilivello |\n| Estrazione di una ricerca file cancellabile riutilizzabile e di lifecycle dedicati per Toaster e gestione dei documenti BitBake | Refactoring TypeScript modulare, ownership esplicita del lifecycle e characterization test che preservano il comportamento |",
        ),
        (
            "- [#541 — npm: minor version updates](https://github.com/yoctoproject/vscode-bitbake/pull/541)",
            "- [#545 — refactor: extract document lifecycle](https://github.com/yoctoproject/vscode-bitbake/pull/545)\n- [#544 — refactor: extract Toaster lifecycle](https://github.com/yoctoproject/vscode-bitbake/pull/544)\n- [#543 — Extract reusable cancellable file search utility](https://github.com/yoctoproject/vscode-bitbake/pull/543)\n- [#541 — npm: minor version updates](https://github.com/yoctoproject/vscode-bitbake/pull/541)",
        ),
        (
            "| Modellazione stocastica a stati finiti | [Lotto Digit Coverage Dynamics](https://github.com/gcomneno/lotto-digit-coverage-dynamics) | Modelli di Markov assorbenti esatti, verifica esaustiva del kernel e confronto storico |",
            "| Modellazione stocastica a stati finiti | [Lotto Digit Coverage Dynamics](https://github.com/gcomneno/lotto-digit-coverage-dynamics) | Modelli di Markov assorbenti esatti, verifica esaustiva del kernel, analisi dei segnali storici, contratti applicativi versionati e GUI di ricerca locale riproducibile |",
        ),
    ],
}


def build() -> dict[Path, str]:
    originals = {}
    for locale, path in PATHS.items():
        if not path.is_file():
            raise SystemExit(f"Missing {path}")
        originals[locale] = path.read_text(encoding="utf-8")

    updated = {}
    for locale, original in originals.items():
        text = original
        for old, new in REPLACEMENTS[locale]:
            count = text.count(old)
            if count != 1:
                raise SystemExit(
                    f"{PATHS[locale]}: expected one approved source fragment, found {count}"
                )
            text = text.replace(old, new, 1)
        updated[PATHS[locale]] = text
    return updated


def main() -> int:
    updated = build()
    for path, text in updated.items():
        path.write_text(text, encoding="utf-8")
    print("Applied approved curated profile refresh to README.md and README.it.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
