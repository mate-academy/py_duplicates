"""Duplicate counter module"""
from typing import List


def find_duplicates(array: List[int]) -> int:
    """
    Duplicate counter function
    :param array: list of int items
    :return: how mane duplicates in list
    """
    result = 0
    for i in array:
        if array.count(i) > 1:
            result += 1
            while i in array:
                array.remove(i)
    return result
