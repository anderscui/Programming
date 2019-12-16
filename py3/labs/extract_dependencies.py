# coding=utf-8
import os
import re

RE_IMPORT_STAT = re.compile(r'from\s+([\w.]+)\s+', re.A)

source = '/Users/andersc/github/cvparse/contrib/classifiers/is_std.py'
output_dir = '/Users/andersc/works/py'

cares = {'aleph': '/Users/andersc/github/aleph/aleph',
         'contrib': '/Users/andersc/github/cvparse/contrib'}


files = [source,
         '/Users/andersc/github/aleph/aleph/node.py',
         '/Users/andersc/github/aleph/aleph/mappers/cleaners/__init__.py',
         '/Users/andersc/github/aleph/aleph/mappers/taggers/__init__.py',
         '/Users/andersc/github/aleph/aleph/utils/iterables.py',
         '/Users/andersc/github/cvparse/contrib/classifiers/std_config.py',
         '/Users/andersc/github/cvparse/contrib/exceptions/__init__.py',
         '/Users/andersc/github/cvparse/contrib/utils.py']

found = []


def parse_file(py_file):
    # print('-----', py_file)
    lines = open(py_file).read().splitlines()
    imports = []
    for line in lines:
        if (line.startswith(('from ', 'import ')) and any(w in line for w in cares)) or line.startswith('from .'):
            imports.append(line)
            # print(line)
            parse_import_line(py_file, line)


def parse_import_line(source_file, line):
    # print(line)
    module = RE_IMPORT_STAT.search(line).group(1)
    parts = module.split('.')
    top = parts[0]
    if top in cares:
        root = cares[parts[0]]
        leaf = '/'.join(parts[1:]) + '.py'
        mfile = os.path.join(root, leaf)
        if not os.path.exists(mfile):
            mfile = os.path.join(root, '/'.join(parts[1:]), '__init__.py')
    elif top == '':
        root = os.path.dirname(source_file)
        leaf = '/'.join(parts[1:]) + '.py'
        mfile = os.path.join(root, leaf)
        if not os.path.exists(mfile):
            mfile = os.path.join(root, '/'.join(parts[1:]), '__init__.py')

    if os.path.exists(mfile):
        # print(mfile)
        # found.append(mfile)
        return mfile
    else:
        print('NOT FOUND', mfile)


def parse_file_recur(py_file):
    if py_file in found:
        print(py_file, 'skipped')
        return

    found.append(py_file)
    lines = open(py_file).read().splitlines()
    imports = []
    for line in lines:
        if (line.startswith(('from ', 'import ')) and any(w in line for w in cares)) or line.startswith('from .'):
            # imports.append(line)
            # print(line)
            imports.append(parse_import_line(py_file, line))

    for imp in imports:
        parse_file_recur(imp)


if __name__ == '__main__':
    # parse_file(source)
    parse_file_recur(source)
    # for file in files:
    #     parse_file(file)

    print('-'*100)
    found.sort()
    for f in found:
        print(f)
    print(len(found))
    print(len(set(found)))
