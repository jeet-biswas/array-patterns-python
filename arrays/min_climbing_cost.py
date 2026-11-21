def min_climbing_cost(costs: list[int]) -> int:
    """Reach position n from 0 or 1 with jumps of 1 or 2, paying on departure.

    Nonnegative costs required. Arrays of length <= 1 cost zero. No mutation.
    """
    if any(x < 0 for x in costs):
        raise ValueError('costs must be nonnegative')
    older = recent = 0
    for i in range(2, len(costs)+1):
        older, recent = recent, min(recent + costs[i-1], older + costs[i-2])
    return recent
