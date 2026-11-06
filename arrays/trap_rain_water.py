def trap_rain_water(heights: list[int]) -> int:
    """Water above unit-width nonnegative bars; negative heights raise ValueError.

    O(n) time and O(1) extra space; does not modify heights.
    """
    if any(height < 0 for height in heights):
        raise ValueError('heights must be nonnegative')
    left, right = 0, len(heights) - 1
    left_max = right_max = total = 0
    while left <= right:
        if heights[left] <= heights[right]:
            left_max = max(left_max, heights[left])
            total += left_max - heights[left]
            left += 1
        else:
            right_max = max(right_max, heights[right])
            total += right_max - heights[right]
            right -= 1
    return total
