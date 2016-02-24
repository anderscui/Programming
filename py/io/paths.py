import os

print('current file: ' + __file__)
print('current wd: ' + os.getcwdu())
# print(os.path.abspath(__file__))

# isabs
# isfile
# isdir
# islink
# ismount

# file name
print('base name: ' + os.path.basename(__file__))
print('dir name: ' + os.path.dirname(__file__))

# exists
print('{0} exists? {1}'.format(__file__, os.path.exists(__file__)))
print('{0} exists? {1}'.format(__file__ + 'y', os.path.exists(__file__ + 'y')))

# file size
print('{0} size: {1}'.format(__file__, os.path.getsize(__file__)))

# normalize
print(__file__)
print(os.path.normcase(__file__))

print('./foo/bar.py')
print(os.path.normpath('./foo/bar.py'))

# split
print(os.path.split(__file__))
print(os.path.splitdrive(__file__))
print(os.path.splitext(__file__))
print(os.path.splitext('test.py'))
