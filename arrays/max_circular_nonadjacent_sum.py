def max_circular_nonadjacent_sum(values: list[int]) -> int:
    """Best sum with no circular neighbors selected; empty selection allowed, no mutation.

    A singleton may be selected; two positions are neighbors.
    """
    n = len(values)
    if n <= 1:
        return max(0, values[0]) if n else 0
    def linear(start, end):
        older = recent = 0
        for i in range(start, end):
            older, recent = recent, max(recent, older + values[i])
        return recent
    return max(linear(0, n-1), linear(1, n))
