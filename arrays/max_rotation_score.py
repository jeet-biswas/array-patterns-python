def max_rotation_score(values: list[int]) -> int:
    """Maximum sum(i*rotated[i]) over all circular rotations; empty -> 0.

    Signed values allowed. O(n) time, O(1) space; input is unchanged.
    """
    total = sum(values)
    score = sum(i * value for i, value in enumerate(values))
    best = score
    n = len(values)
    for step in range(1, n):
        score += total - n * values[n - step]
        best = max(best, score)
    return best
