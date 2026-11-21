def minimum_interval_removals(intervals: list[tuple[int, int]]) -> int:
    """Remove the fewest intervals so nonempty [start,end) ranges do not overlap.

    Requires start < end. Input is unchanged.
    """
    if any(start >= end for start, end in intervals):
        raise ValueError('nonempty intervals required')
    finish = None
    kept = 0
    for start, end in sorted(intervals, key=lambda interval: interval[1]):
        if finish is None or start >= finish:
            finish = end
            kept += 1
    return len(intervals)-kept
