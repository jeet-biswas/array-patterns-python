def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge closed [start, end] pairs, sorted by start; input is unchanged.

    Reversed or non-pair intervals raise ValueError. Touching intervals merge.
    O(n log n) time and O(n) space including the sorting copy and output.
    """
    if any(len(pair) != 2 or pair[0] > pair[1] for pair in intervals):
        raise ValueError('each interval must have two endpoints with start <= end')
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged
