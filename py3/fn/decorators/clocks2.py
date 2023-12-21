# coding=utf-8
import functools
import time


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0

        name = func.__name__
        arg_list = [repr(arg) for arg in args]
        arg_list.extend(f'{k}={v!r}' for k, v in kwargs.items())
        arg_str = ', '.join(arg_list)
        print(f'[{elapsed:0.8f}] {name}({arg_str}) -> {result!r}')
        return result

    return clocked


@functools.cache
@clock
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


if __name__ == '__main__':
    print(fib(100))
