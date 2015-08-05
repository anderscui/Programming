import os
import time

source = [r'C:\temp\byte_of_vim.pdf', r'C:\temp\byte_of_python.pdf']

target_dir = r'C:\backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_cmd = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zipping...')
print(zip_cmd)

if os.system(zip_cmd) == 0:
    print('Backup succeeded, files are stored in ' + target)
else:
    print('Backup failed :(')

