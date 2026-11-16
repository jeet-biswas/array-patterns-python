def longest_mountain(values: list[int]) -> int:
    """Longest contiguous strict ascent followed by strict descent, else zero.

    A mountain has at least three elements. O(n) time, O(1) space; no mutation.
    """
    up = down = best = 0
    for i in range(1, len(values)):
        if values[i] == values[i - 1] or (down and values[i] > values[i - 1]):
            up = down = 0
        if values[i] > values[i - 1]:
            up += 1
        elif values[i] < values[i - 1]:
            down += 1
        if up and down:
            best = max(best, up + down + 1)
    return best
