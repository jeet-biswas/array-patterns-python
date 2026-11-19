def minimum_replacements_sorted(values: list[int]) -> int:
    """Minimum operations replacing an element by two positive integers summing to it.

    Goal: a nondecreasing final array; input must be positive (ValueError
    otherwise). Empty -> 0. O(n) arithmetic operations, O(1) auxiliary space.
    Input is unchanged; actual replacement arrays are not constructed.
    """
    if any(value <= 0 for value in values):
        raise ValueError('values must be positive')
    if not values:
        return 0
    bound = values[-1]
    operations = 0
    for i in range(len(values) - 2, -1, -1):
        parts = (values[i] + bound - 1) // bound
        operations += parts - 1
        bound = values[i] // parts
    return operations
