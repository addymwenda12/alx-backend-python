#!/usr/bin/env python3
"""
Function that takes a float as argument and returns a
function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float, float]]:
    """
    This function takes a float multiplier as
    argument and returns a function that multiplies
    a float by multiplier.

    :param multiplier: A float
    :return: Multiplication of the float
    """
    def multiplier_function(number: float) -> float:
        return number * multiplier

    return multiplier_function
