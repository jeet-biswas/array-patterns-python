def minimum_falling_path_sum(matrix: list[list[int]]) -> int | None:
    """Minimum sum choosing one cell per row, changing column by at most one.

    Any top/bottom column allowed. Rectangular signed input; no cells -> None.
    Input is unchanged.
    """
    columns = len(matrix[0]) if matrix else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    if not matrix or not columns:
        return None
    previous = list(matrix[0])
    for i in range(1, len(matrix)):
        current = []
        for j in range(columns):
            current.append(matrix[i][j]+min(previous[max(0, j-1):min(columns, j+2)]))
        previous = current
    return min(previous)
