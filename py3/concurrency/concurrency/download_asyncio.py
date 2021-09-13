import aiohttp
import asyncio
import time


async def download_site(session, url):
    async with session.get(url) as resp:
        print(f'read {resp.content_length} from {url}')


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    sites = ['https://realpython.com/',
             'https://www.cnblogs.com/'] * 10

    start = time.time()
    # asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    asyncio.run(download_all_sites(sites))
    elapsed = time.time() - start
    # downloaded 20 in 0.9054982662200928 seconds.
    print(f'downloaded {len(sites)} in {elapsed} seconds.')
