#!/usr/bin/env python3
import asyncio
import random
from typing import List
"""
This module contains an asynchronous function that waits for a random delay.
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.
    
    Args:
        max_delay (int): The maximum delay in seconds (default is 10).
    
    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times and returns a list of delays.
    
    Args:
        n (int): The number of times wait_random should be called.
        max_delay (int): The maximum delay in seconds for each call to wait_random.
    
    Returns:
        List[float]: A list of delays.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return delays
