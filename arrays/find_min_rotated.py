def find_min_rotated(values: list[int]) -> int:
    """Minimum of a nonempty rotation of nondecreasing input (unchecked).

    Duplicates allowed. Empty raises ValueError. O(log n) with distinct
    values, O(n) worst case with duplicates; O(1) space. No mutation.
    """
    if not values:
        raise ValueError('values must be nonempty')
    left, right = 0, len(values) - 1
    while left < right:
        middle = (left + right) // 2
        if values[middle] < values[right]:
            right = middle
        elif values[middle] > values[right]:
            left = middle + 1
        else:
            right -= 1
    return values[left]
