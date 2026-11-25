from collections import Counter


def four_array_sum_count(first: list[int], second: list[int], third: list[int], fourth: list[int], target: int = 0) -> int:
    """Count one-index-per-array selections with the requested sum; no mutation."""
    pairs = Counter(x+y for x in first for y in second)
    return sum(pairs[target-x-y] for x in third for y in fourth)
