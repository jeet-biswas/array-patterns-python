def smallest_missing_positive(values: list[int]) -> int:
    """Return the smallest absent positive integer, rearranging input in place.

    Signed integers and duplicates are accepted. Empty -> 1.
    O(n) time and O(1) auxiliary space.
    """
    n = len(values)
    for i in range(n):
        while 1 <= values[i] <= n and values[values[i] - 1] != values[i]:
            destination = values[i] - 1
            values[i], values[destination] = values[destination], values[i]
    for i, value in enumerate(values):
        if value != i + 1:
            return i + 1
    return n + 1
