def next_greater_right(values: list[int]) -> list[int | None]:
    """First strictly greater value to the right of each position, else None.

    O(n) time and O(n) space including stack/output; input is unchanged.
    """
    result = [None] * len(values)
    stack = []
    for i in range(len(values) - 1, -1, -1):
        while stack and stack[-1] <= values[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(values[i])
    return result
