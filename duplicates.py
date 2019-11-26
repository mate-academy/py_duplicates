"""
find_duplicates
"""
from typing import List, Dict


def find_duplicates(numbers: List[int]) -> int:
    """
    :param numbers: [int]
    :return: count of duplicates
    """
    duplicates: Dict[int, int] = {}
    count = 0

    for item in numbers:
        if item in duplicates and duplicates[item] == 1:
            count += 1
            duplicates[item] += 1
        else:
            duplicates[item] = 1

    return count
