def max_uncrossed_matches(first: list[int], second: list[int]) -> int:
    """Maximum equal-value index matches preserving order in both arrays; no mutation."""
    previous = [0] * (len(second)+1)
    for x in first:
        current = [0]
        for j, y in enumerate(second, 1):
            current.append(previous[j-1]+1 if x == y else max(previous[j], current[-1]))
        previous = current
    return previous[-1]
