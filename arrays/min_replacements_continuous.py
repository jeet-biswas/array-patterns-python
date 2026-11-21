def min_replacements_continuous(values: list[int]) -> int:
    """Fewest arbitrary value replacements yielding n distinct consecutive integers.

    Order does not matter. Empty returns zero; input is unchanged.
    """
    n = len(values)
    unique = sorted(set(values))
    left = kept = 0
    for right, value in enumerate(unique):
        while value-unique[left] >= n:
            left += 1
        kept = max(kept, right-left+1)
    return n-kept
