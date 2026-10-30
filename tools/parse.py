"""Parse the consolidated French text of Loi 94-36 (copy hosted by legislation-securite.tn) into corpus.json."""
import re, json, os, hashlib
H = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(H, '.cache')
raw = open(os.path.join(C, 'loi94.txt'), encoding='utf8').read()
SHA = hashlib.sha256(open(os.path.join(C, 'loi94.pdf'), 'rb').read()).hexdigest()
NL = chr(10)
HDR = re.compile(r'^(Base de données|LA LEGISLATION DU SECTEUR DE LA SECURITE EN TUNISIE|Accès aux lois, décrets et autres textes juridiques consolidés et mis à jour|WWW\.LEGISLATION-SECURITE\.TN)\s*$')
pages = re.split(r'^Page \d+ sur 16\s*$', raw, flags=re.M)
body = []
fnums = set()
for pg in pages:
    ls = [l.strip().replace('', '- ').replace(' ', ' ') for l in pg.split(NL)]
    ls = [l for l in ls if l and not HDR.match(l)]
    cut = None
    for i, l in enumerate(ls):
        m = re.match(r"^(\d{1,2}) (Article\b|Art\. |L[’']|Les?\b|La\b|Loi\b|Le\b)", l)
        if m and i > 0:
            cut = i
            break
    if cut is not None:
        for l in ls[cut:]:
            m = re.match(r'^(\d{1,2}) ', l)
            if m:
                fnums.add(int(m.group(1)))
        ls = ls[:cut]
    body += ls
text = NL.join(body)
text = text[text.index('Article premier'):]
text = text.replace('’', "'")
text = re.sub(r'^- +', '- ', text, flags=re.M)


def dref(m):
    return m.group(1) if int(m.group(2)) in fnums else m.group(0)


text = re.sub(r'([A-Za-zÀ-ÿ\.\);:,»])(\d{1,2})(?=[\s,.;:]|$)', dref, text)
text = re.sub(r'[ \t]+', ' ', text)
text = re.sub(r'^- +', '- ', text, flags=re.M)
heads = list(re.finditer(r'^(Article premier|Art\. (\d+)(?: \((bis|ter|quater|quinquies|sexies|nouveau)\))?)\s+[–-]\s*', text, flags=re.M))
units = {}
for i, m in enumerate(heads):
    end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
    chunk = text[m.end():end].strip()
    num = 1 if m.group(1) == 'Article premier' else int(m.group(2))
    suf = m.group(3) if m.group(3) in ('bis', 'ter', 'quater', 'quinquies', 'sexies') else None
    key = f'art-{num:03d}' + (f'-{suf}' if suf else '')
    keep = []
    for l in chunk.split(NL):
        if re.match(r'^(CHAPITRE [IVX]+ [–-]|TITRE |SECTION )', l):
            break
        keep.append(l)
    chunk = NL.join(keep).strip()
    chunk = re.sub(r'^(?:\(nouveau\) )?(?:[–-] )?(?:Modifié|Ajouté) par la loi n° [\d-]+ du \d+ \w+ \d{4}\s*[–-]\s*', '', chunk)
    paras = []
    for l in chunk.split(NL):
        newp = l.startswith('- ') or not paras
        if paras and not newp and re.search(r'[.;:]$', paras[-1]) and re.match(r'^[A-ZÀ-Ý«(]|^[a-z]\)|^\d+\)', l):
            newp = True
        if newp:
            paras.append(l)
        else:
            paras[-1] += ' ' + l
    title = 'Article premier' if num == 1 else f'Article {num}' + (f' {suf}' if suf else '')
    if key in units:
        raise SystemExit('dup ' + key)
    units[key] = {'label': title, 'kind': 'article', 'text': f'# {title}' + NL + NL.join(paras) + NL}
