def shortest_removal_sorted(values: list[int]) -> int:
    """Minimum contiguous deletion length leaving nondecreasing values; no mutation."""
    n = len(values)
    if n < 2:
        return 0
    right = n-1
    while right > 0 and values[right-1] <= values[right]:
        right -= 1
    if right == 0:
        return 0
    best = right
    for left in range(n):
        if left and values[left-1] > values[left]:
            break
        while right < n and values[right] < values[left]:
            right += 1
        best = min(best, right-left-1)
    return best
