def move_zeros(values: list[int]) -> None:
    """Move zeros to the end in place, preserving nonzero order; return None.

    O(n) time and O(1) extra space.
    """
    write = 0
    for read in range(len(values)):
        if values[read] != 0:
            values[write] = values[read]
            write += 1
    for index in range(write, len(values)):
        values[index] = 0
