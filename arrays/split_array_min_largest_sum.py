def split_array_min_largest_sum(values: list[int], k: int) -> int:
    """Split into exactly k nonempty contiguous parts, minimizing the largest sum.

    Requires nonnegative values and 1 <= k <= n, else ValueError.
    O(n log(S+1)) time for S=sum(values), O(1) space; input unchanged.
    """
    if not 1 <= k <= len(values) or any(value < 0 for value in values):
        raise ValueError('nonnegative values and 1 <= k <= n are required')
    low, high = max(values), sum(values)
    while low < high:
        limit = (low + high) // 2
        parts = 1
        subtotal = 0
        for value in values:
            if subtotal + value > limit:
                parts += 1
                subtotal = value
            else:
                subtotal += value
        if parts <= k:
            high = limit
        else:
            low = limit + 1
    return low
