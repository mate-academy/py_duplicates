"""
docstring
"""


def find_duplicates(lst) -> int:
    """

    :param lst:
    :return:
    """
    # new list with items that appends more than one time
    new_lst = [item for index, item in enumerate(lst) if lst.count(item) > 1]
    return len(set(new_lst))
