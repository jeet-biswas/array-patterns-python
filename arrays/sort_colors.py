def sort_colors(values: list[int]) -> None:
    """Sort an array of 0/1/2 in place; invalid values raise ValueError first.

    O(n) time and O(1) extra space, returns None.
    """
    if any(value not in (0, 1, 2) for value in values):
        raise ValueError('only 0, 1, and 2 are accepted')
    low = mid = 0
    high = len(values) - 1
    while mid <= high:
        if values[mid] == 0:
            values[low], values[mid] = values[mid], values[low]
            low += 1
            mid += 1
        elif values[mid] == 1:
            mid += 1
        else:
            values[mid], values[high] = values[high], values[mid]
            high -= 1
