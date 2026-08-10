import json, os, re, datetime

SNAP = "2026-08-10"
NOW = datetime.datetime(2026, 8, 10, tzinfo=datetime.timezone.utc)
OUT = "/srv/ofdata/ministry/content/records"

WIN_NYC = {'daily': 3, 'weekly': 10, 'monthly': 45, 'quarterly': 110,
           'every 6 months': 200, 'annually': 400, 'biannually': 800,
           'semi-annually': 200, 'every 2 weeks': 17}
WIN_LOM = {'giornaliera': 3, 'tempestiva': 3, 'settimanale': 10, 'mensile': 45,
           'trimestrale': 110, 'semestrale': 200, 'annuale': 400,
           'biennale': 800, 'quotidiana': 3}


def ts(s):
    try:
        return datetime.datetime.fromisoformat(str(s).replace('Z', '+00:00'))
    except Exception:
        return None


def slug(s, i):
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:60].strip('-')
    return (s or 'dataset') + '-' + i


def q(s):
    return '"' + str(s).replace('\\', '\\\\').replace('"', '\\"') + '"'


PORTALS = {
    'nyc': dict(name="NYC Open Data", ref="/evaluations/nyc-open-data/",
                place="New York City", cat='nyc.json', probe='probe_nyc.json',
                cols='p3_nyc.json', sample='sample_nyc.json', win=WIN_NYC,
                host='data.cityofnewyork.us', fkey='update-frequency'),
    'lom': dict(name="Open Data Regione Lombardia", ref="/evaluations/dati-lombardia/",
                place="Lombardia", cat='lom.json', probe='probe_lom.json',
                cols='p3_lom.json', sample='sample_lom.json', win=WIN_LOM,
                host='www.dati.lombardia.it', fkey='frequenza'),
}

os.makedirs(OUT, exist_ok=True)
made = 0
summary = []

for tag, P in PORTALS.items():
    meta = {x['resource']['id']: x for x in json.load(open(P['cat']))}
    probe = {r['id']: r for r in json.load(open(P['probe']))}
    coldet = {r['id']: r for r in json.load(open(P['cols']))}

    for rec in json.load(open(P['sample']))[:60]:
        did = rec['id']
        pr = probe.get(did) or {}
        cd = coldet.get(did) or {}
        m = meta.get(did) or {}
        res = m.get('resource') or {}

        freq = ''
        for item in (m.get('classification') or {}).get('domain_metadata') or []:
            k = item.get('key', '').lower()
            if P['fkey'] in k and 'automation' not in k and 'ultima' not in k \
               and ('frequen' in k or 'frequenza' in k):
                freq = (item.get('value') or '').strip()

        t = ts(res.get('data_updated_at'))
        age = (NOW - t).days if t else -1
        win = P['win'].get(freq.lower())
        kept = 'na' if win is None else ('yes' if 0 <= age <= win else 'no')

        cols = cd.get('cols') or []
        http = pr.get('http')
        rows = pr.get('rows') or 0
        n_empty = sum(1 for c in cols if c['empty'] >= 1.0)
        n_mis = sum(1 for c in cols if c.get('mistyped'))
        n_doc = sum(1 for c in cols if c.get('doc'))
        lic = (m.get('metadata') or {}).get('license') or ''

        # Condition reflects defects in THIS dataset. Licensing is a portal-wide
        # property here and belongs in the portal evaluation, not on every record.
        if http != 200 or rows == 0:
            cond = 'broken'
        elif n_empty > 0 or kept == 'no' or (pr.get('dup_rows') or 0) > 0:
            cond = 'attention'
        else:
            cond = 'serviceable'

        src = "https://" + P['host'] + "/d/" + did
        fm = ['---',
              'title: ' + q(rec['name']),
              'date: ' + SNAP,
              'snapshot: ' + SNAP,
              'portal: ' + q(P['name']),
              'portal_ref: ' + q(P['ref']),
              'place: ' + q(P['place']),
              'dataset_id: ' + q(did),
              'source: ' + q(src),
              'category: ' + q(rec.get('cat') or ''),
              'license: ' + q(lic),
              'declared_cadence: ' + q(freq),
              'last_update: ' + (t.strftime('%Y-%m-%d') if t else '""'),
              'age_days: ' + str(age),
              'cadence_kept: ' + q(kept),
              'condition: ' + q(cond),
              'measured:',
              '  http: ' + str(http if http is not None else -1),
              '  secs: ' + str(pr.get('secs', 0)),
              '  rows: ' + str(rows),
              '  columns: ' + str(len(cols)),
              '  null_mean: ' + str(pr.get('null_mean', 0)),
              '  cols_empty: ' + str(n_empty),
              '  cols_mistyped: ' + str(n_mis),
              '  cols_documented: ' + str(n_doc),
              '  dup_rows: ' + str(pr.get('dup_rows', 0))]

        if cols:
            fm.append('columns:')
            for c in cols:
                fm.append('  - f: ' + q(c['f']))
                fm.append('    type: ' + q(c.get('type') or ''))
                fm.append('    empty: ' + str(c['empty']))
                fm.append('    uniq: ' + str(c['uniq']))
                fm.append('    doc: ' + ('true' if c.get('doc') else 'false'))
                if c.get('mistyped'):
                    fm.append('    mistyped: true')
        fm.append('---')

        open(os.path.join(OUT, slug(rec['name'], did) + '.md'), 'w').write("\n".join(fm) + "\n")
        made += 1
        summary.append(cond)

print("records written:", made)
import collections
print(dict(collections.Counter(summary)))
