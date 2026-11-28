def max_pair_sum_equal_digit_sum(values: list[int]) -> int | None:
    """Largest sum of distinct-index values with equal digit sums of their magnitudes.

    Signed integers allowed; zero has digit sum zero. No pair -> None; no mutation.
    """
    largest = {}
    best = None
    for value in values:
        remaining = abs(value)
        digit_sum = 0
        while remaining:
            digit_sum += remaining % 10
            remaining //= 10
        if digit_sum in largest:
            candidate = value+largest[digit_sum]
            best = candidate if best is None else max(best, candidate)
            largest[digit_sum] = max(largest[digit_sum], value)
        else: largest[digit_sum] = value
    return best
