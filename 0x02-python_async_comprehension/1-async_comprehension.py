#!/usr/bin/env python3
"""
Import async_generator from the previous task and then write
a coroutine called async_comprehension that takes no arguments.
The coroutine will collect 10 random numbers using
an async comprehensing over async_generator,
then return the 10 random numbers.
"""


generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    Function that adds the async calls generat4ed into an array
    """
    new_list = [i async for i in generator()]
    return new_list
