def subarrays_exactly_k_distinct(values: list[int], k: int) -> int:
    """Count nonempty contiguous subarrays with exactly k distinct integers.

    k < 0 raises ValueError; k == 0 returns 0. Expected O(n) time and
    O(min(n,k)) space (plus one transient entry). Input is unchanged.
    """
    if k < 0:
        raise ValueError('k must be nonnegative')
    if k == 0:
        return 0

    def at_most(limit):
        counts = {}
        left = total = 0
        for right, value in enumerate(values):
            counts[value] = counts.get(value, 0) + 1
            while len(counts) > limit:
                outgoing = values[left]
                counts[outgoing] -= 1
                if counts[outgoing] == 0:
                    del counts[outgoing]
                left += 1
            total += right - left + 1
        return total

    return at_most(k) - at_most(k - 1)
