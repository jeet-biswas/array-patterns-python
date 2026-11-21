from collections import deque


def count_bounded_spread_subarrays(values: list[int], limit: int) -> int:
    """Count nonempty windows with max-min <= limit; negative limit -> 0. No mutation."""
    if limit < 0:
        return 0
    low, high = deque(), deque()
    left = total = 0
    for right, value in enumerate(values):
        while low and values[low[-1]] >= value:
            low.pop()
        while high and values[high[-1]] <= value:
            high.pop()
        low.append(right)
        high.append(right)
        while values[high[0]] - values[low[0]] > limit:
            if low[0] == left:
                low.popleft()
            if high[0] == left:
                high.popleft()
            left += 1
        total += right-left+1
    return total
