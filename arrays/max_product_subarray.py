def max_product_subarray(values: list[int]) -> int:
    """Maximum product of a nonempty contiguous subarray; empty raises ValueError.

    O(n) arithmetic operations and O(1) auxiliary slots; input is unchanged.
    """
    if not values:
        raise ValueError('values must be nonempty')
    low = high = best = values[0]
    for i in range(1, len(values)):
        value = values[i]
        candidates = value, value * low, value * high
        low, high = min(candidates), max(candidates)
        best = max(best, high)
    return best
