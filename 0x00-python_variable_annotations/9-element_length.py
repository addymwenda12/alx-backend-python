#!/usr/bin/env python3
"""
Function parameters that return values with the appropriate types
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence[object]]) -> List[Tuple[Sequence[object, int]]]:
    """
    This function takes a list of objects as an argument
    and returns a list of tuples.
    Each tuple contains an object from the input list and its length.

    :param lst: A sequence of objects
    :return: A list of tuples containing objects and their lengths
    """
    return [(i, len(i)) for seq in lst for i in lst]
