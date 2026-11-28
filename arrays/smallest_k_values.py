import heapq


def smallest_k_values(values: list[int], k: int) -> list[int]:
    """Return sorted k smallest values, including multiplicities; no mutation.

    Requires 0 <= k <= len(values).
    """
    if not 0 <= k <= len(values): raise ValueError('invalid count')
    if k == 0: return []
    heap = [-values[i] for i in range(k)]
    heapq.heapify(heap)
    for i in range(k, len(values)):
        if values[i] < -heap[0]: heapq.heapreplace(heap, -values[i])
    return sorted(-x for x in heap)
