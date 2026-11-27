def minimum_signed_range_operations(source: list[int], target: list[int]) -> int:
    """Fewest operations adding +1 or -1 to a nonempty contiguous interval.

    Equal lengths required, signed values supported. Inputs are unchanged.
    """
    if len(source) != len(target):
        raise ValueError('equal lengths required')
    old_positive = old_negative = total = 0
    for before, after in zip(source, target):
        delta = after-before
        positive, negative = max(0, delta), max(0, -delta)
        total += max(0, positive-old_positive)+max(0, negative-old_negative)
        old_positive, old_negative = positive, negative
    return total
