def count_increasing_subarrays(values: list[int]) -> int:
    """Count nonempty strictly increasing contiguous windows; no mutation."""
    run = total = 0
    for i, value in enumerate(values):
        run = run+1 if i and values[i-1] < value else 1
        total += run
    return total
