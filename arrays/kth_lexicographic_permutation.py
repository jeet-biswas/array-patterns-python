def kth_lexicographic_permutation(values: list[int], k: int) -> list[int]:
    """One-based kth lexicographic permutation of distinct integer values; no mutation.

    Duplicate values or rank outside 1..n! raise ValueError. Empty has one permutation.
    """
    if len(set(values)) != len(values):
        raise ValueError('distinct values required')
    factorials = [1]
    for i in range(1, len(values)+1):
        factorials.append(factorials[-1]*i)
    if not 1 <= k <= factorials[-1]:
        raise ValueError('rank out of range')
    available = sorted(values)
    result = []
    rank = k-1
    for remaining in range(len(values), 0, -1):
        at, rank = divmod(rank, factorials[remaining-1])
        result.append(available.pop(at))
    return result
