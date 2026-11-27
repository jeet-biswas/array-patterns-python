from functools import lru_cache
from math import isqrt


def count_square_sum_permutations(values: list[int]) -> int:
    """Count distinct value permutations with perfect-square sums at every adjacency.

    Nonnegative integers required; empty has one permutation. Input is unchanged.
    Exponential algorithm intended for small arrays.
    """
    if any(x < 0 for x in values):
        raise ValueError('nonnegative values required')
    ordered = sorted(values)
    n = len(ordered)
    compatible = [[isqrt(a+b)**2 == a+b for b in ordered] for a in ordered]
    full = (1 << n)-1
    @lru_cache(None)
    def count(mask, last):
        if mask == full:
            return 1
        total = 0
        for i, value in enumerate(ordered):
            if mask >> i & 1:
                continue
            if i and ordered[i-1] == value and not mask >> (i-1) & 1:
                continue
            if last == -1 or compatible[last][i]:
                total += count(mask | (1 << i), i)
        return total
    return count(0, -1)
