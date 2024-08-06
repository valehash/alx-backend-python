#!/usr/bin/env python3
import asyncio
tasks= __import__("0-basic_async_syntax").wait_random

def task_wait_random(max_delay : int) -> object:
    c = asyncio.create_task(tasks(max_delay))
    return c

