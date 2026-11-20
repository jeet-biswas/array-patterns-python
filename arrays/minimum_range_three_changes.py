def minimum_range_three_changes(values: list[int]) -> int:
    """Smallest max-min after changing up to three elements to arbitrary integers.

    Empty -> 0. O(n log n) time, O(n) space; input is unchanged.
    """
    if len(values) <= 4:
        return 0
    ordered = sorted(values)
    return min(ordered[len(values)-4+left] - ordered[left] for left in range(4))
