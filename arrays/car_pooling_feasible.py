def car_pooling_feasible(trips: list[tuple[int, int, int]], capacity: int) -> bool:
    """Whether (passengers,start,end) trips fit capacity throughout [start,end).

    Nonnegative capacity/passengers and start < end required; no mutation.
    """
    if capacity < 0:
        raise ValueError('capacity must be nonnegative')
    changes = {}
    for passengers, start, end in trips:
        if passengers < 0 or start >= end:
            raise ValueError('nonnegative passengers and start < end required')
        changes[start] = changes.get(start, 0) + passengers
        changes[end] = changes.get(end, 0) - passengers
    load = 0
    for position in sorted(changes):
        load += changes[position]
        if load > capacity:
            return False
    return True
