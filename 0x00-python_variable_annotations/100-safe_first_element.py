#!/usr/bin/env python3
"""
Augmenting the code with the correct duck-typed annotations
"""
from typing import Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function takes a sequence of objects as
    an argument and returns the first object if the sequence is not empty
    or None otherwise.

    :param lst: A sequence of objects
    :return: The first object in the sequence or None
    """
    if lst:
        return lst[0]
    else:
        return None
