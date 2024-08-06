#!/usr/bin/env python3
import random as rand
import asyncio

async def wait_random(max_delay: int =10) -> float:
    delay = rand.randint() * max_delay
    await asyncio.sleep(delay)
    return delay

