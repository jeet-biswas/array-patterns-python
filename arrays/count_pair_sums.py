def count_pair_sums(values: list[int], target: int) -> int:
    """Count i < j with values[i]+values[j] == target; signed integers allowed.

    Expected O(n) time and O(n) space; input is unchanged.
    """
    frequencies = {}
    total = 0
    for value in values:
        total += frequencies.get(target - value, 0)
        frequencies[value] = frequencies.get(value, 0) + 1
    return total
