def count_odd_sum_subarrays(values: list[int]) -> int:
    """Count nonempty contiguous subarrays with odd sum, without modulo.

    Signed integers supported. O(n) time, O(1) space; input unchanged.
    """
    counts = [1, 0]
    parity = total = 0
    for value in values:
        parity = (parity + value) % 2
        total += counts[1-parity]
        counts[parity] += 1
    return total
