def kth_smallest_subarray_sum(values: list[int], k: int) -> int:
    """One-based kth subarray sum, counting multiplicities; no mutation.

    Nonnegative elements and 1 <= k <= n*(n+1)//2 required.
    """
    n = len(values)
    if any(x < 0 for x in values) or not 1 <= k <= n*(n+1)//2:
        raise ValueError('nonnegative values and valid rank required')
    low, high = 0, sum(values)
    while low < high:
        middle = (low+high)//2
        left = total = count = 0
        for right, value in enumerate(values):
            total += value
            while total > middle:
                total -= values[left]
                left += 1
            count += right-left+1
        if count >= k:
            high = middle
        else:
            low = middle+1
    return low
