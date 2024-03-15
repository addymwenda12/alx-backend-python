#!/usr/bin/env python3
"""
Function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a list of floats and integers
    as an argument and returns their sum as a float.

    :param mxd_lst: A list of floats and integers
    :return: The sum of all elements in the list as a float
    """
    return sum(mxd_lst)
