def max_xor_pair(values: list[int]) -> int:
    """Maximum XOR from two distinct indices of a nonnegative integer array.

    Fewer than two elements or negative values raise ValueError.
    O(nB) trie steps/space for maximum bit length B (at least one).
    Input is unchanged; big-integer operation costs depend on B.
    """
    if len(values) < 2 or any(value < 0 for value in values):
        raise ValueError('at least two nonnegative values are required')
    width = max(1, max(values).bit_length())
    children = [[-1, -1]]

    def insert(value):
        node = 0
        for shift in range(width - 1, -1, -1):
            bit = (value >> shift) & 1
            if children[node][bit] == -1:
                children[node][bit] = len(children)
                children.append([-1, -1])
            node = children[node][bit]

    insert(values[0])
    best = 0
    for i in range(1, len(values)):
        node = score = 0
        for shift in range(width - 1, -1, -1):
            bit = (values[i] >> shift) & 1
            opposite = children[node][bit ^ 1]
            if opposite != -1:
                score |= 1 << shift
                node = opposite
            else:
                node = children[node][bit]
        best = max(best, score)
        insert(values[i])
    return best
