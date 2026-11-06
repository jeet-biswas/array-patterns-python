def max_container_area(heights: list[int]) -> int:
    """Maximum (j-i)*min(heights[i], heights[j]); fewer than 2 bars -> 0.

    Nonnegative heights are required (ValueError otherwise).
    O(n) time and O(1) extra space; input is unchanged.
    """
    if any(height < 0 for height in heights):
        raise ValueError('heights must be nonnegative')
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        best = max(best, (right - left) * min(heights[left], heights[right]))
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return best
