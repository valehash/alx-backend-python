#!/usr/bin/env python3
import random as rand
import asyncio

async def wait_random(max_delay=10):
    delay=(rand.uniform(0, max_delay))
    await asyncio.sleep(delay)
    return delay

