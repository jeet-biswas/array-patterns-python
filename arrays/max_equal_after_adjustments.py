def max_equal_after_adjustments(values: list[int], k: int) -> int:
    """Most equal elements after changing each by an integer in [-k,k]; no mutation.

    k must be nonnegative; signed elements allowed.
    """
    if k < 0:
        raise ValueError('nonnegative k required')
    ordered = sorted(values)
    left = best = 0
    for right, value in enumerate(ordered):
        while value-ordered[left] > 2*k:
            left += 1
        best = max(best, right-left+1)
    return best
