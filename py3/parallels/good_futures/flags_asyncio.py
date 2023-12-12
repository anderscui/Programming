# coding=utf-8
import asyncio

from httpx import AsyncClient

from parallels.good_futures.flags import BASE_URL, save_flag, main, save_flag_async


async def get_flag(client: AsyncClient, cc: str) -> bytes:  # <4>
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=6.1,
                            follow_redirects=True)  # <5>
    return resp.read()  # <6>


async def download_one(client: AsyncClient, cc: str):  # <3>
    image = await get_flag(client, cc)
    # save_flag(image, f'{cc}.gif')
    await save_flag_async(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


def download_many(cc_list: list[str]):
    return asyncio.run(supervisor(cc_list))


async def supervisor(cc_list) -> int:
    async with AsyncClient() as client:
        to_do = [download_one(client, cc) for cc in sorted(cc_list)]
        res = await asyncio.gather(*to_do)

        print(f'\ndownloaded: {res}')
    return len(res)


if __name__ == '__main__':
    main(download_many)
