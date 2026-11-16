def min_moves_equal(values: list[int]) -> int:
    """Minimum +/-1 operations on individual elements to make all values equal.

    Empty -> 0. O(n log n) time, O(n) space; input is unchanged.
    """
    if not values:
        return 0
    ordered = sorted(values)
    median = ordered[len(ordered) // 2]
    return sum(abs(value - median) for value in values)
