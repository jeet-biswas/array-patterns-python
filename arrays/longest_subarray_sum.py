def longest_subarray_sum(values: list[int], target: int) -> int:
    """Longest contiguous subarray length with sum target; no match -> 0.

    Signed integers and zeros are supported. Expected O(n) time and O(n)
    space under expected constant-time dictionary operations. No mutation.
    """
    first = {0: -1}
    prefix = best = 0
    for i, value in enumerate(values):
        prefix += value
        if prefix - target in first:
            best = max(best, i - first[prefix - target])
        first.setdefault(prefix, i)
    return best
