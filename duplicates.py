"""DOC"""
from typing import List


def find_duplicates(lst: List[int]) -> int:
    """return number of duplicates in list"""
    return len({item for item in set(lst) if lst.count(item) > 1})
