def longest_arithmetic_subsequence(values: list[int]) -> int:
    """Length of a subsequence with constant adjacent difference; empty -> 0.

    Equal values are allowed (difference zero). Expected O(n squared) time
    and O(n squared) worst-case space; input is unchanged.
    """
    if len(values) < 2:
        return len(values)
    ending = [{} for _ in values]
    best = 2
    for i in range(len(values)):
        for j in range(i):
            difference = values[i] - values[j]
            length = ending[j].get(difference, 1) + 1
            ending[i][difference] = max(ending[i].get(difference, 0), length)
            best = max(best, ending[i][difference])
    return best
