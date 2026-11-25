def max_binary_matrix_rectangle(matrix: list[list[int]]) -> int:
    """Area of the largest axis-aligned all-one rectangle; no mutation.

    Rectangular binary matrix required; empty or zero-width matrix returns zero.
    """
    columns = len(matrix[0]) if matrix else 0
    if any(len(row) != columns for row in matrix) or any(x not in (0, 1) for row in matrix for x in row):
        raise ValueError('rectangular binary matrix required')
    heights = [0]*columns
    best = 0
    for row in matrix:
        for j, value in enumerate(row):
            heights[j] = heights[j]+1 if value else 0
        stack = []
        for j in range(columns+1):
            height = heights[j] if j < columns else 0
            while stack and heights[stack[-1]] >= height:
                bar = stack.pop()
                left = stack[-1]+1 if stack else 0
                best = max(best, heights[bar]*(j-left))
            stack.append(j)
    return best
