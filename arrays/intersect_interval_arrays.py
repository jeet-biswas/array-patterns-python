def intersect_interval_arrays(first: list[tuple[int, int]], second: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Intersections of sorted, strictly disjoint closed intervals; no mutation.

    Malformed ordering, overlapping intervals, or reversed endpoints raise ValueError.
    """
    for intervals in (first, second):
        previous_end = None
        for start, end in intervals:
            if start > end or previous_end is not None and start <= previous_end:
                raise ValueError('sorted disjoint closed intervals required')
            previous_end = end
    i = j = 0
    result = []
    while i < len(first) and j < len(second):
        start = max(first[i][0], second[j][0])
        end = min(first[i][1], second[j][1])
        if start <= end:
            result.append((start, end))
        if first[i][1] < second[j][1]:
            i += 1
        else:
            j += 1
    return result
