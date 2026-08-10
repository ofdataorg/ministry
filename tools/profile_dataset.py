import json, csv, io, sys, time, re, os, urllib.request, urllib.error, collections

csv.field_size_limit(1 << 30)   # geometry blobs blow past the 128K default

NUMRE = re.compile(r'^-?[\d.,]+$')
DATERE = re.compile(r'^\d{4}-\d{2}-\d{2}')

def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers={'User-Agent': 'ministry-of-data/1.0 (dataset audit)'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()

def profile(rec):
    url = f"https://{rec['host']}/resource/{rec['id']}.csv?$limit=200"
    out = {'id': rec['id'], 'name': rec['name'], 'cat': rec['cat'],
           'cols_meta': rec['cols_meta'], 'updated': rec['updated'], 'license': rec['license']}
    t0 = time.time()
    for attempt in range(3):
        try:
            code, body = fetch(url)
            out['http'] = code
            break
        except urllib.error.HTTPError as e:
            out['http'] = e.code
            if e.code in (429, 503) and attempt < 2:
                time.sleep(5 * (attempt + 1)); continue
            body = b''; break
        except Exception as e:
            if attempt < 2: time.sleep(3); continue
            out['http'] = -1; out['err'] = type(e).__name__; body = b''
    out['secs'] = round(time.time() - t0, 2)
    out['bytes'] = len(body)
    if out.get('http') != 200 or not body:
        return out
    try:
        txt = body.decode('utf-8-sig')
    except UnicodeDecodeError:
        out['nonutf8'] = True
        txt = body.decode('latin-1')
    try:
        rows = list(csv.DictReader(io.StringIO(txt)))
    except Exception as e:
        out['parse_error'] = type(e).__name__
        return out
    out['rows'] = len(rows)
    if not rows:
        out['empty'] = True
        return out
    cols = [c for c in rows[0].keys() if c is not None]
    out['cols'] = len(cols)
    allempty = numastext = single = dupname = 0
    nulls = []
    for c in cols:
        vals = [(r.get(c) or '').strip() for r in rows]
        filled = [v for v in vals if v != '']
        nulls.append(1 - len(filled) / len(vals))
        if not filled:
            allempty += 1; continue
        uniq = len(set(filled))
        if uniq == 1 and len(filled) == len(vals): single += 1
        if sum(1 for v in filled if NUMRE.match(v)) == len(filled) and uniq > 2:
            numastext += 1
    out['null_mean'] = round(sum(nulls) / len(nulls), 4)
    out['cols_allempty'] = allempty
    out['cols_single'] = single
    out['cols_numlike'] = numastext
    out['cols_upper'] = sum(1 for c in cols if c != c.lower())
    out['dup_rows'] = len(rows) - len({tuple(sorted(r.items(), key=lambda kv: str(kv[0]))) for r in rows})
    return out

recs = json.load(open(sys.argv[1]))
res = json.load(open(sys.argv[2])) if os.path.exists(sys.argv[2]) else []
done = {r['id'] for r in res}
recs = [r for r in recs if r['id'] not in done]
print(f"  resuming: {len(done)} done, {len(recs)} to go", flush=True)
for i, rec in enumerate(recs):
    try:
        res.append(profile(rec))
    except Exception as e:
        res.append({'id': rec['id'], 'name': rec['name'], 'cat': rec['cat'],
                    'cols_meta': rec['cols_meta'], 'updated': rec['updated'],
                    'license': rec['license'], 'http': -1, 'err': type(e).__name__})
    if (i + 1) % 25 == 0:
        print(f"  {i+1}/{len(recs)}", flush=True)
        json.dump(res, open(sys.argv[2], 'w'))
    time.sleep(0.35)
json.dump(res, open(sys.argv[2], 'w'))
print(f"done {sys.argv[2]}: {len(res)}")
