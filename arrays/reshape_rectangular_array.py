def reshape_rectangular_array(matrix: list[list[int]], rows: int, columns: int) -> list[list[int]] | None:
    """Return a fresh reshape, or None if cell counts differ; no mutation.

    Source must be rectangular; requested dimensions nonnegative. Zero dimensions
    are valid and preserve the requested number of empty rows.
    """
    source_rows = len(matrix)
    source_columns = len(matrix[0]) if matrix else 0
    if rows < 0 or columns < 0 or any(len(row) != source_columns for row in matrix):
        raise ValueError('nonnegative dimensions and rectangular source required')
    if rows*columns != source_rows*source_columns:
        return None
    result = [[] for _ in range(rows)]
    if not rows or not columns:
        return result
    for i in range(rows):
        for j in range(columns):
            index = i*columns+j
            result[i].append(matrix[index//source_columns][index % source_columns])
    return result
