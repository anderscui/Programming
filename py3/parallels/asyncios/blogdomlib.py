# coding=utf-8
import asyncio
import socket
from collections.abc import Iterable, AsyncIterator

from keyword import kwlist

from typing import NamedTuple

MAX_KEYWORD_LEN = 4

OptionalLoop = asyncio.AbstractEventLoop | None


class Result(NamedTuple):
    domain: str
    found: bool


async def probe(domain: str, loop: OptionalLoop = None) -> Result:
    if loop is None:
        loop = asyncio.get_running_loop()
    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror as e:
        return Result(domain, False)
    return Result(domain, True)


async def multi_probe(domains: Iterable[str]) -> AsyncIterator[Result]:
    loop = asyncio.get_event_loop()
    coros = [probe(domain, loop) for domain in domains]
    for coro in asyncio.as_completed(coros):
        result = await coro
        yield result


async def main() -> None:
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)
    domains = (f'{name}.dev'.lower() for name in names)
    coros = [probe(domain) for domain in domains]
    for coro in asyncio.as_completed(coros):
        domain, found = await coro
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    asyncio.run(main())
