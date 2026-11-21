def has_132_pattern(values: list[int]) -> bool:
    """Whether i<j<k exist with values[i]<values[k]<values[j]; no mutation."""
    stack = []
    middle = None
    for value in reversed(values):
        if middle is not None and value < middle:
            return True
        while stack and value > stack[-1]:
            middle = stack.pop()
        stack.append(value)
    return False
