#!/usr/bin/env python3
import asyncio
wait_rand=__import__('0-basic_async_syntax').wait_random
"""
    an async routine called wait_n 
    that takes in 2 int arguments (in this order): n and max_delay. 
    that spawn wait_random n times with the
    specified max_delay.

    params: max_delay, number of times (n)

    returns:  return the list of all the delays (float values) in ascending order.
"""


async def wait_n(n: int, max_delay: int) -> list[float]:
    """A function that list all the delays created in seconds"""
    array = []
    routine = [wait_rand(max_delay) for i in range(n)]
    for routine in asyncio.as_completed(routine):
        val = await(routine)
        array.append(val)
    return array
