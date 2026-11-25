def minimize_max_after_left_moves(values: list[int]) -> int:
    """Minimum maximum after moving units from i to i-1, repeatedly; no mutation.

    Nonnegative values required. Empty returns zero.
    """
    total = best = 0
    for count, value in enumerate(values, 1):
        if value < 0:
            raise ValueError('nonnegative values required')
        total += value
        best = max(best, (total+count-1)//count)
    return best
