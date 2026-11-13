def min_length_sum(values: list[int], target: int) -> int:
    """Shortest nonempty subarray with sum >= target, or 0 if none.

    Requires target > 0 and nonnegative elements; otherwise ValueError.
    O(n) time and O(1) auxiliary space, without modifying values.
    """
    if target <= 0 or any(value < 0 for value in values):
        raise ValueError('target must be positive and values nonnegative')
    left = total = 0
    best = len(values) + 1
    for right, value in enumerate(values):
        total += value
        while total >= target:
            best = min(best, right - left + 1)
            total -= values[left]
            left += 1
    return best if best <= len(values) else 0
