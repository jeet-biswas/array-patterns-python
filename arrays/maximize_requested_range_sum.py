def maximize_requested_range_sum(values: list[int], requests: list[tuple[int, int]]) -> int:
    """Largest total requested sum after any reordering of values; exact, no mutation.

    Requests are half-open [start,end). Invalid bounds raise IndexError.
    """
    changes = [0]*(len(values)+1)
    for start, end in requests:
        if not 0 <= start <= end <= len(values):
            raise IndexError('invalid range')
        changes[start] += 1
        changes[end] -= 1
    frequency = []
    active = 0
    for i in range(len(values)):
        active += changes[i]
        frequency.append(active)
    return sum(x*y for x, y in zip(sorted(values), sorted(frequency)))
