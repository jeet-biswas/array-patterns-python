def equal_range(values: list[int], target: int) -> tuple[int, int]:
    """Return [start, stop) bounding target in nondecreasing input (unchecked).

    If absent, both bounds equal its insertion position. Empty -> (0, 0).
    O(log(n+1)) time, O(1) space; input is unchanged.
    """
    def bound(upper):
        left, right = 0, len(values)
        while left < right:
            middle = (left + right) // 2
            if values[middle] < target or (upper and values[middle] == target):
                left = middle + 1
            else:
                right = middle
        return left
    return bound(False), bound(True)
