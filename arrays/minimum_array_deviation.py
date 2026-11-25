import heapq


def minimum_array_deviation(values: list[int]) -> int:
    """Smallest max-min after repeatedly doubling odd or halving even elements.

    Positive integers required; empty returns zero. Input is unchanged.
    """
    if any(x <= 0 for x in values):
        raise ValueError('positive values required')
    if not values:
        return 0
    normalized = [x*2 if x % 2 else x for x in values]
    minimum = min(normalized)
    heap = [-x for x in normalized]
    heapq.heapify(heap)
    best = max(normalized)-minimum
    while True:
        maximum = -heapq.heappop(heap)
        best = min(best, maximum-minimum)
        if maximum % 2:
            return best
        reduced = maximum//2
        minimum = min(minimum, reduced)
        heapq.heappush(heap, -reduced)
