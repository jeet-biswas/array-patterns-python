def minimum_triangulation_score(values: list[int]) -> int:
    """Minimum sum of triangle vertex products for a convex polygon in array order.

    Nonnegative values required. Fewer than three vertices cost zero; no mutation.
    """
    if any(x < 0 for x in values):
        raise ValueError('nonnegative labels required')
    n = len(values)
    if n < 3:
        return 0
    dp = [[0]*n for _ in range(n)]
    for width in range(2, n):
        for left in range(n-width):
            right = left+width
            dp[left][right] = min(dp[left][middle]+dp[middle][right]+values[left]*values[middle]*values[right] for middle in range(left+1, right))
    return dp[0][-1]
