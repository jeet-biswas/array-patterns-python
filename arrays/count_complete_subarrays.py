def count_complete_subarrays(values: list[int]) -> int:
    """Count nonempty subarrays with the same value set as the whole array; no mutation."""
    if not values:
        return 0
    needed = len(set(values))
    counts = {}
    left = total = 0
    for value in values:
        counts[value] = counts.get(value, 0) + 1
        while len(counts) == needed:
            removed = values[left]
            counts[removed] -= 1
            if counts[removed] == 0:
                del counts[removed]
            left += 1
        total += left
    return total
