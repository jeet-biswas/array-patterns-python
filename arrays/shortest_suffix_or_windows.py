def shortest_suffix_or_windows(values: list[int]) -> list[int]:
    """For every i, shortest nonempty values[i:j] with OR equal to values[i:].

    Nonnegative values required; input is unchanged.
    """
    if any(x < 0 for x in values): raise ValueError('nonnegative values required')
    bits = max(1, max(values, default=0).bit_length())
    nearest = [-1]*bits
    result = [0]*len(values)
    for i in range(len(values)-1, -1, -1):
        for bit in range(bits):
            if values[i] >> bit & 1: nearest[bit] = i
        result[i] = max(i, max(nearest))-i+1
    return result
