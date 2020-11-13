# coding=utf-8


def remainder(number, divisor):
    return number % divisor


def print_params(**kwargs):
    # kwargs is a regular dict
    for k, v in kwargs.items():
        print(f'{k} = {v}')


if __name__ == '__main__':
    assert remainder(20, 7) == 6
    assert remainder(20, divisor=7) == 6

    # dict as kwargs
    kwargs = {'number': 20, 'divisor': 7}
    assert remainder(**kwargs) == 6

    # kw args
    print_params(a=1, b=2)
