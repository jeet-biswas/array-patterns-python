from bisect import bisect_right


def max_value_k_events(events: list[tuple[int, int, int]], k: int) -> int:
    """Maximum sum of values from <= k nonoverlapping closed (start,end,value) events.

    Signed event values allowed, selecting none yields zero. Invalid ranges or negative
    k raise ValueError. Input is unchanged.
    """
    if k < 0 or any(start > end for start, end, _ in events):
        raise ValueError('nonnegative k and valid closed intervals required')
    ordered = sorted(events)
    starts = [event[0] for event in ordered]
    following = [bisect_right(starts, end) for _, end, _ in ordered]
    previous = [0]*(len(events)+1)
    for _ in range(min(k, len(events))):
        current = [0]*(len(events)+1)
        for i in range(len(events)-1, -1, -1):
            current[i] = max(current[i+1], ordered[i][2]+previous[following[i]])
        previous = current
    return previous[0]
