def count_maximum_or_subsets(values: list[int]) -> int:
    """Exact count of nonempty index subsets attaining the full-array OR.

    Nonnegative values required; duplicates are distinct indices. No mutation.
    """
    if any(x < 0 for x in values): raise ValueError('nonnegative values required')
    states = {0: 1}
    target = 0
    for value in values:
        target |= value
        following = states.copy()
        for old, count in states.items(): following[old | value] = following.get(old | value, 0)+count
        states = following
    return states[target]-int(target == 0)
