def max_and_pair(values: list[int]) -> int:
    """Maximum AND of two distinct indices; require two nonnegative values.

    Invalid input raises ValueError. O(nB) bit checks for maximum bit length B,
    O(1) auxiliary integer slots; bit costs depend on B. Input unchanged.
    """
    if len(values) < 2 or any(value < 0 for value in values):
        raise ValueError('at least two nonnegative values are required')
    best = 0
    for bit in range(max(values).bit_length() - 1, -1, -1):
        candidate = best | (1 << bit)
        if sum((value & candidate) == candidate for value in values) >= 2:
            best = candidate
    return best
