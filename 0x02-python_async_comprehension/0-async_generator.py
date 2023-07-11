#!/usr/bin/env python3
"""Async generator"""
import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """Async generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
