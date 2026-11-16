def can_partition_equal_subset(values: list[int]) -> bool:
    """Whether nonnegative integers can be partitioned into equal-sum subsets.

    Empty subsets allowed; empty input -> True. Negative values raise
    ValueError. O(n*(T+1)) time, O(T+1) space for half-total T. No mutation.
    """
    if any(value < 0 for value in values):
        raise ValueError('values must be nonnegative')
    total = sum(values)
    if total % 2:
        return False
    target = total // 2
    reachable = {0}
    for value in values:
        reachable |= {current + value for current in reachable if current + value <= target}
        if target in reachable:
            return True
    return target in reachable
