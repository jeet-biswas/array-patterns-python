from functools import lru_cache
from math import gcd


def max_weighted_gcd_pairing(values: list[int]) -> int:
    """Pair all indices, scoring round*gcd(pair) for rounds starting at one.

    Even-length positive input required. Empty -> 0; input is unchanged.
    Exponential algorithm intended for small arrays.
    """
    n = len(values)
    if n % 2 or any(x <= 0 for x in values):
        raise ValueError('even length and positive values required')
    common = [[gcd(x, y) for y in values] for x in values]
    full = (1 << n)-1
    @lru_cache(None)
    def solve(mask):
        if mask == full:
            return 0
        multiplier = mask.bit_count()//2+1
        best = 0
        for i in range(n):
            if mask >> i & 1: continue
            for j in range(i+1, n):
                if not mask >> j & 1:
                    best = max(best, multiplier*common[i][j]+solve(mask | (1 << i) | (1 << j)))
        return best
    return solve(0)
