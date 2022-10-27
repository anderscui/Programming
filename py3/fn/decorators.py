# coding=utf-8
import time
from functools import lru_cache


def cached(func):
    _cache = {}

    def decorated(*args):
        start_time = time.time()
        print('_cache: ', _cache)
        if args not in _cache:
            _cache[args] = func(*args)
        print('Compute time: %ss' % round(time.time() - start_time, 2))
        return _cache[args]

    return decorated


@cached
def complex_computation(x, y):
    print('processing...')
    time.sleep(1)
    return x + y


@lru_cache()
def complex_computation2(x, y):
    print('processing...')
    time.sleep(1)
    return x + y


if __name__ == '__main__':
    print(complex_computation(1, 2))
    print(complex_computation(1, 2))

    print(complex_computation2(1, 2))
    print(complex_computation2(1, 2))
