from bisect import bisect_left


def min_absolute_sum_difference(first: list[int], second: list[int]) -> int:
    """Minimum sum of paired absolute differences after at most one replacement.

    A first-array element may be replaced by any value from the original
    first array. Equal lengths required (ValueError otherwise). Exact result,
    no modulo. O(n log n) time, O(n) space; inputs unchanged.
    """
    if len(first) != len(second):
        raise ValueError('arrays must have equal length')
    ordered = sorted(first)
    total = saving = 0
    for a, b in zip(first, second):
        difference = abs(a-b)
        total += difference
        position = bisect_left(ordered, b)
        nearest = difference
        if position < len(ordered):
            nearest = min(nearest, abs(ordered[position]-b))
        if position:
            nearest = min(nearest, abs(ordered[position-1]-b))
        saving = max(saving, difference-nearest)
    return total - saving
