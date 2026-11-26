def diagonal_zigzag_values(matrix: list[list[int]]) -> list[int]:
    """Read anti-diagonals alternately up-right and down-left from top-left.

    Rectangular input required; empty/zero-width -> []; no mutation.
    """
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    if not columns:
        return []
    result = []
    for diagonal in range(rows+columns-1):
        low, high = max(0, diagonal-columns+1), min(rows-1, diagonal)
        indices = range(low, high+1) if diagonal % 2 else range(high, low-1, -1)
        for i in indices: result.append(matrix[i][diagonal-i])
    return result
