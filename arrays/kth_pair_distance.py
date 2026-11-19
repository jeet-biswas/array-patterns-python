def kth_pair_distance(values: list[int], k: int) -> int:
    """Kth smallest absolute difference over distinct index pairs, one-based k.

    Invalid k raises ValueError. Signed values and duplicates allowed.
    O(n log n + n log(D+1)) time for span D, O(n) space; no mutation.
    """
    n = len(values)
    if not 1 <= k <= n * (n - 1) // 2:
        raise ValueError('k must identify an existing index pair')
    ordered = sorted(values)
    low, high = 0, ordered[-1] - ordered[0]
    while low < high:
        distance = (low + high) // 2
        left = count = 0
        for right in range(n):
            while ordered[right] - ordered[left] > distance:
                left += 1
            count += right - left
        if count >= k:
            high = distance
        else:
            low = distance + 1
    return low
