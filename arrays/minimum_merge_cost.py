import heapq


def minimum_merge_cost(weights: list[int]) -> int:
    """Merge any two weights at cost their sum until at most one remains; no mutation.

    All weights must be nonnegative. Empty and singleton arrays cost zero.
    """
    if any(x < 0 for x in weights):
        raise ValueError('nonnegative weights required')
    heap = list(weights)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        merged = heapq.heappop(heap)+heapq.heappop(heap)
        total += merged
        heapq.heappush(heap, merged)
    return total
