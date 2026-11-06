def compact_sorted(values: list[int]) -> int:
    """Compact a sorted array in place and return its unique-prefix length.

    Precondition: values is sorted nondecreasingly (not checked).
    Tail contents are unspecified. O(n) time, O(1) extra space.
    """
    if not values:
        return 0
    write = 1
    for read in range(1, len(values)):
        if values[read] != values[write - 1]:
            values[write] = values[read]
            write += 1
    return write
