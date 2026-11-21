from collections import Counter


def can_pair_doubles(values: list[int]) -> bool:
    """Whether every element can be used in a pair (x, 2*x); signed values allowed.

    Empty is valid. Input is unchanged.
    """
    if len(values) % 2:
        return False
    counts = Counter(values)
    if counts[0] % 2:
        return False
    counts[0] = 0
    for value in sorted(counts, key=abs):
        needed = counts[value]
        if counts[2*value] < needed:
            return False
        counts[2*value] -= needed
        counts[value] = 0
    return True
