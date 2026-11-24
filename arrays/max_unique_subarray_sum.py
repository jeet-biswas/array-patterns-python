def max_unique_subarray_sum(values: list[int]) -> int:
    """Maximum sum of a contiguous distinct-value window; empty allowed, no mutation.

    Nonnegative values required.
    """
    if any(x < 0 for x in values):
        raise ValueError('nonnegative values required')
    seen = set()
    left = total = best = 0
    for value in values:
        while value in seen:
            removed = values[left]
            seen.remove(removed)
            total -= removed
            left += 1
        seen.add(value)
        total += value
        best = max(best, total)
    return best
