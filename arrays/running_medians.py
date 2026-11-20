import heapq


def running_medians(values: list[int]) -> list[float]:
    """Median of every nonempty prefix, as floats; empty -> [].

    Inputs should have float-representable magnitudes. O(n log(n+1)) time,
    O(n) space including heaps and output; input is unchanged.
    """
    lower, upper, result = [], [], []
    for value in values:
        if not lower or value <= -lower[0]:
            heapq.heappush(lower, -value)
        else:
            heapq.heappush(upper, value)
        if len(lower) > len(upper) + 1:
            heapq.heappush(upper, -heapq.heappop(lower))
        elif len(upper) > len(lower):
            heapq.heappush(lower, -heapq.heappop(upper))
        result.append(float(-lower[0]) if len(lower) > len(upper)
                      else (-lower[0] + upper[0]) / 2)
    return result
