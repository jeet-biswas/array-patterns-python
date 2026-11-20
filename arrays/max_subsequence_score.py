import heapq


def max_subsequence_score(first: list[int], second: list[int], k: int) -> int:
    """Choose k common indices maximizing sum(first selected)*min(second selected).

    Equal lengths, nonnegative elements and 1 <= k <= n required, else
    ValueError. O(n log n+n log(k+1)) time, O(n+k) space; no mutation.
    """
    if (len(first) != len(second) or not 1 <= k <= len(first)
            or any(x < 0 for x in first) or any(x < 0 for x in second)):
        raise ValueError('equal nonnegative arrays and valid k are required')
    heap = []
    total = best = 0
    for minimum, value in sorted(zip(second, first), reverse=True):
        heapq.heappush(heap, value)
        total += value
        if len(heap) > k:
            total -= heapq.heappop(heap)
        if len(heap) == k:
            best = max(best, total * minimum)
    return best
