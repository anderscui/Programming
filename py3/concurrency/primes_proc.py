# coding=utf-8
import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues

from primes import is_prime, NUMBERS


class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float


JobQueue = queues.SimpleQueue[int]
ResultQueue = queues.SimpleQueue[PrimeResult]


def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    prime = is_prime(n)
    return PrimeResult(n, prime, perf_counter() - t0)


def worker(jobs: JobQueue, results: ResultQueue):
    while n := jobs.get():
        results.put(check(n))
    results.put(PrimeResult(0, False, 0.0))


def start_jobs(procs: int, jobs: JobQueue, results: ResultQueue):
    for n in NUMBERS:
        jobs.put(n)
    for _ in range(procs):
        proc = Process(target=worker, args=(jobs, results))
        proc.start()
        jobs.put(0)


def report(procs: int, results: ResultQueue):
    checked = 0
    procs_done = 0
    while procs_done < procs:
        n, prime, elapsed = results.get()
        if n == 0:
            procs_done += 1
        else:
            checked += 1
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')
    return checked


def main():
    n_procs = cpu_count()
    print(f'use {n_procs} processes.')
    print(f'checking {len(NUMBERS)} numbers sequentially:')

    t0 = perf_counter()
    jobs = SimpleQueue()
    results = SimpleQueue()
    start_jobs(n_procs, jobs, results)
    checked = report(n_procs, results)
    elapsed = perf_counter() - t0
    # total time: 6.54s
    print(f'{checked} checks in {elapsed:.2f}s')


if __name__ == '__main__':
    main()
