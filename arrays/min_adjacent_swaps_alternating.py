def min_adjacent_swaps_alternating(values: list[int]) -> int:
    """Minimum adjacent swaps to alternate binary values, or -1 if impossible.

    Empty is already alternating. Input is unchanged.
    """
    if any(x not in (0, 1) for x in values):
        raise ValueError('binary values required')
    positions = [i for i, x in enumerate(values) if x]
    best = None
    for first in (0, 1):
        targets = range(first, len(values), 2)
        if len(targets) == len(positions):
            cost = sum(abs(a-b) for a, b in zip(positions, targets))
            best = cost if best is None else min(best, cost)
    return -1 if best is None else best
