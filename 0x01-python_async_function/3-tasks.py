#!/usr/bin/env python3
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
"""
This function is used to wait for a random amount of time.
"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task that waits for
    a random delay up to max_delay seconds.
    
    :param max_delay:
    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
