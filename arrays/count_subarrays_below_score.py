def count_subarrays_below_score(values: list[int], limit: int) -> int:
    """Count nonempty windows with sum(window)*len(window) < limit; no mutation.

    Nonnegative values required; zero values are supported.
    """
    if any(x < 0 for x in values):
        raise ValueError('nonnegative values required')
    if limit <= 0:
        return 0
    left = total = answer = 0
    for right, value in enumerate(values):
        total += value
        while total*(right-left+1) >= limit:
            total -= values[left]
            left += 1
        answer += right-left+1
    return answer
