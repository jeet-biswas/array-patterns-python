def contains_sorted_matrix_value(matrix: list[list[int]], target: int) -> bool:
    """Whether target occurs; rows AND columns must be nondecreasing (unchecked).

    Rectangular input required. Empty matrices return False; no mutation.
    """
    columns = len(matrix[0]) if matrix else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    i, j = 0, columns-1
    while i < len(matrix) and j >= 0:
        value = matrix[i][j]
        if value == target:
            return True
        if value > target:
            j -= 1
        else:
            i += 1
    return False
