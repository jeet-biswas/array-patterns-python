def longest_disjoint_bit_window(values: list[int]) -> int:
    """Longest subarray where every pair has bitwise AND zero; no mutation.

    Values must be nonnegative integers; zero can appear any number of times.
    """
    if any(x < 0 for x in values):
        raise ValueError('nonnegative values required')
    mask = left = best = 0
    for right, value in enumerate(values):
        while mask & value:
            mask ^= values[left]
            left += 1
        mask |= value
        best = max(best, right-left+1)
    return best
