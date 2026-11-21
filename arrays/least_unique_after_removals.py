from collections import Counter


def least_unique_after_removals(values: list[int], k: int) -> int:
    """Minimum remaining distinct values after exactly k element removals; no mutation.

    Requires 0 <= k <= len(values).
    """
    if not 0 <= k <= len(values):
        raise ValueError('invalid removal count')
    counts = sorted(Counter(values).values())
    remaining = len(counts)
    for count in counts:
        if count > k:
            break
        k -= count
        remaining -= 1
    return remaining
