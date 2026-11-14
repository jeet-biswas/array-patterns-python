def best_sightseeing_pair(values: list[int]) -> int:
    """Maximum values[i]+values[j]+i-j over i < j; signed values allowed.

    Fewer than two values raises ValueError. O(n) time, O(1) space.
    Input is unchanged.
    """
    if len(values) < 2:
        raise ValueError('at least two values are required')
    left_best = values[0]
    best = values[0] + values[1] - 1
    for j in range(1, len(values)):
        best = max(best, left_best + values[j] - j)
        left_best = max(left_best, values[j] + j)
    return best
