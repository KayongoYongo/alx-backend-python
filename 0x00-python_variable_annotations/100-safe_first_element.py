#!/usr/bin/env python3
"""Correct code"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Correct code"""
    if lst:
        return lst[0]
    else:
        return None
