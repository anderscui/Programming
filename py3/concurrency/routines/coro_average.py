# coding=utf-8
from collections.abc import Generator
from typing import Union, NamedTuple, TypeAlias


# two versions of coroutine


def averager() -> Generator[float, float, None]:
    total = 0.0
    n = 0
    avg = 0.0
    while True:
        term = yield avg
        total += term
        n += 1
        avg = total / n


class Result(NamedTuple):
    n: int
    average: float


class Sentinel:
    def __repr__(self):
        return f'<Sentinel>'


STOP = Sentinel()

SendType: TypeAlias = float | Sentinel


def averager2(verbose: bool = False) -> Generator[None, SendType, Result]:
    """Dont' return value, so `None`"""
    total = 0.0
    n = 0
    avg = 0.0
    while True:
        # yield None, but receive data
        term = yield
        if verbose:
            print(f'received: {term}')
        if isinstance(term, Sentinel):
            break
        total += term
        n += 1
        avg = total / n
    return Result(n, avg)


def compute():
    res = yield from averager2()
    print(f'computed: {res}')
    return res


if __name__ == '__main__':
    coro_avg = averager()
    print(coro_avg.send(None))  # or next(coro_avg) to start the coro
    for val in (10, 30, 5):
        print(coro_avg.send(val))
    coro_avg.close()

    coro_avg2 = averager2(False)
    next(coro_avg2)
    for val in (10, 30, 6.5):
        print(coro_avg2.send(val), end=' ')
    print(coro_avg2.close())  # no result after GeneratorExit

    coro_avg2 = averager2(False)
    next(coro_avg2)
    for val in (10, 30, 6.5):
        coro_avg2.send(val)
    try:
        coro_avg2.send(STOP)
    except StopIteration as e:
        # result is wrapped in an exception
        result = e.value
        print(result)

    # can be used in yield from
    comp = compute()
    for val in (None, 10, 20, 30, STOP):
        try:
            comp.send(val)
        except StopIteration as e:
            result = e.value
            print(result)
