#!/usr/bin/env python3
"""Concurrent execution"""

import asyncio
from typing import List
from heapq import nsmallest

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """concurrent execution"""
    random_list = []
    for i in range(n):
        random_list.append(await wait_random(max_delay))

    return nsmallest(n, random_list)
