"""duplicate module."""
from typing import List


def find_duplicates(input_list: List[int]) -> int:
    """returns number of duplicates in list."""
    if input_list:
        duplicates = []
        for number in input_list:
            if input_list.count(number) > 1:
                duplicates.append(number)
        return len(set(duplicates))
    return 0
