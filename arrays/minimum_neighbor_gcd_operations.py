from math import gcd


def minimum_neighbor_gcd_operations(values: list[int]) -> int:
    """Fewest operations replacing either of two neighbors by their GCD to make all ones.

    Positive values required; impossible -> -1, empty -> 0. Input is unchanged.
    """
    if any(x <= 0 for x in values):
        raise ValueError('positive values required')
    n = len(values)
    ones = values.count(1)
    if ones or not values:
        return n-ones
    shortest = n+1
    for start in range(n):
        common = 0
        for end in range(start, n):
            common = gcd(common, values[end])
            if common == 1:
                shortest = min(shortest, end-start+1)
                break
    return n+shortest-2 if shortest <= n else -1
