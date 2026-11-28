def missing_numbers_one_to_n(values: list[int]) -> list[int]:
    """Find missing values in 1..n; all input entries must already be in that range.

    Temporarily marks the mutable input, then restores it before returning.
    Output is ascending; empty input is valid.
    """
    n = len(values)
    if any(not 1 <= x <= n for x in values): raise ValueError('values outside 1..n')
    for i in range(n):
        index = abs(values[i])-1
        values[index] = -abs(values[index])
    result = [i+1 for i in range(n) if values[i] > 0]
    for i in range(n): values[i] = abs(values[i])
    return result
