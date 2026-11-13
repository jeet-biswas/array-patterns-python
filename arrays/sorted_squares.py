def sorted_squares(values: list[int]) -> list[int]:
    """Square nondecreasing integers and return sorted results without mutation.

    Sortedness is a precondition, not checked. O(n) time and output space;
    O(1) auxiliary space beyond the result. Empty input returns [].
    """
    result = [0] * len(values)
    left, right = 0, len(values) - 1
    for write in range(len(values) - 1, -1, -1):
        if abs(values[left]) > abs(values[right]):
            result[write] = values[left] ** 2
            left += 1
        else:
            result[write] = values[right] ** 2
            right -= 1
    return result
