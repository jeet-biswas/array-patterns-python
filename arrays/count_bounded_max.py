def count_bounded_max(values: list[int], lower: int, upper: int) -> int:
    """Count nonempty contiguous subarrays with lower <= max <= upper.

    Reversed bounds raise ValueError. O(n) time, O(1) space; no mutation.
    """
    if lower > upper:
        raise ValueError('lower must not exceed upper')
    last_bad = last_good = -1
    total = 0
    for i, value in enumerate(values):
        if value > upper:
            last_bad = i
        if lower <= value <= upper:
            last_good = i
        total += max(0, last_good - last_bad)
    return total
