from collections import Counter


def minimum_basket_swap_cost(first: list[int], second: list[int]) -> int | None:
    """Equalize multisets by cross-array swaps costing min(swapped values).

    Equal lengths and positive values required. None if impossible; no mutation.
    """
    if len(first) != len(second) or any(x <= 0 for a in (first, second) for x in a):
        raise ValueError('equal lengths and positive values required')
    if not first:
        return 0
    difference = Counter(first)
    difference.subtract(second)
    left, right = [], []
    for value, count in difference.items():
        if count % 2:
            return None
        if count > 0: left.extend([value]*(count//2))
        elif count < 0: right.extend([value]*(-count//2))
    minimum = min(min(first), min(second))
    return sum(min(a, b, 2*minimum) for a, b in zip(sorted(left), sorted(right, reverse=True)))
