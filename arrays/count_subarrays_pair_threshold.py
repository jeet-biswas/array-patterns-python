def count_subarrays_pair_threshold(values: list[int], k: int) -> int:
    """Count nonempty subarrays with >= k equal-value index pairs; no mutation.

    k must be nonnegative; zero accepts every nonempty subarray.
    """
    if k < 0:
        raise ValueError('k must be nonnegative')
    if k == 0:
        return len(values) * (len(values)+1) // 2
    counts = {}
    left = pairs = total = 0
    for value in values:
        pairs += counts.get(value, 0)
        counts[value] = counts.get(value, 0) + 1
        while pairs >= k:
            removed = values[left]
            counts[removed] -= 1
            pairs -= counts[removed]
            left += 1
        total += left
    return total
