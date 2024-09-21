# coding=utf-8
from pathlib import Path, PurePath

from toolz import take

p = Path('../parallels')
assert p.exists()

# yield dir contents, not recursive
# for f in p.iterdir():
#     if f.is_dir():
#         print(f'dir: {f}')
#     if f.is_file():
#         print(f'file: {f}')

# glob files, current and subs
for f in take(10, p.glob('**/*.py')):
    print(f'py file: {f}')

# resolve
q = p / 'seqs' / 'iterators.py'
print(f'q: {q}')  # pathlib.PosixPath
# absolute path
print(q.resolve())
print(f'{type(q)}, {q.exists()}, {q.is_dir()}')

# open a file
with q.open() as f:
    print(f.readline())
