def range_additions(length: int, updates: list[tuple[int, int, int]]) -> list[int]:
    """Start with length zeros and apply (start, stop, delta) on [start, stop).

    Negative length, malformed triples, or bounds outside
    0 <= start <= stop <= length raise ValueError. Empty ranges do nothing.
    O(length + number of updates) time and O(length) space. No input mutation.
    """
    if length < 0:
        raise ValueError('length must be nonnegative')
    for update in updates:
        if len(update) != 3 or not 0 <= update[0] <= update[1] <= length:
            raise ValueError('updates must be valid (start, stop, delta) triples')
    difference = [0] * (length + 1)
    for start, stop, delta in updates:
        difference[start] += delta
        difference[stop] -= delta
    total = 0
    for i in range(length):
        total += difference[i]
        difference[i] = total
    difference.pop()
    return difference
