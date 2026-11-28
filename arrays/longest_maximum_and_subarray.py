def longest_maximum_and_subarray(values: list[int]) -> int:
    """Longest nonempty subarray attaining the largest bitwise AND; empty -> 0.

    Nonnegative values required; no mutation.
    """
    if any(x < 0 for x in values): raise ValueError('nonnegative values required')
    maximum = max(values, default=0)
    run = best = 0
    for value in values:
        run = run+1 if value == maximum else 0
        best = max(best, run)
    return best
