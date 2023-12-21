# coding=utf-8
if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = l1[:]
    print(l1 == l2, l1 is l2)

    t1 = (1, 2, 3)
    t2 = t1[:]
    t3 = tuple(t1)
    print(t1 == t2, t1 is t2, t1 is t3)

    # check also str, bytes, frozenset
    # they are `immutables`
