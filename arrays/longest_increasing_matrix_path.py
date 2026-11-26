from collections import deque


def longest_increasing_matrix_path(matrix: list[list[int]]) -> int:
    """Longest strict increasing path using four-direction neighbors; no mutation.

    Rectangular signed input required; no cells -> 0.
    """
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    if not columns:
        return 0
    def neighbors(i, j):
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            a, b = i+di, j+dj
            if 0 <= a < rows and 0 <= b < columns:
                yield a, b
    indegree = [[0]*columns for _ in range(rows)]
    queue = deque()
    for i in range(rows):
        for j in range(columns):
            indegree[i][j] = sum(matrix[a][b] < matrix[i][j] for a, b in neighbors(i, j))
            if indegree[i][j] == 0: queue.append((i, j))
    layers = 0
    while queue:
        layers += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for a, b in neighbors(i, j):
                if matrix[a][b] > matrix[i][j]:
                    indegree[a][b] -= 1
                    if indegree[a][b] == 0: queue.append((a, b))
    return layers
