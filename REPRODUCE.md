# How this repository was made (Tunisia)

This file is written by the build on 2026-11-03, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| legislation-securite.tn: Loi n° 94-36 du 24 février 1994 (consolidated text, PDF) | <https://legislation-securite.tn/wp-content/uploads/sites/5/2023/11/Loi-n°-94-36-du-24-Fevrier-1994-Fr.pdf> | 2026-10-30 | Official text; excluded from copyright by article premier of Law 94-36 as amended |
| Imprimerie Officielle de la République Tunisienne (IORT), codes en vigueur publiés sur legislation.tn, le portail national de l'information juridique | <http://www.legislation.tn/fr/recherche/codes-en-vigueur> | 2026-11-03 | Textes officiels d'ordre législatif: hors du droit d'auteur (loi n° 94-36, art. 1er, modifié par la loi n° 2009-33) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `propriete-litteraire-artistique` | Loi n° 94-36 du 24 février 1994, relative à la propriété littéraire et artistique (texte consolidé) | 1 | 2009-06-23 to 2009-06-23 |
| `code-de-l-arbitrage` | Code de l'arbitrage | 1 | 2019-12-06 to 2019-12-06 |
| `code-des-assurances` | Code des assurances | 1 | 2019-12-06 to 2019-12-06 |
| `code-de-droit-international-prive` | Code de droit international privé | 1 | 2019-12-06 to 2019-12-06 |
| `code-irpp-is` | Code de l'impôt sur le revenu des personnes physiques et de l'impôt sur les sociétés | 1 | 2020-03-31 to 2020-03-31 |
| `code-de-la-nationalite-tunisienne` | Code de la nationalité tunisienne | 1 | 2020-11-12 to 2020-11-12 |
| `code-penal` | Code pénal | 1 | 2021-03-01 to 2021-03-01 |
| `code-de-la-route` | Code de la route | 1 | 2020-03-31 to 2020-03-31 |
| `code-du-statut-personnel` | Code du statut personnel | 1 | 2020-02-28 to 2020-02-28 |
| `code-des-changes-et-du-commerce-exterieur` | Code des changes et du commerce extérieur | 1 | 2019-12-06 to 2019-12-06 |
| `code-de-la-comptabilite-publique` | Code de la comptabilité publique | 1 | 2021-02-28 to 2021-02-28 |
| `code-de-deontologie-medicale` | Code de déontologie médicale | 1 | 2020-02-15 to 2020-02-15 |
| `code-des-droits-d-enregistrement-et-de-timbre` | Code des droits d'enregistrement et de timbre | 1 | 2020-01-10 to 2020-01-10 |
| `code-des-droits-reels` | Code des droits réels | 1 | 2019-12-06 to 2019-12-06 |
| `code-de-la-fiscalite-locale` | Code de la fiscalité locale | 1 | 2020-03-27 to 2020-03-27 |
| `code-des-organismes-de-placement-collectif` | Code des organismes de placement collectif | 1 | 2019-07-15 to 2019-07-15 |
| `code-des-ports-maritimes` | Code des ports maritimes | 1 | 2020-09-27 to 2020-09-27 |
| `code-de-la-poste` | Code de la poste | 1 | 2020-03-27 to 2020-03-27 |
| `code-des-droits-et-procedures-fiscaux` | Code des droits et procédures fiscaux | 1 | 2020-01-10 to 2020-01-10 |
| `code-des-telecommunications` | Code des télécommunications | 1 | 2021-01-09 to 2021-01-09 |
| `code-de-l-amenagement-du-territoire-et-de-l-urbanisme` | Code de l'aménagement du territoire et de l'urbanisme | 1 | 2019-12-06 to 2019-12-06 |

The build made 21 commits:

| Commits | Kind |
| ---: | --- |
| 21 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futur`: laws not yet in force on 2026-11-03.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 2 laws in the record.
- 21 tags.

## Dates

Each commit is dated at noon (Africa/Tunis) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Law 94-36 as amended by Law 2009-33 of 23 June 2009. The consolidated copy carries the amending law's date; it does not give the Official Gazette (JORT) publication date of either law. https://legislation-securite.tn/wp-content/uploads/sites/5/2023/11/Loi-n°-94-36-du-24-Fevrier-1994-Fr.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `9e27760a9947add2b20981cc6c050e2ad7efc2e5c305b47c7ac8f59d38e622e8` (2267775 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `5d719354ea4c62d240c93d2cae446307d81d9e81`, `on.py` `aff48cf1b68d50c7ba8f399ca32261871c301824`.
- Python 3.14.4; git version 2.53.0.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Tunisia's Constitution of 2022 and its other laws are not included. The only official Arabic copy found (the Official Gazette special issue of 18 August 2022, as a PDF on arp.tn) is a scan in an ornate, fully vowelled typeface that Tesseract 5.4 (Arabic, tessdata_best) read as nonsense, and the arp.tn text-layer PDF found is garbled. No OCR output was put in the repository.
- The text is a consolidated copy hosted by legislation-securite.tn, with the amendments of Law 2009-33 already applied. It is one version, dated by the amending law (23 June 2009) because the copy does not give the Official Gazette date, and credited to loi-2009-33 as the oldest version available.
- Page headers, footers and amendment footnotes of the PDF were removed, footnote reference numbers were removed, and wrapped lines were joined. Repealed articles are kept as units whose text reads 'Abrogé par la loi n° 2009-33'.
- Official legislative texts are not protected by copyright in Tunisia (Law 94-36, article premier, as amended), so a third-party copy of this official text may be reused; the host is credited as the source of the bytes.
- Codes: each code in force that legislation.tn published as a consolidated French PDF (the IORT edition) is one current-text version. The source states the edition and the last amending law it takes into account, but not the day that law came into force, so each version is dated by the day the Internet Archive captured the file from the portal and is credited to the publisher; the last amending law is named in the version's note.
- Only the code's own articles are kept, one file per article; the promulgating law or decree printed before a code, headings of books, titles, chapters and sections, page headers, page numbers and footnotes are left out, and so are the editors' bracketed notes naming the law that added, amended or repealed an article. An article the edition prints as repealed keeps only that note.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Sonnet 5.5) wrote the extraction code. No model wrote, edited or summarised legal text.
- Claude Code wrote the parser; it did not write or alter any legal text.
