def partition_max_sum(values: list[int], k: int) -> int:
    """Partition into blocks of length <= k and maximize sum of block maxima times lengths.

    k must be positive. Signed values are allowed; empty returns zero. No mutation.
    """
    if k <= 0:
        raise ValueError('k must be positive')
    dp = [0] * (len(values) + 1)
    for end in range(1, len(values) + 1):
        maximum = values[end-1]
        best = None
        for size in range(1, min(k, end) + 1):
            maximum = max(maximum, values[end-size])
            candidate = dp[end-size] + maximum * size
            best = candidate if best is None else max(best, candidate)
        dp[end] = best
    return dp[-1]
