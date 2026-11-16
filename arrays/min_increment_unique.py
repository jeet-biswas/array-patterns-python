def min_increment_unique(values: list[int]) -> int:
    """Minimum total +1 operations required for all values to be distinct.

    Empty -> 0. O(n log n) time, O(n) sorting space; input is unchanged.
    """
    next_free = None
    operations = 0
    for value in sorted(values):
        assigned = value if next_free is None else max(value, next_free)
        operations += assigned - value
        next_free = assigned + 1
    return operations
