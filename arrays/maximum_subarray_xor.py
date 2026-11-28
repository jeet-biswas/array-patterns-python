def maximum_subarray_xor(values: list[int]) -> int:
    """Maximum nonempty subarray XOR, or zero for empty; nonnegative input, no mutation."""
    if any(x < 0 for x in values): raise ValueError('nonnegative values required')
    bits = max(1, max(values, default=0).bit_length())
    children = [[-1, -1]]
    def insert(value):
        node = 0
        for bit in range(bits-1, -1, -1):
            digit = (value >> bit) & 1
            if children[node][digit] == -1:
                children[node][digit] = len(children)
                children.append([-1, -1])
            node = children[node][digit]
    insert(0)
    prefix = best = 0
    for value in values:
        prefix ^= value
        node = score = 0
        for bit in range(bits-1, -1, -1):
            digit = (prefix >> bit) & 1
            if children[node][digit ^ 1] != -1:
                score |= 1 << bit
                node = children[node][digit ^ 1]
            else: node = children[node][digit]
        best = max(best, score)
        insert(prefix)
    return best
