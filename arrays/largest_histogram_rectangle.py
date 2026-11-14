def largest_histogram_rectangle(heights: list[int]) -> int:
    """Largest rectangle below unit-width nonnegative bars; empty -> 0.

    Negative heights raise ValueError. O(n) time, O(n) space; no mutation.
    """
    if any(height < 0 for height in heights):
        raise ValueError('heights must be nonnegative')
    stack = []
    best = 0
    for right in range(len(heights) + 1):
        height = heights[right] if right < len(heights) else 0
        while stack and heights[stack[-1]] >= height:
            middle = stack.pop()
            left = stack[-1] if stack else -1
            best = max(best, heights[middle] * (right - left - 1))
        if right < len(heights):
            stack.append(right)
    return best
