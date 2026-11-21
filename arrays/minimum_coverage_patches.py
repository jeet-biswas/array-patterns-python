def minimum_coverage_patches(values: list[int], target: int) -> int:
    """Fewest positive integers to add so subset sums cover every integer 1..target.

    Values must be sorted positive integers, target nonnegative. No mutation.
    """
    if target < 0 or any(x <= 0 for x in values):
        raise ValueError('positive values and nonnegative target required')
    if any(values[i-1] > values[i] for i in range(1, len(values))):
        raise ValueError('values must be sorted')
    missing = 1
    index = patches = 0
    while missing <= target:
        if index < len(values) and values[index] <= missing:
            missing += values[index]
            index += 1
        else:
            missing *= 2
            patches += 1
    return patches
