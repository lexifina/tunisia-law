# Tunisia: law history in git

The law of Tunisia as a git history: one file per article, one commit per law on the day it took effect, and the law (or the publisher) behind each change as the commit's author. `git blame` names the source of every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**Language.** French, one of the two languages in which Tunisian laws circulate. The official Arabic text is not in this repository.

## What it holds

| Folder | Text | Versions |
| --- | --- | ---: |
| `propriete-litteraire-artistique/` | Loi n° 94-36 du 24 février 1994, relative à la propriété littéraire et artistique, as amended by Law 2009-33 | 1 |
| one folder per code (`code-penal/`, `code-du-statut-personnel/`, ...) | The codes in force published by the Imprimerie Officielle de la République Tunisienne (IORT) on legislation.tn, the national legal information portal, in their consolidated French editions | 1 each |
| `code-de-l-aeronautique-civile/` | Code de l'aéronautique civile, IORT edition revised and corrected 19 January 2018; latest code amendment identified there is Law 2009-25 | 1 |

**Current text, not yet a history.** Each code is one version: the consolidated text as the IORT edition gives it. The aviation code's latest identified amendment, Law 2009-25, appears in JORT no. 38 of 12 May 2009, p. 1270. That issue records deposit in Tunis on 13 May. Law 93-64, Article 2 (JORT no. 50 of 6 July 1993, p. 931), makes texts executable five days after deposit, excluding the deposit day, unless an express exception applies. Law 2009-25 states no exception, so the aviation version's In-force date is **18 May 2009**. The 19 January 2018 date is an editorial revision date only. The other codes use their recorded retrieval dates. Each is credited to the publisher and its commit message names the source edition. Earlier wordings are not rebuilt yet; they can be added later as separate, labelled commits.

Only each code's own articles are kept, one file per article. The promulgating law or decree printed before a code, the headings of books, titles, chapters and sections, page headers, page numbers and footnotes are left out, and so are the editors' notes in brackets that name the law which added, amended or repealed an article. Where the edition prints an article only as repealed, that note is kept as the article's text. The separate decrees printed after the aviation code under "ANNEXES" are not part of that code entry.

## Dates

Each commit is dated at noon, Africa/Tunis, on the day the version applies from; the day is in the `In-force:` trailer.

## Source and licence

Sources: the IORT codes from [legislation.tn](http://www.legislation.tn/fr/recherche/codes-en-vigueur); Law 94-36 from a consolidated copy hosted by [legislation-securite.tn](https://legislation-securite.tn/). Official legislative texts are outside copyright in Tunisia (Law 94-36, article premier). See [`LICENSE`](LICENSE). For anything that matters, read the Official Gazette (JORT).
