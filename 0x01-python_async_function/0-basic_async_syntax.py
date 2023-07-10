#!/usr/bin/env python3
"""A function that waits for a random delay"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """The function waits for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
