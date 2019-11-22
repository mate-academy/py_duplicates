import duplicates


def test_empty():
    assert duplicates.find_duplicates([]) == 0


def test_none():
    assert duplicates.find_duplicates([1, 2, 3]) == 0


def test_dup():
    assert duplicates.find_duplicates([1, 2, 3, 10, 2, 3, 3]) == 2