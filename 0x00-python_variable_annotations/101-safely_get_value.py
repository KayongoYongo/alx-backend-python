#!/usr/bin/env python3
"""Get value safely"""


from typing import Mapping, TypeVar, Union, Any


K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(
    dct: Mapping[K, V],
    key: Any,
    default: Union[V, None] = None
) -> Union[Any, V]:

    """Get value safely"""
    if key in dct:
        return dct[key]
    else:
        return default
