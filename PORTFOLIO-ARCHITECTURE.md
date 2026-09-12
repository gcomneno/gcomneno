# Portfolio Architecture

Status: **Canonical**  
Owner: **gcomneno**  
Baseline inventory: **2026-09-12**

## Purpose

This document defines the portfolio architecture for repositories owned by `gcomneno`.

The account contains software products, infrastructure, learning laboratories, research experiments, upstream contribution working copies, creative work, archives and sandboxes. These repositories are intentionally not treated as peers.

The architecture separates:

```text
profile -> portfolio category -> repository -> lifecycle status
```

The profile repository is the presentation layer. This document is the governance layer.

## Principles

1. Repository count is not itself a quality signal.
2. Every repository has one primary portfolio category.
3. Lifecycle status and portfolio category are separate dimensions.
4. A learning repository must not be presented as production experience.
5. An upstream fork or contribution working copy must not be presented as an original product.
6. Creative work is legitimate portfolio material, but remains separate from the engineering portfolio.
7. Sandboxes and archives may exist without appearing in the public profile.
8. `gcomneno/gcomneno` is the canonical entry point for the public portfolio; it is not a dumping ground for operational state.
9. Changes to visibility, archival state, naming or portfolio promotion should follow an explicit review rather than repository deletion by default.

## Portfolio categories

### 1. Portfolio & Governance
Identity, governance and cross-repository architecture.

### 2. Infrastructure & Tooling
Reusable development infrastructure and operational tooling.

### 3. Products & Utilities
Original software with a concrete user or operational purpose.

### 4. Learning & Education
Courses, study repositories and verification-oriented learning laboratories.

### 5. Research & Experiments
Reproducible technical, mathematical or computational investigations and prototypes.

### 6. OSS Contributions
Forks or working copies whose primary purpose is contribution to an upstream project.

### 7. Creative & Narrative
Narrative, social and other creative work.

### 8. Archive & Sandbox
Historical snapshots, retired repositories and intentionally disposable experimental environments.

## Lifecycle statuses

| Status | Meaning |
| --- | --- |
| `CORE` | Foundational to identity, governance or the principal engineering portfolio. |
| `ACTIVE` | Intentionally maintained or relevant to the current portfolio. This does not imply continuous development. |
| `LAB` | Learning or training repository whose educational status must remain explicit. |
| `ARCHIVE` | Historical or concluded work retained for evidence or reference. |
| `SANDBOX` | Experimental environment that may be reset, replaced or discarded. |
| `CREATIVE` | Creative/narrative work governed outside the engineering portfolio. |

## Portfolio decisions

| Decision | Meaning |
| --- | --- |
| `KEEP` | Keep the repository and its current portfolio role. |
| `PROMOTE` | Increase its visibility in the public profile or selected-project surfaces. |
| `ARCHIVE` | Preserve history but mark the repository as concluded/archived. |
| `REVIEW` | Identity, category, naming, visibility or continued value needs explicit examination. |

No repository is deleted merely because it is not promoted.

# Canonical inventory

The baseline below contains **65 repositories verified through the connected GitHub account on 2026-09-12**.

A separately declared private repository, `gcomneno/job-search-ops`, is recorded after the verified inventory because it was not returned by the connected GitHub inventory at baseline time.

## 1. Portfolio & Governance

| Repository | Status | Visibility | Decision |
| --- | --- | --- | --- |
| `gcomneno` | CORE | public | PROMOTE |
| `.github` | CORE | public | KEEP |
| `giadaware` | CORE | private | KEEP |
| `agent-standards` | CORE | private | KEEP |
| `verifiable-learning-engine` | CORE | private | KEEP |

## 2. Infrastructure & Tooling

| Repository | Status | Visibility | Decision |
| --- | --- | --- | --- |
| `local-dev-infrastructure` | CORE | private | KEEP |
| `oss-toolbox` | ACTIVE | private | KEEP |
| `ubuntu-system-tools` | ACTIVE | public | KEEP |

## 3. Products & Utilities

