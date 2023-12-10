# coding=utf-8
import time
from collections import Counter
from pathlib import Path
from http import HTTPStatus

import httpx
import tqdm

from parallels.good_futures.flags2.common import main, save_flag, DownloadStatus

DEFAULT_CONCUR_REQ = 1
MAX_CONCUR_REQ = 1


def get_flag(base_url, cc):
    url = f'{base_url}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url, timeout=6.1, follow_redirects=True)
    resp.raise_for_status()
    return resp.content


def download_one(cc: str, base_url: str, verbose: bool = False) -> DownloadStatus:
    try:
        image = get_flag(base_url, cc)
    except httpx.HTTPStatusError as ex:
        res = ex.response
        if res.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND
            msg = f'not found: {res.url}'
        else:
            raise
    else:
        save_flag(image, f'{cc}.gif')
        status = DownloadStatus.OK
        msg = 'OK'

    if verbose:
        print(cc, msg)
    return status


def download_many(cc_list: list[str], base_url: str, verbose: bool,
                  _unused_concur_req: int) -> Counter[DownloadStatus]:
    counter = Counter()
    cc_iter = sorted(cc_list)
    if not verbose:
        cc_iter = tqdm.tqdm(cc_iter)
    for cc in cc_iter:
        try:
            status = download_one(cc, base_url, verbose)
        except httpx.HTTPStatusError as ex:
            error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
            error_msg = error_msg.format(resp=ex.response)
        except httpx.RequestError as ex:
            error_msg = f'{ex} {type(ex)}'.strip()
        except KeyboardInterrupt:
            break
        else:
            error_msg = ''

        if error_msg:
            status = DownloadStatus.ERROR
        counter[status] += 1
        if verbose and error_msg:
            print(f'{cc} error: {error_msg}')

    return counter


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
