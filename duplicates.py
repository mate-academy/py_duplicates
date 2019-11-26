"""Count duplicate elements in  a list."""

from typing import List


def find_duplicates(arr: List[int]) -> int:
    """General func"""
    amout_duplicate = 0
    items_set = set(arr)
    for i in items_set:
        if arr.count(i) > 1:
            amout_duplicate += 1
    return amout_duplicate
