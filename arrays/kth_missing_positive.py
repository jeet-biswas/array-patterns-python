def kth_missing_positive(values: list[int], k: int) -> int:
    """Kth absent positive integer; input must be strictly increasing and positive.

    Input ordering/positivity are unchecked preconditions. k <= 0 raises
    ValueError. O(log(n+1)) time, O(1) space; no mutation. Empty -> k.
    """
    if k <= 0:
        raise ValueError('k must be positive')
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] - middle - 1 < k:
            left = middle + 1
        else:
            right = middle
    return left + k
