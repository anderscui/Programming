# coding=utf-8
from contextlib import asynccontextmanager


@asynccontextmanager
async def web_page(url):
    # download_webpage should be awaitable
    data = await download_webpage(url)
    # make the func as async generator function
    yield data
    await update_status(url)


async with web_page('google.com') as data:
    preprocess(data)
