#!/usr/bin/env python3
"""Async comprehensions"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async comprehensions"""
    random_numbers = [number async for number in async_generator()]
    return random_numbers
