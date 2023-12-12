# coding=utf-8
from concurrent import futures

from flags import save_flag, get_flag, main


def download_one(cc):
    """each thread will execute"""
    img = get_flag(cc)
    save_flag(img, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


def download_many(cc_list):
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            # schedules the callable to be executed, and returns a future.
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f'Scheduled for {cc}: {future}')

        results = []
        for count, future in enumerate(futures.as_completed(to_do), 1):
            res = future.result()
            print(f'{future} result: {res!r}')
            results.append(res)
        print(results)

    return count


if __name__ == '__main__':
    main(download_many)
