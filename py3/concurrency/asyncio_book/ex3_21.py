# coding=utf-8
from contextlib import contextmanager


@contextmanager
def web_page(url):
    data = download_webpage(url)
    yield data
    update_status(url)


with web_page('google.com') as data:
    preprocess(data)
