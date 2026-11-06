def array_leaders(values: list[int]) -> list[int]:
    """Return strict right-side leaders in original order; last item qualifies.

    Equal values to the right disqualify an earlier item. O(n) time,
    O(1) auxiliary space excluding output (which may have n elements).
    """
    result = []
    maximum = None
    for i in range(len(values) - 1, -1, -1):
        if maximum is None or values[i] > maximum:
            result.append(values[i])
            maximum = values[i]
    result.reverse()
    return result
