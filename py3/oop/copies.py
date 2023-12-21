# coding=utf-8
from copy import deepcopy

if __name__ == '__main__':
    a = [10, 20]
    b = [a, 30]
    a.append(b)
    print(a)
    print(a[2][0][2][0][2][0][0])

    c = deepcopy(a)
    print(c)
    # RecursionError: maximum recursion depth exceeded in comparison
    print(c == a)
