def max_points_from_ends(values: list[int], k: int) -> int:
    """Maximum sum from exactly k successive left/right end removals.

    Require 0 <= k <= n, else ValueError. Signed values allowed; k=0 -> 0.
    O(k) time and O(1) auxiliary space; input is unchanged.
    """
    if not 0 <= k <= len(values):
        raise ValueError('k must be between zero and array length')
    score = sum(values[i] for i in range(k))
    best = score
    for right_count in range(1, k + 1):
        score += values[-right_count] - values[k - right_count]
        best = max(best, score)
    return best
