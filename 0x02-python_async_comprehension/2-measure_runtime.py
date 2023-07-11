#!/usr/bin/env python3
"""Run time for parallel comprehension"""


import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time: float = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time: float = perf_counter()
    return end_time - start_time
