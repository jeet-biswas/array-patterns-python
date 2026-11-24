def minimum_stick_cut_cost(length: int, cuts: list[int]) -> int:
    """Minimum total cost to perform all cuts, each costing its current piece length.

    Positive length and distinct cut positions strictly inside the stick required.
    The cut array is unchanged; no cuts costs zero.
    """
    if length <= 0 or any(not 0 < x < length for x in cuts) or len(set(cuts)) != len(cuts):
        raise ValueError('positive length and distinct interior cuts required')
    positions = [0]+sorted(cuts)+[length]
    n = len(positions)
    dp = [[0]*n for _ in range(n)]
    for width in range(2, n):
        for left in range(n-width):
            right = left+width
            dp[left][right] = positions[right]-positions[left]+min(dp[left][middle]+dp[middle][right] for middle in range(left+1, right))
    return dp[0][-1]
