#!/usr/bin/env python3
"""
Add type annotations to the function using TypeVar
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T],
                     key: Any, default: Union[T, None] =
                     None) -> Union[T, Any]:
    """
    This function takes a mapping (e.g., dictionary) and
    a key as arguments and returns the value associated with the key if
    it exists, or the default value otherwise.

    :param dct: A mapping (e.g., dictionary)
    :param key: A key
    :param default: The default value if the key is not found in the mapping
    :return: The value associated with the key or the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
