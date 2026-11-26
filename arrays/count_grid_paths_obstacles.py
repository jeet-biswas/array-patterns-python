def count_grid_paths_obstacles(blocked: list[list[int]]) -> int:
    """Count paths from top-left to bottom-right using right/down moves.

    Rectangular binary matrix: 1 blocked, 0 open. No cells -> 0; no mutation.
    """
    columns = len(blocked[0]) if blocked else 0
    if any(len(row) != columns for row in blocked) or any(x not in (0, 1) for row in blocked for x in row):
        raise ValueError('rectangular binary matrix required')
    if not blocked or not columns:
        return 0
    dp = [0]*columns
    dp[0] = 1
    for row in blocked:
        for j, value in enumerate(row):
            if value:
                dp[j] = 0
            elif j:
                dp[j] += dp[j-1]
    return dp[-1]
