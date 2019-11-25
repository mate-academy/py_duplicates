'''
Module
'''
from typing import List


def find_duplicates(lst: List[int]) -> int:
    '''

    :param lst:
    :return:
    '''
    perevir: List[int] = []
    count_duplicates = 0
    for number in lst:
        if number not in perevir:
            if lst.count(number) > 1:
                count_duplicates += 1
            perevir.append(number)
    return count_duplicates
