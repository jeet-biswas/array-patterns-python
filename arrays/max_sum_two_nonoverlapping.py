def max_sum_two_nonoverlapping(values: list[int], first: int, second: int) -> int:
    """Maximum combined sum of disjoint subarrays of exactly first/second lengths.

    Both lengths must be positive and fit together, else ValueError.
    Signed values are allowed. O(n) time, O(n) space; input is unchanged.
    """
    if first <= 0 or second <= 0 or first + second > len(values):
        raise ValueError('two positive window lengths must fit in the array')
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)

    def ordered(a, b):
        best_first = prefix[a]
        best = None
        for stop in range(a + b, len(values) + 1):
            best_first = max(best_first, prefix[stop-b] - prefix[stop-b-a])
            candidate = best_first + prefix[stop] - prefix[stop-b]
            best = candidate if best is None else max(best, candidate)
        return best

    return max(ordered(first, second), ordered(second, first))
