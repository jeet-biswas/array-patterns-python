def longest_ones_after_flips(values: list[int], flips: int) -> int:
    """Longest contiguous run achievable by flipping at most flips zeros.

    Requires binary values and flips >= 0, else ValueError.
    O(n) time and O(1) space; input is unchanged.
    """
    if flips < 0 or any(value not in (0, 1) for value in values):
        raise ValueError('binary values and nonnegative flips are required')
    left = zeros = best = 0
    for right, value in enumerate(values):
        zeros += value == 0
        while zeros > flips:
            zeros -= values[left] == 0
            left += 1
        best = max(best, right - left + 1)
    return best
