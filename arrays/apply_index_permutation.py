def apply_index_permutation(values: list[int], destinations: list[int]) -> None:
    """Move original values[i] to destinations[i], in place; returns None.

    Destinations must permute 0..n-1 and use a separate list from values.
    Invalid input is rejected before mutation.
    """
    n = len(values)
    if values is destinations or len(destinations) != n or set(destinations) != set(range(n)):
        raise ValueError('separate valid destination permutation required')
    visited = [False]*n
    for start in range(n):
        if visited[start]: continue
        current, carried = start, values[start]
        while not visited[current]:
            visited[current] = True
            following = destinations[current]
            values[following], carried = carried, values[following]
            current = following
