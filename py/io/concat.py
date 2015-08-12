#!/usr/bin/env python
# encoding=utf-8
import os
import sys
import getopt
import xerox


def usage():
    print('please use the correct options')
    print('concat.py -s, -u\' -b(')
    print('-s: separator; -u: surroud with; -b: begin/end')


try:
    opts, args = getopt.getopt(sys.argv[1:], "hs:u:b:", ["help", "sep=", "sur=", "begin="])
except getopt.GetoptError as err:
    print str(err)
    usage()
    sys.exit(2)

separator = ","
surround = ""
begin = ""
end = ""

for o, a in opts:
    if o in ("-s", "--sep"):
        separator = a
    elif o in ("-u", "--sur"):
        surround = a
    elif o in ("-b", "--begin"):
        begin = a
        if begin:
            if begin == "(":
                end = ")"
            elif begin == "[":
                end = "]"
            elif begin == "{":
                end = "}"
    elif o in ("-h", "--help"):
        usage()
        sys.exit()
    else:
        assert False, "unknown option"

# print(separator)
# print(surroud)
# print(begin)
# print(end)

# print('args: ', args)

lines = []
if args:
    file_name = args[0]
    with open(file_name) as f:
        for l in f:
            if l:
                lines.append(surround + l.strip() + surround)
else:
    to_copy = xerox.paste().split(os.linesep)
    for l in to_copy:
        # print(l)
        if l:
            lines.append(surround + l.strip() + surround)

print(lines)
print begin + separator.join(lines) + end

if __name__ == '__main__':
    pass
