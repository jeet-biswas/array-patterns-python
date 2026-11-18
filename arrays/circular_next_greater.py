def circular_next_greater(values: list[int]) -> list[int | None]:
    """First strictly greater value encountered clockwise, else None.

    Each search examines at most n-1 other positions. O(n) time and O(n)
    space including output; input is unchanged.
    """
    n = len(values)
    result = [None] * n
    stack = []
    for i in range(2 * n - 1, -1, -1):
        value = values[i % n]
        while stack and stack[-1] <= value:
            stack.pop()
        if i < n and stack:
            result[i] = stack[-1]
        stack.append(value)
    return result
