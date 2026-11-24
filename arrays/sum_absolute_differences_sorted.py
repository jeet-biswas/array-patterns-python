def sum_absolute_differences_sorted(values: list[int]) -> list[int]:
    """For each value, sum its absolute differences to all elements; no mutation.

    Input must be nondecreasing; unsorted input raises ValueError.
    """
    if any(values[i-1] > values[i] for i in range(1, len(values))):
        raise ValueError('sorted values required')
    total = sum(values)
    prefix = 0
    result = []
    for i, value in enumerate(values):
        left = value*i-prefix
        right = total-prefix-value-value*(len(values)-i-1)
        result.append(left+right)
        prefix += value
    return result
