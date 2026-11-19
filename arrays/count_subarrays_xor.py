def count_subarrays_xor(values: list[int], target: int) -> int:
    """Count nonempty contiguous subarrays with XOR equal to target.

    Uses Python integer XOR, including signed values. Expected O(n) hash
    operations, O(n) space; bit-operation costs depend on integer sizes.
    Input is unchanged.
    """
    counts = {0: 1}
    prefix = total = 0
    for value in values:
        prefix ^= value
        total += counts.get(prefix ^ target, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
    return total
