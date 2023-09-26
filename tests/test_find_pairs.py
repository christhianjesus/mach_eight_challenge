from mach_eight_challenge.find_pairs import find_pairs


def test_happy_path():
    """
    Test the find_pairs function with the given example.
    """
    numbers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
    target = 12

    tuples = find_pairs(numbers, target)

    assert len(tuples) == 3
    assert tuples == [(12, 0), (16, -4), (7, 5)]


def test_no_match():
    """
    Test the find_pairs function with a mismatched target.
    """
    numbers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
    target = 120

    tuples = find_pairs(numbers, target)

    assert len(tuples) == 0


def test_negative_target():
    """
    Test the find_pairs function with a negative target.
    """
    numbers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
    target = -4

    tuples = find_pairs(numbers, target)

    assert len(tuples) == 1
    assert tuples == [(-4, 0)]


def test_empty_list():
    """
    Test the find_pairs function with an empty list of integers.
    """
    numbers = []
    target = 12

    tuples = find_pairs(numbers, target)

    assert len(tuples) == 0


def test_special_case():
    """
    Test the find_pairs function with a number added with itself that
    is equal to the target value.
    """
    numbers = [1, 2, 3, 4, 5]
    target = 6

    tuples = find_pairs(numbers, target)

    assert len(tuples) == 2
    assert tuples == [(4, 2), (5, 1)]
