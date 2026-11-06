def count_subarrays_sum(values: list[int], target: int) -> int:
    """Count nonempty contiguous subarrays with sum target, including overlaps.

    Works with negative values and zeros. Expected O(n) time, O(n) space.
    """
    counts = {0: 1}
    prefix = total = 0
    for value in values:
        prefix += value
        total += counts.get(prefix - target, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
    return total
