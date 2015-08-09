import sys


def fprintf(file, fmt, *args):
    file.write(fmt % args)


fprintf(sys.stdout, '%d %s %f', 42, 'hello', 3.45)
print('')


##

def add(a, b, *more):
    result = a + b
    for num in more:
        result += num

    return result

print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))
