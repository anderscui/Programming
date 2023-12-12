# coding=utf-8
with open('files.py') as fp:
    src = fp.read(1000)

print(len(src))
print(fp)
print(fp.closed, fp.encoding)
# ValueError: I/O operation on closed file.
print(fp.read(10))
