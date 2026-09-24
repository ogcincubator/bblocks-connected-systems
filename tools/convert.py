import json, re, shutil, sys, os, glob
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent / 'ogcapi-connected-systems'
OUT = Path(__file__).resolve().parent.parent / '_sources'
GH = 'https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/'
PREFIX = 'ogc.api.connected-systems.'
TODAY = '2026-09-23T00:00:00Z'
LINK_BLOCK = 'bblocks://ogc.ogc-utils.json-link'
FEATURE = 'bblocks://ogc.geo.features.feature'
FEATURE_COLL = 'bblocks://ogc.geo.features.featureCollection'
GEOJSON_MAP = {
    'https://geojson.org/schema/Feature.json': FEATURE,
    'https://geojson.org/schema/FeatureCollection.json': FEATURE_COLL,
}
MARK = '<!-- generated -->'
ABSTRACTS = json.load(open(Path(__file__).with_name('abstracts.json'))) if Path(__file__).with_name('abstracts.json').exists() else {}
EXCLUDES = json.load(open(Path(__file__).with_name('known_failing_examples.json'))) if Path(__file__).with_name('known_failing_examples.json').exists() else {}
# The blocks are faithful copies of the upstream schemas: known problems are NOT fixed, so that the specification's
# own examples that fail against them show up as failures in the validation report. `--fixed` applies the possible resolutions instead,
# to check that they resolve the failures (it is not always clear whether the schema or the example is at fault).
FIXED = '--fixed' in sys.argv
if FIXED:
    sys.argv.remove('--fixed')
ISSUES = {
    'basicTypes.json': ['`DateTimeNumberOrSpecial` uses `oneOf`: strings such as `NaN`/`Infinity` match both branches unless `format: date-time` is asserted, so valid instances fail. Possible resolution: `anyOf`.'],
    'timeInstantOrNow.json': ['Uses `oneOf`: the string `now` also matches the `date-time` branch unless `format` is asserted, so valid instances fail. Possible resolution: `anyOf`.'],
    'DescribedObject.json': ['`uniqueId` is `required`, but embedded components, modes and inline processes in the specification examples do not have one. Possible resolution: remove it from `required` (or add `uniqueId` to the examples) (top-level systems still require it in the Part 1 system schemas).'],
    'uris.json': ['`ProcedureTypeUris` does not allow `http://www.w3.org/ns/ssn-system/SensorKind`, which the specification\'s own procedure examples use as `featureType`/`definition`. Possible resolution: add it (or change the examples).'],
    'datastream1.json': ['The DataStream example does not validate: the first field of `elementType` has no `name`, which is required. Possible resolution: add `"name": "time"` to the example.'],
}
FAILING = {}   # block schema path -> [(title, example path)] known to fail against the block's schema

def kebab(name):
    name = name.replace('_', '-')
    return re.sub(r'(?<=[a-z0-9])(?=[A-Z])', '-', name).lower()

# --- block registry: absolute source path -> (block dir relative to _sources, group, display suffix)
BLOCKS = {}
ALIASES = {}   # shim files whose $defs are (mostly) aliases
def reg(pattern, base, group, suffix='', skip=(), name_suffix=''):
    for f in sorted(glob.glob(str(REPO / pattern))):
        p = Path(f)
        if p.name in skip:
            continue
        BLOCKS[p] = (f'{base}/{kebab(p.stem)}{suffix}', group, name_suffix)

reg('swecommon/schemas/json/*.json', 'swecommon', 'SWE Common')
reg('sensorml/schemas/json/*.json', 'sensorml', 'SensorML', skip=('commonDefs.json', 'sweCommonDefs.json'))
reg('common/*.json', 'common', 'Common', skip=('xlink.json',))
reg('api/part1/openapi/schemas/geojson/*.json', 'part1', 'Part 1', name_suffix=' (GeoJSON)')
reg('api/part1/openapi/schemas/sensorml/*.json', 'part1', 'Part 1', suffix='-sensorml', skip=('sensormlDefs.json',), name_suffix=' (SensorML)')
reg('api/part1/openapi/schemas/common/*.json', 'part1', 'Part 1', skip=('commonDefs.json',))
reg('api/part2/openapi/schemas/json/*.json', 'part2', 'Part 2')
# swecommon/sweCommon.json keeps its (kebab) name: swe-common
COMMON_DEFS = REPO / 'sensorml/schemas/json/commonDefs.json'
SWE_DEFS = REPO / 'sensorml/schemas/json/sweCommonDefs.json'
BLOCKS[COMMON_DEFS] = ('sensorml/common-defs', 'SensorML', '')
SHIMS = {p for p in REPO.glob('api/part*/openapi/schemas/*/*Defs.json')} | {SWE_DEFS, COMMON_DEFS}
SHIMS -= {REPO / 'api/part1/openapi/schemas/common/uris.json'}
# part1/common/commonDefs.json and both part2 common/*Defs.json are pure alias shims
LINK_FILES = set()

