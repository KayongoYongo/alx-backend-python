#!/usr/bin/env python3
"""Returns a asyncio task"""

import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Returns an asyncio task"""
    async def wait_random_coroutine():
        delay = random.uniform(0, max_delay)
        await asyncio.sleep(delay)
        return delay

    coro = wait_random_coroutine()
    task = asyncio.ensure_future(coro)
    return task
