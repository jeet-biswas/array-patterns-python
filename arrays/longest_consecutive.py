def longest_consecutive(values: list[int]) -> int:
    """Length of longest consecutive integer sequence, independent of input order.

    Duplicates do not extend a sequence. Empty -> 0. Expected O(n) time,
    O(n) extra space; hash-table operations are assumed expected O(1).
    """
    unique = set(values)
    best = 0
    for start in unique:
        if start - 1 not in unique:
            stop = start
            while stop in unique:
                stop += 1
            best = max(best, stop - start)
    return best
