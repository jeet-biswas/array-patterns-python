from collections import Counter
import heapq


def top_k_frequent_values(values: list[int], k: int) -> list[int]:
    """Return k distinct values ordered by descending frequency then ascending value.

    Requires 0 <= k <= distinct count. Input is unchanged.
    """
    counts = Counter(values)
    if not 0 <= k <= len(counts): raise ValueError('invalid count')
    if k == 0: return []
    heap = []
    for value, count in counts.items():
        pair = (count, -value)
        if len(heap) < k: heapq.heappush(heap, pair)
        elif pair > heap[0]: heapq.heapreplace(heap, pair)
    return [-value for count, value in sorted(heap, reverse=True)]
