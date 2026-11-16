def max_sum_increasing_subsequence(values: list[int]) -> int:
    """Maximum sum of a nonempty strictly increasing subsequence.

    Empty raises ValueError; all-negative inputs return the largest element.
    O(n squared) time, O(n) space; input is unchanged.
    """
    if not values:
        raise ValueError('values must be nonempty')
    best = values.copy()
    for i in range(len(values)):
        for j in range(i):
            if values[j] < values[i]:
                best[i] = max(best[i], best[j] + values[i])
    return max(best)
