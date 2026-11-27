from collections import Counter


def count_subsets_avoiding_difference(values: list[int], k: int) -> int:
    """Count nonempty index subsets with no two values differing by positive k.

    Signed values and duplicates allowed; equal indices are never reused.
    Exact integer result; input is unchanged.
    """
    if k <= 0:
        raise ValueError('positive difference required')
    counts = Counter(values)
    groups = {}
    for value in sorted(counts):
        groups.setdefault(value % k, []).append(value)
    answer = 1
    for group in groups.values():
        skip, take = 1, 0
        previous = None
        for value in group:
            ways = (1 << counts[value])-1
            total = skip+take
            take = (skip if previous is not None and value-previous == k else total)*ways
            skip = total
            previous = value
        answer *= skip+take
    return answer-1
