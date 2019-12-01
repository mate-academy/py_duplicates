"""docstring"""


from typing import List


def find_duplicates(list_item: List[int]) -> int:
    """return count of duplicate"""
    return len([i for i in set(list_item) if list_item.count(i) > 1])
