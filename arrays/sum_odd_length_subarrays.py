def sum_odd_length_subarrays(values: list[int]) -> int:
    """Sum sums of all nonempty odd-length contiguous subarrays; empty -> 0.

    Signed integers allowed. O(n) arithmetic operations, O(1) auxiliary
    space under unit-cost arithmetic; input is unchanged.
    """
    n = len(values)
    return sum(value * (((i + 1) * (n - i) + 1) // 2) for i, value in enumerate(values))
