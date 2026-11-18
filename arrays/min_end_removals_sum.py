def min_end_removals_sum(values: list[int], target: int) -> int:
    """Fewest left/right end removals whose values sum to target, else -1.

    Signed integers allowed. Removing nothing or everything is permitted.
    Expected O(n) time, O(n) space; input is unchanged.
    """
    keep_target = sum(values) - target
    longest = 0 if keep_target == 0 else -1
    earliest = {0: -1}
    prefix = 0
    for i, value in enumerate(values):
        prefix += value
        if prefix - keep_target in earliest:
            longest = max(longest, i - earliest[prefix - keep_target])
        earliest.setdefault(prefix, i)
    return len(values) - longest if longest >= 0 else -1
