#!/usr/bin/env python3
import asyncio
from typing import List

wait_random = __import__('previous_file').wait_random
"""
This function is used to wait a random amount of
time before returning.
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function waits for `n` seconds and then
    returns a list with the time it waited in each iteration.
    
    :param n: The number of iterations to perform.
    """
    delays = []
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in tasks:
        delay = await task
        delays.append(delay)
    return sorted(delays)
