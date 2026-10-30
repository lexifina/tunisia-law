# Tunisia: law history in git

The law of Tunisia as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `propriete-litteraire-artistique/` | Loi n° 94-36 du 24 février 1994, relative à la propriété littéraire et artistique (the Copyright Act), consolidated text, articles 1 to 59 | 1 | One version: the text as amended by Law 2009-33 of 23 June 2009 (the oldest version available; the 1994 text as enacted is not here) |

**Language.** French, one of the two languages in which Tunisian laws circulate (the official Arabic text is not in this repository). This text is in French; no English text is held.

**Source.** [legislation-securite.tn](https://legislation-securite.tn/): *Loi n° 94-36 du 24 février 1994, relative à la propriété littéraire et artistique*, a consolidated French copy that applies the amendments of Law 2009-33 (PDF, 16 pages, text layer). It is a third-party copy of an official text, not an official consolidation; Lexifina credits the host as the source of the bytes. Retrieved 30 October 2026.

**This repository holds a law's text only for the Copyright Act. It does not hold Tunisia's Constitution or any other law, because the official copies could not be read:** the Constitution of 2022 (Official Gazette special issue of 18 August 2022, published on arp.tn) is a scan in an ornate, fully vowelled Arabic typeface that OCR (Tesseract 5.4) read as nonsense, the Official Gazette's own site (iort.gov.tn) does not answer from the machine that built this, and the next step is a clean Arabic or French text from an official source.

## Dates

The single version is dated 23 June 2009, the date of the amending law that produced the consolidated text; the source does not give the Official Gazette (JORT) date of either law. The commit is credited to Law 2009-33 as the oldest version available. Law 94-36 itself (24 February 1994) is named as an earlier law.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`<law key>@legislation-securite.tn.invalid`). The single version is credited to Law 2009-33. The committer is always Lexifina.

## Limits

One law, one version. Footnote reference numbers, page headers and footers, and the amendment footnotes of the PDF were removed; repealed articles are kept as units reading 'Abrogé par la loi n° 2009-33'. The consolidation is unofficial: for anything that matters, read the Official Gazette (JORT).
