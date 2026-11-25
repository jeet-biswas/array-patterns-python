def max_spliced_array_sum(first: list[int], second: list[int]) -> int:
    """Largest total of either array after swapping at most one same-index segment.

    Equal lengths required, signed values allowed. Empty returns zero; no mutation.
    """
    if len(first) != len(second):
        raise ValueError('equal lengths required')
    gain_a = gain_b = best_a = best_b = 0
    total_a = total_b = 0
    for a, b in zip(first, second):
        total_a += a
        total_b += b
        gain_a = max(0, gain_a+b-a)
        gain_b = max(0, gain_b+a-b)
        best_a = max(best_a, gain_a)
        best_b = max(best_b, gain_b)
    return max(total_a+best_a, total_b+best_b)
