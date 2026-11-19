from collections import deque


def longest_subarray_limit(values: list[int], limit: int) -> int:
    """Longest contiguous length with max-min <= limit; empty -> 0.

    Negative limit raises ValueError. O(n) time and O(n) space; no mutation.
    """
    if limit < 0:
        raise ValueError('limit must be nonnegative')
    maxima, minima = deque(), deque()
    left = best = 0
    for right, value in enumerate(values):
        while maxima and values[maxima[-1]] <= value:
            maxima.pop()
        while minima and values[minima[-1]] >= value:
            minima.pop()
        maxima.append(right)
        minima.append(right)
        while values[maxima[0]] - values[minima[0]] > limit:
            if maxima[0] == left:
                maxima.popleft()
            if minima[0] == left:
                minima.popleft()
            left += 1
        best = max(best, right - left + 1)
    return best
