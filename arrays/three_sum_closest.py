def three_sum_closest(values: list[int], target: int) -> int:
    """Closest sum of three distinct indices; ties choose the smaller sum.

    Fewer than three elements raises ValueError. No mutation.
    O(n squared) time and O(n) auxiliary space for sorting.
    """
    if len(values) < 3:
        raise ValueError('at least three values are required')
    ordered = sorted(values)
    best = sum(ordered[:3])
    for i in range(len(ordered) - 2):
        left, right = i + 1, len(ordered) - 1
        while left < right:
            total = ordered[i] + ordered[left] + ordered[right]
            if (abs(total - target), total) < (abs(best - target), best):
                best = total
            if total == target:
                return total
            if total < target:
                left += 1
            else:
                right -= 1
    return best
