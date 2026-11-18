def wiggle_subsequence_length(values: list[int]) -> int:
    """Longest subsequence with alternating positive/negative differences.

    Zero differences are excluded. Empty -> 0; singleton -> 1.
    O(n) time and O(1) space; input is unchanged.
    """
    if not values:
        return 0
    up = down = 1
    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            up = down + 1
        elif values[i] < values[i - 1]:
            down = up + 1
    return max(up, down)
