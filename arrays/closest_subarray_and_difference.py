def closest_subarray_and_difference(values: list[int], target: int) -> int | None:
    """Smallest absolute distance from target to a nonempty subarray AND, or None.

    Nonnegative values and target required. Input is unchanged.
    """
    if target < 0 or any(x < 0 for x in values): raise ValueError('nonnegative inputs required')
    previous = set()
    best = None
    for value in values:
        previous = {old & value for old in previous} | {value}
        distance = min(abs(old-target) for old in previous)
        best = distance if best is None else min(best, distance)
    return best
