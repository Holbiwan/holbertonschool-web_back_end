#!/usr/bin/env python3
"""
Takes a string k and an int OR float v as arguments and
returns a tuple.
The first element of the tuple is the string k
The second element is the square of the int/float v annotated as a float
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple: (string 'k', square of int/float 'v' as a float)"""
    return (k, v ** 2)
