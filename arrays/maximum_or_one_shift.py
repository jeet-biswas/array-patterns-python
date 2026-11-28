def maximum_or_one_shift(values: list[int], shift: int) -> int:
    """Choose exactly one value to left-shift by shift bits, maximizing whole-array OR.

    Nonnegative values and shift required. Empty returns zero; no mutation.
    """
    if shift < 0 or any(x < 0 for x in values): raise ValueError('nonnegative inputs required')
    suffix = [0]*(len(values)+1)
    for i in range(len(values)-1, -1, -1): suffix[i] = suffix[i+1] | values[i]
    prefix = best = 0
    for i, value in enumerate(values):
        best = max(best, prefix | (value << shift) | suffix[i+1])
        prefix |= value
    return best
