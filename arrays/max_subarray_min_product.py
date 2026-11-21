def max_subarray_min_product(values: list[int]) -> int:
    """Maximum sum(window)*min(window), exactly (no modulus); empty -> 0.

    Values must be nonnegative; input is unchanged.
    """
    if any(x < 0 for x in values):
        raise ValueError('values must be nonnegative')
    prefix = [0]
    for x in values:
        prefix.append(prefix[-1] + x)
    stack = []
    best = 0
    for i in range(len(values)+1):
        while stack and (i == len(values) or values[stack[-1]] >= values[i]):
            middle = stack.pop()
            left = stack[-1]+1 if stack else 0
            best = max(best, values[middle] * (prefix[i]-prefix[left]))
        stack.append(i)
    return best
