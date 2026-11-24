def count_global_max_occurrences(values: list[int], k: int) -> int:
    """Count nonempty windows containing the whole-array maximum >= k times.

    k must be positive. Empty input returns zero; no mutation.
    """
    if k <= 0:
        raise ValueError('positive k required')
    if not values:
        return 0
    maximum = max(values)
    left = count = total = 0
    for value in values:
        count += value == maximum
        while count >= k:
            count -= values[left] == maximum
            left += 1
        total += left
    return total
