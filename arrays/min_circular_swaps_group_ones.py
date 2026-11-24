def min_circular_swaps_group_ones(values: list[int]) -> int:
    """Minimum arbitrary index swaps to make all ones consecutive circularly.

    Binary values required; empty returns zero. Input is unchanged.
    """
    if any(x not in (0, 1) for x in values):
        raise ValueError('binary values required')
    n = len(values)
    width = sum(values)
    if width <= 1:
        return 0
    ones = sum(values[i] for i in range(width))
    best = width-ones
    for start in range(1, n):
        ones += values[(start+width-1) % n]-values[start-1]
        best = min(best, width-ones)
    return best
