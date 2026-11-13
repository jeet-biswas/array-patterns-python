def min_jumps(values: list[int]) -> int:
    """Each value is a maximum forward jump. Return fewest jumps, or -1 if stuck.

    Empty/singleton -> 0. Negative jump lengths raise ValueError.
    O(n) time, O(1) space; input is unchanged.
    """
    if any(value < 0 for value in values):
        raise ValueError('jump lengths must be nonnegative')
    if len(values) < 2:
        return 0
    end = farthest = jumps = 0
    for i in range(len(values) - 1):
        farthest = max(farthest, i + values[i])
        if i == end:
            if farthest == end:
                return -1
            jumps += 1
            end = farthest
            if end >= len(values) - 1:
                return jumps
    return -1
