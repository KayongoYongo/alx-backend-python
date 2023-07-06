#!/usr/bin/env python3
"""Antonate the function"""


from typing import Iterable, Sequence, List, Tuple, Dict


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Antonate the fuction"""
    return [(i, len(i)) for i in lst]