| Repository | Status | Visibility | Decision |
| --- | --- | --- | --- |
| `smart-file-organizer` | CORE | public | PROMOTE |
| `giadaware-ai` | CORE | public | PROMOTE |
| `giadaware-ui-components` | ACTIVE | public | KEEP |
| `health-vault-cli` | ACTIVE | private | KEEP |
| `big-deal-watcher` | ACTIVE | private | KEEP |
| `grocery-deal-intelligence` | ACTIVE | public | KEEP |
| `semantic-mail-archivist` | ACTIVE | public | KEEP |
| `lele-manager` | ACTIVE | public | KEEP |
| `lele-quizzer` | ACTIVE | public | KEEP |
| `atelier-kit` | ACTIVE | public | PROMOTE |
| `cat-couch-guardian` | ACTIVE | public | KEEP |
| `onion-compressor-framework` | ACTIVE | private | KEEP |

## 4. Learning & Education

| Repository | Status | Visibility | Decision |
| --- | --- | --- | --- |
| `cyse-lab` | LAB | public | KEEP |
| `bug-hunting-lab` | LAB | private | KEEP |
| `build-a-database-lab` | LAB | public | KEEP |
| `build-your-own-redis-lab` | LAB | public | KEEP |
| `linux-container-lab` | LAB | public | KEEP |
| `yocto-qemu-mini-lab` | LAB | public | KEEP |
| `oop-in-c-lab` | LAB | public | KEEP |
| `boardlab` | LAB | public | KEEP |
| `js-lab-didattico` | LAB | public | KEEP |
| `system-design-study` | LAB | public | KEEP |
| `distributed-systems-study` | LAB | public | KEEP |
| `software-architecture-study` | LAB | public | KEEP |
| `physics-study` | LAB | public | KEEP |
| `kleis-corso-sviluppo-software` | LAB | public | KEEP |
| `concorso-inps-assistente-informatico` | LAB | public | KEEP |
| `web` | LAB | public | KEEP |

## 5. Research & Experiments

| Repository | Status | Visibility | Decision |
| --- | --- | --- | --- |
| `digit-probe` | ACTIVE | public | PROMOTE |
| `lotto-digit-coverage-dynamics` | ACTIVE | public | KEEP |
| `system-log-dynamics` | ACTIVE | public | KEEP |
| `petra` | ACTIVE | private | PROMOTE |
| `gyte` | ACTIVE | public | KEEP |
| `gyte-ai-learning-pipeline` | ACTIVE | public | KEEP |
| `midas` | ACTIVE | public | KEEP |
| `turbo-bucketizer` | ACTIVE | public | KEEP |
| `crystal-codec-gcc-v1` | ACTIVE | public | KEEP |
| `huffman-compressor` | ACTIVE | public | KEEP |
| `lasagna-v2` | ACTIVE | public | KEEP |
| `prime-tower-clocks` | ACTIVE | public | KEEP |
| `oeis-probe` | ACTIVE | public | KEEP |
| `integer-structural-search` | ACTIVE | public | KEEP |

## 6. OSS Contributions

These repositories are contribution working copies/forks. Their portfolio value is the accepted upstream work, not ownership of the upstream project.

| Repository | Status | Visibility | Decision |
| --- | --- | --- | --- |
| `rockcraft` | ACTIVE | public | KEEP |
| `craft-parts` | ACTIVE | public | KEEP |
| `snapcraft` | ACTIVE | public | KEEP |
| `craft-cli` | ACTIVE | public | KEEP |
| `vscode-bitbake` | ACTIVE | public | PROMOTE |
| `tree-sitter-bitbake` | ACTIVE | public | KEEP |
| `bmaptool` | ACTIVE | public | KEEP |
| `craft-application` | ARCHIVE | public | KEEP |
| `craft-providers` | ARCHIVE | public | KEEP |

## 7. Creative & Narrative

| Repository | Status | Visibility | Decision |
| --- | --- | --- | --- |
| `archivio-narrativo` | CREATIVE | private | KEEP |
| `ombre-quotidiane` | CREATIVE | private | KEEP |
| `universi-condivisi` | CREATIVE | private | KEEP |
| `club-dell-assurdo` | CREATIVE | private | KEEP |

