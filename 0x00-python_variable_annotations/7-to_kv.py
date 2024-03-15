#!/usr/bin/env python3
"""
Type annotated function that that takes a string and an int
OR
float as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string a and an int OR
    float v as arguments and returns a tuple.
    The first element of the tuple is the string a.
    The second element is the square of the int/float
    v and should be annotated as a float.

    :param k: A string
    :param v: An int OR float
    :return: A tuple containing the string a and the square of v as a float
    """
    return (k, v ** 2)
