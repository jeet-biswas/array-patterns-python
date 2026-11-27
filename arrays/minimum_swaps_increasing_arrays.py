def minimum_swaps_increasing_arrays(first: list[int], second: list[int]) -> int | None:
    """Fewest swaps of first[i] with second[i] making both arrays strictly increasing.

    Equal lengths required; None if impossible, empty -> 0. No mutation.
    """
    if len(first) != len(second):
        raise ValueError('equal lengths required')
    if not first:
        return 0
    previous = [0, 1]
    for i in range(1, len(first)):
        current = [None, None]
        for swapped in (0, 1):
            a, b = (second[i], first[i]) if swapped else (first[i], second[i])
            for old in (0, 1):
                x, y = (second[i-1], first[i-1]) if old else (first[i-1], second[i-1])
                if previous[old] is not None and x < a and y < b:
                    cost = previous[old]+swapped
                    current[swapped] = cost if current[swapped] is None else min(current[swapped], cost)
        previous = current
    return min((x for x in previous if x is not None), default=None)
