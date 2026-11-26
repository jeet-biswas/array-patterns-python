def max_submatrix_sum(matrix: list[list[int]]) -> int | None:
    """Largest nonempty rectangle sum, or None if there are no cells; no mutation."""
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    if not columns:
        return None
    best = None
    for top in range(rows):
        totals = [0]*columns
        for bottom in range(top, rows):
            ending = None
            for j in range(columns):
                totals[j] += matrix[bottom][j]
                ending = totals[j] if ending is None else max(totals[j], ending+totals[j])
                best = ending if best is None else max(best, ending)
    return best
