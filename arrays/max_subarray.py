def max_subarray(values: list[int]) -> int:
    """Maximum sum of a nonempty contiguous subarray; raises ValueError if empty.

    O(n) time and O(1) extra space. Input is not modified.
    """
    if not values:
        raise ValueError('values must be nonempty')
    ending = best = values[0]
    for index in range(1, len(values)):
        ending = max(values[index], ending + values[index])
        best = max(best, ending)
    return best
