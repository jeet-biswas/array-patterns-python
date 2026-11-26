from collections import Counter
from math import factorial


def multiset_permutation_rank(values: list[int]) -> int:
    """One-based lexicographic rank among distinct permutations of these values.

    Signed integers and duplicates allowed; empty rank is one. No mutation.
    """
    counts = Counter(values)
    keys = sorted(counts)
    total = factorial(len(values))
    for count in counts.values():
        total //= factorial(count)
    rank = 1
    remaining = len(values)
    for value in values:
        smaller = 0
        for key in keys:
            if key >= value: break
            smaller += counts[key]
        rank += total*smaller//remaining
        total = total*counts[value]//remaining
        counts[value] -= 1
        remaining -= 1
    return rank
