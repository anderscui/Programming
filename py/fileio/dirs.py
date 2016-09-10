import glob
import os
from os.path import isfile, isdir, join


def get_file_system_objects(path, file_only=False):
    if file_only:
        return [f for f in os.listdir(path) if isfile(join(path, f))]
    else:
        return os.listdir(path)


def get_sub_dirs(path):
    return [f for f in os.listdir(path) if isdir(join(path, f))]


def glob_file_system_objects(path):
    return glob.glob(path)



# for fs in get_file_system_objects('.', file_only=True):
#     print(fs)
#
# print('')
# for fs in get_file_system_objects('.'):
#     print(fs)
#
# print('')
# for fs in get_sub_dirs('.'):
#     print(fs)


# for fs in glob_file_system_objects('./*'):
#     print(fs)
#
# for fs in glob_file_system_objects(r'./test_dir/*'):
#     print(fs)
