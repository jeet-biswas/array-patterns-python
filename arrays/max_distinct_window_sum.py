def max_distinct_window_sum(values: list[int], k: int) -> int | None:
    """Best sum of exactly k consecutive distinct values, or None; no mutation.

    k must be positive; signed values are supported.
    """
    if k <= 0:
        raise ValueError('positive k required')
    counts = {}
    total = 0
    best = None
    for i, value in enumerate(values):
        total += value
        counts[value] = counts.get(value, 0)+1
        if i >= k:
            removed = values[i-k]
            total -= removed
            counts[removed] -= 1
            if counts[removed] == 0:
                del counts[removed]
        if i >= k-1 and len(counts) == k:
            best = total if best is None else max(best, total)
    return best
