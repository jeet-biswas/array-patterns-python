def count_bad_pairs(values: list[int]) -> int:
    """Count i < j where j-i differs from values[j]-values[i].

    Expected O(n) time, O(n) space; signed integers allowed, no mutation.
    """
    frequencies = {}
    total = 0
    for i, value in enumerate(values):
        key = value - i
        total += i - frequencies.get(key, 0)
        frequencies[key] = frequencies.get(key, 0) + 1
    return total
