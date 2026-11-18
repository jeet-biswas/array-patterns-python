def count_product_below(values: list[int], threshold: int) -> int:
    """Count nonempty subarrays with product < threshold; positive integers only.

    Nonpositive values raise ValueError, even for threshold <= 1.
    O(n) arithmetic operations, O(1) auxiliary slots. Large integer costs
    depend on product size. Input is unchanged.
    """
    if any(value <= 0 for value in values):
        raise ValueError('all values must be positive')
    if threshold <= 1:
        return 0
    left = total = 0
    product = 1
    for right, value in enumerate(values):
        product *= value
        while product >= threshold:
            product //= values[left]
            left += 1
        total += right - left + 1
    return total
