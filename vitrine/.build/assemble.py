import base64
import glob
import gzip
import hashlib
import pathlib
import sys

parts = sorted(glob.glob('vitrine/.build/part-*.b64'))
print('parts:', parts)
b = ''
for p in parts:
    t = pathlib.Path(p).read_text(encoding='ascii')
    print('part', p, len(t), 'chars')
    b += t
b = b.replace('\r', '').replace('\n', '')
print('total b64 chars', len(b))
raw = gzip.decompress(base64.b64decode(b))
out = pathlib.Path('vitrine/index.html')
out.write_bytes(raw)
print('written bytes', len(raw))
print('sha256', hashlib.sha256(raw).hexdigest())
sys.stdout.flush()
