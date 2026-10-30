# How this repository was made (Tunisia)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| legislation-securite.tn: Loi n° 94-36 du 24 février 1994 (consolidated text, PDF) | <https://legislation-securite.tn/wp-content/uploads/sites/5/2023/11/Loi-n°-94-36-du-24-Fevrier-1994-Fr.pdf> | 2026-10-30 | Official text; excluded from copyright by article premier of Law 94-36 as amended |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `propriete-litteraire-artistique` | Loi n° 94-36 du 24 février 1994, relative à la propriété littéraire et artistique (texte consolidé) | 1 | 2009-06-23 to 2009-06-23 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futur`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 2 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (Africa/Tunis) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Law 94-36 as amended by Law 2009-33 of 23 June 2009. The consolidated copy carries the amending law's date; it does not give the Official Gazette (JORT) publication date of either law. https://legislation-securite.tn/wp-content/uploads/sites/5/2023/11/Loi-n°-94-36-du-24-Fevrier-1994-Fr.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `bee61fa140474f0640e8c5b0f5c376ecc706121d55879906c8d766f8a4f1495f` (66796 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Tunisia's Constitution of 2022 and its other laws are not included. The only official Arabic copy found (the Official Gazette special issue of 18 August 2022, as a PDF on arp.tn) is a scan in an ornate, fully vowelled typeface that Tesseract 5.4 (Arabic, tessdata_best) read as nonsense, and the arp.tn text-layer PDF found is garbled. No OCR output was put in the repository.
- The text is a consolidated copy hosted by legislation-securite.tn, with the amendments of Law 2009-33 already applied. It is one version, dated by the amending law (23 June 2009) because the copy does not give the Official Gazette date, and credited to loi-2009-33 as the oldest version available.
- Page headers, footers and amendment footnotes of the PDF were removed, footnote reference numbers were removed, and wrapped lines were joined. Repealed articles are kept as units whose text reads 'Abrogé par la loi n° 2009-33'.
- Official legislative texts are not protected by copyright in Tunisia (Law 94-36, article premier, as amended), so a third-party copy of this official text may be reused; the host is credited as the source of the bytes.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Sonnet 5.5) wrote the extraction code. No model wrote, edited or summarised legal text.
