def minimum_decrements_zigzag(values: list[int]) -> int:
    """Minimum unit decrements to alternate strict < and >; no mutation.

    Signed values allowed and may be decreased without a lower bound.
    """
    costs = [0, 0]
    for i, value in enumerate(values):
        neighbors = []
        if i:
            neighbors.append(values[i-1])
        if i+1 < len(values):
            neighbors.append(values[i+1])
        if neighbors:
            costs[i % 2] += max(0, value-min(neighbors)+1)
    return min(costs)
