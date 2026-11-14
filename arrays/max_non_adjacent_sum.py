def max_non_adjacent_sum(values: list[int]) -> int:
    """Maximum sum selecting no adjacent indices; empty selection yields zero.

    Signed values are allowed. O(n) time, O(1) space; no mutation.
    """
    previous = before_previous = 0
    for value in values:
        previous, before_previous = max(previous, before_previous + value), previous
    return previous
