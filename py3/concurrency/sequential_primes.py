# coding=utf-8
from time import perf_counter
from typing import NamedTuple

from primes import is_prime, NUMBERS


class Result(NamedTuple):
    prime: bool
    elapsed: float


def check(n: int) -> Result:
    t0 = perf_counter()
    prime = is_prime(n)
    return Result(prime, perf_counter() - t0)


def main():
    print(f'checking {len(NUMBERS)} numbers sequentially:')
    t0 = perf_counter()
    for n in NUMBERS:
        prime, elapsed = check(n)
        label = 'P' if prime else ' '
        print(f'{n:16}  {label} {elapsed:9.6f}s')
    elapsed = perf_counter() - t0
    # total time: 28.11s
    print(f'total time: {elapsed:.2f}s')


if __name__ == '__main__':
    main()
