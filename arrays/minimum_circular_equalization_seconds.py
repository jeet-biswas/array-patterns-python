def minimum_circular_equalization_seconds(values: list[int]) -> int:
    """Seconds to equalize a circle; each cell simultaneously copies self or a neighbor.

    Empty and already-equal arrays need zero seconds. Input is unchanged.
    """
    if not values:
        return 0
    positions = {}
    for i, value in enumerate(values):
        positions.setdefault(value, []).append(i)
    best = len(values)
    for indices in positions.values():
        gap = indices[0]+len(values)-indices[-1]
        for left, right in zip(indices, indices[1:]):
            gap = max(gap, right-left)
        best = min(best, gap//2)
    return best
