#!/usr/bin/env python3
"""Multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Set multiplier"""
    def multiplier_fn(num: float) -> float:
        return num * multiplier
    return multiplier_fn
