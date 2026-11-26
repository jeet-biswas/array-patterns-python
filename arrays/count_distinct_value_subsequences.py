def count_distinct_value_subsequences(values: list[int]) -> int:
    """Count distinct nonempty value sequences obtainable by deleting indices.

    Equal value sequences count once, regardless of chosen indices. Exact result;
    input is unchanged.
    """
    total = 1
    previous = {}
    for value in values:
        following = 2*total-previous.get(value, 0)
        previous[value] = total
        total = following
    return total-1
