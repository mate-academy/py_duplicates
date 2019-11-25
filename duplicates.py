"""
Find count duplicate elements in  a list
"""

from typing import List


def find_duplicates(lst: List[int]) -> int:
    """Find count"""
    count = 0
    for value in set(lst):
        if lst.count(value) > 1:
            count += 1
    return count
