# coding=utf-8


def swap_without_helper_vars(a: int, b: int):
    raw_a, raw_b = a, b
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(raw_a, raw_b, a, b)
    assert raw_a == b and raw_b == a


def swap_without_helper_vars2(a: int, b: int):
    raw_a, raw_b = a, b
    a, b = b, a  # ROT_TWO op
    print(raw_a, raw_b, a, b)
    assert raw_a == b and raw_b == a


if __name__ == '__main__':
    swap_without_helper_vars(1, 1002)
    swap_without_helper_vars(1, -1002)
    swap_without_helper_vars2(1, -1002)
