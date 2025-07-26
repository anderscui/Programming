# coding=utf-8
import os
from pathlib import Path, PurePath

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # resolve: Make the path absolute, resolving all symlinks on the way and also normalizing it.
# BASE_DIR2 = Path(__file__).resolve().parent.parent

print('current working dir:', Path.cwd())
for p in Path.cwd().iterdir():
    print(p.parent, p.stem, p.suffix)

my_dir = Path.cwd()
new_file = my_dir / 'new_file.txt'
print('new file:', new_file, 'exists? ', new_file.exists())

# absolute vs. relative
print(Path('..').absolute())
print(Path('..').resolve())

# tilda and expanding user
print(Path('~/.zshrc').resolve())
print(Path('~/.zshrc').expanduser().resolve())
print(Path('./.zshrc').expanduser().resolve())

# home
p = Path.home() / '.zshrc'
print(p.name, p.exists())

# globs
base_dir = Path.cwd().parent.resolve()
print(base_dir)
for p in base_dir.rglob('*small*.json', case_sensitive=False):
    print(p)
    break

# open files
with p.open() as f:
    print(f.read())

# use open func
with open(p) as f:
    print(f.read())

# dirs
p = Path('temp_dir')
p.mkdir(parents=True, exist_ok=True)

# for non-empty dirs, use shutil module
p.rmdir()

# files
p = Path('temp_file.txt')
p.touch()
p = p.rename('temp_file.md')
p = p.replace('temp_file2.md')

# delete files
p.unlink()
