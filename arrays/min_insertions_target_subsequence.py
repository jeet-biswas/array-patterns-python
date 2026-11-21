from bisect import bisect_left


def min_insertions_target_subsequence(target: list[int], source: list[int]) -> int:
    """Fewest insertions into source making target a subsequence; no mutation.

    Target values must be distinct; source values may repeat.
    """
    positions = {x: i for i, x in enumerate(target)}
    if len(positions) != len(target):
        raise ValueError('target values must be distinct')
    tails = []
    for x in source:
        if x not in positions:
            continue
        index = positions[x]
        at = bisect_left(tails, index)
        if at == len(tails):
            tails.append(index)
        else:
            tails[at] = index
    return len(target)-len(tails)
