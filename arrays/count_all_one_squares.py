def count_all_one_squares(matrix: list[list[int]]) -> int:
    """Count axis-aligned nonempty all-one squares; rectangular binary input required.

    Empty and zero-width matrices return zero. Input is unchanged.
    """
    columns = len(matrix[0]) if matrix else 0
    if any(len(row) != columns for row in matrix) or any(x not in (0, 1) for row in matrix for x in row):
        raise ValueError('rectangular binary matrix required')
    previous = [0]*(columns+1)
    total = 0
    for row in matrix:
        current = [0]*(columns+1)
        for j, value in enumerate(row, 1):
            if value:
                current[j] = 1+min(previous[j], previous[j-1], current[j-1])
                total += current[j]
        previous = current
    return total
