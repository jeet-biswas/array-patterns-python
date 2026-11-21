def count_alternating_binary_subarrays(values: list[int]) -> int:
    """Count nonempty windows with alternating 0/1 values; no mutation.

    Any element outside {0, 1} raises ValueError.
    """
    run = total = 0
    for i, value in enumerate(values):
        if value not in (0, 1):
            raise ValueError('binary values required')
        run = run+1 if i and values[i-1] != value else 1
        total += run
    return total
