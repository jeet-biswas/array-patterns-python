def shortest_unsorted_window(values: list[int]) -> int:
    """Length of the shortest contiguous window whose sorting sorts the array.

    Nondecreasing input returns zero. O(n) time, O(1) space; no mutation.
    """
    if not values:
        return 0
    maximum = values[0]
    end = -1
    for i, value in enumerate(values):
        maximum = max(maximum, value)
        if value < maximum:
            end = i
    if end == -1:
        return 0
    minimum = values[-1]
    start = 0
    for i in range(len(values) - 1, -1, -1):
        minimum = min(minimum, values[i])
        if values[i] > minimum:
            start = i
    return end - start + 1
