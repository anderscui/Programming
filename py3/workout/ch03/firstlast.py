# coding=utf-8


# def firstlast(vals: str | tuple | list):
#     if isinstance(vals, str):
#         return vals[0] + vals[-1]
#     elif isinstance(vals, list):
#         return [vals[0], vals[-1]]
#     elif isinstance(vals, tuple):
#         return (vals[0], vals[-1])
#     else:
#         raise TypeError(f'Unsupported type: {type(vals)}')


def firstlast(vals: str | tuple | list):
    # the upper impl can be simplified as:
    if isinstance(vals, (str, tuple, list)):
        return vals[:1] + vals[-1:]
    raise TypeError(f'Unsupported type: {type(vals)}')


if __name__ == '__main__':
    assert firstlast('abc') == 'ac'
    assert firstlast([1, 2, 3]) == [1, 3]
    assert firstlast((1, 2, 3)) == (1, 3)
