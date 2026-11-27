def minimum_deletions_unequal_pairs(values: list[int]) -> int:
    """Delete the fewest elements so length is even and a[2i] != a[2i+1].

    Empty result allowed; values may be signed. Input is unchanged.
    """
    pending = None
    kept = 0
    for value in values:
        if pending is None:
            pending = value
        elif value != pending:
            kept += 2
            pending = None
    return len(values)-kept
