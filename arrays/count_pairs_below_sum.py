def count_pairs_below_sum(values: list[int], threshold: int) -> int:
    """Count index pairs i < j whose sum is strictly below threshold.

    Signed integers and duplicates supported. O(n log n) time, O(n) space.
    Input is unchanged.
    """
    ordered = sorted(values)
    left, right = 0, len(ordered) - 1
    total = 0
    while left < right:
        if ordered[left] + ordered[right] < threshold:
            total += right - left
            left += 1
        else:
            right -= 1
    return total
