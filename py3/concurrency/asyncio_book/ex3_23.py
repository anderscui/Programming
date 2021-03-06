# coding=utf-8
import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, download_webpage, url)
    yield data
    await loop.run_in_executor(None, update_status, url)


async with web_page('google.com') as data:
    preprocess(data)
