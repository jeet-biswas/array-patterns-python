def longest_turbulent_subarray(values: list[int]) -> int:
    """Longest contiguous subarray with alternating nonzero adjacent differences.

    Empty -> 0; singleton -> 1. O(n) time, O(1) space; no mutation.
    """
    if not values:
        return 0
    up = down = best = 1
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            up, down = down + 1, 1
        elif values[i] < values[i-1]:
            up, down = 1, up + 1
        else:
            up = down = 1
        best = max(best, up, down)
    return best
