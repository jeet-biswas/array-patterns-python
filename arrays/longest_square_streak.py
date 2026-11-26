def longest_square_streak(values: list[int]) -> int:
    """Longest chain x,x*x,... from a reordered subset, or -1 if shorter than two.

    Integer values >= 2 required; duplicates allowed. Input is unchanged.
    """
    if any(x < 2 for x in values):
        raise ValueError('values must be at least two')
    lengths = {}
    best = 0
    for value in sorted(set(values), reverse=True):
        lengths[value] = 1+lengths.get(value*value, 0)
        best = max(best, lengths[value])
    return best if best >= 2 else -1
