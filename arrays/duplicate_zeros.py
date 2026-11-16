def duplicate_zeros(values: list[int]) -> None:
    """Duplicate every zero in place, discarding overflow and keeping length fixed.

    Nonzero elements keep their order. O(n) time, O(1) auxiliary space.
    Returns None.
    """
    write = len(values) + values.count(0) - 1
    for read in range(len(values) - 1, -1, -1):
        value = values[read]
        if write < len(values):
            values[write] = value
        write -= 1
        if value == 0:
            if write < len(values):
                values[write] = 0
            write -= 1
