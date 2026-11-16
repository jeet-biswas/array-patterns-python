def max_min_distance(positions: list[int], count: int) -> int:
    """Choose count distinct indices to maximize minimum pairwise distance.

    Requires 2 <= count <= n, else ValueError. Coordinates may repeat.
    O(n log n + n log(D+1)) time for coordinate span D, O(n) space.
    Input is unchanged.
    """
    if not 2 <= count <= len(positions):
        raise ValueError('count must be between two and the array length')
    ordered = sorted(positions)
    low, high = 0, ordered[-1] - ordered[0]
    while low < high:
        distance = (low + high + 1) // 2
        selected = 1
        last = ordered[0]
        for i in range(1, len(ordered)):
            if ordered[i] - last >= distance:
                selected += 1
                last = ordered[i]
        if selected >= count:
            low = distance
        else:
            high = distance - 1
    return low
