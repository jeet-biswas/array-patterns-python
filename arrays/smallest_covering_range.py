import heapq


def smallest_covering_range(arrays: list[list[int]]) -> tuple[int, int]:
    """Smallest inclusive range containing at least one value from every array.

    Ties prefer the smaller left endpoint. Nonempty sorted arrays required; no mutation.
    """
    if not arrays or any(not a for a in arrays):
        raise ValueError('at least one nonempty array required')
    if any(a[i-1] > a[i] for a in arrays for i in range(1, len(a))):
        raise ValueError('arrays must be sorted')
    heap = [(a[0], row, 0) for row, a in enumerate(arrays)]
    heapq.heapify(heap)
    maximum = max(a[0] for a in arrays)
    best = (heap[0][0], maximum)
    while True:
        minimum, row, column = heapq.heappop(heap)
        if (maximum-minimum, minimum) < (best[1]-best[0], best[0]):
            best = (minimum, maximum)
        column += 1
        if column == len(arrays[row]):
            return best
        value = arrays[row][column]
        maximum = max(maximum, value)
        heapq.heappush(heap, (value, row, column))
