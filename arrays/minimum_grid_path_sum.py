def minimum_grid_path_sum(matrix: list[list[int]]) -> int | None:
    """Minimum top-left to bottom-right sum using right/down moves; no mutation.

    Both endpoints count. Rectangular signed input allowed; no cells -> None.
    """
    columns = len(matrix[0]) if matrix else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    if not matrix or not columns:
        return None
    dp = [0]*columns
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if i == j == 0:
                dp[j] = value
            elif i == 0:
                dp[j] = dp[j-1]+value
            elif j == 0:
                dp[j] += value
            else:
                dp[j] = min(dp[j], dp[j-1])+value
    return dp[-1]
