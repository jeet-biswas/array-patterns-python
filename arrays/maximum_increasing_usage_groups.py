def maximum_increasing_usage_groups(limits: list[int]) -> int:
    """Most groups of strictly increasing positive sizes, distinct indices per group.

    Index i may appear across groups at most limits[i] times. Nonnegative limits
    required; unused capacity allowed. Input is unchanged.
    """
    if any(x < 0 for x in limits):
        raise ValueError('nonnegative limits required')
    capacity = groups = 0
    for limit in sorted(limits):
        capacity += limit
        if capacity >= (groups+1)*(groups+2)//2:
            groups += 1
    return groups
