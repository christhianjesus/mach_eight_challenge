def find_pairs(numbers: list[int], target: int) -> list[tuple[int, int]]:
    """
    Find pairs of integers in a list that sum to a given target value.

    This function takes a list of integers and a target sum. It iterates through
    the list and identifies pairs of integers whose sum matches the target sum.

    Args:
        numbers (list of int): The list of integers to search for pairs in.
        target (int): The target sum to find pairs that add up to.

    Returns:
        list of tuple: A list of pairs (tuple of two integers) that sum to the target
        value.

    Algorithm Complexity:
        The algorithm has a time complexity of O(n), where 'n' is the number
        of integers in the 'numbers' list. It efficiently identifies pairs
        that sum to the target value without the need for nested loops.

    Example:
        >>> find_pairs([1, 2, 3, 4, 5], 6)
        [(5, 1), (4, 2)]
    """
    pairs = []
    seen = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs
