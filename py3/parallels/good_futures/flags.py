# coding=utf-8
import os
import time
import sys

import requests

POP20_CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    # Python normally waits for a line break to flush the stdout buffer
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        img = get_flag(cc)
        show(cc)
        save_flag(img, cc.lower() + '.gif')

    return len(cc_list)


def main(downloader):
    start = time.time()
    count = downloader(POP20_CC)
    elapsed = time.time() - start
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)
