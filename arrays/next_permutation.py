def next_permutation(values: list[int]) -> bool:
    """Advance in place and return True, or wrap to first permutation and return False.

    Empty/singleton inputs return False. Duplicates are supported.
    O(n) time and O(1) extra space.
    """
    pivot = len(values) - 2
    while pivot >= 0 and values[pivot] >= values[pivot + 1]:
        pivot -= 1
    if pivot < 0:
        values.reverse()
        return False
    successor = len(values) - 1
    while values[successor] <= values[pivot]:
        successor -= 1
    values[pivot], values[successor] = values[successor], values[pivot]
    left, right = pivot + 1, len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1
    return True
