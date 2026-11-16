def max_absolute_subarray(values: list[int]) -> int:
    """Maximum absolute contiguous sum; empty input returns zero.

    O(n) time and O(1) space; input is unchanged.
    """
    prefix = smallest = largest = 0
    for value in values:
        prefix += value
        smallest = min(smallest, prefix)
        largest = max(largest, prefix)
    return largest - smallest
