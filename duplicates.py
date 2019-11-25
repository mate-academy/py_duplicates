"""Count duplicate elements in a list"""
from typing import List


def find_duplicates(values: List[int]) -> int:
    """Method that count duplicate elements in a list"""
    return len(set({_ for _ in values if values.count(_) > 1}))
