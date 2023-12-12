# coding=utf-8
import asyncio
from collections import Counter
from http import HTTPStatus
from pathlib import Path

import httpx
import tqdm

from parallels.good_futures.flags2.common import main, save_flag, DownloadStatus

DEFAULT_CONCUR_REQ = 20
MAX_CONCUR_REQ = 1000


async def get_flag(client: httpx.AsyncClient,
                   base_url: str,
                   cc: str):
    url = f'{base_url}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=6.1, follow_redirects=True)
    resp.raise_for_status()
    return resp.content


async def download_one(client: httpx.AsyncClient,
                       cc: str,
                       base_url: str,
                       semaphore: asyncio.Semaphore,
                       verbose: bool = False) -> DownloadStatus:
    try:
        async with semaphore:
            image = await get_flag(client, base_url, cc)
    except httpx.HTTPStatusError as ex:
        res = ex.response
        if res.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND
            msg = f'not found: {res.url}'
        else:
            raise
    else:
        await asyncio.to_thread(save_flag, image, f'{cc}.gif')
        status = DownloadStatus.OK
        msg = 'OK'

    if verbose:
        print(cc, msg)
    return status


async def supervisor(cc_list: list[str],
                     base_url: str,
                     verbose: bool,
                     concur_req: int) -> Counter[DownloadStatus]:
    counter = Counter()
    semaphore = asyncio.Semaphore(concur_req)
    async with httpx.AsyncClient() as client:
        todos = [download_one(client, cc, base_url, semaphore, verbose) for cc in sorted(cc_list)]
        todo_iter = asyncio.as_completed(todos)
        if not verbose:
            todo_iter = tqdm.tqdm(todo_iter, total=len(cc_list))
        error: httpx.HTTPError | None = None
        for future in todo_iter:
            try:
                status = await future
            except httpx.HTTPStatusError as ex:
                error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
                error_msg = error_msg.format(resp=ex.response)
                error = ex
            except httpx.RequestError as ex:
                error_msg = f'{ex} {type(ex)}'.strip()
                error = ex
            except KeyboardInterrupt:
                break

            if error:
                status = DownloadStatus.ERROR
                if verbose:
                    url = str(error.request.url)
                    cc = Path(url).stem.upper()
                    print(f'{cc} error: {error_msg}')
            counter[status] += 1

    return counter


def download_many(cc_list: list[str],
                  base_url: str,
                  verbose: bool,
                  concur_req: int) -> Counter[DownloadStatus]:
    coro = supervisor(cc_list, base_url, verbose, concur_req)
    return asyncio.run(coro)


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
