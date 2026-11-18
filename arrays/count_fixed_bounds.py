def count_fixed_bounds(values: list[int], minimum: int, maximum: int) -> int:
    """Count nonempty contiguous subarrays with exactly these min/max values.

    minimum > maximum raises ValueError. O(n) time, O(1) space; no mutation.
    """
    if minimum > maximum:
        raise ValueError('minimum must not exceed maximum')
    last_min = last_max = last_bad = -1
    total = 0
    for i, value in enumerate(values):
        if not minimum <= value <= maximum:
            last_bad = i
        if value == minimum:
            last_min = i
        if value == maximum:
            last_max = i
        total += max(0, min(last_min, last_max) - last_bad)
    return total
