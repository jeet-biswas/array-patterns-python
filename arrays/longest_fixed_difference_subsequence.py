def longest_fixed_difference_subsequence(values: list[int], difference: int) -> int:
    """Longest subsequence whose consecutive differences equal difference; no mutation."""
    lengths = {}
    best = 0
    for value in values:
        length = lengths.get(value-difference, 0) + 1
        lengths[value] = max(lengths.get(value, 0), length)
        best = max(best, lengths[value])
    return best
