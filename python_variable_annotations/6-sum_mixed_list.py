#!/usr/bin/env python3
"""Sum_mixed_list takes a list of numbers, returns their sum as a float."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of integers and floats in the mixed list"""
    return sum(mxd_lst)
