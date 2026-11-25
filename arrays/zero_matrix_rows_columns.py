def zero_matrix_rows_columns(matrix: list[list[int]]) -> None:
    """In place, zero all rows and columns containing an original zero; return None.

    Rectangular shape and independent mutable rows required. Shape errors are
    detected before mutation; empty and zero-width matrices are valid.
    """
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    if not rows or not columns:
        return
    first_row = any(x == 0 for x in matrix[0])
    first_column = any(matrix[i][0] == 0 for i in range(rows))
    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if first_row:
        for j in range(columns): matrix[0][j] = 0
    if first_column:
        for i in range(rows): matrix[i][0] = 0
