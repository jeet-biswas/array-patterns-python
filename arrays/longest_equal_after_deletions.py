def longest_equal_after_deletions(values: list[int], k: int) -> int:
    """Longest equal-valued contiguous block obtainable after at most k deletions.

    k must be nonnegative. Returns retained block length; input is unchanged.
    """
    if k < 0:
        raise ValueError('nonnegative k required')
    positions = {}
    for i, value in enumerate(values):
        positions.setdefault(value, []).append(i)
    best = 0
    for indices in positions.values():
        left = 0
        for right in range(len(indices)):
            while indices[right]-indices[left]-(right-left) > k:
                left += 1
            best = max(best, right-left+1)
    return best
