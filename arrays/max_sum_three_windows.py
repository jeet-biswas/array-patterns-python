def max_sum_three_windows(values: list[int], width: int) -> tuple[int, int, int]:
    """Starts of three disjoint width-sized windows with maximum total sum.

    Ties choose lexicographically smallest starts. Signed integers allowed.
    Require width > 0 and n >= 3*width, else ValueError. O(n) time/space.
    Input is unchanged.
    """
    if width <= 0 or len(values) < 3 * width:
        raise ValueError('three positive-width windows must fit')
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)
    sums = [prefix[i+width] - prefix[i] for i in range(len(values)-width+1)]
    left = [0] * len(sums)
    right = [0] * len(sums)
    best = 0
    for i in range(len(sums)):
        if sums[i] > sums[best]:
            best = i
        left[i] = best
    best = len(sums) - 1
    for i in range(len(sums) - 1, -1, -1):
        if sums[i] >= sums[best]:
            best = i
        right[i] = best
    answer = score = None
    for middle in range(width, len(sums)-width):
        indices = left[middle-width], middle, right[middle+width]
        total = sum(sums[i] for i in indices)
        if score is None or total > score or (total == score and indices < answer):
            answer, score = indices, total
    return answer
