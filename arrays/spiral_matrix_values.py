def spiral_matrix_values(matrix: list[list[int]]) -> list[int]:
    """Clockwise spiral from top-left; rectangular matrices required, no mutation.

    Empty matrices and zero-width rows return [].
    """
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    top, bottom, left, right = 0, rows-1, 0, columns-1
    result = []
    while top <= bottom and left <= right:
        for j in range(left, right+1): result.append(matrix[top][j])
        top += 1
        for i in range(top, bottom+1): result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left-1, -1): result.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1): result.append(matrix[i][left])
            left += 1
    return result
