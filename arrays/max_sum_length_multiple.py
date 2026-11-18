def max_sum_length_multiple(values: list[int], k: int) -> int | None:
    """Best nonempty contiguous sum whose length is divisible by positive k.

    Return None if no eligible subarray. k <= 0 raises ValueError.
    Expected O(n) time, O(min(n,k)+1) space; input is unchanged.
    """
    if k <= 0:
        raise ValueError('k must be positive')
    minimum_prefix = {0: 0}
    prefix = 0
    best = None
    for stop, value in enumerate(values, 1):
        prefix += value
        remainder = stop % k
        if remainder in minimum_prefix:
            candidate = prefix - minimum_prefix[remainder]
            best = candidate if best is None else max(best, candidate)
        minimum_prefix[remainder] = min(minimum_prefix.get(remainder, prefix), prefix)
    return best
