import heapq


def max_attendable_events(events: list[tuple[int, int]]) -> int:
    """Maximum events attended, each on one integer day in its inclusive range.

    One event per day. Reversed endpoints raise ValueError; no mutation.
    """
    if any(start > end for start, end in events):
        raise ValueError('start must not exceed end')
    ordered = sorted(events)
    deadlines = []
    index = total = 0
    day = ordered[0][0] if ordered else 0
    while index < len(ordered) or deadlines:
        if not deadlines:
            day = max(day, ordered[index][0])
        while index < len(ordered) and ordered[index][0] <= day:
            heapq.heappush(deadlines, ordered[index][1])
            index += 1
        while deadlines and deadlines[0] < day:
            heapq.heappop(deadlines)
        if deadlines:
            heapq.heappop(deadlines)
            total += 1
            day += 1
    return total
