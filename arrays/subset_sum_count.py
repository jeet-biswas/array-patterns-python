def subset_sum_count(values: list[int], target: int) -> int:
    """Count index-distinct subsets summing to target, including the empty subset.

    Signed integers and zeros allowed. Expected O(nR) arithmetic operations,
    O(R) space for maximum reachable-sum count R (possibly exponential).
    Counts use arbitrary-precision integers. Input is unchanged.
    """
    counts = {0: 1}
    for value in values:
        updated = counts.copy()
        for total, count in counts.items():
            next_total = total + value
            updated[next_total] = updated.get(next_total, 0) + count
        counts = updated
    return counts.get(target, 0)
