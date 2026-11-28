from bisect import bisect_left


def range_value_frequencies(values: list[int], queries: list[tuple[int, int, int]]) -> list[int]:
    """Answer (start,end,value) counts in half-open ranges; no mutation.

    Invalid bounds raise IndexError; empty ranges are valid.
    """
    positions = {}
    for i, value in enumerate(values): positions.setdefault(value, []).append(i)
    result = []
    for start, end, value in queries:
        if not 0 <= start <= end <= len(values): raise IndexError('invalid range')
        indices = positions.get(value, [])
        result.append(bisect_left(indices, end)-bisect_left(indices, start))
    return result