_shim_cache = {}
def shim(p):
    if p not in _shim_cache:
        _shim_cache[p] = json.load(open(p))
    return _shim_cache[p]

def is_alias(d):
    return isinstance(d, dict) and set(d) == {'$ref'}

def fragment_name(frag):
    m = re.match(r'^/\$defs/(\w+)$', frag)
    if not m:
        raise ValueError(f'unsupported fragment {frag}')
    return m.group(1)

def resolve(src, ref, seen=()):
    if ref in GEOJSON_MAP:
        return GEOJSON_MAP[ref]
    if ref.startswith('#') or re.match(r'^https?://', ref):
        return ref
    file, _, frag = ref.partition('#')
    target = (src.parent / file).resolve()
    if target in LINK_FILES:
        return LINK_BLOCK
    if target in SHIMS:
        name = fragment_name(frag)
        d = shim(target)['$defs'][name]
        if is_alias(d):
            return resolve(target, d['$ref'])
        return f'bblocks://{PREFIX}{BLOCKS[COMMON_DEFS][0].replace("/", ".")}#{name}'
    if target not in BLOCKS:
        raise KeyError(f'{src}: unresolved ref {ref} -> {target}')
    bid = PREFIX + BLOCKS[target][0].replace('/', '.')
    return f'bblocks://{bid}' + (f'#{fragment_name(frag)}' if frag else '')

def rewrite(node, src):
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k == '$ref' and isinstance(v, str):
                out[k] = resolve(src, v)
            else:
                out[k] = rewrite(v, src)
        return out
    if isinstance(node, list):
        return [rewrite(x, src) for x in node]
    return node

def add_anchors(schema):
    for k, v in schema.get('$defs', {}).items():
        if isinstance(v, dict):
            v['$anchor'] = k

def source_schema(p):
    s = json.load(open(p))
    if p == COMMON_DEFS:
        for k in ('XLink', 'TimeInstant', 'TimePeriod'):
            s['$defs'].pop(k)
        s['$defs']['AnyConstraint'] = json.load(open(SWE_DEFS))['$defs']['AnyConstraint']
        for k in ('XLink',):
            pass
    return s

def own_properties(schema):
    props, req = {}, set()
    def walk(n):
        if not isinstance(n, dict):
            return
        for k, v in n.get('properties', {}).items():
            if isinstance(v, dict):
                props.setdefault(k, v)
        req.update(n.get('required', []))
        for br in n.get('allOf', []):
            if isinstance(br, dict) and '$ref' not in br:
                walk(br)
    walk(schema)
    return props, req

def prop_type(v):
    if '$ref' in v:
        r = v['$ref']
        return '[' + r.replace('bblocks://' + PREFIX, '') + '](' + r.split('#')[0] + ')' if r.startswith('bblocks://') else f'`{r}`'
    if 'const' in v:
        return f'`{json.dumps(v["const"])}`'
    t = v.get('type')
    if isinstance(t, list):
        t = '/'.join(t)
    return f'`{t}`' if t else ''

def description(p, name, schema, bid, examples):
    props, req = own_properties(schema)
    desc = schema.get('description') or schema.get('title') or ''
    lines = [MARK, f'# {name}', '']
    if desc:
        lines += [desc, '']
    lines += [f'Converted from [`{p.relative_to(REPO)}`]({GH + str(p.relative_to(REPO))}) in the OGC API - Connected Systems repository.', '']
    if schema.get('$defs'):
        lines += ['## Definitions', '', 'The following definitions can be referenced individually using their anchor, e.g. `bblocks://' + PREFIX + bid + '#' + next(iter(schema['$defs'])) + '`:', '']
        for k, v in schema['$defs'].items():
            d = v.get('description', '') if isinstance(v, dict) else ''
            lines.append(f'- `{k}`' + (f': {d}' if d else ''))
        lines.append('')
    if props:
        lines += ['## Properties', '', '| Property | Type | Required | Description |', '|---|---|---|---|']
        for k, v in props.items():
            d = (v.get('description') or '').replace('\n', ' ').replace('|', '\\|')
            lines.append(f'| `{k}` | {prop_type(v)} | {"yes" if k in req else ""} | {d} |')
        lines.append('')
    for fn in (p.name, *[e[1].name for e in examples]):
        pass
    failing = FAILING.get(p, [])
    diffs = ISSUES.get(p.name, []) + [x for _, e in (*examples, *failing) for x in ISSUES.get(e.name, [])]
    if p.name == 'links.json' and 'part1' not in str(p):
        diffs = [x for x in diffs if 'Part 1' not in x]
    if diffs:
        lines += ['## Known issues in the source', '', 'This block is a faithful copy of the upstream file, which has the following mismatches with the examples of the specification (see `SCHEMA-FIXES.md`):', ''] + [f'- {x}' for x in diffs] + ['']
    if failing:
        lines += ['## Known failing examples', '', f'{len(failing)} of the examples taken from the specification do **not** validate against this schema. They are included on purpose, so the validation report shows the problem:', ''] + [f'- `{e.name}`: {EXCLUDES.get(e.name, {}).get("reason", "see above")}' for _, e in failing] + ['']
    if examples:
        lines += ['## Examples', '', f'{len(examples)} example(s) taken from the specification are included and validated against this schema.', '']
    return '\n'.join(lines)

def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write('\n')

def convert(p, examples=(), extra_meta=None):
    bdir, group, name_suffix = BLOCKS[p]
    bid = bdir.replace('/', '.')
    d = OUT / bdir
    shutil.rmtree(d / 'examples', ignore_errors=True)
    (d / 'examples.yaml').unlink(missing_ok=True)
    schema = source_schema(p)
    add_anchors(schema)
    schema = rewrite(schema, p)
    if FIXED and p.name == 'DescribedObject.json':
        schema['required'] = [r for r in schema['required'] if r != 'uniqueId']
    if FIXED and p.name == 'timeInstantOrNow.json':
        schema['anyOf'] = schema.pop('oneOf')  # 'now' also matches date-time when format is not asserted
    if FIXED and p.name == 'uris.json':
        schema['$defs']['ProcedureTypeUris']['enum'].append('http://www.w3.org/ns/ssn-system/SensorKind')
    if FIXED and p.name == 'basicTypes.json':
        # Upstream fix: 'Infinity' strings match both branches when format is not asserted
        dt = schema['$defs']['DateTimeNumberOrSpecial']
        dt['anyOf'] = dt.pop('oneOf')
    write_json(d / 'schema.json', schema)
    stem = p.stem
    name = ('Common Definitions' if p == COMMON_DEFS else stem[0].upper() + stem[1:]) + name_suffix
    abstract = (schema.get('description') or schema.get('title') or f'{name} schema.').split('\n')[0]
    meta = {
        'name': name, 'abstract': abstract, 'status': 'under-development',
        'dateTimeAddition': TODAY, 'itemClass': 'schema', 'version': '0.1', 'group': group,
        'sources': [{'title': f'{p.relative_to(REPO)} in opengeospatial/ogcapi-connected-systems', 'link': GH + str(p.relative_to(REPO))}],
    }
    if bdir in ABSTRACTS:
        meta['abstract'] = ABSTRACTS[bdir]
    if p == COMMON_DEFS:
        meta['abstract'] = 'Definitions shared by SensorML schemas: observable properties, terms, any-property and any-constraint unions, path references and time instant-or-period.'
    if 'allOf' in schema and isinstance(schema['allOf'][0], dict) and schema['allOf'][0].get('$ref', '').startswith('bblocks://') and group == 'Part 1' and name_suffix == ' (GeoJSON)':
        meta['isProfileOf'] = [schema['allOf'][0]['$ref']]
    if extra_meta:
        meta.update(extra_meta)
    write_json(d / 'bblock.json', meta)
    dm = d / 'description.md'
    if not dm.exists() or dm.read_text().startswith(MARK):
        dm.write_text(description(p, name, source_schema(p), bdir.replace('/', '.'), examples) + '\n')
    if examples:
        (d / 'examples').mkdir(exist_ok=True)
        lines = ['examples:']
        for title, src in examples:
            dst = d / 'examples' / src.name
            shutil.copy(src, dst)
            if FIXED and src.name == 'datastream1.json':
                ex_json = json.load(open(src))
                ex_json['elementType']['fields'][0]['name'] = 'time'  # upstream example lacks the required name
                write_json(dst, ex_json)
            lines += [f'  - title: {title}', '    snippets:', '      - language: json', f'        ref: examples/{src.name}']
        (d / 'examples.yaml').write_text('\n'.join(lines) + '\n')
    for old in (d / 'tests').glob('spec-*-fail.json'):
        old.unlink()   # generated by an earlier version of this script
    return bid

