import heapq


def total_hiring_cost(costs: list[int], k: int, candidates: int) -> int:
    """Run k hiring rounds, choosing cheapest among first/last candidates remaining.

    Ties use smaller original index. Nonnegative costs, positive candidates and
    0 <= k <= len(costs) required. Input is unchanged.
    """
    if candidates <= 0 or not 0 <= k <= len(costs) or any(x < 0 for x in costs):
        raise ValueError('invalid costs, hiring count or candidate count')
    left, right = 0, len(costs)-1
    heap = []
    for _ in range(min(candidates, len(costs))):
        heapq.heappush(heap, (costs[left], left))
        left += 1
    for _ in range(min(candidates, right-left+1)):
        heapq.heappush(heap, (costs[right], right))
        right -= 1
    total = 0
    for _ in range(k):
        cost, index = heapq.heappop(heap)
        total += cost
        if left <= right:
            if index < left:
                heapq.heappush(heap, (costs[left], left))
                left += 1
            else:
                heapq.heappush(heap, (costs[right], right))
                right -= 1
    return total
