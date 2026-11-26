# Structure

Folder names are in French, as the Imprimerie Officielle de la République Tunisienne (IORT) names the texts in the
French edition of the Journal Officiel (JORT). The law text itself is Arabic, the authentic language, with the IORT's
French translation beside it.

| Folder | What it holds |
| --- | --- |
| `constitution/` | The Constitution: the 1959 text as last amended in 2008, then the 2022 text, as successive versions of the same files (`art-001.md`, ..., `preambule.md` with the visas and preamble, `fin.md` with the promulgation); the 2014 Constitution is not on the IORT's page and is not here |
| `codes/<code>/` | A code in the IORT's consolidated French edition, e.g. `codes/code-du-travail/` |
| `lois/<année>/<NNN>-<objet>/` | A law (قانون, including organic and finance laws) as published in the JORT, by year and number, e.g. `lois/2008/019-enseignement-superieur/` |
| `decrets-lois/<année>/<NNN>-<objet>/` | A decree-law (مرسوم), e.g. `decrets-lois/2011/115-liberte-de-la-presse-de-l-imprimerie-et-de-l-edition/` |
| `decrets/<année>/<tranche>/<NNNN>-<objet>/` | A decree (أمر, including government and presidential decrees), by year, thousand (`0000-0999`, `1000-1999`, ...) and number, e.g. `decrets/2009/1000-1999/1062-<objet>/` |

`<objet>` is the subject of the French title (or of the Arabic title when the IORT gives no French), lower case,
without accents, cut at 60 characters. No folder holds more than 1,000 entries.

## Files in a text's folder

| File | What it holds |
| --- | --- |
| `art-001.md`, `art-002.md`, ... | One file per article (فصل) of the Arabic text; `art-012-bis.md` is article 12 bis (مكرر) |
| `preambule.md` | The title, the visas and the enacting formula, up to the first article |
| `fin.md` | The publication order, the place and date, the signature and the footnotes (travaux préparatoires) |
| `texte.md` | The whole text, when it has no numbered articles |
| `fr/...` | The same files for the French translation the IORT publishes with the text |
| `README.md` | Title in both languages, JORT issue, page, dates and source |

Articles are cut where a line starts "الفصل N ـ" / "Article N -" with the next number in order, so the articles an
amending law quotes (`الفصل 12 (جديد)`) stay inside the article that quotes them.

Codes (`codes/<code>/`) keep their earlier layout: one file per article (`art-0112.md`), from the IORT's French
consolidations, one version each.

## Dates

Each version is one commit, dated 12:00 Africa/Tunis (UTC+1) on the day it took effect, which its `In-force:` trailer
repeats; `In-force-basis:` says where that day comes from:

- `law-93-64`: published in the JORT on or after 11 July 1993. Law 93-64 of 5 July 1993, article 2, makes a text
  enforceable five days after the issue is deposited at the seat of the Tunis governorate, the deposit day not
  counted. The deposit day is not on the IORT's page; it is taken to be the issue day, so the date is the issue day
  plus five days, the earliest day the text took effect;
- `publication-clause`: the text says it takes effect from its publication; dated by the JORT issue;
- `jort-publication`: published before Law 93-64 applied; dated by the JORT issue;
- `signature`: no JORT issue given; dated by the day the text was signed.

A text that states a later start date for some of its provisions took effect then; those dates are not read from
the text. The codes keep the dates of their earlier commits (the IORT edition, see REPRODUCE.md). Git cannot store a
date before 1970: such commits are dated 1 January 1970, the real day staying in the trailer. No date in this
repository is the day we downloaded anything.

## Authors

A law, decree-law or decree is the author of its own commit (`Loi n° 2023-1 <loi-2023-1@jort.iort.gov.tn.invalid>`);
the committer is Lexifina. The codes are credited to the IORT, their publisher.