## 8. Archive & Sandbox

| Repository | Status | Visibility | Decision |
| --- | --- | --- | --- |
| `gcomneno-profile-history-private-20260802` | ARCHIVE | private | KEEP |
| `atelier-kit-demo-sandbox` | SANDBOX | private | KEEP |

`craft-application` and `craft-providers` are lifecycle `ARCHIVE` but remain categorized under **OSS Contributions**, because category and lifecycle are independent dimensions.

## Declared repository not visible to baseline inventory

| Repository | Category | Status | Visibility | Decision |
| --- | --- | --- | --- | --- |
| `job-search-ops` | Infrastructure & Tooling / Personal Operations | ACTIVE | private | KEEP |

This repository must not be included in verified account totals until the GitHub connection returns it.

# Baseline status distribution

For the 65 GitHub-verified repositories:

| Status | Count |
| --- | ---: |
| CORE | 8 |
| ACTIVE | 33 |
| LAB | 16 |
| ARCHIVE | 3 |
| SANDBOX | 1 |
| CREATIVE | 4 |
| **Total** | **65** |

# Presentation policy

The profile README should remain selective. It should emphasize, in order:

1. selected original engineering projects;
2. accepted upstream open-source contributions;
3. selected research;
4. learning in public, explicitly identified as learning;
5. only then supporting or historical material when useful.

The profile SHOULD NOT enumerate every repository merely because it exists.

Private governance, personal operations, private health tooling, creative archives and sandboxes are not automatically candidates for public promotion.

## Presentation alignment gate — 2026-09-12

The English and Italian profile READMEs were checked against the canonical `PROMOTE` decisions.

- `gcomneno` is the profile surface itself.
- `atelier-kit`, `smart-file-organizer`, `giadaware-ai`, `digit-probe` and `vscode-bitbake` are represented in the public profile through selected-project, operational-project, selected-research or open-source sections.
- `petra` remains `PROMOTE` as a portfolio decision but is private, so it is not forced into the public profile.
- Repositories marked `KEEP` may still appear when they strengthen the portfolio narrative; `PROMOTE` is not an exclusivity list.
- English and Italian profile surfaces follow the same presentation structure.

**Gate:** `PUBLIC_PROMOTE_COVERAGE=PASS`.

# Review queue

## Review pass 1 — 2026-09-12

The first `inspect -> classify -> decide` pass produced these decisions without renaming, archiving or changing repository visibility:

| Repository | Classification | Decision | Result |
| --- | --- | --- | --- |
| `web` | Learning & Education / LAB | KEEP | Umbrella web-learning lab with distinct Laravel and PHP sub-labs; generic name alone is not sufficient reason to mutate it. |
| `petra` | Research & Experiments / ACTIVE | PROMOTE | Maintained PETRA runtime with canonical specification, CLI, tests and active replacement roadmap. |
| `crystal-codec-gcc-v1` | Research & Experiments / ACTIVE | KEEP | Explicit conceptual codec prototype with specification, roadmap, examples and tests. |
| `lasagna-v2` | Research & Experiments / ACTIVE | KEEP | Explicit research MVP with CLI, `.lsg2` format, demos, tests and CI/security tooling. |
| `onion-compressor-framework` | Products & Utilities / ACTIVE | KEEP | Verifiable lossless packager/framework with concrete CLI, formats, verification semantics, tests and reproducible benchmarks. |

### Remaining review queue

No repositories remain in the current review queue.

Review means **inspect before mutation**. No rename, visibility change, archive action or deletion follows automatically from this document.

# Governance rule

Future repositories should be created only when they have an explicit answer to all four questions:

1. What primary portfolio category owns this repository?
2. What lifecycle status does it start with?
3. Why is a separate repository preferable to extending an existing one?
4. Should it appear in the public profile now, later, or never?

If those answers are absent, repository creation should default to `REVIEW` rather than silently expanding the portfolio.
