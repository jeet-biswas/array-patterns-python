def search_rotated(values: list[int], target: int) -> int:
    """Index of target in a rotation of a strictly increasing array, else -1.

    Distinct, rotated-sorted input is required but not checked.
    O(log n) time, O(1) space; no mutation.
    """
    left, right = 0, len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[left] <= values[middle]:
            if values[left] <= target < values[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if values[middle] < target <= values[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1
