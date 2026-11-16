def peak_index(values: list[int]) -> int:
    """Return any strict local maximum index, or -1 for empty input.

    Adjacent values must differ (unchecked). Endpoints have one neighbor.
    O(log(n+1)) time, O(1) space; no mutation.
    """
    if not values:
        return -1
    left, right = 0, len(values) - 1
    while left < right:
        middle = (left + right) // 2
        if values[middle] < values[middle + 1]:
            left = middle + 1
        else:
            right = middle
    return left
