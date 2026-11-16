def plus_one(digits: list[int]) -> list[int]:
    """Add one to nonempty base-10 digits, most significant first; no mutation.

    Digits must be 0..9 with no leading zero except [0], else ValueError.
    O(n) time and O(n) output space.
    """
    if not digits or any(d < 0 or d > 9 for d in digits) or (len(digits) > 1 and digits[0] == 0):
        raise ValueError('canonical decimal digits are required')
    result = digits.copy()
    for i in range(len(result) - 1, -1, -1):
        if result[i] < 9:
            result[i] += 1
            return result
        result[i] = 0
    return [1] + result
