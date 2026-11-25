def longest_interval_chain(pairs: list[tuple[int, int]]) -> int:
    """Longest reordered chain with previous end < next start; no mutation.

    Pairs must satisfy start <= end. Touching endpoints cannot join.
    """
    if any(start > end for start, end in pairs):
        raise ValueError('reversed endpoints')
    end = None
    total = 0
    for left, right in sorted(pairs, key=lambda pair: pair[1]):
        if end is None or left > end:
            total += 1
            end = right
    return total
