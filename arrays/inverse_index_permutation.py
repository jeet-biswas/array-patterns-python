def inverse_index_permutation(permutation: list[int]) -> list[int]:
    """Return q with q[permutation[i]] == i; no mutation.

    Input must permute 0..n-1; invalid input raises ValueError.
    """
    n = len(permutation)
    if set(permutation) != set(range(n)): raise ValueError('invalid permutation')
    inverse = [0]*n
    for i, destination in enumerate(permutation): inverse[destination] = i
    return inverse
