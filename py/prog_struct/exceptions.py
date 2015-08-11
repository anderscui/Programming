import sys


def sys_ex_hook(extype, val, tb):
    print('Oops, some error occurred...')

    print(extype)
    print(val)

sys.excepthook = sys_ex_hook

print(5 / 0)

try:
    f = open('foo')
except IOError as e:
    print e