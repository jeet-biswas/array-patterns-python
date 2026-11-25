def max_burst_balloon_coins(values: list[int]) -> int:
    """Maximum reward when removing x earns left*x*right using current neighbors.

    Missing neighbors have value 1. Nonnegative values required; no mutation.
    """
    if any(x < 0 for x in values):
        raise ValueError('nonnegative values required')
    padded = [1]+list(values)+[1]
    n = len(padded)
    dp = [[0]*n for _ in range(n)]
    for width in range(2, n):
        for left in range(n-width):
            right = left+width
            dp[left][right] = max(dp[left][middle]+dp[middle][right]+padded[left]*padded[middle]*padded[right] for middle in range(left+1, right))
    return dp[0][-1]
