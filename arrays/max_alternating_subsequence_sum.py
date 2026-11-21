def max_alternating_subsequence_sum(values: list[int]) -> int:
    """Maximize x0-x1+x2-... over subsequences, including empty; no mutation."""
    even, odd = 0, None
    for value in values:
        next_odd = max(odd, even + value) if odd is not None else even + value
        even = max(even, odd - value) if odd is not None else even
        odd = next_odd
    return max(even, odd) if odd is not None else even
