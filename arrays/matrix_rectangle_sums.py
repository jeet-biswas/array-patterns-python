def matrix_rectangle_sums(matrix: list[list[int]], queries: list[tuple[int, int, int, int]]) -> list[int]:
    """Sum each (top,left,bottom,right) half-open rectangle; input is unchanged.

    Ragged matrices raise ValueError; out-of-bounds or reversed ranges raise IndexError.
    An empty outer matrix has shape 0 by 0; rows of length zero are supported.
    """
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    prefix = [[0]*(columns+1) for _ in range(rows+1)]
    for i, row in enumerate(matrix, 1):
        total = 0
        for j, value in enumerate(row, 1):
            total += value
            prefix[i][j] = prefix[i-1][j]+total
    result = []
    for top, left, bottom, right in queries:
        if not (0 <= top <= bottom <= rows and 0 <= left <= right <= columns):
            raise IndexError('invalid rectangle')
        result.append(prefix[bottom][right]-prefix[top][right]-prefix[bottom][left]+prefix[top][left])
    return result
