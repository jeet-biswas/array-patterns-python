def max_score_containing_index(values: list[int], index: int) -> int:
    """Maximize min(window)*len(window) for windows containing index; no mutation.

    Nonnegative values required. Invalid index raises IndexError.
    """
    if not 0 <= index < len(values):
        raise IndexError('index outside array')
    if any(x < 0 for x in values):
        raise ValueError('values must be nonnegative')
    stack = []
    best = 0
    for right in range(len(values)+1):
        while stack and (right == len(values) or values[stack[-1]] >= values[right]):
            middle = stack.pop()
            left = stack[-1]+1 if stack else 0
            if left <= index < right:
                best = max(best, values[middle] * (right-left))
        stack.append(right)
    return best
