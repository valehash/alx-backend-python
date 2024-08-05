#!/usr/bin/python3
import asyncio
wait_rand=__import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int):
    array = []
    routine = [wait_rand(max_delay) for i in range(n)]
    for routine in asyncio.as_completed(routine):
        val = await(routine)
        array.append(val)
    return array

