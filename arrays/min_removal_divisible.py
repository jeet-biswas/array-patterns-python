def min_removal_divisible(values: list[int], p: int) -> int:
    """Shortest contiguous removal leaving a sum divisible by positive p.

    Cannot remove the entire nonempty array; return -1 if impossible.
    Signed values allowed; already divisible (including empty) -> 0.
    p <= 0 raises ValueError. Expected O(n) time, O(min(n,p)+1) space.
    """
    if p <= 0:
        raise ValueError('p must be positive')
    needed = sum(values) % p
    if needed == 0:
        return 0
    latest = {0: -1}
    prefix = 0
    best = len(values)
    for i, value in enumerate(values):
        prefix = (prefix + value) % p
        wanted = (prefix - needed) % p
        if wanted in latest:
            best = min(best, i - latest[wanted])
        latest[prefix] = i
    return best if best < len(values) else -1
