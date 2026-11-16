def pascal_row(index: int) -> list[int]:
    """Return zero-based Pascal row; a negative index raises ValueError.

    O(index squared) arithmetic operations and O(index) output space.
    Python integer bit costs grow with coefficient sizes.
    """
    if index < 0:
        raise ValueError('index must be nonnegative')
    row = [1] + [0] * index
    for level in range(1, index + 1):
        for column in range(level, 0, -1):
            row[column] += row[column - 1]
    return row
