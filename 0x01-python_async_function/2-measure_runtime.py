#!/usr/bin/env python3
"""Find the runtime of programs"""
import time
from asyncio import run


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the run time"""
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_time / n
    return avg_time
