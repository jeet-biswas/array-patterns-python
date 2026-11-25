def minimum_parallel_resources(intervals: list[tuple[int, int]]) -> int:
    """Minimum resources for nonempty [start,end) intervals; no mutation.

    Touching intervals can reuse a resource. Invalid ranges raise ValueError.
    """
    events = []
    for start, end in intervals:
        if start >= end:
            raise ValueError('nonempty half-open intervals required')
        events.extend(((start, 1), (end, -1)))
    active = best = 0
    for _, change in sorted(events):
        active += change
        best = max(best, active)
    return best
