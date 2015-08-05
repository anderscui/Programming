import os
import time

source = [r'C:\temp\byte_of_vim.pdf', r'C:\temp\byte_of_python.pdf']

target_dir = r'C:\backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)

zip_cmd = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zipping...')
print(zip_cmd)

if os.system(zip_cmd) == 0:
    print('Backup succeeded, files are stored in ' + target)
else:
    print('Backup failed :(')

