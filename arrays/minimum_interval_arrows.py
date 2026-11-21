def minimum_interval_arrows(intervals: list[tuple[int, int]]) -> int:
    """Minimum points intersecting every closed [start,end]; no mutation.

    Reversed endpoints raise ValueError; zero-width intervals are allowed.
    """
    if any(start > end for start, end in intervals):
        raise ValueError('start must not exceed end')
    point = None
    total = 0
    for start, end in sorted(intervals, key=lambda interval: interval[1]):
        if point is None or start > point:
            point = end
            total += 1
    return total
