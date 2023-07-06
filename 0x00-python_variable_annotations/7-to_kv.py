#!/usr/bin/env python3
"""Take a string and return a tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Retuns a tuple"""
    return (k, float(v**2))
