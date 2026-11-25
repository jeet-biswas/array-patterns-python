def max_subarray_one_square(values: list[int]) -> int:
    """Best nonempty subarray sum with exactly one of its elements squared.

    Empty raises ValueError. Signed values supported; input is unchanged.
    """
    if not values:
        raise ValueError('nonempty array required')
    plain = values[0]
    modified = best = values[0]**2
    for index in range(1, len(values)):
        value = values[index]
        modified = max(value**2, plain+value**2, modified+value)
        plain = max(value, plain+value)
        best = max(best, modified)
    return best
