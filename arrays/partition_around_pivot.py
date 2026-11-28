def partition_around_pivot(values: list[int], pivot: int) -> tuple[int, int]:
    """Partition in place, returning [lower,upper) boundaries of values equal to pivot.

    Prefix is < pivot, suffix is > pivot. Unstable; pivot need not occur.
    """
    lower = index = 0
    upper = len(values)
    while index < upper:
        if values[index] < pivot:
            values[lower], values[index] = values[index], values[lower]
            lower += 1
            index += 1
        elif values[index] > pivot:
            upper -= 1
            values[index], values[upper] = values[upper], values[index]
        else: index += 1
    return lower, upper
