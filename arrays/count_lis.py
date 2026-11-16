def count_lis(values: list[int]) -> int:
    """Count index-distinct longest strictly increasing subsequences; empty -> 0.

    O(n squared) arithmetic operations, O(n) space; input is unchanged.
    Counts use arbitrary-precision integers and may grow exponentially.
    """
    if not values:
        return 0
    lengths = [1] * len(values)
    counts = [1] * len(values)
    for i in range(len(values)):
        for j in range(i):
            if values[j] < values[i]:
                candidate = lengths[j] + 1
                if candidate > lengths[i]:
                    lengths[i], counts[i] = candidate, counts[j]
                elif candidate == lengths[i]:
                    counts[i] += counts[j]
    longest = max(lengths)
    return sum(count for length, count in zip(lengths, counts) if length == longest)
