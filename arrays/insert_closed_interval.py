def insert_closed_interval(intervals: list[tuple[int, int]], new: tuple[int, int]) -> list[tuple[int, int]]:
    """Insert a closed interval, merging overlaps including shared endpoints; no mutation.

    Original intervals must be sorted and strictly disjoint. Invalid input raises ValueError.
    """
    start, end = new
    if start > end:
        raise ValueError('reversed new interval')
    previous = None
    for left, right in intervals:
        if left > right or previous is not None and left <= previous:
            raise ValueError('sorted disjoint closed intervals required')
        previous = right
    result = []
    i = 0
    while i < len(intervals) and intervals[i][1] < start:
        result.append(tuple(intervals[i]))
        i += 1
    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    result.append((start, end))
    result.extend(tuple(interval) for interval in intervals[i:])
    return result
