# coding=utf-8
import os
from concurrent import futures

from parallels.good_futures.flags import save_flag, get_flag, show, main

MAX_WORKERS = 20


def download_one(cc):
    """each thread will execute"""
    img = get_flag(cc)
    show(cc)
    save_flag(img, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))


# def download_many_proc(cc_list):
#     with futures.ProcessPoolExecutor() as executor:
#         res = executor.map(download_one, sorted(cc_list))
#
#     return len(list(res))


if __name__ == '__main__':
    print(os.cpu_count())
    # main(download_many_proc)
    main(download_many)
