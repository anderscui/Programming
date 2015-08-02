import time


def head(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.strip()


def grep(lines, search):
    for line in lines:
        if search in line:
            yield line

file_name = 'texts.log'
# for l in head(file_name):
#     print(l)

logs = head(file_name)
daylines = grep(logs, 'day')
for l in daylines:
    print(l)
