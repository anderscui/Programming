# coding=utf-8
import functools
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


class clock:
    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*_args, **kwargs):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0

            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)

            # allow any local var to be referenced int the fmt.
            print(self.fmt.format(**locals()))

            return _result
        return clocked


# @clock('{name}: {elapsed}s')
@clock('{name}({args}) dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)


if __name__ == '__main__':
    for i in range(3):
        snooze(.123)
