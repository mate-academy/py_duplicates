"""module docstring"""
#from typing import List


def find_duplicates(list_of_numbers):
    """function docstring"""
    duplicates = []
    sorted_list = sorted(list_of_numbers)
    for item in sorted_list:
        if item not in duplicates and sorted_list.count(item) > 1:
            duplicates.append(item)
    return len(duplicates)
