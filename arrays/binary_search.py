def binary_search(values: list[int], target: int) -> int:
    """Return first matching index in a sorted array, or -1 if absent.

    Input must be nondecreasing (not checked). O(log n) time, O(1) space.
    """
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left if left < len(values) and values[left] == target else -1
