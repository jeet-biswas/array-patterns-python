def min_swaps_permutation(values: list[int]) -> int:
    """Minimum arbitrary swaps to sort a permutation of 0..n-1, without mutation.

    Invalid permutations raise ValueError. Empty -> 0.
    O(n) time and O(n) auxiliary space.
    """
    n = len(values)
    present = [False] * n
    for value in values:
        if not 0 <= value < n or present[value]:
            raise ValueError('values must be a permutation of 0..n-1')
        present[value] = True
    visited = [False] * n
    total = 0
    for start in range(n):
        if visited[start]:
            continue
        position = start
        size = 0
        while not visited[position]:
            visited[position] = True
            size += 1
            position = values[position]
        total += size - 1
    return total
