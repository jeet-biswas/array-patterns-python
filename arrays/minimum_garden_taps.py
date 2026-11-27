def minimum_garden_taps(ranges: list[int]) -> int | None:
    """Fewest taps covering [0,len(ranges)-1]; tap i covers i +/- ranges[i].

    Nonempty nonnegative integer radius array required. A zero-length garden costs
    zero taps; None means a positive-length garden cannot be covered. No mutation.
    """
    if not ranges or any(x < 0 for x in ranges):
        raise ValueError('nonempty nonnegative radii required')
    n = len(ranges)-1
    reach = [0]*(n+1)
    for i, radius in enumerate(ranges):
        left, right = max(0, i-radius), min(n, i+radius)
        reach[left] = max(reach[left], right)
    farthest = covered = taps = 0
    for position in range(n):
        farthest = max(farthest, reach[position])
        if position == covered:
            if farthest <= position:
                return None
            taps += 1
            covered = farthest
    return taps
