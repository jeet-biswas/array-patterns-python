def count_equal_xor_triplets(values: list[int]) -> int:
    """Count i < j <= k with XOR(values[i:j]) == XOR(values[j:k+1]).

    Signed Python integers allowed. Expected O(n) hash operations, O(n)
    space; bit costs depend on integer sizes. Input is unchanged.
    """
    counts = {0: 1}
    positions = {0: 0}
    prefix = total = 0
    for stop, value in enumerate(values, 1):
        prefix ^= value
        total += counts.get(prefix, 0) * (stop - 1) - positions.get(prefix, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
        positions[prefix] = positions.get(prefix, 0) + stop
    return total
