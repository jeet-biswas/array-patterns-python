def max_chunks_sorted(values: list[int]) -> int:
    """Most contiguous chunks whose individually sorted concatenation is sorted.

    Duplicates and signed integers are supported. Empty -> 0.
    O(n) time, O(n) space; input is unchanged.
    """
    maxima = []
    for value in values:
        if not maxima or value >= maxima[-1]:
            maxima.append(value)
        else:
            maximum = maxima.pop()
            while maxima and maxima[-1] > value:
                maxima.pop()
            maxima.append(maximum)
    return len(maxima)
