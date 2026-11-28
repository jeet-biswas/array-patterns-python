def minimum_k_value_spread(values: list[int], k: int) -> int:
    """Minimum max-min among k selected indices; 0 <= k <= n required.

    k=0 or 1 returns zero. Signed values and duplicates allowed; no mutation.
    """
    if not 0 <= k <= len(values): raise ValueError('invalid selection count')
    if k <= 1: return 0
    ordered = sorted(values)
    return min(ordered[i+k-1]-ordered[i] for i in range(len(values)-k+1))
