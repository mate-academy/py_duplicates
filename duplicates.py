"""DOC"""
from typing import List


def find_duplicates(lst):
    """return count of duplicates"""
    duplicates = []
    unique = []
    duplicate_count = 0
    for element in lst:
        if element not in unique:
            unique.append(element)
        else:
            if element not in duplicates:
                duplicates.append(element)
                duplicate_count += 1

    return duplicate_count
