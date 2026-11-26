def count_ordered_target_sums(values: list[int], target: int) -> int:
    """Exact number of ordered reusable-value sequences summing to target.

    Positive values and nonnegative target required; duplicate values ignored.
    Empty sequence counts once for target zero. Input is unchanged.
    """
    if target < 0 or any(x <= 0 for x in values):
        raise ValueError('positive values and nonnegative target required')
    unique = sorted(set(values))
    ways = [0]*(target+1)
    ways[0] = 1
    for amount in range(1, target+1):
        for value in unique:
            if value > amount: break
            ways[amount] += ways[amount-value]
    return ways[target]
