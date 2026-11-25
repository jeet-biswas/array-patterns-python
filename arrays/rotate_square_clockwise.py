def rotate_square_clockwise(matrix: list[list[int]]) -> None:
    """Rotate a square matrix 90 degrees clockwise in place; return None.

    Rows must be independent mutable lists. Nonsquare shapes raise ValueError
    before mutation. Empty is valid.
    """
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError('square matrix required')
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
