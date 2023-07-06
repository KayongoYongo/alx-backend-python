#!/usr/bin/env python3
"""Finds the sum of a list of integers and floats"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of a List of integers and floats"""
    return sum(mxd_lst)