def is_failing(f):
    e = EXCLUDES.get(f.name)
    return bool(e) and not (FIXED and e.get('fixed'))

def type_index():
    return {p.stem: p for p in BLOCKS if BLOCKS[p][1] in ('SWE Common', 'SensorML') and p != COMMON_DEFS}

def spec_examples():
    """Map block path -> [(title, example path)] using each example's `type`."""
    idx = type_index()
    out = {}
    pats = ['swecommon/schemas/json/examples/spec/*.json', 'sensorml/schemas/json/examples/spec/*.json', 'sensorml/schemas/json/examples/*.json']
    for pat in pats:
        for f in sorted(glob.glob(str(REPO / pat))):
            f = Path(f)
            try:
                t = json.load(open(f)).get('type')
            except Exception:
                continue
            if isinstance(t, str) and t in idx:
                title = f.stem.replace('_', ' ').replace('-', ' ')
                item = (title[0].upper() + title[1:], f)
                out.setdefault(idx[t], []).append(item)
                if is_failing(f):
                    FAILING.setdefault(idx[t], []).append(item)
    return out

def api_examples():
    def blk(d, name):
        for p, (bdir, *_r) in BLOCKS.items():
            if bdir == f'{d}/{name}':
                return p
        raise KeyError(name)
    out = {}
    def add(d, name, f):
        f = Path(f)
        t = f.stem.replace('_', ' ').replace('-', ' ')
        item = (t[0].upper() + t[1:], f)
        out.setdefault(blk(d, name), []).append(item)
        if is_failing(f):
            FAILING.setdefault(blk(d, name), []).append(item)
    p1 = REPO / 'api/part1/openapi/examples'
    for f in sorted(p1.glob('systems/*.json')):
        if f.name.endswith('.links.json'):
            continue
        add('part1', 'system-sensorml' if f.stem.endswith('-sml') else 'system', f)
    for sub, name in [('deployments', 'deployment'), ('procedures', 'procedure')]:
        for f in sorted(p1.glob(f'{sub}/*.json')):
            add('part1', name + ('-sensorml' if f.stem.endswith('-sml') else ''), f)
    for f in sorted(p1.glob('sampling/*.json')):
        add('part1', 'sampling-feature', f)
    for f in sorted(p1.glob('properties/*.json')):
        add('part1', 'property-sensorml', f)
    p2 = REPO / 'api/part2/openapi/examples'
    for sub, name in [('commandResult', 'command-result'), ('commands', 'command'), ('commandStatus', 'command-status'), ('events', 'system-event'), ('observations', 'observation')]:
        for f in sorted(p2.glob(f'{sub}/*.json')):
            add('part2', name, f)
    for sub, name in [('controlstreams', 'control-stream'), ('datastreams', 'data-stream')]:
        for f in sorted(p2.glob(f'{sub}/*.json')):
            add('part2', name + ('-create' if f.stem.endswith('-create') else ''), f)
    for f in sorted(p2.glob('schemas/*.json')):
        kind = 'command' if f.name.startswith('commandSchema') else 'observation'
        if 'swe' in f.stem:
            add('part2', f'{kind}-schema-swe', f)
        elif f.stem.endswith('-json') or 'imagelink' in f.stem or f.stem.endswith('-vector-json'):
            add('part2', f'{kind}-schema-json', f)
    return out

if __name__ == '__main__':
    only = sys.argv[1:]
    ex = spec_examples()
    ex.update(api_examples())
    for p in BLOCKS:
        if only and not any(o in str(p) for o in only):
            continue
        print('wrote', convert(p, ex.get(p, ())))
