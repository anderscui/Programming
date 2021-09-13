import asyncio
import logging
import re
import sys
from os import PathLike
from typing import IO, Union
import urllib.error
import urllib.parse

import aiofiles
import aiohttp
from aiohttp import ClientSession

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True

HREF_RE = re.compile(r'href="(.*?)"')


async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    """GET request wrapper to fetch page HTML.

    kwargs are passed to `session.request()`
    """
    resp = await session.request(method='GET', url=url, timeout=5, **kwargs)
    resp.raise_for_status()
    logger.info(f'Got response [{resp.status}] for url: {url}')
    html = await resp.text()
    return html


async def parse(url: str, session: ClientSession, **kwargs) -> set:
    """Find hrefs in the HTML of `url`."""
    found = set()
    try:
        html = await fetch_html(url=url, session=session, **kwargs)
    except (
        aiohttp.ClientError,
        asyncio.exceptions.TimeoutError,
    ) as e:
        logger.error(
            f'aiohttp exception for {url} [{getattr(e, "status", None)}]: {getattr(e, "message", None)}'
        )
        return found
    except Exception as e:
        logger.exception(f'Non-aiohttp exception occurred: {getattr(e, "__dict__", {})}')
        return found
    else:
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError):
                logger.exception(f'Error parsing url: {link}')
                pass
            else:
                found.add(abslink)
        logger.info(f'Found {len(found)} for {url}')
        return found


async def write_one(file: Union[str, PathLike], url: str, **kwargs):
    """Write the found hrefs from `url` to `file`"""
    res = await parse(url=url, **kwargs)
    if not res:
        return None
    async with aiofiles.open(file, 'a') as f:
        for p in res:
            await f.write(f'{url}\t{p}\n')
        logger.info(f'Wrote results for source url: {url}')


async def bulk_crawl_and_write(file: Union[str, PathLike], urls: set, **kwargs):
    """Crawl and write concurrently to `file` for multiple `urls`."""
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(write_one(file=file, url=url, session=session, **kwargs))
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    import pathlib
    import sys

    assert sys.version_info >= (3, 7)
    here = pathlib.Path(__file__).parent

    with open(here.joinpath('urls.txt')) as inf:
        urls = set(map(str.strip, inf))

    out_path = here.joinpath('found_urls.txt')
    with open(out_path, 'w') as outf:
        outf.write(f'source_url\tparsed_url\n')

    asyncio.run(bulk_crawl_and_write(file=out_path, urls=urls))
