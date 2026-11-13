def pivot_index(values: list[int]) -> int:
    """First index with equal sums strictly to its left and right, or -1.

    Empty sides sum to zero. O(n) time and O(1) space; input is unchanged.
    """
    right = sum(values)
    left = 0
    for i, value in enumerate(values):
        right -= value
        if left == right:
            return i
        left += value
    return -1
