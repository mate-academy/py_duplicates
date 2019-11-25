"""module duplicates"""

from typing import List


def find_duplicates(lst: List[int]) -> int:
    """
    Count duplicate elements in a list.
    :param lst: lst
    :return: int
    """
    uniq_lst = {x for x in lst if lst.count(x) > 1}
    return len(uniq_lst)
