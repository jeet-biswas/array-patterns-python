def max_width_ramp(values: list[int]) -> int:
    """Maximum j-i for i < j and values[i] <= values[j], or 0 if no pair.

    O(n) time and O(n) space; input is unchanged.
    """
    candidates = []
    for i, value in enumerate(values):
        if not candidates or value < values[candidates[-1]]:
            candidates.append(i)
    best = 0
    for right in range(len(values) - 1, -1, -1):
        while candidates and values[candidates[-1]] <= values[right]:
            best = max(best, right - candidates.pop())
    return best
