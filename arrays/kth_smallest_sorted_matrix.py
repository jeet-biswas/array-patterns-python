import heapq


def kth_smallest_sorted_matrix(matrix: list[list[int]], k: int) -> int:
    """One-based kth value in a nonempty rectangular row/column sorted matrix.

    Invalid shape, ordering or rank raises ValueError. Input is unchanged.
    """
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if not columns or any(len(row) != columns for row in matrix) or not 1 <= k <= rows*columns:
        raise ValueError('nonempty rectangle and valid rank required')
    for i in range(rows):
        for j in range(columns):
            if j and matrix[i][j-1] > matrix[i][j] or i and matrix[i-1][j] > matrix[i][j]:
                raise ValueError('rows and columns must be sorted')
    heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
    heapq.heapify(heap)
    for _ in range(k):
        value, row, column = heapq.heappop(heap)
        if column+1 < columns:
            heapq.heappush(heap, (matrix[row][column+1], row, column+1))
    return value
