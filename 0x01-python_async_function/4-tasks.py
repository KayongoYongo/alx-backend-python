#!/usr/bin/env python3
"""Random task"""
import asyncio
from typing import List
from heapq import nsmallest

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Concurrent execution using task_wait_random"""
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    random_list = await asyncio.gather(*tasks)
    return nsmallest(n, random_list)
