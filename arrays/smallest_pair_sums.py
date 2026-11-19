import heapq


def smallest_pair_sums(left: list[int], right: list[int], k: int) -> list[tuple[int, int]]:
    """First k pairs ordered by (sum, left value, right value), preserving multiplicity.

    Inputs must be nondecreasing (unchecked); negative k raises ValueError.
    Returns all pairs if k exceeds their count. O(r+t*log(r+1)) time,
    O(r) heap space plus output, r=min(k,len(left)), t=min(k,n*m). No mutation.
    """
    if k < 0:
        raise ValueError('k must be nonnegative')
    if not left or not right or k == 0:
        return []
    heap = [(left[i] + right[0], i, 0) for i in range(min(k, len(left)))]
    heapq.heapify(heap)
    result = []
    while heap and len(result) < k:
        _, i, j = heapq.heappop(heap)
        result.append((left[i], right[j]))
        if j + 1 < len(right):
            heapq.heappush(heap, (left[i] + right[j+1], i, j+1))
    return result
