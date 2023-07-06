#!/usr/bin/env python3
"""Get value safely"""


from typing import TypeVar, Dict, Optional


K = TypeVar('K')
V = TypeVar('V')

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    """Get value safely"""
    if key in dct:
        return dct[key]
    else:
        return default
