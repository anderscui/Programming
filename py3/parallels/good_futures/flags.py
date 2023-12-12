# coding=utf-8
import time
from pathlib import Path
from typing import Callable

import aiofiles
import httpx

POP20_CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split()

BASE_URL = 'https://www.fluentpython.com/data/flags'
DEST_DIR = Path('downloaded')


async def save_flag_async(img: bytes, filename: str):
    async with aiofiles.open(DEST_DIR / filename, 'wb') as f:
        await f.write(img)


def save_flag(img: bytes, filename: str):
    (DEST_DIR / filename).write_bytes(img)


def get_flag(cc):
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url, timeout=6.1, follow_redirects=True)
    resp.raise_for_status()
    return resp.content


def download_many(cc_list: list[str]):
    for cc in sorted(cc_list):
        img = get_flag(cc)
        save_flag(img, f'{cc}.gif')
        print(cc, end=' ', flush=True)

    return len(cc_list)


def main(downloader: Callable):
    DEST_DIR.mkdir(exist_ok=True)
    start = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - start
    print(f'\n{count} flags downloaded in {elapsed:.2f}s')


if __name__ == '__main__':
    main(download_many)
