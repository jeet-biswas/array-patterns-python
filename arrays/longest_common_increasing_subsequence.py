def longest_common_increasing_subsequence(first: list[int], second: list[int]) -> int:
    """Length of a strictly increasing subsequence present in both arrays; no mutation."""
    lengths = [0]*len(second)
    for value in first:
        smaller = 0
        for j, other in enumerate(second):
            if other < value:
                smaller = max(smaller, lengths[j])
            elif other == value:
                lengths[j] = max(lengths[j], smaller+1)
    return max(lengths, default=0)
