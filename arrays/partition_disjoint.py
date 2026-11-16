def partition_disjoint(values: list[int]) -> int | None:
    """Smallest split with two nonempty parts and max(left) <= min(right).

    Return left length, or None when no split exists. O(n) time, O(1) space.
    Input is unchanged.
    """
    if len(values) < 2:
        return None
    left_max = seen_max = values[0]
    boundary = 0
    for i in range(1, len(values)):
        seen_max = max(seen_max, values[i])
        if values[i] < left_max:
            boundary = i
            left_max = seen_max
    return boundary + 1 if boundary < len(values) - 1 else None
