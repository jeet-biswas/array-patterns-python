def max_sum_divisible_three(values: list[int]) -> int:
    """Maximum sum of a subset divisible by three; empty subset is allowed.

    Signed integers supported. O(n) time, O(1) auxiliary space; no mutation.
    """
    best = [0, None, None]
    for value in values:
        updated = best.copy()
        for remainder, total in enumerate(best):
            if total is not None:
                candidate = total + value
                next_remainder = (remainder + value) % 3
                previous = updated[next_remainder]
                if previous is None or candidate > previous:
                    updated[next_remainder] = candidate
        best = updated
    return best[0]
