# coding=utf-8
import asyncio


async def network_request_async(n):
    await asyncio.sleep(1.0)
    return {'success': True, 'result': n ** 2}


async def fetch_square(n):
    resp = await network_request_async(n)
    if resp['success']:
        print(f'result is {resp["result"]}')


loop = asyncio.get_event_loop()
asyncio.ensure_future(fetch_square(2))
asyncio.ensure_future(fetch_square(3))
asyncio.ensure_future(fetch_square(4))
loop.run_forever()
