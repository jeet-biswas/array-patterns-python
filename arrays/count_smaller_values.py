from collections import Counter


def count_smaller_values(values: list[int]) -> list[int]:
    """For each index, count all array elements strictly smaller than its value.

    Counts include both sides of the index. Signed values allowed; no mutation.
    """
    counts = Counter(values)
    smaller = {}
    total = 0
    for value in sorted(counts):
        smaller[value] = total
        total += counts[value]
    return [smaller[value] for value in values]
