def maximum_distance_between_arrays(arrays: list[list[int]]) -> int:
    """Largest absolute difference using elements from two different arrays.

    At least two nonempty nondecreasing arrays required; sortedness is unchecked.
    No mutation.
    """
    if len(arrays) < 2 or any(not a for a in arrays): raise ValueError('two or more nonempty arrays required')
    minimum, maximum = arrays[0][0], arrays[0][-1]
    best = 0
    for i in range(1, len(arrays)):
        row = arrays[i]
        best = max(best, abs(row[-1]-minimum), abs(maximum-row[0]))
        minimum = min(minimum, row[0])
        maximum = max(maximum, row[-1])
    return best
