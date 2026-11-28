def count_pairs_xor_interval(values: list[int], low: int, high: int) -> int:
    """Count i<j with low <= values[i]^values[j] <= high; no mutation.

    Requires nonnegative values and 0 <= low <= high. B includes high+1 bit width.
    """
    if not 0 <= low <= high or any(x < 0 for x in values): raise ValueError('invalid nonnegative bounds or values')
    bits = max(1, max(max(values, default=0), high+1).bit_length())
    children, counts = [[-1, -1]], [0]
    def less(value, bound):
        node = 0
        total = 0
        for bit in range(bits-1, -1, -1):
            if node == -1: break
            digit = (value >> bit) & 1
            if bound >> bit & 1:
                same = children[node][digit]
                if same != -1: total += counts[same]
                node = children[node][digit ^ 1]
            else: node = children[node][digit]
        return total
    answer = 0
    for value in values:
        answer += less(value, high+1)-less(value, low)
        node = 0
        for bit in range(bits-1, -1, -1):
            digit = (value >> bit) & 1
            if children[node][digit] == -1:
                children[node][digit] = len(children)
                children.append([-1, -1])
                counts.append(0)
            node = children[node][digit]
            counts[node] += 1
    return answer
