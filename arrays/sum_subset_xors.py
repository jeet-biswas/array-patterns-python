def sum_subset_xors(values: list[int]) -> int:
    """Exact sum of XORs over all index subsets; nonnegative values, no mutation.

    Empty subset contributes zero; empty array returns zero.
    """
    combined = 0
    for value in values:
        if value < 0: raise ValueError('nonnegative values required')
        combined |= value
    return combined << (len(values)-1) if values else 0
