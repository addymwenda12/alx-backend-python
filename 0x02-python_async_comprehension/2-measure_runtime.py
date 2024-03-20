#!/usr/bin/env python3
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.perf_counter()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = time.perf_counter()
    total_runtime = end_time - start_time

    return total_runtime
