def largest_divisible_subset(values: list[int]) -> list[int]:
    """Return one largest sorted subset where each pair divides in one direction.

    Positive values required; duplicates represent distinct elements. No mutation.
    Ties keep the first optimal endpoint and predecessor in sorted order.
    """
    if any(x <= 0 for x in values):
        raise ValueError('positive values required')
    ordered = sorted(values)
    if not ordered:
        return []
    lengths = [1]*len(ordered)
    parents = [-1]*len(ordered)
    best = 0
    for i, value in enumerate(ordered):
        for j in range(i):
            if value % ordered[j] == 0 and lengths[j]+1 > lengths[i]:
                lengths[i] = lengths[j]+1
                parents[i] = j
        if lengths[i] > lengths[best]:
            best = i
    result = []
    while best != -1:
        result.append(ordered[best])
        best = parents[best]
    return result[::-1]