print(len(units), 'articles; footnotes', sorted(fnums))
LAWS = {
    'loi-1994-36': {'label': 'Loi n° 94-36', 'title': 'Loi n° 94-36 du 24 février 1994, relative à la propriété littéraire et artistique', 'kind': 'law', 'enacted': '1994-02-24', 'published': '1994-02-24', 'url': 'https://www.wipo.int/wipolex/en/legislation/details/3840', 'temporary_until': None, 'restores': None, 'note': None},
    'loi-2009-33': {'label': 'Loi n° 2009-33', 'title': 'Loi n° 2009-33 du 23 juin 2009, modifiant et complétant la loi n° 94-36 relative à la propriété littéraire et artistique', 'kind': 'law', 'enacted': '2009-06-23', 'published': '2009-06-23', 'url': 'https://www.wipo.int/wipolex/en/legislation/details/3841', 'temporary_until': None, 'restores': None, 'note': None},
}
URL = 'https://legislation-securite.tn/wp-content/uploads/sites/5/2023/11/Loi-n°-94-36-du-24-Fevrier-1994-Fr.pdf'
corpus = {
    'country': {'code': 'TN', 'name': 'Tunisia', 'slug': 'tunisia', 'lang': 'fr', 'tz': 'Africa/Tunis', 'future_branch': 'futur',
                'publisher': {'name': 'legislation-securite.tn (consolidated copy of the official text)', 'email': 'legislation-securite@legislation-securite.invalid'},
                'default_in_force_rule': {'text': "Law 94-36 as amended by Law 2009-33 of 23 June 2009. The consolidated copy carries the amending law's date; it does not give the Official Gazette (JORT) publication date of either law.", 'source': URL},
                'licence_note': "Official legislative texts are outside copyright in Tunisia: Law 94-36 of 24 February 1994, article premier, as amended by Law 2009-33: \"La protection au titre du droit d'auteur s'étend aux expressions et ne couvre pas [...] les textes officiels d'ordre législatif, administratif ou judiciaire et leurs traductions officielles.\" The bytes come from a consolidated copy hosted by legislation-securite.tn."},
    'sources': [{'name': 'legislation-securite.tn: Loi n° 94-36 du 24 février 1994 (consolidated text, PDF)', 'url': URL, 'retrieved': '2026-10-30', 'requests': 1,
                 'licence': 'Official text; excluded from copyright by article premier of Law 94-36 as amended', 'notes': 'Third-party consolidated copy of an official text, with amendment footnotes (Law 2009-33). Not an official consolidation.'}],
    'laws': LAWS,
    'acts': [{'slug': 'propriete-litteraire-artistique', 'short': 'Loi 94-36', 'title': 'Loi n° 94-36 du 24 février 1994, relative à la propriété littéraire et artistique (texte consolidé)', 'url': 'https://www.wipo.int/wipolex/en/legislation/details/3840',
              'first_law': None, 'earlier_laws': ['loi-1994-36', 'loi-2009-33'],
              'versions': [{'from': '2009-06-23', 'source_url': URL, 'sha256': SHA, 'units': units, 'credits': {k: ['loi-2009-33'] for k in units},
                            'note': 'Consolidated text as amended by Law 2009-33; oldest version available. The 1994 text as enacted is not in this repository.'}]}],
    'applies': [],
    'decisions': [
        "Tunisia's Constitution of 2022 and its other laws are not included. The only official Arabic copy found (the Official Gazette special issue of 18 August 2022, as a PDF on arp.tn) is a scan in an ornate, fully vowelled typeface that Tesseract 5.4 (Arabic, tessdata_best) read as nonsense, and the arp.tn text-layer PDF found is garbled; iort.gov.tn does not answer from this machine. No OCR output was put in the repository.",
        "The text is a consolidated copy hosted by legislation-securite.tn, with the amendments of Law 2009-33 already applied. It is one version, dated by the amending law (23 June 2009) because the copy does not give the Official Gazette date, and credited to loi-2009-33 as the oldest version available.",
        "Page headers, footers and amendment footnotes of the PDF were removed, footnote reference numbers were removed, and wrapped lines were joined. Repealed articles are kept as units whose text reads 'Abrogé par la loi n° 2009-33'.",
        "Official legislative texts are not protected by copyright in Tunisia (Law 94-36, article premier, as amended), so a third-party copy of this official text may be reused; the host is credited as the source of the bytes.",
    ],
    'ai_use': ['Claude Code (Claude Sonnet 5.5) wrote the extraction code. No model wrote, edited or summarised legal text.'],
}
json.dump(corpus, open(os.path.join(H, 'corpus.json'), 'w', encoding='utf8', newline=NL), ensure_ascii=False, indent=1)
