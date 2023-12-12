# coding=utf-8
import os
from concurrent import futures

from parallels.good_futures.flags import save_flag, get_flag, main

MAX_WORKERS = 20


def download_one(cc):
    """each thread will execute"""
    img = get_flag(cc)
    save_flag(img, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


def download_many(cc_list):
    with futures.ThreadPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))

    # <generator object Executor.map.<locals>.result_iterator>
    res = list(res)
    print()
    print(res)
    return len(res)


if __name__ == '__main__':
    print(os.cpu_count())
    # main(download_many_proc)
    main(download_many)
