def max_frequency_increments(values: list[int], budget: int) -> int:
    """Largest possible equal-value count after at most budget +1 operations.

    Signed values allowed; negative budget raises ValueError. Empty -> 0.
    O(n log n) time, O(n) sorting space; input is unchanged.
    """
    if budget < 0:
        raise ValueError('budget must be nonnegative')
    ordered = sorted(values)
    left = total = best = 0
    for right, value in enumerate(ordered):
        total += value
        while value * (right - left + 1) - total > budget:
            total -= ordered[left]
            left += 1
        best = max(best, right - left + 1)
    return best
