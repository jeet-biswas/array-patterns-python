def max_xor_under_limits(values: list[int], queries: list[tuple[int, int]]) -> list[int | None]:
    """For (x,limit), maximize x^value over array values <= limit; no mutation.

    Array and x values must be nonnegative; limits may be negative. None means no candidate.
    """
    if any(x < 0 for x in values) or any(x < 0 for x, _ in queries): raise ValueError('nonnegative XOR operands required')
    bits = max(1, max(max(values, default=0), max((x for x, _ in queries), default=0)).bit_length())
    ordered = sorted(values)
    children = [[-1, -1]]
    at = 0
    answer = [None]*len(queries)
    for limit, x, query_id in sorted((limit, x, i) for i, (x, limit) in enumerate(queries)):
        while at < len(ordered) and ordered[at] <= limit:
            node = 0
            for bit in range(bits-1, -1, -1):
                digit = (ordered[at] >> bit) & 1
                if children[node][digit] == -1:
                    children[node][digit] = len(children)
                    children.append([-1, -1])
                node = children[node][digit]
            at += 1
        if at == 0: continue
        node = score = 0
        for bit in range(bits-1, -1, -1):
            digit = (x >> bit) & 1
            if children[node][digit ^ 1] != -1:
                score |= 1 << bit
                node = children[node][digit ^ 1]
            else: node = children[node][digit]
        answer[query_id] = score
    return answer
