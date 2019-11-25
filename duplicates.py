"""
Find count duplicate elements in  a list
"""

from typing import List


def find_duplicates(lst: List[int]) -> int:
    """Find count"""
    return sum(1 for i in set(lst) if lst.count(i) > 1)
