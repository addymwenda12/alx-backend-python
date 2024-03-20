#!/usr/bin/env python3
"""
This module contains an asynchronous generator function
`async_generator`. 
The purpose of this function is to generate random numbers.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [i async for i in async_generator()][:10]
