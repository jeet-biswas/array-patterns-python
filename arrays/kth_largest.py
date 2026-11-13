import heapq


def kth_largest(values: list[int], k: int) -> int:
    """Return kth largest value counting duplicates; require 1 <= k <= n.

    Invalid k raises ValueError. O(n log(k+1)) time, O(k) extra space.
    The input is unchanged.
    """
    if not 1 <= k <= len(values):
        raise ValueError('k must be between 1 and array length')
    heap = values[:k]
    heapq.heapify(heap)
    for i in range(k, len(values)):
        if values[i] > heap[0]:
            heapq.heapreplace(heap, values[i])
    return heap[0]
