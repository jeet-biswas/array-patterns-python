def max_sum_k_windows(values: list[int], width: int, count: int) -> int:
    """Best total from exactly count disjoint contiguous width-sized windows.

    Requires width > 0, count >= 0 and width*count <= n, else ValueError.
    Signed values allowed; count=0 -> 0. O(n*count) time, O(n) space.
    Input is unchanged.
    """
    if width <= 0 or count < 0 or width * count > len(values):
        raise ValueError('valid window width/count must fit the array')
    if count == 0:
        return 0
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)
    previous = [0] * (len(values) + 1)
    for _ in range(count):
        current = [None] * (len(values) + 1)
        for stop in range(1, len(values) + 1):
            current[stop] = current[stop-1]
            if stop >= width and previous[stop-width] is not None:
                take = previous[stop-width] + prefix[stop] - prefix[stop-width]
                current[stop] = take if current[stop] is None else max(current[stop], take)
        previous = current
    return previous[-1]
