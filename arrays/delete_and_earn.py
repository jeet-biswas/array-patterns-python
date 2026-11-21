from collections import Counter


def delete_and_earn(values: list[int]) -> int:
    """Choose values for their total frequency-weighted score, forbidding x and x+1.

    Values must be nonnegative. Input is unchanged.
    """
    if any(x < 0 for x in values):
        raise ValueError('values must be nonnegative')
    counts = Counter(values)
    take = skip = 0
    previous = None
    for value in sorted(counts):
        best = max(take, skip)
        take = (skip if previous is not None and value == previous + 1 else best) + value * counts[value]
        skip = best
        previous = value
    return max(take, skip)
