def sum_subarray_ranges(values: list[int]) -> int:
    """Sum max-min over all nonempty contiguous subarrays; empty -> 0.

    Signed integers allowed. O(n) time, O(n) stack space; no mutation.
    """
    def extreme_sum(minimum):
        stack = []
        total = 0
        for right in range(len(values) + 1):
            while stack:
                if right < len(values):
                    pop = values[stack[-1]] >= values[right] if minimum else values[stack[-1]] <= values[right]
                    if not pop:
                        break
                middle = stack.pop()
                left = stack[-1] if stack else -1
                total += values[middle] * (middle - left) * (right - middle)
            if right < len(values):
                stack.append(right)
        return total

    return extreme_sum(False) - extreme_sum(True)
