#!/usr/bin/env python3
"""
Function sum_list which takes a list input_list of
floats as argument and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
       Returns the sum of the given list of float numbers.

    :param input_list: The list of float numbers.
    :return: The sum of the given list of float numbers.
    """
    return sum(input_list)
