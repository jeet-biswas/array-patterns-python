from bisect import bisect_left


def reconstruct_lis_indices(values: list[int]) -> list[int]:
    """Indices of one longest strictly increasing subsequence, in source order.

    Equal tails prefer the latest source index. Input is unchanged.
    """
    tails, tail_indices = [], []
    parents = [-1]*len(values)
    for i, value in enumerate(values):
        at = bisect_left(tails, value)
        if at: parents[i] = tail_indices[at-1]
        if at == len(tails):
            tails.append(value)
            tail_indices.append(i)
        else:
            tails[at] = value
            tail_indices[at] = i
    result = []
    index = tail_indices[-1] if tail_indices else -1
    while index != -1:
        result.append(index)
        index = parents[index]
    result.reverse()
    return result
