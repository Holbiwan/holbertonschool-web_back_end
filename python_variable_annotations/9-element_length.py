#!/usr/bin/env python3
""" Element_length: Iterable 'lst' -> List[Tuple[Sequence, int]] """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns list of tuples: elements from 'lst' and their lengths"""
    return [(i, len(i)) for i in lst]
