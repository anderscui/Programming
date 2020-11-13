# coding=utf-8
import asyncio

loop = asyncio.get_event_loop()
loop2 = asyncio.get_event_loop()
print(loop is loop2)
