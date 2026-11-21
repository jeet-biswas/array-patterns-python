def longest_common_subarray(first: list[int], second: list[int]) -> int:
    """Length of the longest equal contiguous blocks in both arrays; no mutation."""
    lengths = [0] * (len(second)+1)
    best = 0
    for x in first:
        for j in range(len(second), 0, -1):
            lengths[j] = lengths[j-1]+1 if x == second[j-1] else 0
            best = max(best, lengths[j])
    return best
