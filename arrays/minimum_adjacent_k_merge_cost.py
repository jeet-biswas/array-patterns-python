def minimum_adjacent_k_merge_cost(values: list[int], k: int) -> int | None:
    """Merge exactly k adjacent piles at their total weight until one remains.

    Returns minimum total cost, or None if impossible. Nonnegative weights and
    k >= 2 required; empty/singleton cost zero. Input is unchanged.
    """
    if k < 2 or any(x < 0 for x in values):
        raise ValueError('nonnegative weights and k >= 2 required')
    n = len(values)
    if n <= 1:
        return 0
    if (n-1) % (k-1):
        return None
    prefix = [0]
    for x in values:
        prefix.append(prefix[-1]+x)
    dp = [[0]*n for _ in range(n)]
    for size in range(k, n+1):
        for left in range(n-size+1):
            right = left+size-1
            dp[left][right] = min(dp[left][middle]+dp[middle+1][right] for middle in range(left, right, k-1))
            if (size-1) % (k-1) == 0:
                dp[left][right] += prefix[right+1]-prefix[left]
    return dp[0][-1]
