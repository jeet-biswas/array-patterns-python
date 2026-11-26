def matrix_block_sums(matrix: list[list[int]], k: int) -> list[list[int]]:
    """Sum cells within row and column distance k of every cell; no mutation.

    Nonnegative k and rectangular matrix required. Output preserves its shape.
    """
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if k < 0 or any(len(row) != columns for row in matrix):
        raise ValueError('nonnegative radius and rectangle required')
    prefix = [[0]*(columns+1) for _ in range(rows+1)]
    for i in range(rows):
        for j in range(columns):
            prefix[i+1][j+1] = matrix[i][j]+prefix[i][j+1]+prefix[i+1][j]-prefix[i][j]
    result = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        top, bottom = max(0, i-k), min(rows, i+k+1)
        for j in range(columns):
            left, right = max(0, j-k), min(columns, j+k+1)
            result[i][j] = prefix[bottom][right]-prefix[top][right]-prefix[bottom][left]+prefix[top][left]
    return result
