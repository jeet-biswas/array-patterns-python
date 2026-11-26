from bisect import bisect_left


def maximum_envelope_nesting(envelopes: list[tuple[int, int]]) -> int:
    """Most envelopes nested with both dimensions strictly increasing; no mutation.

    Positive dimensions required. Rotation is not allowed; duplicates permitted.
    """
    if any(w <= 0 or h <= 0 for w, h in envelopes):
        raise ValueError('positive dimensions required')
    tails = []
    for _, height in sorted(envelopes, key=lambda pair: (pair[0], -pair[1])):
        at = bisect_left(tails, height)
        if at == len(tails): tails.append(height)
        else: tails[at] = height
    return len(tails)
