def zero_filled_subarrays(values: list[int]) -> int:
    """Count nonempty all-zero subarrays; input is unchanged."""
    run = total = 0
    for value in values:
        run = run + 1 if value == 0 else 0
        total += run
    return total
