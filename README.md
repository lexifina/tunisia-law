# Tunisia: law history in git

The law of Tunisia as a git history: one file per article, one commit per law on the day it took effect, and the law (or the publisher) behind each change as the commit's author. `git blame` names the source of every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**Language.** French, one of the two languages in which Tunisian laws circulate. The official Arabic text is not in this repository.

## What it holds

| Folder | Text | Versions |
| --- | --- | ---: |
| `propriete-litteraire-artistique/` | Loi n° 94-36 du 24 février 1994, relative à la propriété littéraire et artistique, as amended by Law 2009-33 | 1 |
| one folder per code (`code-penal/`, `code-du-statut-personnel/`, ...) | The codes in force published by the Imprimerie Officielle de la République Tunisienne (IORT) on legislation.tn, the national legal information portal, in their consolidated French editions | 1 each |

**Current text, not yet a history.** Each code is one version: the consolidated text as the IORT edition gives it. The editions state which amending law they take into account, but not the day that law came into force, so each code is dated by the day its text was retrieved from the portal and credited to the publisher; the commit message names the source edition. Earlier wordings are not rebuilt yet; they can be added later as separate, labelled commits. A code whose edition could not be split into articles reliably is not here yet.

Only each code's own articles are kept, one file per article. The promulgating law or decree printed before a code, the headings of books, titles, chapters and sections, page headers, page numbers and footnotes are left out, and so are the editors' notes in brackets that name the law which added, amended or repealed an article. Where the edition prints an article only as repealed, that note is kept as the article's text.

## Dates

Each commit is dated at noon, Africa/Tunis, on the day the version applies from; the day is in the `In-force:` trailer.

## Source and licence

Sources: the IORT codes from [legislation.tn](http://www.legislation.tn/fr/recherche/codes-en-vigueur); Law 94-36 from a consolidated copy hosted by [legislation-securite.tn](https://legislation-securite.tn/). Official legislative texts are outside copyright in Tunisia (Law 94-36, article premier). See [`LICENSE`](LICENSE). For anything that matters, read the Official Gazette (JORT).
