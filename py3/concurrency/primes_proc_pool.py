# coding=utf-8
from time import perf_counter
from typing import NamedTuple
from concurrent.futures import ProcessPoolExecutor

from primes import is_prime, NUMBERS


class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float


def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    prime = is_prime(n)
    return PrimeResult(n, prime, perf_counter() - t0)


def main():
    # n_procs = cpu_count()
    n_procs = None
    executor = ProcessPoolExecutor(max_workers=n_procs)
    actual_workers = executor._max_workers
    print(f'checking {len(NUMBERS)} numbers with {actual_workers} processes:')

    t0 = perf_counter()
    numbers = sorted(NUMBERS, reverse=True)
    with executor:
        for n, prime, elapsed in executor.map(check, numbers):
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')

    elapsed = perf_counter() - t0
    # total time: 6.54s
    print(f'{len(numbers)} checks in {elapsed:.2f}s')


if __name__ == '__main__':
    main()
