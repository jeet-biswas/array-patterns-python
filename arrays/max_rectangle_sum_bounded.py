from bisect import bisect_left, insort


def max_rectangle_sum_bounded(matrix: list[list[int]], limit: int) -> int | None:
    """Maximum nonempty rectangle sum <= limit; None if absent. No mutation."""
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError('rectangular matrix required')
    if not columns:
        return None
    best = None
    for top in range(rows):
        totals = [0]*columns
        for bottom in range(top, rows):
            prefixes = [0]
            running = 0
            for j in range(columns):
                totals[j] += matrix[bottom][j]
                running += totals[j]
                at = bisect_left(prefixes, running-limit)
                if at < len(prefixes):
                    candidate = running-prefixes[at]
                    best = candidate if best is None else max(best, candidate)
                insort(prefixes, running)
    return best
