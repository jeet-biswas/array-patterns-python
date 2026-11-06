from collections import deque


def sliding_window_max(values: list[int], size: int) -> list[int]:
    """Return maxima for all full windows; require 1 <= size <= len(values).

    Invalid size raises ValueError, including every size for empty input.
    O(n) time, O(size) auxiliary space plus O(n-size+1) output.
    """
    if not 1 <= size <= len(values):
        raise ValueError('size must be between 1 and the array length')
    candidates = deque()
    result = []
    for i, value in enumerate(values):
        while candidates and candidates[0] <= i - size:
            candidates.popleft()
        while candidates and values[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(i)
        if i >= size - 1:
            result.append(values[candidates[0]])
    return result
