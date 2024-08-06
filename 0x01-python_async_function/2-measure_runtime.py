#!/usr/bin/python3
import time
import asyncio

wait_routine = __import__('1-concurrent_coroutines').wait_n

def measure_time(n :int , max_delay : int) -> float:
    start_time = time.perf_counter()
    asyncio.run(wait_routine(n , max_delay))
    end_time = time.perf_counter()
    totaltime = end_time - start_time
    return totaltime / n
