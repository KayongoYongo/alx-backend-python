#!/usr/bin/env python3
"""antonate te function"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Antonate the function"""
    return [(i, len(i)) for i in lst]
