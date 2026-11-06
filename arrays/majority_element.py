def majority_element(values: list[int]) -> int | None:
    """Return a value occurring more than n/2 times, else None.

    O(n) time and O(1) extra space. Input is not modified.
    """
    candidate = None
    votes = 0
    for value in values:
        if votes == 0:
            candidate = value
        votes += 1 if value == candidate else -1
    if values and sum(value == candidate for value in values) > len(values) // 2:
        return candidate
    return None
