def valid_stack_sequences(pushed: list[int], popped: list[int]) -> bool:
    """Whether distinct pushed values can produce popped via one stack; no mutation.

    Duplicate pushed values raise ValueError. Length/value mismatches return False.
    """
    if len(set(pushed)) != len(pushed):
        raise ValueError('pushed values must be distinct')
    if len(pushed) != len(popped) or set(pushed) != set(popped):
        return False
    stack = []
    at = 0
    for value in pushed:
        stack.append(value)
        while stack and at < len(popped) and stack[-1] == popped[at]:
            stack.pop()
            at += 1
    return at == len(popped)
