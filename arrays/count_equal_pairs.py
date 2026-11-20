def count_equal_pairs(values: list[int]) -> int:
    """Count i < j with values[i] == values[j].

    Expected O(n) time, O(n) space under constant-time hashing; no mutation.
    """
    frequencies = {}
    total = 0
    for value in values:
        total += frequencies.get(value, 0)
        frequencies[value] = frequencies.get(value, 0) + 1
    return total
