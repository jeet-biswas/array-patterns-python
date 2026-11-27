def minimum_range_increments(target: list[int]) -> int:
    """Fewest +1 operations on contiguous nonempty intervals, starting from zeros.

    Target values must be nonnegative; empty costs zero. Input is unchanged.
    """
    previous = total = 0
    for value in target:
        if value < 0:
            raise ValueError('nonnegative target required')
        total += max(0, value-previous)
        previous = value
    return total
