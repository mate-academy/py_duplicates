"""Docstring"""
from typing import List


def find_duplicates(lis: List[int]) -> int:
    """
    Returns number of duplicates in the given list
    :param lis: List[int]
    :return: int
    """
    return len({x for x in lis if lis.count(x) > 1})
