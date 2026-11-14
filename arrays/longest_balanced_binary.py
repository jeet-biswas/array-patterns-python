def longest_balanced_binary(values: list[int]) -> int:
    """Longest contiguous subarray with equal zero/one counts; empty -> 0.

    Nonbinary elements raise ValueError. Expected O(n) time, O(n) space.
    Input is unchanged.
    """
    if any(value not in (0, 1) for value in values):
        raise ValueError('values must contain only zero and one')
    first = {0: -1}
    balance = best = 0
    for i, value in enumerate(values):
        balance += 1 if value else -1
        if balance in first:
            best = max(best, i - first[balance])
        else:
            first[balance] = i
    return best
