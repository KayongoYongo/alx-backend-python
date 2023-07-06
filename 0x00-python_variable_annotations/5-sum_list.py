#!/usr/bin/env python3
"""Takes a list and returns their sum"""

def sum_list(input_list: float) -> float:
    total: float = 0

    for i in input_list:
        total += i

    return total
