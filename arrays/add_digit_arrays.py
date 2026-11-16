def add_digit_arrays(left: list[int], right: list[int]) -> list[int]:
    """Add canonical nonnegative decimal digit arrays without modifying them.

    Both must be nonempty, digits 0..9, no leading zeros except [0];
    invalid input raises ValueError. O(n+m) time and O(max(n,m)) output space.
    """
    for digits in (left, right):
        if not digits or any(d < 0 or d > 9 for d in digits) or (len(digits) > 1 and digits[0] == 0):
            raise ValueError('canonical decimal digits are required')
    i, j = len(left) - 1, len(right) - 1
    carry = 0
    result = []
    while i >= 0 or j >= 0 or carry:
        total = carry + (left[i] if i >= 0 else 0) + (right[j] if j >= 0 else 0)
        carry, digit = divmod(total, 10)
        result.append(digit)
        i -= 1
        j -= 1
    result.reverse()
    return result
