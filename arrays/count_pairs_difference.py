def count_pairs_difference(values: list[int], difference: int) -> int:
    """Count i < j with abs(values[i]-values[j]) == difference.

    Negative difference raises ValueError. Expected O(n) time, O(n) space.
    Signed values supported; input is unchanged.
    """
    if difference < 0:
        raise ValueError('difference must be nonnegative')
    frequencies = {}
    total = 0
    for value in values:
        total += frequencies.get(value - difference, 0)
        if difference:
            total += frequencies.get(value + difference, 0)
        frequencies[value] = frequencies.get(value, 0) + 1
    return total
