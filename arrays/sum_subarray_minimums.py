def sum_subarray_minimums(values: list[int]) -> int:
    """Sum minimums of all nonempty contiguous subarrays, with no modulo.

    Signed integers are supported; empty -> 0. O(n) time and O(n) stack space.
    The input is not changed.
    """
    stack = []
    total = 0
    for right in range(len(values) + 1):
        while stack and (right == len(values) or values[stack[-1]] >= values[right]):
            middle = stack.pop()
            left = stack[-1] if stack else -1
            total += values[middle] * (middle - left) * (right - middle)
        if right < len(values):
            stack.append(right)
    return total
