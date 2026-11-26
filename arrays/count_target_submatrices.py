def count_target_submatrices(matrix: list[list[int]], target: int) -> int:
    """Count nonempty axis-aligned rectangles summing to target; no mutation.

    Rectangular input required. Empty or zero-width matrices return zero.
    """
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    if not columns:
        return 0
    answer = 0
    for top in range(rows):
        totals = [0]*columns
        for bottom in range(top, rows):
            seen = {0: 1}
            prefix = 0
            for j in range(columns):
                totals[j] += matrix[bottom][j]
                prefix += totals[j]
                answer += seen.get(prefix-target, 0)
                seen[prefix] = seen.get(prefix, 0)+1
    return answer
