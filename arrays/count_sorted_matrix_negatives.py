def count_sorted_matrix_negatives(matrix: list[list[int]]) -> int:
    """Count negative cells; rows AND columns must be nonincreasing (unchecked).

    Ragged shape raises ValueError; empty/zero-width -> 0. No mutation.
    """
    columns = len(matrix[0]) if matrix else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    i, j = len(matrix)-1, 0
    total = 0
    while i >= 0 and j < columns:
        if matrix[i][j] < 0:
            total += columns-j
            i -= 1
        else:
            j += 1
    return total
