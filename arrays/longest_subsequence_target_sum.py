def longest_subsequence_target_sum(values: list[int], target: int) -> int | None:
    """Largest length of an index subsequence summing to target, or None.

    Signed values allowed; empty subsequence qualifies for zero. No mutation.
    """
    lengths = {0: 0}
    for value in values:
        updated = lengths.copy()
        for total, length in lengths.items():
            updated[total+value] = max(updated.get(total+value, -1), length+1)
        lengths = updated
    return lengths.get(target)
