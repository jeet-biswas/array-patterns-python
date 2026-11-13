def max_circular_subarray(values: list[int]) -> int:
    """Best nonempty circular sum using each array position at most once.

    Empty input raises ValueError. O(n) time, O(1) space; no mutation.
    """
    if not values:
        raise ValueError('values must be nonempty')
    high = low = best = worst = total = values[0]
    for i in range(1, len(values)):
        value = values[i]
        high = max(value, high + value)
        low = min(value, low + value)
        best, worst = max(best, high), min(worst, low)
        total += value
    return best if best < 0 else max(best, total - worst)
