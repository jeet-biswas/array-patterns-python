def index_permutation_power(permutation: list[int], exponent: int) -> list[int]:
    """Return repeated-composition power p^exponent, allowing negative exponents.

    p must permute 0..n-1. Zero power is identity; input is unchanged.
    """
    n = len(permutation)
    if set(permutation) != set(range(n)): raise ValueError('invalid permutation')
    visited = [False]*n
    result = [0]*n
    for start in range(n):
        if visited[start]: continue
        cycle = []
        current = start
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = permutation[current]
        shift = exponent % len(cycle)
        for i, value in enumerate(cycle): result[value] = cycle[(i+shift) % len(cycle)]
    return result
