from bisect import bisect_left


def lis_length(values: list[int]) -> int:
    """Length of a strictly increasing (not necessarily contiguous) subsequence.

    Empty -> 0. O(n log(n+1)) time, O(n) space; input is unchanged.
    """
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)
